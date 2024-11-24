import requests, sys, re

FLAG = None

def getUrls(content):
    urls = re.findall(r'href="([a-zA-Z0-9/]+)"', content)
    return urls

def getContent(url):
    print("Explore ", url)

    try:
        response = requests.get(url)
        
        content = response.text

        urls = getUrls(content)

        if content.isdigit():
            print("Found flag: ", content)
            FLAG = content
            return content
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

    print("Flag: ", FLAG)