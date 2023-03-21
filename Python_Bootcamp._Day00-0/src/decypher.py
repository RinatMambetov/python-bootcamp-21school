import sys


def first_letter_word(phrase):
    words = phrase.split()
    first_letters = [word[0] for word in words]
    word = ''.join(first_letters)
    return word


def main():
    if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
        print("Error: invalid argument")
        return

    word = first_letter_word(sys.argv[1])
    print(word)


if __name__ == '__main__':
    main()
