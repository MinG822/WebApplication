import requests
from bs4 import BeautifulSoup
#1. op.gg.에 요청을 보낸다.

url="https://www.op.gg/summoner/userName=cuzz"
response=requests.get(url)

document=BeautifulSoup(response.text, 'html.parser')
win=document.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
lose=document.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text
print(win.replace('W',''))
print(lose[:3])