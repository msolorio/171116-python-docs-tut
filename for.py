animals = ['cat', 'dog', 'goose']

for animal in animals:
    print(animal, len(animal))

print('..............................')

words = ['tree', 'calendar', 'rock', 'sun', 'paleontologist']

for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)

print(words)

print('..............................')

for i in range(3):
    print(i)

print('..............................')

for i in range(0, 21, 2):
    print(i)

print('..............................')

a = ['Mary', 'had', 'a', 'large', 'lamb']
for i in range(len(a)):
    print(i+1, a[i])

for i in range(0, -10, -2):
    print(i)

print('..............................')

print(list(range(5)))

print('..............................')

# else block only runs if we havcen't broken out of inner
# for loop after all iterations of x
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print('..............................')
