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
        return (self.gid, self.title, self.content, self.url)

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


req = requests.get(
    'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=1604270&count=3&maxlength=600&format=json')  # returning json
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


#  Checking for new news. Side of code

previously_gathered = []

f = open("news.txt")


gathered = []

if(f.read() == None or f.read() == ''):
# if(True):
    print('saveing data')
    for i in news_List:
        gid, title, content, url = i.getfull()
        item = {'gid': gid, 'title': title, 'content': content, 'url': url}

        gathered.append(item)
        # print(item)
        
    f.close()
    
    f = open("news.txt",'w')
    f.write(json.dumps(gathered))
    f.close()

else:
    print("Loadnig json")
    
    try:
        prev = json.load(f.read())
    except:
        print('Failed to load json')

# print(gathered)


# print(news_List[0])

# json.


# news_List[0].display() # displat missing
