import requests
import json
import datetime


class news:
    def __init__(self, gid, title, content, url):
        self.gid = gid
        self.title = title
        self.content = content
        self.url = url
        

    def getfull(self):
        return (self.id, self.title, self.content)

    def get_gid(self):
        return self.gid

    def get_Content(self):
        return self.content

    def get_Title(self):
        return self.title
    
    def get_url(self):
        return self.url


    def display(self):
        print(f"\nTitle: {self.title}\nContent:\n{self.content}\n\n{self.url}")


req = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=1604270&count=3&maxlength=600&format=json') # returning json
response = json.loads(req.text)
container = response['appnews']

news_List = []

for item in container['newsitems']:    
    gid = item['gid']
    title = item['title']
    content = item['contents']
    url = item['url']

    news_Item = news(gid, title, content, url)
    news_List.append(news_Item)


# for i in news_List:
#     if(i.get_gid()=='5059268099240480567'): # if new item 
#         # display
#         i.display()

news_List[0].display()


