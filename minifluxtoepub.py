#!/usr/bin/python3
import requests
from datetime import datetime
import os
import subprocess

# YOUR DATA
URL = 'your miniflux json api url'
DATA = '{"jsonrpc": "2.0", "method": "item.list_unread", "id":1}'
AUTH = ('username','apikey')
DIRECTORY = 'your directory'

r = requests.post(URL, data = DATA, auth=AUTH)

j = r.json()
fecha = datetime.now().strftime('%Y%m%d')
tefile = DIRECTORY + fecha
htmlfile = tefile + '.html'
epubfile = tefile + '.epub'
if os.path.exists(htmlfile):
    raise Exception('El fichero html existe, abortando')

for archivo in j['result']:
    codigoweb = '<div class="chapter"><h1>' + archivo['title'] + '</h1></div> ' + archivo['content']
    with open(htmlfile, "a") as text_file:
        text_file.write(codigoweb)

subprocess.run(["ebook-convert", htmlfile, epubfile])
os.remove(htmlfile)
