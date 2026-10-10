'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    data = file.read(1024)
    while data:
        sys.stdout.buffer.write(data)
        data = file.read(1024)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
