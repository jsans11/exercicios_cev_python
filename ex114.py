import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://web.whatsapp.com/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo ok')