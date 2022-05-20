src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
repeatings=src.copy()
# result = [23, 1, 3, 10, 4, 11]
len_src = len(src) - 1
uniq_items=set(src)
result=[]
for i in uniq_items:
    repeatings.remove(i)
uniq_set=uniq_items-set(repeatings)
for i in src:
    if i in uniq_set:
        result.append(i)
print(result)