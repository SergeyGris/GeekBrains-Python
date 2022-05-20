def thesaurus(*args):
    dict_1= {}
    for i in range(len(args)):  # args
        name = args[i]
        letter = name[0]
        if letter in dict_1:
            dict_1[letter].append(name)
        else:
            dict_1[letter]=[name]
        final_dict_keys=sorted(dict_1)
    final_dict={}
    for key in final_dict_keys:
        final_dict[key]=dict_1[key]
    print(final_dict)
    return final_dict
thesaurus("Иван", "Мария", "Петр", "Илья")

