import urllib.request

url = 'http://www.pudim.com.br'
try:
    site = urllib.request.urlopen(url)
except:
    print('INDISPONÍVEL')
else:
    print('DISPONÍVEL')
