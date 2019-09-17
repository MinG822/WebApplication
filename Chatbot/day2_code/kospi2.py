import requests
import bs4

url2 = "https://www.naver.com/"
response2 = requests.get(url2).text
# print(response2)
document2 = bs4.BeautifulSoup(response2, "html.parser")
# print(document2)
rank1keyword = document2.select('.ah_a')

for i in rank1keyword:
    print(i.text)


