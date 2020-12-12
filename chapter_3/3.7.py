guests = ['Паша', 'Иван', 'Ира']
print(f'Приходи на обед, {guests[0]}')
print(f'Приходи на обед, {guests[1]}')
print(f'Приходи на обед, {guests[2]}')

print(f'{guests[1]} не сможет прийти на обед...')
guests[1] = 'Олег'
print(f'Приходи на обед, {guests[0]}')
print(f'Приходи на обед, {guests[1]}')
print(f'Приходи на обед, {guests[2]}')

print('В связи с расширением, хочу пригласить ещё троих гостей.')
guests.insert(0, 'Дима')
guests.insert(3, 'Влад')
guests.append('Сергей')
print(f'Приходи на обед, {guests[0]}')
print(f'Приходи на обед, {guests[1]}')
print(f'Приходи на обед, {guests[2]}')
print(f'Приходи на обед, {guests[3]}')
print(f'Приходи на обед, {guests[4]}')
print(f'Приходи на обед, {guests[5]}')

print('К сожалению могу пригласить только двоих гостей.')
popped = guests.pop()
print(popped + ' - сожалею об отмене приглашения.')
popped = guests.pop()
print(popped + ' - сожалею об отмене приглашения.')
popped = guests.pop()
print(popped + ' - сожалею об отмене приглашения.')
popped = guests.pop()
print(popped + ' - сожалею об отмене приглашения.')

print(f'Приходи на обед, {guests[0]}')
print(f'Приходи на обед, {guests[1]}')
print('Приглашения для вас остаются в силе!')
del guests[0]
del guests[0]

print(guests)