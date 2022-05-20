def thesaurus_adv(*args):
    dict_1 = {}
    for i in range(len(args)):
        full_name = args[i]
        name, surname = full_name.split(' ')
        first_letter_surname = surname[0]
        if first_letter_surname in dict_1:
            dict_1[first_letter_surname].append(full_name)
        else:
            dict_1[first_letter_surname] = [full_name]
    # print(dict_1)
    sorted_dict_1={}
    letters_dict_1=sorted(dict_1)
    for i in letters_dict_1:
        sorted_dict_1[i]=dict_1[i]
    # print(sorted_dict_1)
    function_2(sorted_dict_1)
def function_2(*args):
    dict_1=args[0]
    final_dict={}
    for letter in dict_1:
        names=dict_1[letter]
        dict_2 = {}
        for i in range(len(names)):
            fullname = names[i]
            fisrt_name,sur_name = fullname.split(' ')
            first_letter = fisrt_name[0]
            if first_letter in dict_2:
                dict_2[first_letter].append(fullname)
            else:
                dict_2[first_letter] = [fullname]
        sorted_dict_2 = {}
        letters_dict_2 = sorted(dict_2)
        for i in letters_dict_2:
            sorted_dict_2[i] = dict_2[i]
        final_dict[letter]=sorted_dict_2
    print(final_dict)
    return(final_dict)

thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
              "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
