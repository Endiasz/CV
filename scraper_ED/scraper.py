from bs4 import BeautifulSoup
import requests

p_to_scrape = requests.get('https://www.digitalcombatsimulator.com/en/news/')
doc = BeautifulSoup(p_to_scrape.text, "html.parser")

class news:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def getfull(self):
        return (self.id, self.title, self.content)

    def get_ID(self):
        return self.id

    def get_Content(self):
        return self.content

    def get_Title(self):
        return self.title

news_list = []

for post in doc.find_all('div', attrs={'class': 'news'}):
    whole = post.parent
    id = whole.get('id')
    content = post.find('p')
    title = post.find('h3')
    # print(id," " ,title.string ," ", content)
    
    news_item = news(id, title.string, content)
    news_list.append(news_item)




print("I have :", news_list.__len__()," items")
print(news_list)