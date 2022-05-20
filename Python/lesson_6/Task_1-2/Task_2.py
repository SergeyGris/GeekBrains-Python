pars_list=[]
ip_list=[]
with open('nginx_logs.txt', encoding='utf-8') as file_1:
    for line in file_1:
        ip_border=line.index(' - -')
        ip=line[0:ip_border]
        action_left_border=line.index(' "')+2
        action_right_border = line.index('" ')
        action=line[action_left_border:action_right_border]
        if 'GET' in action:
            log='GET'
            adress=action[4:]
        else:
            log="HEAD"
            adress=action[5:]
        pars = ip, log, adress
        pars_list.append(pars)
        ip_list.append(ip)
uniq_dict={}
# uniq_dict={ip:1 if ip not in uniq_dict else ip:uniq_dict[ip]+=1
for ip in ip_list:
    if ip not in uniq_dict:
        uniq_dict[ip]=1
    else:
        uniq_dict[ip]+=1
# print(uniq_dict)
inv_uniq_d={}
inv_uniq_d= {value: key if key not in inv_uniq_d else inv_uniq_d[value].append(key) for key, value in uniq_dict.items()}
spammer_count=max(inv_uniq_d)
spammer_id=inv_uniq_d[spammer_count]
print(f"Спаммер с ip: {spammer_id} совершил {spammer_count} запросов")