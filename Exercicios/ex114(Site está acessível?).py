import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim ão está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read()) → # possível ler o conteudo inteiro do site
