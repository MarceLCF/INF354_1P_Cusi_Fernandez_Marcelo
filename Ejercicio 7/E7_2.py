from kanren import run, eq, var, Relation, fact, conde

X = var()
Y = var()
# Define la relación parentesco
parentesco = Relation()


fact(parentesco, ("Abuelo", "Padre"), ("Abuela", "Padre"), ("Padre", "Hijo"), ("Madre", "Hijo"), ("Padre", "Primo"), ("Madre", "Primo"))

print("Realizando algunas consultas)
print("Abuelos:")
abuelos = run(0, X, conde(parentesco(X, "Padre")))
print(abuelos)

print("Primos:")
primos = run(0, X, conde(parentesco("Padre", Y), parentesco(X, Y), X != "Padre"))
print(primos)

print("Hijos:")
hijos = run(0, X, parentesco(X, "Padre"))
print(hijos)
