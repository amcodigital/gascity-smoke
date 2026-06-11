# Live alias e2e: proves worker ran through smoke/polecat — gcspike-kcf (smoke/gascity.polecat-1, 2026-06-11)
import sys

VERSION = "alias-0.1"


def main():
    if "--version" in sys.argv[1:]:
        print(VERSION)
    else:
        print("hello alias from gas city")


if __name__ == "__main__":
    main()
