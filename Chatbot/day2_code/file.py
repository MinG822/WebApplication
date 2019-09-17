import os
# print(os.listdir())
# os.rename('hello.py','dogdog.py')
# print(os.listdir())
os.chdir('report')

file = os.listdir()

for i in file:
    os.rename(i, i.replace("SSAFY","ssafy"))