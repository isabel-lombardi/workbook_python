# Random Lottery Numbers
from random import randint

numbers = []

for i in range(6):
    x = randint(1, 50)
    while x in numbers:
        x = randint(1, 50)
    numbers.append(x)

numbers.sort()
print("Your number are: ")
print(*numbers, sep=", ")


"""Ho provato a svolgere l'esercizio utilizzando le list comprehension, e se non fosse stato per il
"assicurati che non ci siano duplicati" avrei potuto chiudere l'esercizio con le tre righe 
che seguono"

from random import randint

number = [randint(1, 49)for n in range(1, 7)]   # OLD number = [randint(1, 49)for n in range(1, 7)]
number.sort()
print(number)

Anche dopo MOLTI tentativi, non sono riuscita ad ottenere il risultato sperato, e di conseguenza,
ho abbandonato l'idea di utilizzarle le comprehension in questo caso.
"""