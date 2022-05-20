def iterator_without_yield(n):
    el=0
    while el<=n:
        if el%2!=0 and el**2<200:
            print(el)
            yield el
        el+=1
n = int(input())
gen1 = iterator_without_yield(n)
for i in gen1:
    next(gen1)
