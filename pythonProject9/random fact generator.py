import randfacts as rf

print('Random Facts')
x = ''

while x == '':
    print('Press enter for Fact')
    x = input()
    fact = rf.get_fact()
    print(fact)

