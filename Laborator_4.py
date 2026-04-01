#Exercitiul 1
while True:
    pass

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