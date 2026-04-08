#Exercitiul 1
# while True:
#     pass

    # j1 = input("Jucător 1 alege: ")
    # j2 = input("Jucător 2 alege: ")

    
    # if j1 == j2:
    #     print("Este egalitate!")
    # elif (j1 == "piatra" and j2 == "foarfeca") or \
    #      (j1 == "foarfeca" and j2 == "hartia") or \
    #      (j1 == "hartia" and j2 == "piatra"):
    #     print("Felicitări Jucător 1! Ai câștigat!")
    # else:
    #     print("Felicitări Jucător 2! Ai câștigat!")

    # restart = input("Vreți să mai jucați? (da/nu): ")
    # if restart != "da":
    #     print("Joc încheiat.")
    #     break

#Exercitiul 2
# def generare_factura(client, **produse):
#     print(f"Factura pentru clientul: {client}")
#     total = 0
#     for produs, pret in produse.items():
#         print(f"{produs}: {pret} lei")
#         total += pret
#     print("-" * 30)
#     print(f"Total de plată: {total} lei")   
#     generare_factura("Ion Popescu", {"Laptop": 3000, "Mouse": 150, "Tastatură": 200})       

#Exercitiul 3

# def normalizeaza_date(lista_numere):

#     minim = min(lista_numere)
#     maxim = max(lista_numere)
    
   
#     if maxim == minim:
#         return [0.0] * len(lista_numere)
    
#     lista_noua = []
#     for x in lista_numere:
        
#         rezultat = (x - minim) / (maxim - minim)
#         lista_noua.append(rezultat)
        
#     return lista_noua


# date_test = [10, 20, 30, 40, 50]
# date_normalizate = normalizeaza_date(date_test)

# print("Date originale:", date_test)
# print("Date normalizate:", date_normalizate)

#Exercitiul 4

# my_list = [1, 2, 3]
# rezultat = list(map(lambda x: x**2, my_list))
# print(rezultat) 

#Exercitiul 5

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# sorted_a = sorted(a, key=lambda x: x[1])
# print(sorted_a)

#  Exercitiul 6

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# sorted_a = sorted(a, key=lambda x: x[1])
# print(sorted_a)

# Exercitiul 7

# preturi = [100, None, 50, 200, None, 30]
# preturi_filtrate = filter(lambda x: x is not None, preturi)
# preturi_reduse = map(lambda x: x * 0.9, preturi_filtrate)
# rezultat = list(preturi_reduse)
# print(rezultat)

# Exercitiul 8

# import datetime
# acum = datetime.datetime.now()
# extrage_anul = lambda dt: dt.year
# extrage_luna = lambda dt: dt.month
# extrage_ziua = lambda dt: dt.day
# extrage_ora = lambda dt: dt.strftime("%H:%M:%S.%f")
# print(acum)
# print(extrage_anul(acum))
# print(f"{extrage_luna(acum):02}") 
# print(extrage_ziua(acum))
# print(extrage_ora(acum))

# Exercitiul 9

# list1 = [1, 2, 3, 4, 5] 
# list2 = [10, 20, 30, 40, 50] 

# def sum_lists(l1, l2):
#     return [(a + b,) for a, b in zip(l1, l2)]

# result = sum_lists(list1, list2)
# print(result)

# Exercitiul 10

# pare = [x for x in range(0, 101, 2)]
# cuburi = [x**3 for x in range(1, 11)]
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [3, 4, 5, 6, 7]
# comune = [x for x in lista1 if x in lista2]
# print("Pare:", pare)
# print("Cuburi:", cuburi)
# print("Comune:", comune)

# Exercitiul 11

# pare = {x for x in range(0, 20, 2)}

# text = "programare"
# litere = {char for char in text}

# propozitie = "Python este un limbaj de programare fascinant"
# cuvinte_lungi = {cuv for cuv in propozitie.split() if len(cuv) >= 5}

# print(f"Pare: {pare}")
# print(f"Litere distincte: {litere}")
# print(f"Cuvinte lungi: {cuvinte_lungi}")

#Exercitiul 12

# patrate = {x: x**2 for x in range(1, 11)}

# text = "succes"
# frecventa = {char: text.count(char) for char in text}

# divizori = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}

# print("Pătrate:", patrate)
# print("Frecvență litere:", frecventa)
# print("Divizori:", divizori)