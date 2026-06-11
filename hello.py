# Phase 3 close-out smoke: verified prints hello — gcspike-4mz (smoke/claude-1, 2026-06-11)
import sys

VERSION = "gascity-smoke 0.1.0"


def main():
    if "--version" in sys.argv[1:]:
        print(VERSION)
    else:
        print("hello from gas city")


if __name__ == "__main__":
    main()
