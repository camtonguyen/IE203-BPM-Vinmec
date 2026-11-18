#!/usr/bin/env python3
"""Công cụ kiểm tra liên kết (Broken Link Checker) cho các tài liệu Markdown.

Phục vụ đồ án IE203 - Bệnh viện Đa khoa Quốc tế Vinmec Central Park.
Nhiệm vụ: Task T04 - CI GitHub Actions & Kiểm soát chất lượng tài liệu.

Quy tắc kiểm tra:
- Quét toàn bộ file .md trong repository (bỏ qua .git, venv, node_modules).
- Trích xuất các liên kết dạng Markdown [text](path) và ![alt](path).
- Bỏ qua các URL ngoại vi (http://, https://, ftp://), mailto: và anchor nội bộ (#).
- Đối với đường dẫn nội bộ tương đối (relative local path):
  + Tách phần anchor (#anchor nếu có).
  + Kiểm tra sự tồn tại của file hoặc thư mục đích trên hệ thống tệp.
- Trả về mã thoát (exit code):
  + 0: Tất cả liên kết nội bộ đều hợp lệ.
  + 1: Phát hiện ít nhất một liên kết hỏng.
"""

import os
import re
import sys
from pathlib import Path

# Regex trích xuất liên kết markdown: [text](url) hoặc ![alt](url)
LINK_PATTERN = re.compile(r'!?\[(?P<text>[^\]]*)\]\((?P<url>[^)]+)\)')

# Thư mục bỏ qua khi quét
EXCLUDE_DIRS = {'.git', 'venv', '.venv', 'env', 'node_modules', '__pycache__'}


def find_markdown_files(root_dir: Path) -> list[Path]:
    """Tìm tất cả các file .md trong cây thư mục, trừ các thư mục bị loại trừ."""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Lọc bỏ thư mục loại trừ
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for file in filenames:
            if file.endswith('.md'):
                md_files.append(Path(dirpath) / file)
    return sorted(md_files)


def check_file_links(file_path: Path, repo_root: Path) -> list[dict]:
    """Kiểm tra các liên kết trong một file markdown."""
    errors = []
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [{'file': file_path, 'line': 0, 'link': '', 'error': f'Không thể đọc file: {e}'}]

    lines = content.splitlines()
    for line_num, line in enumerate(lines, 1):
        for match in LINK_PATTERN.finditer(line):
            raw_url = match.group('url').strip()
            link_text = match.group('text').strip()

            # Làm sạch URL nếu có title phụ (ví dụ: [text](path "title"))
            url_part = raw_url.split()[0].strip('<>"\'')

            # Bỏ qua liên kết web, email, và anchor nội bộ cùng trang
            if url_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')) or url_part.startswith('#'):
                continue

            # Tách đường dẫn và anchor (#)
            target_path_str = url_part.split('#')[0].strip()
            if not target_path_str:
                continue

            # Xử lý URL encoding nếu có (ví dụ %20 thành khoảng trắng)
            target_path_str = target_path_str.replace('%20', ' ')

            # Giải quyết đường dẫn tương đối từ thư mục chứa file md
            if target_path_str.startswith('/'):
                # Đường dẫn tuyệt đối so với repo root
                target_path = (repo_root / target_path_str.lstrip('/')).resolve()
            else:
                target_path = (file_path.parent / target_path_str).resolve()

            if not target_path.exists():
                try:
                    rel_file = file_path.relative_to(repo_root)
                except ValueError:
                    rel_file = file_path
                try:
                    rel_target = target_path.relative_to(repo_root)
                except ValueError:
                    rel_target = target_path

                errors.append({
                    'file': rel_file,
                    'line': line_num,
                    'text': link_text,
                    'url': raw_url,
                    'target': rel_target,
                })

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1]).resolve()
        if target_path.is_file():
            md_files = [target_path]
        else:
            md_files = find_markdown_files(target_path)
    else:
        md_files = find_markdown_files(repo_root)

    print("=== KIỂM TRA LIÊN KẾT TÀI LIỆU MARKDOWN (Task T04) ===")
    print(f"Thư mục gốc: {repo_root}")
    print(f"Số lượng file Markdown quét: {len(md_files)}")
    print("-" * 60)

    total_errors = 0
    broken_links = []

    for md_file in md_files:
        errors = check_file_links(md_file, repo_root)
        if errors:
            broken_links.extend(errors)
            total_errors += len(errors)

    if broken_links:
        print(f" PHÁT HIỆN {total_errors} LIÊN KẾT HỎNG (BROKEN LINKS):")
        for err in broken_links:
            print(f"  - {err['file']}:{err['line']}")
            print(f"    Liên kết: [{err['text']}]({err['url']})")
            print(f"    Đích đến không tồn tại: {err['target']}")
        print("-" * 60)
        print("Vui lòng sửa các liên kết trên hoặc cập nhật file tương ứng.")
        return 1

    print(f"HOÀN TẤT: Toàn bộ {len(md_files)} file Markdown không có liên kết hỏng.")
    print("-" * 60)
    return 0


if __name__ == '__main__':
    sys.exit(main())
