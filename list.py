while True:
    list = {
    'Grocery':'Apple ''Mango',
    'Bakery':'Bread ''Cake'
}
    what = input('What list do you want to see?').lower()
    if what == 'grocery':
        print(list.get('Grocery'))
    elif what == 'bakery':
        print(list.get('Bakery'))

    ans = input('Do you want to get more list(y/n)').lower()
    if ans == 'y':
        continue
    else:
        break

