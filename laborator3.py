#ex1

#picture = [
#[0,0,0,1,0,0,0],
#[0,0,1,1,1,0,0],
#[0,1,1,1,1,1,0],
#[1,1,1,1,1,1,1],
#[0,0,0,1,0,0,0],
#[0,0,0,1,0,0,0]]

#for i in picture:
  #  for j in i:
  #      if j == 0:
  #          print(' ', end='')
   #     else:
   #         print('*', end='')
   # print('')

#ex2

# while True:
#     try:
#         nota = float(input("Introduceți nota (0-10): "))

#         if 0 <= nota <= 10:
#             if nota >= 9:
#                 print("Calificativ: Excelent")
#             elif nota >= 7:
#                 print("Calificativ: Bine")
#             elif nota >= 5:
#                 print("Calificativ: Suficient")
#             else:
#                 print("Calificativ: Reexaminare")
#             break  # Ieșim din buclă pentru că nota a fost validă
#         else:
#             print("Eroare: Nota trebuie să fie între 0 și 10.")
            
#     except ValueError:
#         print("Eroare: Te rugăm să introduci un număr, nu litere sau simboluri.")


#ex3 

# import random

# numar_secret = random.randint(1, 50)
# incercari = 0

# print("Am ales un număr între 1 și 50. Ghicește-l!")

# while True:
#     try:
#         ghicit = int(input("Introduceți numărul (1-50): "))
#         incercari += 1

#         if ghicit < numar_secret:
#             print("Numărul căutat este MAI MARE.")
#         elif ghicit > numar_secret:
#             print("Numărul căutat este MAI MIC.")
#         else:
#             print(f"Felicitări! Ai ghicit numărul în {incercari} încercări.")
#             break
            
#     except ValueError:
#         print("Eroare: Introdu un număr valid!")

#ex4

# orase=["București", "Cluj-Napoca", "Timișoara", "Iași", "Constanța"]

# for i, oras in enumerate(orase):
#     print(f"{i+1}. {oras}")

#ex5

# import random

# print("Bine ai venit la Loteria Python!")
# print("Alege 6 numere între 1 și 49.")

# alese = [int(input(f"Numărul {i+1}: ")) for i in range(6)]

# extrase = random.sample(range(1, 50), 6)

# ghicite = list(set(alese) & set(extrase))
# nr_ghicite = len(ghicite)

# print(f"\nNumere extrase: {extrase}")
# print(f"Ai ghicit {nr_ghicite} numere: {ghicite}")

# if nr_ghicite == 6:
#     print("Felicitări! Ai câștigat MARELE PREMIU!")
# elif nr_ghicite >= 3:
#     print("Felicitări! Ai câștigat un premiu mic!")
# else:
#     print("Mai încearcă! Data viitoare poate ai mai mult noroc.")
    
#ex6

# print("--- Aventură în Pădurea Magică ---")
# inventar = []

# directie = input("Ești la o răscruce. Mergi spre 'stânga' sau 'dreapta'? ").lower()

# if directie == "stânga":
#     print("Ai ajuns la un lac de cristal. Un spiriduș îți oferă o 'baghetă'.")
#     alegere = input("O accepți? (da/nu): ").lower()
#     if alegere == "da":
#         inventar.append("baghetă magică")
#         print("Ai acum o baghetă! Te simți mai puternic.")
#     else:
#         print("Spiridușul s-a supărat și te-a udat din cap până în picioare.")

# elif directie == "dreapta":
#     print("Te-ai întâlnit cu un lup fioros!")
#     if "baghetă magică" in inventar:
#         print("Folosești bagheta și transformi lupul într-un cățeluș prietenos.")
#     else:
#         print("Nu ai arme! Trebuie să fugi repede. În fugă, ai găsit o 'potcoavă' de aur.")
#         inventar.append("potcoavă de aur")

# else:
#     print("Te-ai rătăcit pentru că nu ai ales o direcție validă.")


# print("\n--- Rezumatul aventurii ---")
# if inventar:
#     print(f"Ai terminat aventura cu următoarele obiecte: {', '.join(inventar)}")
# else:
#     print("Inventarul tău este gol, dar ai scăpat cu viață!")
# print("Sfârșit.")

#ex7

# comentariu = input("Introdu un comentariu: ").lower().split()

# pozitive = {"bine", "frumos", "super", "excelent", "minunat"}
# negative = {"urât", "prost", "groaznic", "dezamăgitor"}

# if set(comentariu) & pozitive:
#     print("Comentariu pozitiv!")
# elif set(comentariu) & negative:
#     print("Comentariu negativ!")
# else:
#     print("Comentariu neutru.")

#ex8

# tari_risc = ["Coreea de Nord", "Siria", "Iran"]
# tranzactii_suspecte = 0

# print("--- Sistem Detectare Fraudă Bancară ---")

# while tranzactii_suspecte < 3:
#     print(f"\n(Tranzacții riscante detectate: {tranzactii_suspecte}/3)")
    
#     try:
#         suma = float(input("Sumă tranzacție (RON): "))
#         tara = input("Țara de origine: ")
#     except ValueError:
#         print("Te rog introdu o sumă validă.")
#         continue

#     if tara in tari_risc:
#         print(f"Tranzacție: {suma} RON din {tara} → FRAUDULOASĂ (țară risc ridicat)")
#         tranzactii_suspecte += 1
#     elif suma > 10000:
#         print(f"Tranzacție: {suma} RON din {tara} → SUSPICIOASĂ (sumă mare)")
#         tranzactii_suspecte += 1
#     else:
#         print(f"Tranzacție: {suma} RON din {tara} → SIGURĂ")

# print("\n!!! 3 tranzacții suspecte detectate! CONT BLOCAT !!!")