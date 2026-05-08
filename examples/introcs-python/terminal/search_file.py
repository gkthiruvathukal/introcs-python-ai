import argparse
import sys


def search_file(filename: str, keyword: str,
                case_sensitive: bool = True,
                line_numbers: bool = False) -> int:
    try:
        with open(filename, "r") as f:
            for line_num, line in enumerate(f, start=1):
                haystack = line if case_sensitive else line.lower()
                needle = keyword if case_sensitive else keyword.lower()
                if needle in haystack:
                    if line_numbers:
                        print(f"{line_num}: {line.rstrip()}")
                    else:
                        print(line.rstrip())
        return 0
    except FileNotFoundError:
        print(f"Error: '{filename}' not found", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: permission denied for '{filename}'", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search for a keyword in a text file",
        epilog="Example: python search_file.py data.txt Python -i -n"
    )
    parser.add_argument("filename", help="Path to the file to search")
    parser.add_argument("keyword", help="Keyword to search for")
    parser.add_argument("-i", "--ignore-case", action="store_true",
                        help="Case-insensitive search")
    parser.add_argument("-n", "--line-numbers", action="store_true",
                        help="Show line numbers in output")
    args = parser.parse_args()

    return search_file(
        args.filename,
        args.keyword,
        case_sensitive=not args.ignore_case,
        line_numbers=args.line_numbers,
    )


if __name__ == "__main__":
    sys.exit(main())
