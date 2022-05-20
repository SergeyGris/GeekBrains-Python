pars_list = []
with open('nginx_logs.txt', encoding='utf-8') as file_1:
    for line in file_1:
        ip_border = line.index(' - -')
        ip = line[0:ip_border]
        action_left_border = line.index(' "') + 2
        action_right_border = line.index('" ')
        action = line[action_left_border:action_right_border]
        if 'GET' in action:
            log = 'GET'
            adress = action[4:]
        else:
            log = "HEAD"
            adress = action[5:]
        pars = ip, log, adress
        pars_list.append(pars)
print(pars_list)
