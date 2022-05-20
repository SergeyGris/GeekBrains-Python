import json
from os.path import join

def generator_hobbies(users, hobbies):
    length = len(hobbies)
    for idx, man in enumerate(users):
        if idx < length:
            yield man, hobbies[idx]
        else:
            yield man, None

users_dict={}
users=[]
hobbies=[]
with open(file=join(".", "task_3_users.csv"), encoding="utf-8") as file_users:
    for user in file_users:
        Name,Surname,Lastname=user.strip().split(',')
        ABB=f'{Name[0]}{Surname[0]}{Lastname[0]}'
        users.append(ABB)
with open(file=join(".", "task_3_hobby.csv"), encoding="utf-8") as file_hobby:
    for hobby in file_hobby:
        hobby=hobby.strip()
        hobbies.append(hobby)
gen_hobbies=generator_hobbies(users, hobbies)
users_dict={key:value for key,value in gen_hobbies}
print(users_dict)
with open(join(".", "task_3_rezult.json"),'a', encoding="utf-8") as file_result:
    result=json.dumps(users_dict)
    file_result.write(result)