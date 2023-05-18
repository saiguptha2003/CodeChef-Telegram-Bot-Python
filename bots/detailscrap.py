import requests
from bs4 import BeautifulSoup
import requests
 
page = requests.get('https://www.codechef.com/contests?itm_medium=navmenu&itm_campaign=allcontests') 
soup = BeautifulSoup(page.content, 'html.parser')

for table in soup.find_all('table'):
    print(table.get('class'))