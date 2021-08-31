import os
from pprint import pprint
from collections import OrderedDict

file_names = []

#получение всех txt файлов из текущей директории
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        file_names.append(file)

file_dict = {}

#формируем словарь с названием файла, кол-во строк и содержимым
for file_name in file_names:
    file_path = os.path.join(os.getcwd(),file_name)
    count_str = 0 
    content = ""
    with open(file_path, 'rt', encoding='UTF8') as file:
        for line in file:
            count_str += 1
            content += line
        file_dict[file_name] = {'count_str': count_str,'content': content}

#сортировка словаря по значению count_str
sorted_dict = OrderedDict()
sorted_keys = sorted(file_dict, key=lambda x: file_dict[x]["count_str"])     

for key in sorted_keys: 
    sorted_dict[key] = file_dict[key]

#вывод результата
for key,value in sorted_dict.items():        
    print(key)
    print(value['count_str'])
    print(value['content'])
    print("\n")

   