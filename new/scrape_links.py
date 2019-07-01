from bs4 import BeautifulSoup

import requests

# Ask the user for the input URL for example https://www.census.gov/data/tables/2016/demo/popest/state-total.html
url = input("Enter a website to extract the URL's from: ")

# Request data from the server using GET protocol,
r = requests.get(url)
# In order to retrieve the data from the response object convert the raw response to text
data = r.text

# Pythons HTML parser
soup = BeautifulSoup(data, 'html.parser')

list = ''

# Get all URLS from <a> tags with attribute href
for tag in soup.find_all('article'):
    for link in tag.find_all('a'):
        list += 'https://www.unicef.org' + link.get('href') + '\n'

f = open("womanandkids_link.txt", "a")
f.write(list)
f.close()
