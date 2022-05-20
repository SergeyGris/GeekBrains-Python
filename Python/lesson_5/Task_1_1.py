def iterator_without_yield(n):
    gen1 = (el for el in range(n) if el % 2 != 0 and el**2<200)
    return gen1

n = int(input())
gen1 = iterator_without_yield(n)
for i in gen1:
    print(i)
    next(gen1)
