S = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []

for i in range (0,26):
    answer.append(S.find(alphabet[i]))

print(*answer)

