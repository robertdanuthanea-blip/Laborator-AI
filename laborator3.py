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


#ex3 revin are o eroare

import random

numar_secret = random.randint(1, 50)
incercari = 0

print("Am ales un număr între 1 și 50. Ghicește-l!")

while True:
    try:
        ghicit = int(input("Introduceți numărul (1-50): "))
        incercari += 1

        if ghicit < numar_secret:
            print("Numărul căutat este MAI MARE.")
        elif ghicit > numar_secret:
            print("Numărul căutat este MAI MIC.")
        else:
            print(f"Felicitări! Ai ghicit numărul în {incercari} încercări.")
            break
            
    except ValueError:
        print("Eroare: Introdu un număr valid!")

#ex4

# orase=["București", "Cluj-Napoca", "Timișoara", "Iași", "Constanța"]

# for i, oras in enumerate(orase):
#     print(f"{i+1}. {oras}")
    