import requests, sys, re

READMES = []

def getUrls(content):
    urls = re.findall(r'href="([a-zA-Z0-9/]+)"', content)
    return urls

def getContent(url):
    try:
        response = requests.get(url)
        
        content = response.text

        urls = getUrls(content)
        
        if "README" in url:
            if content not in READMES:
                print(content)
                READMES.append(content)
        else:
            for childrenUrl in urls:
                getContent(
                    url=url + childrenUrl,
                )


    except Exception as e:
        print("Error: %s" % e)
        return None

if __name__ == '__main__':
    args = sys.argv

    if len(args) < 2:
        print('Usage: python script.py <url>')
        sys.exit(1)

    baseUrl = args[1]

    print("Check urls from ", baseUrl)

    content = getContent(
        url=baseUrl,
    )