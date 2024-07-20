#!/usr/bin/env python

import requests
import json

# Get the latest version of Calibre-Web

URL = "https://api.github.com/repos/janeczku/calibre-web/releases/latest"

def get_latest(channel):
    r = requests.get(URL)
    data = json.loads(r.text)
    version = data['tag_name'].removeprefix("v")
    return version

if __name__ == "__main__":
    import sys
    channel = sys.argv[1]
    print(get_latest(channel))
