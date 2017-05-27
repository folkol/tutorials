words = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(words)):
    print(i, words[i])

for i, word in enumerate(words):
    print(i, word)

for i in range(0):
    if i is 11:
        print(i)
        break
else:
    print("Didn't break")
