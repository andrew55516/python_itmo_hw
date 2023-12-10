import sys


def tail(file=None, line_count=10):
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
            if len(lines) < 10:
                line_count = 0
            for line in lines[-line_count:]:
                print(line, end='')
    else:
        lines = sys.stdin.readlines()
        if len(lines) < 10:
            line_count = 0
        for line in lines[-line_count:]:
            print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, filename in enumerate(sys.argv[1:]):
            if len(sys.argv) > 2:
                log = f"==> {filename} <=="
                if i > 0:
                    log = "\n" + log
                print(log)
            tail(filename)
    else:
        tail(line_count=17)
