class NumReverse:
    def __init__(self):
        self.cache = {}

        #store first fullrange into cache
        fullRange = 1000
        for i in range(fullRange):
            self.cache[i] = self.num_reverse(i)

    def num_reverse(self, n):
        #look for n in cache
        if n in self.cache:
            print("Cache hit")
            return self.cache[n]

        #if not in cache make calculation
        print('Cache miss')
        n2 = list(str(n))
        n2.reverse()
        n2 = ''.join(n2)

        self.cache[n] = int(n2)

        return self.cache[n]

import urllib.request
import datetime
class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = str(get_timestamp())

cache = {}

def get_timestamp():
    return datetime.datetime.now().timestamp()

def get_data(url):
    if url in cache and get_timestamp() < (float(cache[url].timestamp) + 10):
        print('in cache')
        return cache[url].timestamp
    else:
        print('not in cache')
        resp = urllib.request.urlopen(url)

        data = resp.read()

        resp.close()
        #turn bites into a string
           
        #cache[url] = data.decode('utf-8')
        # #now with timestamp 
        cache[url] = CacheEntry(url, data.decode('utf-8')) #put data into CacheEntry, so can store with timestamp
        return cache[url].timestamp

if __name__ == '__main__':
    while True:
        url = input('Enter a URL:')
        #only print first 100 bites
        print(get_data(url)[:100])

#building a cache table, key is what you have, value is what you want to get