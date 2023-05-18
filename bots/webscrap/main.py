from requests_html import HTMLSession
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url="https://fid4sa-repository.ub.uni-heidelberg.de/view/schriftenreihen/sr-257.html?lang=en"

session = HTMLSession()
r = session.get(url)

b  = requests.get(url)
soup = BeautifulSoup(b.text, "ep_view_page ep_view_page_view_schriftenreihen")

for link in soup.find_all('a'):
    print(link.text, '-', link.get('href'))