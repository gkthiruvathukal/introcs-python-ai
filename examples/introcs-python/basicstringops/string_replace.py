# start: string_replace
def string_replace(s: str, target: str, replacement: str) -> str:
    """Return s with the first occurrence of target replaced by replacement.

    If target is not in s, return s unchanged.
    """
    i = s.find(target)
    if i == -1:
        return s
    before = s[:i]
    after = s[i + len(target):]
    return before + replacement + after
# end: string_replace


def main() -> None:
    print(string_replace("It was the best of times.", "best", "worst"))
    print(string_replace("abcabc", "bc", "X"))
    print(string_replace("hello", "xyz", "Q"))
    print(string_replace("aaaa", "aa", "B"))


if __name__ == '__main__':
    main()
