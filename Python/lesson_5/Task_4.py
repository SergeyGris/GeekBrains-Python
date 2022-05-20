src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# # result = [12, 44, 4, 10, 78, 123]
len_src = len(src) - 1
result_1 = [src[i] for i in range(len_src) if src[i] > src[i - 1]]
print(result_1)
