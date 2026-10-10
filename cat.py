'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 1024 * 1024

def cat(file):
    for chunk in iter(lambda: file.read(CHUNK_SIZE), b''):
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
