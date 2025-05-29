import json
import csv
import pandas as pd
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
data = [{
    'name': '王伟',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2,ensure_ascii=False))
    
# CSV文件存储
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
# CSV文件读取
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
df = pd.read_csv('data.csv')
print(df)