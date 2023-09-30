import urllib.request


with urllib.request.urlopen('https://google.com') as response:
    h = response.read();
    h.
