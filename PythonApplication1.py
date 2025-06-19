edad = 10

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 60:
    print("Eres un adulto.")
elif edad == 60:
    print("Felices 60.")
else:
    print("Eres adulto mayor.")


    # -*- coding: utf-8 -*-

edad = int(input("¿Cuántos años tienes? "))

if edad < 0:
    print("Edad no válida.")
elif edad < 12:
    print("Eres un niño o niña.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un joven adulto.")
elif edad < 60:
    print("Eres un adulto.")
elif edad == 60:
    print("¡Felices 60!")
else:
    print("Eres un adulto mayor.")
