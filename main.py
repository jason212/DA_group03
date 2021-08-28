# This is for TAsk 5 , @kenneth can do task 6?
import requests

r = requests.get('https://brickset.com/sets/year-2000')
print("\t *", r.status_code)


h = requests.head('https://brickset.com/sets/year-2000')
print("Header:")
print("****")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("****")


# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
