

def suma(a, b):
    return a+b

def resta(a, b):
    
    if not type(a) == float or not type(a) == int:
        return 'ERROR'
    return a-b


if __name__ == '__main__':
    print(suma(3,2))