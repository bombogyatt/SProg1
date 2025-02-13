e = [2, 3, 11, 0, -5, 6, 4]

max = 0
min = e[0]
avg = 0
for i in range(len(e)):
    if e[i] > max:
        max = e[i]
    if e[i] < min:
        min = e[i]
    avg += e[i]

print(f"nejvetsi cislo je {max} a nejmensi je {min}, prumer je {avg / len(e)}")



