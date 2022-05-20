import re

def parsed_line(line):
    pattern = re.compile(r'(?P<remote_addr>((\d+.?){4}|([a-zA-Z0-9]+?:*?){2,8}))'
                         r'\s?-\s?-\s?\['
                         r'(?P<request_datetime>\d+/\w+/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})\W+?'
                         r'(?P<request_type>\w{3,4})\s'
                         r'(?P<requested_resource>/\w+/\w+)\s\w+?/\d.\d"\s'
                         r'(?P<response_code>\d+)\s'
                         r'(?P<response_size>\d+)'
                            , re.VERBOSE)
    rez = pattern.search(line)
    rez_dict = rez.groupdict()
    print(rez_dict)
    ip=rez_dict['remote_addr']
    return ip
ip_list=[]
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        ip=parsed_line(line)
        ip_list.append(ip)
ip_list=set(ip_list)
print(ip_list)