import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://suporte.barsottisolucoes.com.br:891')
except urllib.error.URLError:
    print('O site do suporte não está acessivel no momento')
else:
    print('Consegui acessar o site do suporte com sucesso')
    print(site.read())
