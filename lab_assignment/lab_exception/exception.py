
for i in range(10):
    try:
        #print(10 / i)
        result = 10 / i
    except ZeroDivisionError as e:
    #except ZeroDivisionError:
        print(e)
        print("Not divided by 0")
    else:
        print(10 / i)