def is_m_pattern(img):
    m_pattern = ['*   *', '** **', '* * *']

    for i in range(len(img)):
        for j in range(len(img[0])):
            if m_pattern[i][j] == '*' and img[i][j] != '*':
                return False
            if img[i][j] == '*' and m_pattern[i][j] != '*':
                return False
    return True


def main():
    try:
        image = [input().strip() for _ in range(3)]
    except EOFError:
        print('Error')
        return

    if any(len(line) != 5 for line in image):
        print('Error')
    elif is_m_pattern(image):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()
