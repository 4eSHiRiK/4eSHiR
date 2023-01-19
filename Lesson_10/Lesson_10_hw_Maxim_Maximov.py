







while start != 'n':
    print('Name of product - Price - Amount')
    for key in shop_dict:
        print(key, '-', shop_dict[key][0], '-', shop_dict[key][1])
    user_product = input('Enter name of product')
    user_amount = int(input('Enter amount of product'))
    if user_product in shop_dict:
        if user_amount > shop_dict[user_product][1]:
            print('Incorrect amount')
        else:
            sum += (shop_dict[user_product][0]*user_amount)
            shop_dict[user_product][1] = shop_dict[user_product][1] - user_amount
        start = input('Enter continue or n for break')
    else:
        print('Unfortunately we do not hve this product, please choose from list above')
        start = input('Enter continue or n for break')
else:
    print(f'Total: {sum}')
    print('Thanks')
