for i in range(100):
    try:
        s = input()
        if s[len(s)-1] == " ":
            break
        else:
            print(s)
    except EOFError:
        break
