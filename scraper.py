from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient()

url = 'http://www.registrar.ucla.edu/catalog/catalog-curricul.htm'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all("a", { "class" : "main" }):
    coursetitle = link.contents[0]
    intourl = 'http://www.registrar.ucla.edu/catalog/' + link.get('href')
    # print(url + "/" + link.get('href') + "\n" + coursetitle)
    soup2 = BeautifulSoup(requests.get(intourl).text)
    for link2 in soup2.find_all("a", { "class" : "nav-landing-menu" }):
        if 'Course Listings' in link2.contents[0]:
            courseDescriptUrl = 'http://www.registrar.ucla.edu/catalog/' + link2.get('href')
            soup3 = BeautifulSoup(requests.get(courseDescriptUrl).text)
            for link3 in soup3.find_all("p", { "class" : "coursebody" }):
                print(link3)
