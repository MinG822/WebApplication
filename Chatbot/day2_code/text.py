# with open('ssafy.txt','w',encoding='utf-8') as f:
#     f.write('위드를 썼다\n'*5)
 
lunch = {
    'a':'b',
    'c':'d'
}

# with open('lunch.csv', 'w', encoding='utf-8') as f:
#     for i,v in lunch.items():
#         f. write(f"{i},{v}\n")

# # ',' join울 통해 스트링 만들기
# with open('lunch.csv', 'w', encoding='utf-8') as f:
#     for i in lunch.items():
#         f.writelines(','.join(i))

# #csv writer
import csv
# with open('lunch.csv', 'w', encoding='utf-8', newline='') as f:
#     csv_writer = csv.writer(f)
#     for i in lunch.items():
#         csv_writer.writerow(i)

# DictWriter
with open('student.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames=['1','2']
    writer=csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data=[{'1':'a','2':'b'}, {'1':'c','2':'d'}]
    writer.writerow(data[0])
    