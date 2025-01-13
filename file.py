text = "ABCd"
for k,i in enumerate(text,0):
    for k2, j in enumerate(text,1):
        if k>=k2 or k>= len(text):
            continue
        else:
            print(text[k:k2])


