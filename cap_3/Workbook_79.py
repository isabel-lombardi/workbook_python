# Maximum Integer

from random import randint

max_number = randint(1, 100)   #  intero casuale tra 1 e 100
counter = 0

for n in range(1, 99):    # 99 interi casuali aggiuntivi tra 1 e 100
    atm = randint(1, 100)
    if atm > max_number:    # e è più grande del numero massimo incontrato finora.
        max_number = atm    # aggiornare il numero massimo incontrato
        counter += 1              # contare l'aggiornamento.

        print(atm, "<--- New Maximum")
    else:
        print(atm)

print("The maximum value found is: {}". format(max_number))
print("The value has been updated {} times".format(counter))
