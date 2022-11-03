# For loop

names = ['Shaun', 'Ana', 'Patrick', 'Laura']

for name in names:
    print(f'Hello, {name}')


# we loop over the iterable

sentence = 'We are going to showcase the iterable'

for c in sentence:
    print(c)


# range(start, stop, step)

for i in range(900, 1000, 5):
    print(i)


# break and continue

print('We have a long way ahead')
for i in range(1000):
    print(i)
    if i == 10:
        break
    print('almost there...')
print("That wasn't that bad after all.")

print('We have a long road ahead.')
for i in range(1000):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost there...')
print("That wasn't half bad.")