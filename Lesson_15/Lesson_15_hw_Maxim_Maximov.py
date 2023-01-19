




while True:
    str = input('Enter 2 values data')
    lst = str.split()
    try:
        res = int(lst[0]) / int(lst[1])
        print(res)
        break
    except ZeroDivisionError:
        if int(lst[1]) == 0:
            print('Zero Division, try one more time')
    except ValueError:
        print('You enter letters')
    except IndexError:
        print('Enter 2 values')


