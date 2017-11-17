words = ['tree', 'calendar', 'rock', 'sun', 'paleontologist']
# for word in words:
#     print(word, len(word))

for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)

print(words)

for i in range(3):
    print(i)

print('..............................')

for i in range(0, 21, 2):
    print(i)

print('..............................')

a = ['Mary', 'had', 'a', 'large', 'lamb']
for i in range(len(a)):
    print(i, a[i])
