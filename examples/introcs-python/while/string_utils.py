def one_char_per_line(s: str) -> None:
    """Print each character of s on a separate line."""
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


def count_vowels(s: str) -> int:
    """Return the number of vowel characters in s."""
    vowels = "aeiouAEIOU"
    count = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            count += 1
        i += 1
    return count


def all_digits(s: str) -> bool:
    """Return True if every character of s is a digit."""
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            return False
        i += 1
    return True


def find_char(s: str, target: str) -> int:
    """Return the index of the first occurrence of target in s, or -1."""
    i = 0
    while i < len(s):
        if s[i] == target:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    one_char_per_line("bug")
    print(count_vowels("Hello World"))
    print(all_digits("12345"), all_digits("123a5"))
    print(find_char("Python", "t"))
