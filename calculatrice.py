#Ma première calculatrice en python.
print("===Ma calculatrice===")
nbre1 = float(input("Entrez le premier nombre : "))
operation = input("Choisis une opération (+, -, *, /) : ")
nbre2 = float(input("Entrez le deuxième nombre : "))
if operation == "+" :
  resultat = nbre1 + nbre2
  print("Resultat :", resultat)
elif operation == "-" : 
  resultat = nbre1 - nbre2
  print("Resultat :", resultat)
elif operation == "*" :
  resultat = nbre1 * nbre2
  print("Resultat :", resultat)
elif operation == "/" :
  if nbre2 !=0:
    resultat = nbre1 / nbre2
  print("Resultat :", resultat)
  else :
  print("Erreur : division par zéro impossible.")
else :
print("Opération inconnue")

