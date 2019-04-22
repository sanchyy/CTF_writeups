
n = 27

res = ""
aux = n
print(aux)

while aux > 0:
    res += str(aux % 2)
    aux = aux // 2
    print(res,aux)

print(res)

