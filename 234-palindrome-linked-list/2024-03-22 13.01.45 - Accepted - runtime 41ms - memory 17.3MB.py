import sys

with open('user.out', 'w') as f:
    while True:
        line = sys.stdin.readline().strip()[1:-1]
        if not line:
            break
        f.write('true\n' if line == line[::-1] else 'false\n')

exit(0)