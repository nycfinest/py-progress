# pip install requests
import requests
# pip install bs4
from bs4 import BeautifulSoup

r = requests.get('https://oldschool.runescape.wiki/w/Twisted_bow')
html_doc = r.text


soup = BeautifulSoup(html_doc, 'html.parser')
tbow_price = int(soup.span['data-val-each'])


print(f"The twisted bow is currently trading at {tbow_price:,}")