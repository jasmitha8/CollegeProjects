
import urllib3
import html2text
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib3.urlopen('index (1).html').read())

txt = soup.find('div', {'class' : 'body'})

print(html2text.html2text(txt))