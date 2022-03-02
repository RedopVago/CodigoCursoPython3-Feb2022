import pickle

def escribir():
    with open('data.dat', 'wb') as file:
        animals = ['Python', 'Monkey', 'Camel']

        pickle.dump(animals, file)

def leer():
    with open('data.dat', 'rb') as file:
        unpickler = pickle.Unpickler(file)  ### read()

        read_animals = unpickler.load()  ### bin --> list

        print(read_animals)


if __name__ == '__main__':

    # escribir()

    leer()