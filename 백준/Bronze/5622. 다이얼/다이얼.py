s = input()
sum = 0
for i in range(len(s)):
    if s[i] in ["A","B","C"]:
        sum += 3
    elif s[i] in ["D","E","F"]:
        sum += 4
    elif s[i] in ["G","H","I"]:
        sum += 5
    elif s[i] in ["J","K","L"]:
        sum += 6
    elif s[i] in ["M","N","O"]:
        sum += 7
    elif s[i] in ["P","Q","R","S"]:
        sum += 8
    elif s[i] in ["T","U","V"]:
        sum += 9
    elif s[i] in ["W","X","Y","Z"]:
        sum += 10
    else:
        break
print(sum)