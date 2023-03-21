import sys
import os
import requests
from bs4 import BeautifulSoup

SERVER_URL = 'http://localhost:8888'


def upload_file(filepath):
    if not os.path.isfile(filepath):
        print(f"{filepath} does not exist")
        return

    # send HTTP POST request to server to upload file
    with open(filepath, 'rb') as f:
        requests.post(f"{SERVER_URL}/upload", files={'file': f})


def list_files():
    folder_path = 'uploads'
    response = requests.get(f"{SERVER_URL}/{folder_path}")
    files = response.text
    soup = BeautifulSoup(files, 'html.parser')
    a_tags = soup.find_all('a')

    for a in a_tags:
        file_name = a.text.strip()
        print(file_name)


def main():
    if len(sys.argv) < 2:
        print("Usage: python screwdriver.py [upload|list] [filepath]")
        sys.exit()

    if sys.argv[1] == 'upload':
        if len(sys.argv) < 3:
            print("Usage: python screwdriver.py upload [filepath]")
            sys.exit()
        upload_file(sys.argv[2])
    elif sys.argv[1] == 'list':
        list_files()
    else:
        print("Invalid command")


if __name__ == '__main__':
    main()
