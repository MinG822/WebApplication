# 1. 평균을 구하시오.
score = {'수학': 80,'국어': 90,'음악': 100}
    
# 내 답
s=0
c=0
for i in score:
    s+=score[i]
    c+=1


print(s/c)

# 선생님 답

sum(score.values())/len(score.values())



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
            'a':{
                '수학': 80,
                '국어': 90,
                '음악': 100
                },
            'b':{
                '수학': 80,
                '국어': 90,
                '음악': 100
                }
        }

# 아래에 코드를 작성해 주세요.

# 내답
s=0
c=0
li=[]
for i in scores:
    for j in scores[i]:
        s+=scores[i][j]
        c+=1
    print(s/c)
    li.append(s/c)
print(sum(li)/len(li))

#선생님답
print(sum(scores['a'].values())/len(scores['a'].values()))

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.

#내답

li2=[]
for i in city:
    print(round(sum(city[i])/len(city[i]),2))
    li2.append(round(sum(city[i])/len(city[i]),2))


#선생님답
for temp in city.values():
     print(sum(temp)/len(temp))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
#내답

for c, temp in city.items():
    if round(sum(temp)/len(temp),2)  == max(li2):
        print(c)
        


for c, t in city.items():
    if round(sum(t)/len(t),2)  == min(li2):
        print(c)

#선생님답
# min(city.values())는 어떤 값을 반환하나?
# list를 flatten하게 만들어줘야한다. 
# 리스트안에 리스트를 그냥 하나의 큰 리스트로 바꿔주는 작업
# Numpy에서 flatten 기능을 지원한다.
# 또 itertools도 있음! 
# 어쨌든 데이터 사이언티스트에게 되게 중요한 기능

maxes=[]
mins=[]
for  temp in city.values():
    maxes.append(max(temp))
    mins.append(min(tmep))

high = max(maxes)
low = min(mins)

# 도시별로 최대/최소값 을 뽑아서 그 중에서 다시 최대/최소를 뽑는 방법

print(high)
print(low)

for k,v in city.items():
    if high in value:
        print(k)

for k,v in city.items():
    if low in value:
        print(k)


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
if 2 in city['서울']:
    print("yes")
else:
    print("no!")

#선생님
print(2 in city['서울'])