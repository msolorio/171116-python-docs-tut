def printLine():
    print('....................')

# writes fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# fib(100)

printLine()

def fib2(n):
    '''return a list containing fibonacci series'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# print(fib2(100))

printLine()

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    bool = True

    while bool == True:
        ok = input(prompt)
        retries = retries - 1
        if ok in ('n', 'no', 'nop', 'nope'):
            bool = False
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('is 2 greater than 3?\n')

printLine()

# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# print(f(1))
# print(f(2))
# print(f(3))

def cheeseshop(kind, *arguments, **keywords):
    print('-- do you have any', kind, '?')
    print('-- i\'m sorry, we\'re all out of', kind)

    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print (kw, ':', keywords[kw])

cheeseshop('fromage', 'asdf', '1234', 'qwert', carrots=3, figs=2)
