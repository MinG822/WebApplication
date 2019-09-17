# lotto api를 통해 최신 당첨 번호를 가져온다.

import requests
import random

url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
requests.get(url)
response = requests.get(url)
# json파일을 파이썬 딕셔너리로 바꿈
dict_lotto = response.json()

#로또 당첨 번호알려주기
winner=[]
for i in range(1,7):
    winner.append(dict_lotto["drwtNo{}".format(i)])

print("당첨번호는 {}입니다.".format(winner))


# # 로또 당첨 여부 알려주기
# your_lotto = sorted(random.sample(range(1,46),6))
#  count=0
# for i in winner:
#     for j in your_lotto:
#         if i==j:
#             count=+1
#             break
# print ("{}등 당첨입니다! 축하드려요!".format(7-count))

# count = len(set(winner) & set(your_lotto)) 교집합의 길이를 재주는 코드. 이러면 for 문을 쓸 필요가 없다.


# 몇 번 째에 로또가 당첨되었는지를 알려주는 코드
count2=0
while True:
    count2+=1
    your_lotto = sorted(random.sample(range(1,46),6))
    if your_lotto == winner:
        break

print("당신의 로또는 {}입니다.".format(your_lotto))

print("{}회차에 당첨되셨습니다. 당첨금은 {}이고 비용은 {}원입니다. 총 {}를 획득하셨어요! 수고하셨습니다!".format(count2, 1868470000, count2*5000, 1868470000-count2*5000))

