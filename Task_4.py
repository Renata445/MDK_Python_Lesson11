def count():
    i = 0
    while i < 11:
        print(i, end = ' ')
        i += 1

count()
print()

def count1(num = 0):
    if num > 10:
        print(num, end=' ')
    count(num + 1)
count()
