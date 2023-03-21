import sys


def main():
    if len(sys.argv) != 2:
        print("Error: wrong num of arguments")
        return

    try:
        num_lines = int(sys.argv[1])
    except ValueError:
        print("Error: argument should be an integer")
        return

    for i in range(num_lines):
        line = input().strip()

        if len(line) == 32 and line.startswith("00000") and line[5] != '0':
            print(line)


if __name__ == '__main__':
    main()
