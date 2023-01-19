import json



# Programm korzina

lst_name = []
lst_cost = []
while True:
    name = input('Enter name of product')
    if name != 'stop':
        cost = int(input('Enter cost of this product'))
        lst_name.append(name)
        lst_cost.append(cost)
    else:
        break
total = dict(zip(lst_name,lst_cost))
# print(total)

with open('korzina.json','w') as f:
    json.dump(total,f,ensure_ascii=False)


#RESULT


with open('korzina.json') as f:
    data_work = json.load(f)
    total_sum = 0
    for elem in data_work.values():
        total_sum += int(elem)
    print(f'Total: {total_sum}$')
