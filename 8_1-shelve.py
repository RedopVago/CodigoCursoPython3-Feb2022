
import shelve

# animals = ['Python', 'monkey', 'camel']
# animals = ['Dog', 'Cat', 'BUtterfly']


with shelve.open('shelve') as s:

    # s['second'] = animals


    for i in s:
        print(f'{i}: {s[i]}')

...


# if __name__ == '__main__':

