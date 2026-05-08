import sys

file_path = sys.argv[1] if len(sys.argv) > 1 else "example.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
        lines = contents.splitlines()
        words = contents.split()

        print(f"File: {file_path}")
        print(f"Number of lines: {len(lines)}")
        print(f"Number of words: {len(words)}")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
