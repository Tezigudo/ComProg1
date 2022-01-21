menu = {'water': 20, 'soda': 30, 'juice': 40, 'tea':60, 'coffee': 80}

def order(menu):
    name = input('Enter name: ')
    l_menu = menu.split(', ')[:-1]
    l = []
    while 1:
        print(menu)
        tmp = input('Enter choice (q to quit): ')
        if tmp == 'q':
            return name, l
        elif tmp not in l_menu:
            print(f'{tmp} is not in menu.')
        else:
            l+=[tmp]

menu_str = ', '.join(menu.keys())+', '
name, food = order(menu_str)
print(food)
print(f"{name}'s order = {food}")
print(f'Payment for {name} = {sum(menu[k] for k in food)} Baht')

