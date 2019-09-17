import requests
url="https://finance.naver.com/sise/"
import bs4
response = requests.get(url).text
document = bs4.BeautifulSoup(response, "html.parser")
kosdaq = document.select_one('#KOSDAQ_now').text
print(" 현재 코스닥 지수는 : "+ kosdaq)


url = "https://finance.naver.com/marketindex/"
response = requests.get(url).text
document = bs4.BeautifulSoup(response, "html.parser")
exchange=document.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text
print(exchange)
