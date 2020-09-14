total = 100
print("Остаток - ",total)
i = 0
while i < 5:
    n = int(input())
    total = total - n
    i = i + 1
    if total < 0:
        print("Опа!")
        break
    else:
        print("Остаток", total)