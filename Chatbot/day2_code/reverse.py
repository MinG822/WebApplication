# 1. problem.txt 파일 생성 후, 다음과 같은 내용을 작성
0
1
2
3
# problem.txt의 파일 내용을 다음과 같이 변경
3
2
1
0

with open("problem.txt",'r') as f:
     result=f.readlines()
     result2=reversed(result)

     
with open("reversed.txt",'w') as d:
    d.writelines(result2)
     