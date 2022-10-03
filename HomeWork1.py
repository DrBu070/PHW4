N = int(input('Введите кол-во знаков после запятой числа "П": '))
pi = 0
for k in range(N):
    number_solution = (1/(16**k))*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6)))
    pi += number_solution
print("Пи =", round(pi, N))
