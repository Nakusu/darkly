import requests, sys, re

URLS_CONTENT = {}

def getUrls(content):
    urls = re.findall(r'href="([a-zA-Z0-9/]+)"', content)
    return urls

def getContent(url, baseUrl = None):
    print("Explore ", url)

    try:
        response = requests.get(url)
        
        content = response.text

        urls = getUrls(content)

        if len(urls) == 0 and url != "README":
            URLS_CONTENT[baseUrl] = [
                url
            ]
        else:
            URLS_CONTENT[baseUrl] = []

            for childrenUrl in urls:
                getContent(
                    url=url + childrenUrl,
                    baseUrl=url
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
        baseUrl=baseUrl
    )

    for item in URLS_CONTENT:
        if (len(item) > 0):
            print(item, ":", URLS_CONTENT[item])