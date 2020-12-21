pizzas = ['tempo', 'proshuto', 'hawaii']
friend_pizzas = pizzas[:]
pizzas.append('diablo')
friend_pizzas.append('mexicano')
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('I really love pizza!')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())
print('My friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza.title())