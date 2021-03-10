def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('YOU CANNOT DIVIDE BY ZERO')

print(div42by(2))
print(div42by(0))
