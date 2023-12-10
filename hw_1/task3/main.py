import sys


def wc(file=None):
    entry = ""
    if file:
        with open(file, 'r') as f:
            entry = f.read()
    else:
        entry = sys.stdin.read()

    lines = entry.count("\n")
    words = len(entry.split())
    chars = len(entry)
    if file:
        chars += lines
    return lines, words, chars


if __name__ == "__main__":
    total_lines, total_words, total_chars = 0, 0, 0
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            lines, words, chars = wc(filename)
            print(f" {lines}  {words} {chars} {filename}")
            total_lines += lines
            total_words += words
            total_chars += chars
        if len(sys.argv) > 2:
            print(f" {total_lines}  {total_words} {total_chars} total")
    else:
        lines, words, chars = wc()
        print(f" {lines}  {words} {chars}")
