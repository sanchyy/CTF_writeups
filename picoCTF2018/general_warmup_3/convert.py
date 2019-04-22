

n = "0x3D"

conv = { "A" : 10,
         "B" : 11,
         "C" : 12,
         "D" : 13,
         "E" : 14,
         "F" : 15
        }

for i,c in enumerate(n):
    res = 0
    if i > 1:
        mult = len(n) - 2 - i
        num = conv[c] if (c > 'A' and c < 'F')  else int(c)
        res += 16*mult*num

print(res)

