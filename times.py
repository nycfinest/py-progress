n = 4
words = ["word", "localization", "internationalization", "pneumonoultramicroscopicsilicovolcanoconiosis"]


for i in range(len(words)):
    if(len(words[i]) <= n):
        print(words[i])
    else:
        print(words[i][0] + str((len(words[i]) - 2)) + words[i][-1])