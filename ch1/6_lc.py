if __name__ == "__main__":
    miles = [100, 10, 9.5, 1000, 30]
    kilometers = [x * 1.60934 for x in miles]
    print ('miles to kilometers:')
    for i, row in enumerate(kilometers):
        print ('{:>4} {:>8}{:>8} {:>2}'.
               format(miles[i],'miles is', round(row,2), 'km'))
    print ('\npet:')
    pet = ['cat', 'dog', 'rabbit', 'parrot', 'guinea pig', 'fish']
    print (pet)
    print ('\npets:')
    pets = [x + 's' if x != 'fish' else x for x in pet]
    print (pets)
    subset = [x for x in pets if x != 'fish' and x != 'rabbits'
              and x != 'parrots' and x != 'guinea pigs']
    print ('\nmost common pets:')
    print (subset[1], 'and', subset[0])
    sales = [9000, 20000, 50000, 100000]
    print ('\nbonuses:')
    bonus = [0 if x < 10000 else x * .02 if x >= 10000 and x <= 20000
             else x * .03 for x in sales]
    print (bonus)
    print ('\nbonus dict:')
    people = ['dave', 'sue', 'al', 'sukki']
    d = {}
    for i, row in enumerate(people):
        d[row] = bonus[i]
    print (d, '\n')
    print ('{:<5} {:<5}'.format('emp', 'bonus'))
    for k, y in d.items():
        print ('{:<5} {:>6}'.format(k, y))
