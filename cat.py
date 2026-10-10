'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    for line in file:
        sys.stdout.buffer.write(line)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
