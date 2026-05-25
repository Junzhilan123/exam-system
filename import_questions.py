#!/usr/bin/env python
"""从本地 JSON 文件增量导入题库。

用法示例:
  python import_questions.py --file new_questions.json --subject CS205 --semester 2026SP
  python import_questions.py --file bank.json --subject CS201 --semester 2026SP --allow-duplicates
  python import_questions.py --stats
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(description="增量导入题库到考试系统")
    parser.add_argument("--file", "-f", help="本地 JSON 题库文件路径")
    parser.add_argument("--subject", "-s", default="CS201", help="科目代码，如 CS201")
    parser.add_argument("--semester", "-m", default="2026SP", help="学期代码，如 2026SP")
    parser.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="允许重复题目（默认跳过重复）",
    )
    parser.add_argument("--stats", action="store_true", help="仅显示当前题库统计")
    args = parser.parse_args()

    from app.data.bank_storage import get_bank_stats, import_from_file
    from app.data.question_bank import question_bank

    if args.stats:
        stats = get_bank_stats(question_bank)
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        return

    if not args.file:
        parser.error("请指定 --file 或使用 --stats")

    if not os.path.exists(args.file):
        print(f"错误: 文件不存在 {args.file}", file=sys.stderr)
        sys.exit(1)

    stats = import_from_file(
        args.file,
        args.subject,
        args.semester,
        skip_duplicates=not args.allow_duplicates,
    )

    print(f"导入完成: 新增 {stats['added']} 题, 跳过 {stats['skipped']} 题")
    if stats["errors"]:
        print("警告:")
        for err in stats["errors"][:20]:
            print(f"  - {err}")
        if len(stats["errors"]) > 20:
            print(f"  ... 共 {len(stats['errors'])} 条")


if __name__ == "__main__":
    main()
