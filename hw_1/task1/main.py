import sys


def print_lines_with_index(file=None):
    if file:
        with open(file, 'r') as f:
            for i, line in enumerate(f, 1):
                print(f"{i}\t{line}", end='')
    else:
        for i, line in enumerate(sys.stdin, 1):
            print(f"{i}\t{line}", end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_lines_with_index(sys.argv[1])
    else:
        print_lines_with_index()
