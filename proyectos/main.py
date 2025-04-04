
def bienvenida():
    print("=" * 60)
    print("🌟 BIENVENIDO AL CUESTIONARIO DE CONOCIMIENTOS GENERALES 🌟")
    print("=" * 60)
    print()
    print("👋 ¡Hola! Prepárate para responder algunas preguntas divertidas.")
    print("📋 Solo necesitas escribir la letra de la opción que creas correcta.")
    print("✅ Por cada respuesta correcta ganarás un punto.")
    print("❌ Por cada incorrecta, no te preocupes, ¡seguirás aprendiendo!")
    print()
bienvenida()
puntaje = 0 #se crearia un contador para el puntaje final.
while True:
    # Pregunta 1
    while True:
        print("\n¿Cuál es el continente más grande del mundo?\n")
        print("1. África")
        print("2. Asia")
        print("3. Europa")
        print("4. América")
        respuesta = input("\nTu respuesta (1-4): ")
        try:
            respuesta = int(respuesta)
            if 1 <= respuesta <= 4:
                if respuesta == 2:
                    print("¡Correcto!")
                    puntaje += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break
            else:
                print("Por favor ingresa un número entre 1 y 4.")
        except ValueError:
            print("Estás ingresando una respuesta no válida. Por favor ingresa un número.")
    # Pregunta 2
    while True:
        print("¿Quién escribió Cien años de soledad?")
        print("1. Mario Vargas Llosa")
        print("2. Gabriel García Márquez")
        print("3. Isabel Allende")
        print("4. Julio Cortázar")
       
        try:
            respuesta = int(respuesta)
            if 1 <= respuesta <= 4:
                if respuesta == 2:
                    puntaje += 1
                    break
                else:
                    break
            else:
                print("Por favor ingresa un número entre 1 y 4.")
        except ValueError:
            print("Estás ingresando una respuesta no válida. Por favor ingresa un número.")

    respuesta = input("\nTu respuesta (1-4): ")
    if respuesta == "2":
        print("¡Correcto!")
        puntaje += 1
    else:
        print("Incorrecto.")
    # Pregunta 3
    while True:
        print("¿En qué año comenzó la Segunda Guerra Mundial?")
        print("1. 1929")
        print("2. 1939")
        print("3. 1941")
        print("4. 1914")        
        respuesta = input("\nTu respuesta (1-4): ")
        try:
            respuesta = int(respuesta)
            if 1 <= respuesta <= 4:
                if respuesta == 2:
                    print("¡Correcto!")
                    puntaje += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break
            else:
                print("Por favor ingresa un número entre 1 y 4.")
        except ValueError:
            print("Estás ingresando una respuesta no válida. Por favor ingresa un número.")
    while True:
        print("¿Cuál es el símbolo químico del oxígeno?")
        print("1. O")
        print("2. O2")
        print("3. Ox")
        print("4. O3")       
        respuesta = input("\nTu respuesta (1-4): ")
        try:
            respuesta = int(respuesta)
            if 1 <= respuesta <= 4:
                if respuesta == 1:
                    print("¡Correcto!")
                    puntaje += 1
                    break
                else:
                    break
            else:
                print("Por favor ingresa un número entre 1 y 4.")
        except ValueError:
            print("Estás ingresando una respuesta no válida. Por favor ingresa un número.")
        # hasta aca las preguntas para la seleccion correcta.
    # ahora seguira el resumen.
    print("\n" + "="*30)
    print(f"Puntaje final: {puntaje}/4")
    if puntaje == 4:
        print("¡Excelente! 🎉")
        print("="*30)
        break
    elif puntaje == 3:
        print("¡Buen trabajo! 👍")
        print("="*30)
        break
    elif puntaje == 2:
        print("Puedes mejorar")
        print("="*30)
        break
    else:
        print("Sigue practicando")
        print("="*30)
        break   