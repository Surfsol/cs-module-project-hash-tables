import urllib.request

url = 'http://espn.com'

cache = {}

page = None

if url in cache:
    page = cache[url]

else:
    print('getting from server')

    resp = urllib.request.urlopen(url)
    data = resp.read()
    cache[url] = data
return cache[url]

    