import random
import math
import sympy as sp
import pygame
import json
import os
import matplotlib.pyplot as plt

def puntaje(acum):
    clear_shell()
    print("Felicidades por haber completado el juego")
    print("Aquí un breve resumen de tus resutados")
    enter()
    # Etiquetas y datos
    categorias = ['Resp. correctas', 'Resp. incorrectas']
    valores = [acum, 15-acum]

    # Crear el gráfico de barras
    plt.bar(categorias, valores, color=['green', 'red'])

    # Añadir título y etiquetas
    plt.title('Resultados del Jugador')
    plt.xlabel('Tipo de Respuesta')
    plt.ylabel('Cantidad')

    # Mostrar el gráfico
    plt.show()

def resp_correcta():
    print("\n")
    print("¡Respuesta correcta!")    
    print("\n")
    enter()
    return 

def resp_incorrecta():
    print("\n")
    print("Respuesta incorrecta")
    print("\n")
    enter()
    return 

def operaciones_matematicas(puntos):
    aciertos = 0

    # Matriz de preguntas con sus respuestas
    preguntas = [
        ["¿Cuál es el resultado de 8 + 12?", ["a. 20", "b. 21", "c. 22", "d. 23"], "A"],
        ["¿Cuál es el resultado de 15 - 7?", ["a. 7", "b. 8", "c. 9", "d. 10"], "B"],
        ["¿Cuál es el resultado de 6 * 7?", ["a. 42", "b. 48", "c. 36", "d. 40"], "A"],
        ["¿Cuál es el resultado de 64 / 8?", ["a. 6", "b. 7", "c. 8", "d. 9"], "C"],
        ["¿Cuál es la raíz cuadrada de 81?", ["a. 8", "b. 9", "c. 7", "d. 10"], "B"],
        ["Lista: Si tenemos [3, 6, 9, 12], ¿qué número es el resultado de sumar todos sus elementos?", ["a. 21", "b. 30", "c. 36", "d. 24"], "B"],
        ["Lista: Si restamos 2 de cada número en [5, 10, 15], ¿cuál es el nuevo número en la segunda posición?", ["a. 8", "b. 6", "c. 7", "d. 5"], "A"],
        ["Lista: Si tenemos una lista [4, 5, 6, 7], ¿cuál es el resultado de multiplicar el primer y último número?", ["a. 21", "b. 28", "c. 24", "d. 18"], "B"],
        ["¿Cuál es el valor de pi (aproximado)?", ["a. 3.16", "b. 3.15", "c. 3.14", "d. 3.13"], "C"],
        ["¿Cuál es el valor de 10!", ["a. 3628800", "b. 10000", "c. 720", "d. 120"], "A"]
    ]

    print("Tienes 10 preguntas de matemáticas. Cada pregunta correcta te dará 5 puntos, y las incorrectas no te restarán puntos.")

    # Iterar por cada pregunta de la matriz
    for i, pregunta in enumerate(preguntas):
        print(f"\n{i+1}. {pregunta[0]}")
        # Imprimir las opciones del segundo elemento de cada renglón
        for opcion in pregunta[1]:
            print(opcion)

        # Validar la respuesta del usuario
        while True:
            respuesta = input("Respuesta: ").upper()
            if respuesta not in ["A", "B", "C", "D"]:
                print("Por favor, selecciona una opción válida (a, b, c o d).")
            elif respuesta == pregunta[2]:
                resp_correcta()
                aciertos += 1
                break
            else:
                resp_incorrecta()
                break

    clear_shell()
    print(f"Haz terminado las preguntas. Obtuviste {aciertos} aciertos.")
    puntos_ganados = 5 * aciertos
    puntos += puntos_ganados
    print(f"Ganaste {puntos_ganados} puntos. ")
    print("Tus puntos actuales son: {puntos}")

def adivina_palabra(puntos):
    aciertos = 0
    respuestas=[["a. Inercia", "b. Gravedad", "c. Electromagnetismo", "d. Fricción"],["a. Átomo","b. Organismo","c. Célula","d. Tejido"],["a. Elemento","b. Compuesto","c. Molécula","d. Electrón"],["a. Trigonometría","b. Álgebra","c. Geometría","d. Cálculo"],["a. Coeficiente","b. Exponente","c. Porcentaje","d. Logaritmo"],["a. Fórmula del área del círculo","b. Fórmula cuadrática","c. Teorema de Pitágoras","d. Fórmula de derivada"],["a. Épica","b. Fábula","c. Drama","d. Ensayo"],["a. Ética","b. Estética","c. Lógica","d. Metafísica"],["a. Respiración celular","b. Fotosíntesis","c. Fermentación","d. Ciclo de Krebs"],["a. Sistema nervioso","b. Sistema endocrino","c. Sistema digestivo","d. Sistema circulatorio"],]#matriz

    print("Tienes 10 preguntas, y cada una tiene una sola respuesta correcta. Si respondes todas bien, ganas 50 puntos. Cada respuesta incorrecta representa 5 puntos menos que puedes ganar")
    enter()
    print("\n")
    print("1. Es la fuerza que atrae los cuerpos hacia el centro de la Tierra, y es responsable de que todo permanezca en su lugar. ¿Qué es?")
    print("\n")
    primer_renglon = respuestas[0]
    # Imprimir cada elemento del primer renglón en una nueva línea
    for elemento in primer_renglon:
        print(elemento)    
    while (True):
        r1=input("Respuesta: ")
        if(r1.upper() != "A" and r1.upper() != "B" and r1.upper() != "C" and r1.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r1.upper() == "A"):
            resp_incorrecta()
            break
        elif(r1.upper() == "B"):
            resp_correcta()
            aciertos +=1
            break
        elif(r1.upper() == "C"):
            resp_incorrecta()
            break
        elif(r1.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("2. Es la unidad básica de la vida y está presente en todos los seres vivos. Puede ser procariota o eucariota. ¿Qué es?")
    print("\n")
    segundo_renglon = respuestas[1]
    for elemento in segundo_renglon:
        print(elemento)
    while (True):
        r2=input("Respuesta: ")
        if(r2.upper() != "A" and r2.upper() != "B" and r2.upper() != "C" and r2.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r2.upper() == "A"):
            resp_incorrecta()
            break
        elif(r2.upper() == "B"):
            resp_incorrecta()
            break
        elif(r2.upper() == "C"):
            resp_correcta()
            aciertos +=1
            break
        elif(r2.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("3. Es una sustancia que no puede descomponerse en otras más simples mediante procesos químicos. Se encuentra en la tabla periódica. ¿Qué es?")
    print("\n")
    tercer_renglon = respuestas[2]
    for elemento in tercer_renglon:
        print(elemento)    
    while (True):
        r3=input("Respuesta: ")
        if(r3.upper() != "A" and r3.upper() != "B" and r3.upper() != "C" and r3.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r3.upper() == "A"):
            resp_correcta()
            aciertos +=1
            break
        elif(r3.upper() == "B"):
            resp_incorrecta()
            break
        elif(r3.upper() == "C"):
            resp_incorrecta()
            break
        elif(r3.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("4. Es la rama de las matemáticas que se ocupa del estudio de las formas, tamaños y propiedades de las figuras geométricas. ¿Qué es?")
    print("\n")
    cuarto_renglon = respuestas[3]
    for elemento in cuarto_renglon:
        print(elemento)    
    while (True):
        r4=input("Respuesta: ")
        if(r4.upper() != "A" and r4.upper() != "B" and r4.upper() != "C" and r4.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r4.upper() == "A"):
            resp_incorrecta()
            break
        elif(r4.upper() == "B"):
            resp_incorrecta()
            break
        elif(r4.upper() == "C"):
            resp_correcta()
            aciertos +=1
            break
        elif(r4.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("5. Es un número que representa una cantidad sobre un total, expresado como una fracción con denominador 100. ¿Qué es?")
    print("\n")
    quinto_renglon = respuestas[4]
    for elemento in quinto_renglon:
        print(elemento)    
    while (True):
        r5=input("Respuesta: ")
        if(r5.upper() != "A" and r5.upper() != "B" and r5.upper() != "C" and r5.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r5.upper() == "A"):
            resp_incorrecta()
            break
        elif(r5.upper() == "B"):
            resp_incorrecta()
            break
        elif(r5.upper() == "C"):
            resp_correcta()
            aciertos +=1
            break
        elif(r5.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("6. Es la fórmula que se utiliza para encontrar las raíces de una ecuación cuadrática. ¿Cuál es?")
    print("\n")
    sexto_renglon = respuestas[5]
    for elemento in sexto_renglon:
        print(elemento)    
    while (True):
        r6=input("Respuesta: ")
        if(r6.upper() != "A" and r6.upper() != "B" and r6.upper() != "C" and r6.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r6.upper() == "A"):
            resp_incorrecta()
            break
        elif(r6.upper() == "B"):
            resp_correcta()
            aciertos +=1
            break
        elif(r6.upper() == "C"):
            resp_incorrecta()
            break
        elif(r6.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("7. Es un género literario en el que se narra la historia de héroes y dioses mitológicos, con obras clásicas como 'La Ilíada' y 'La Odisea'. ¿Qué género es?")
    print("\n")
    septimo_renglon = respuestas[6]
    for elemento in septimo_renglon:
        print(elemento)    
    while (True):
        r7=input("Respuesta: ")
        if(r7.upper() != "A" and r7.upper() != "B" and r7.upper() != "C" and r7.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r7.upper() == "A"):
            resp_correcta()
            aciertos +=1
            break
        elif(r7.upper() == "B"):
            resp_incorrecta()
            break
        elif(r7.upper() == "C"):
            resp_incorrecta()
            break
        elif(r7.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("8. Es una rama de la filosofía que estudia los principios fundamentales del conocimiento, la realidad y la existencia. ¿Qué es?")
    print("\n")
    octavo_renglon = respuestas[7]
    for elemento in octavo_renglon:
        print(elemento)    
    while (True):
        r8=input("Respuesta: ")
        if(r8.upper() != "A" and r8.upper() != "B" and r8.upper() != "C" and r8.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r8.upper() == "A"):
            resp_incorrecta()
            break
        elif(r8.upper() == "B"):
            resp_incorrecta()
            break
        elif(r8.upper() == "C"):
            resp_incorrecta()
            enter()
            break
        elif(r8.upper() == "D"):
            resp_correcta()
            aciertos +=1
            break
    print("\n")
    print("9. Es el proceso mediante el cual las plantas convierten la luz solar en energía química, produciendo oxígeno como subproducto. ¿Qué es?")
    print("\n")
    noveno_renglon = respuestas[8]
    for elemento in noveno_renglon:
        print(elemento)    
    while (True):
        r9=input("Respuesta: ")
        if(r9.upper() != "A" and r9.upper() != "B" and r9.upper() != "C" and r9.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r9.upper() == "A"):
            resp_incorrecta()
            break
        elif(r9.upper() == "B"):
            resp_correcta()
            aciertos +=1
            break
        elif(r9.upper() == "C"):
            resp_incorrecta()
            enter()
            break
        elif(r9.upper() == "D"):
            resp_incorrecta()
            break
    print("\n")
    print("10. Es el sistema del cuerpo humano encargado de transportar oxígeno y nutrientes a través de la sangre. ¿Qué sistema es?")
    print("\n")
    decimo_renglon = respuestas[9]
    for elemento in decimo_renglon:
        print(elemento)    
    while (True):
        r10=input("Respuesta: ")
        if(r10.upper() != "A" and r10.upper() != "B" and r10.upper() != "C" and r10.upper() != "D"):
            print("Seleccione una opción válida")
        elif(r10.upper() == "A"):
            resp_incorrecta()
            break
        elif(r10.upper() == "B"):
            resp_incorrecta()
            break
        elif(r10.upper() == "C"):
            resp_incorrecta()
            enter()
            break
        elif(r10.upper() == "D"):
            resp_correcta()
            aciertos +=1
            break
    clear_shell()
    print("Haz terminado las preguntas")
    print("\n")
    print("Obtuviste ", aciertos, " aciertos")
    print("\n")
    puntos = puntos + (5*aciertos)
    print("Ganaste ", 5*aciertos, " puntos")
    print("Tus puntos actuales son: ", puntos)
    enter()
    clear_shell()

def mini_game(puntos):
    clear_shell()
    print("¡¡Bienvenido a la opción de mini juego!!")
    while (True):
        print("Elige un juego:")
        print("1. Adivina la palabra")
        print("2. Realiza operaciones matemáticas")
        print("3. Salir")
        op = int(input("Ingresa la opción que desees: "))
        if (op != 1 and op != 2 and op != 3):
            clear_shell()
            print("Ingresa una opción válida")
        if (op == 3):
            clear_shell()
            while (True):
                salir = input(("¿Estás segur@ que quieres salir? s/n: "))
                if (salir.upper() != "S" and salir.upper() != "N"):
                    print("Ingresa s/n")
                if (salir.upper() == "N"):
                    clear_shell()
                    break
                else:
                    clear_shell()
                    break
        if (op == 1):
            clear_shell()
            print("¡¡Bienvenido al juego de adivinar la palabra!!")
            adivina_palabra(puntos)
        elif(op == 2):
            clear_shell()
            print("¡¡Bienvenido al juego de operaciones matemáticas!!")
            operaciones_matematicas(puntos)
        break        


def clear_shell():
    for i in range(100):
        print("\n")


def enter():
    return input("\nPresiona enter para continuar...")


def guardar_progreso(puntos, pistas, segundaop):
    progreso = {"puntos": puntos, "pistas": pistas, "segundaop": segundaop}
    with open('progreso.json', 'w') as archivo:
        json.dump(progreso, archivo)
    print("Progreso guardado.")


def cargar_progreso():
    if os.path.exists('progreso.json'):
        with open('progreso.json', 'r') as archivo:
            progreso = json.load(archivo)
            return progreso.get("puntos",
                                100), progreso.get("pistas", 0), progreso.get(
                                    "segundaop", 0)
    else:
        return 100, 0, 0  # Valores por defecto si no hay archivo


def sonido_menu():
    # Inicializa el mixer de Pygame
    pygame.init()
    # Carga el archivo de sonido
    pygame.mixer.music.load('MENU_SOUND.mp3')
    # Reproduce el sonido en bucle infinito
    pygame.mixer.music.play(-1)


def sonido_preguntas():
    pygame.mixer.init()
    pygame.mixer.music.load('PREGUNTAS_SOUND.mp3')
    pygame.mixer.music.play(-1)


def silencio():
    pygame.mixer.music.stop()


def menu(puntos, pistas, segundaop):
    print("====INICIAR AVENTURA====")
    name = input("Ingresa tu nombre: ")
    sonido_menu()
    while (True):
        print("====MENÚ====")
        print(
            "Selecciona una opción, recuerda que debes seleccionar el número de opción"
        )
        print("1. Iniciar aventura")
        print("2. Continuar Historia")
        print("3. Consultar tus puntos")
        print("4. Progreso")
        print("5. Ayuda")
        print("6. SALIR")
        print("==================")
        opm = int(input())  #opm opción menú
        if (opm != 1 and opm != 2 and opm != 3 and opm != 4 and opm != 5):
            clear_shell()
            print(
                "Selecciona una opción valida dentro del rango mencionado\nIntenta de nuevo"
            )
        if (opm == 5):
            clear_shell()
            while (True):
                salir = input(("¿Estás segur@ que quieres salir? s/n: "))
                if (salir.upper() != "S" and salir.upper() != "N"):
                    print("Ingresa s/n")
                if (salir.upper() == "N"):
                    clear_shell()
                    break
                else:
                    clear_shell()
                    break
            if (salir.upper() == "S"):
                guardar_progreso(puntos, pistas, segundaop)
                print("Gracias por jugar", "\nVuleve pronto!!")
                break

        elif (opm == 1):
            iniciar_aventura(puntos, pistas, segundaop)

        elif (opm == 2):
            apocalipsis_ecap(puntos, pistas, segundaop, name)
        elif (opm == 3):
            consultar_puntos(puntos, pistas, segundaop)

#         elif(opm == 4):
#             progreso()
        elif (opm == 4):
            ayuda()


def consultar_puntos(puntos, pistas, segundaop):

    clear_shell()
    silencio()
    print("Tus puntos actuales son: ", puntos)
    print("Tienes ", pistas, " pistas")
    print("Tienes ", segundaop, " segundas oportunidades")
    print("\n")
    while (True):
        print("1. Consultar tienda")
        print("2. Volver al menú")
        print("3. Ganar más puntos")
        op = int(input())
        if (op == 1):
            tienda(puntos, pistas, segundaop)
        elif (op == 2):
            clear_shell()
            menu(puntos, pistas, segundaop)
        elif (op == 3):
            mini_game(puntos)


def tienda(puntos, pistas, segundaop):
    clear_shell()
    print("$$$$$~~TIENDA~~$$$$$")
    print("\n")
    print("Tus puntos actuales son: ", puntos)
    print("Tienes ", pistas, " pistas")
    print("Tienes ", segundaop, " segundas oportunidades")
    print("\n")
    precios = [["Código", "Producto", "        Precio"],
               [1, "Pista", "                20 puntos"],
               [2, "Segunda oportunidad", "50 puntos"]]
    for r in range(0, len(precios), 1):
        for c in range(0, len(precios[r]), 1):
            print(precios[r][c], end="\t")
        print()  #salto de linea
    print("\n\n")
    print()
    while (True):
        print("¿Deseas comprar algo? s/n")
        op = input()
        if (op.upper() != "S" and op.upper() != "N"):
            print("Ingresa s/n")
        if (op.upper() == "N"):
            clear_shell()
            break
        elif (op.upper() == "S"):
            print("\n")
            print("Ingresa el código del producto que deseas comprar: ")
            codigo = int(input())
            if (codigo == 1):
                if (puntos >= 20):
                    puntos = puntos - 20
                    pistas = pistas + 1
                    print("¡Compra realizada con éxito!")
                    enter()
                    print("\n")
                    consultar_puntos(puntos, pistas, segundaop)
                elif (puntos < 20):
                    print("\n")
                    print("No tienes suficientes puntos")
                    print("Esfuérzate más para conseguir más puntos")
                    enter()
                    print("\n")
                    consultar_puntos(puntos, pistas, segundaop)
            elif (codigo == 2):
                if (puntos >= 50):
                    puntos = puntos - 50
                    segundaop = segundaop + 1
                    print("¡Compra realizada con éxito!")
                    enter()
                    print("\n")
                    consultar_puntos(puntos, pistas, segundaop)
                elif (puntos < 50):
                    print("\n")
                    print("No tienes suficientes puntos")
                    print("Esfuérzate más para conseguir más puntos")
                    enter()
                    print("\n")
                    consultar_puntos(puntos, pistas, segundaop)


def ayuda():
    clear_shell()
    print("Opción ayuda\n\nAquí puedes encontras cómo funciona el juego")
    print("En este juego, vivirás una aventura dividida en 5 capítulos.")
    print("\n")
    print(
        "Cada capítulo contiene 3 preguntas relacionadas con un área matemática:"
    )
    print("1. Aritmética")
    print("2. Álgebra")
    print("3. Geometría")
    print("4. Trigonometría")
    print("5. Cálculo")
    print("\n")
    print(
        "Las preguntas estarán adaptadas al contexto de la historia que se cuenta en cada capítulo."
    )
    print("\nReglas del juego:")
    print("1. Comienzas el juego con 100 puntos.")
    print("2. Cuentas con 1 pista y 1 segunda oportunidad.")
    print(
        "3. Puedes usar tus puntos para obtener pistas y segundas oportunidades"
    )
    print("   - Las pistas cuestan 20 puntos.")
    print("   - Las segundas oportunidades cuestan 50 puntos.")
    print(
        "   - Si te equivocas, puedes tener una segunda oportunidad seleccionando 'Volver a intentarlo'."
    )
    print(
        "   - Si respondes correctamente una pregunta, sumarás 10 puntos a tu cuenta."
    )
    print(
        "3. Si respondes correctamente más del 80% de las preguntas de la historia, se considerará como completada exitosamente."
    )
    print(
        "\n¡Recuerda gestionar bien tus puntos para poder avanzar en la historia y llegar al final!"
    )
    print("¡Buena suerte y disfruta de la aventura!.")
    print("\nPresiona enter para volver al menú")
    input()
    clear_shell()


def apo_problema2(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 2===============")

    while (True):
        rp2 = random.randint(20, 60)  # rp2 random problema 2
        if (rp2 % 3 == 0):
            break

    print("\n")
    print(
        "En su camino hacia el norte, encuentran un río contaminado. Usan filtros para purificar agua a un ritmo de 3 litros por hora y necesitan al menos",
        rp2, "litros para continuar su viaje.")
    print("\n")

    sp2 = rp2 / 3  # sp2 = solución problema 2
    i = 0
    max_i = 2

    while i < max_i:
        print(f"¿Cuántas horas necesitan para purificar {rp2} litros de agua?")
        try:
            resp2 = float(
                input())  # resp2 = respuesta ingresada por el usuario
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if sp2 == resp2:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! Sara y tú deben esperar {sp2} horas para tener {rp2} litros de agua purificada."
            )
            apo_problema3(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(f"La respuesta correcta es {sp2} horas.")
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_problema2(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_problema3(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_problema3(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 3===============")
    print("\n")

    rp3 = random.randint(4, 6)  # rp3 random problema 3

    print(
        "Sara y tú caminan hacia el refugio al norte, avanzando a un ritmo de",
        rp3, "km por hora durante un máximo de 6 horas diarias.")

    sp3 = 180 / (rp3 * 6)  # sp3 = solución problema 3
    i = 0
    max_i = 2

    while i < max_i:
        try:
            resp3 = float(
                input(
                    "Si el refugio está a 180 km de distancia, ¿cuántos días les tomará llegar? "
                ))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if sp3 == resp3:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! Sara y tú deben caminar durante {sp3} días para llegar al refugio."
            )
            apo_cap2pro1(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(f"La respuesta correcta es {sp3} días.")
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_problema3(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap2pro1(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap2pro1(acum, puntos, pistas, segundaop):
    silencio()
    print("\n")
    enter()
    clear_shell()
    print("~~~~~~~~~~CAPITULO 2~~~~~~~~~")
    print("\n")
    print(
        "Al pasar unos días, Sara y tú avanzan hacia el norte, pero la tensión crece entre ustedes. Cada uno teme que el otro esconda algo, por lo que deciden dividir sus recursos para mantener el equilibrio y tener una mayor tranquilidad."
    )
    print("\n")
    enter()
    print("===============Problema 1===============")
    print("\n")
    sonido_preguntas()
    while (True):
        raciones = random.randint(50, 100)
        if (raciones % 2 == 0):
            break
    while (True):
        botellas = random.randint(50, 100)
        if (botellas % 2 == 0):
            break
    print(
        "Sara y tú tienen", raciones, "raciones de comida y", botellas,
        "botellas de agua. Deciden dividir todo de manera equitativa, pero también quieren tener una reserva extra de 10 raciones de comida y 8 botellas de agua para emergencias."
    )
    print(
        "Si reservan las cantidades extra, ¿cuántas raciones le tocan a cada uno?"
    )

    i = 0
    max_i = 2

    while i < max_i:
        try:
            resp4r = int(input("Introduce las raciones de comida: "))
            resp4b = int(input("Introduce las botellas de agua: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        sp4r = (raciones - 10) / 2  # Solución problema raciones
        sp4b = (botellas - 8) / 2  # Solución problema botellas

        if (sp4r == resp4r and sp4b == resp4b):
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! Sara y tú deben repartir {sp4r} raciones y {sp4b} botellas de agua."
            )
            apo_cap2pro2(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"Las respuestas correctas son {sp4r} raciones y {sp4b} botellas."
                )
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap2pro1(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap2pro2(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap2pro2(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 2===============")
    print("\n")
    print(
        "Tienes una idea para moverse más rápido: alternar la velocidad según la situación del terreno. Propones caminar a 'x' km/h en terrenos planos y 'x + 2' km/h en bajadas. En una jornada de 6 horas, recorren 2 horas en terreno plano y 4 horas en bajadas."
    )
    while (True):
        km = random.randint(20, 60)
        if ((km - 8) % 6 == 0):
            break
    print(
        f"Si recorren un total de {km} km en ese día, ¿cuál es el valor de x?")

    i = 0
    max_i = 2

    while i < max_i:
        try:
            resc2p2 = int(input("Introduce el valor de x: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        sc2p2 = (km - 8) / 6  # Solución problema 2

        if sc2p2 == resc2p2:
            acum += 1
            puntos += 10
            print(f"¡Correcto! Su velocidad en ese día fue de {sc2p2} km/h.")
            apo_cap2pro3(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(f"La respuesta correcta es {sc2p2} km/h.")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip2 = int(input())
                if rip2 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap2pro2(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip2 == 2:
                    apo_cap2pro3(acum, puntos, pistas, segundaop)
                elif rip2 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap2pro3(acum, puntos, pistas, segundaop):
    horas = random.randint(6, 12)
    while horas % 3 != 0:
        horas = random.randint(6, 12)
    print("\n")
    enter()
    print("===============Problema 3===============")
    print("\n")
    print(
        f"Sara y tú deciden hacer guardias nocturnas para protegerse de peligros. Sara se ofrece a hacer el doble de horas de guardia que tú, pero solo pueden hacer un total de {horas} horas de vigilancia por noche."
    )
    print("¿Cuántas horas de guardia hace cada uno?")

    i = 0
    max_i = 2

    sc2p3_Sara = (horas / 3) * 2  # Solución problema guardia Sara
    sc2p3 = (horas / 3)  # Solución problema guardia usuario

    while i < max_i:
        try:
            resc2p3_Sara = int(input("¿Cuántas horas de guardia hará Sara?: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if sc2p3_Sara == resc2p3_Sara:
            print(
                f"¡Correcto! Las horas de guardia que hará Sara son: {sc2p3_Sara} horas."
            )
            try:
                resc2p3 = int(input("¿Cuántas horas de guardia harás tú?: "))
            except ValueError:
                print("Por favor ingresa un número válido.")
                continue

            if sc2p3 == resc2p3:
                acum += 1
                puntos += 10
                print(
                    f"¡Correcto! Las horas de guardia que harás tú son: {sc2p3} horas."
                )
                apo_cap3pro1(acum, puntos, pistas, segundaop)
                return
            else:
                i += 1
                print(f"Incorrecto. Te quedan {max_i - i} intentos.")
                if i == max_i:
                    print(f"La respuesta correcta es {sc2p3} horas.")
                    print(
                        "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                    )
                    rip3 = int(input())
                    if rip3 == 1:
                        if (segundaop >= 1):
                            print(
                                "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                            )
                            segundaop -= 1
                            enter()
                            apo_cap2pro3(acum, puntos, pistas, segundaop)
                        else:
                            print("\n")
                            print("No cuentas con segundas oportunidades")
                            while (True):
                                print("¿Deseas consultar la tienda? s/n")
                                op = input()
                                if (op.upper() != "S" and op.upper() != "N"):
                                    print("Ingresa s/n")
                                if (op.upper() == "N"):
                                    clear_shell()
                                    break
                                elif (op.upper() == "S"):
                                    tienda(puntos, pistas, segundaop)
                    elif rip3 == 2:
                        apo_cap3pro1(acum, puntos, pistas, segundaop)
                    elif rip3 == 3:
                        clear_shell()
                        menu(puntos, pistas, segundaop)
                    return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(f"La respuesta correcta es {sc2p3_Sara} horas.")
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap2pro3(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap3pro1(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap3pro1(acum, puntos, pistas, segundaop):
    silencio()
    clear_shell()
    print("~~~~~~~~~~CAPITULO 3~~~~~~~~~")
    print(
        "Durante el viaje, Sara y tú encuentran una torre alta, perfecta para observar el terreno, pero rota y peligrosa de escalar. Usan sus habilidades para calcular medidas y planificar su ascenso."
    )
    print("\n")
    print(
        "Sara y tú encuentran una torre y necesitan calcular su altura usando la semejanza de triángulos."
    )
    print("\n")
    enter()
    print("===============Problema 1===============")
    print("\n")
    sonido_preguntas()
    sombra_torre = random.randint(10, 20)
    sombra_sara = random.randint(1, 3)
    altura_sara = round(random.uniform(1.5, 2), 2)
    print(
        f"La torre tiene una sombra de {sombra_torre} m y Sara, con una altura de {altura_sara} m, proyecta una sombra de {sombra_sara} m."
    )

    i = 0
    max_i = 2
    altura_torre = (altura_sara / sombra_sara) * sombra_torre
    error_margin = 0.1  # Margen de error para respuestas decimales

    while i < max_i:
        try:
            resp1 = float(
                input(
                    "¿Cuál es la altura de la torre? (Responde en metros): "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if abs(resp1 - altura_torre) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! La altura de la torre es {altura_torre:.2f} metros."
            )
            apo_cap3pro2(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"La respuesta correcta está entre {altura_torre - error_margin:.2f} y {altura_torre + error_margin:.2f} metros."
                )
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap3pro1(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap3pro2(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap3pro2(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 2===============")
    print("\n")

    area_refugio = random.randint(10, 30)
    print(
        f"En la cima de la torre hay un refugio cuadrado con un área de {area_refugio} m²."
    )

    i = 0
    max_i = 2
    lado_refugio = math.sqrt(area_refugio)
    error_margin = 0.1  # Margen de error para respuestas decimales

    while i < max_i:
        try:
            resp2 = float(
                input(
                    "¿Cuál es la longitud de cada lado del refugio? (Responde en metros): "
                ))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if abs(resp2 - lado_refugio) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! Cada lado del refugio mide {lado_refugio:.2f} metros."
            )
            apo_cap3pro3(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"La respuesta correcta está entre {lado_refugio - error_margin:.2f} y {lado_refugio + error_margin:.2f} metros."
                )
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap3pro2(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap3pro3(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap3pro3(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 3===============")
    print("\n")

    longitud_escalera = random.randint(8, 15)
    angulo = random.randint(25, 35)
    print(
        f"Una escalera rota mide {longitud_escalera} m de largo y forma un ángulo de {angulo}° con el suelo."
    )

    i = 0
    max_i = 2
    altura_escalera = longitud_escalera * math.sin(math.radians(angulo))
    error_margin = 0.1  # Margen de error para respuestas decimales

    while i < max_i:
        try:
            resp3 = float(
                input(
                    "¿Qué tan lejos del suelo está la parte superior de la escalera? (Responde en metros): "
                ))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if abs(resp3 - altura_escalera) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! La parte superior de la escalera está a {altura_escalera:.2f} metros del suelo."
            )
            apo_cap4pro1(acum, puntos, pistas,
                         segundaop)  # Continuar al siguiente capítulo
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"La respuesta correcta está entre {altura_escalera - error_margin:.2f} y {altura_escalera + error_margin:.2f} metros."
                )
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap3pro3(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap4pro1(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap4pro1(acum, puntos, pistas, segundaop):
    silencio()
    clear_shell()
    print("~~~~~~~~~~CAPITULO 4~~~~~~~~~")
    print(
        "Sara y tu alcanzan una colina desde la que pueden ver el refugio del que hablaba la radio, pero entre ellos hay un valle y un río ancho. Tendrán que calcular bien sus movimientos."
    )
    print("\n")
    print("En la colina y deben calcular la distancia al otro lado de un río.")
    print("\n")
    enter()
    print("===============Problema 1===============")
    print("\n")
    sonido_preguntas()
    altura_colina = random.randint(30, 70)
    angulo_depresion = random.randint(15, 25)
    print(
        f"Desde la colina, estiman que el ángulo de depresión hacia la otra orilla del río es de {angulo_depresion}° y que la colina tiene {altura_colina} m de altura."
    )
    resp1 = float(input("¿Cuál es la anchura del río? (Responde en metros): "))

    # Solución esperada
    anchura_rio = altura_colina / math.tan(math.radians(angulo_depresion))
    error_margin = 0.1  # Margen de error para respuestas decimales

    if abs(resp1 - anchura_rio) <= error_margin:
        acum += 1
        puntos += 10
        print(
            f"¡Correcto! La anchura del río es aproximadamente {anchura_rio:.2f} metros."
        )
        apo_cap4p2(acum, puntos, pistas, segundaop)
    else:
        print("Incorrecto.")
        print(
            f"La respuesta correcta está entre {anchura_rio - error_margin:.2f} y {anchura_rio + error_margin:.2f} metros."
        )
        print(
            "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
        )
        rip1 = int(input())
        if rip1 == 1:
            if (segundaop >= 1):
                print("\n¡Has utilizado con éxito una segunda oportunidad!\n")
                segundaop -= 1
                enter()
                apo_cap4pro1(acum, puntos, pistas, segundaop)
            else:
                print("\n")
                print("No cuentas con segundas oportunidades")
                while (True):
                    print("¿Deseas consultar la tienda? s/n")
                    op = input()
                    if (op.upper() != "S" and op.upper() != "N"):
                        print("Ingresa s/n")
                    if (op.upper() == "N"):
                        clear_shell()
                        break
                    elif (op.upper() == "S"):
                        tienda(puntos, pistas, segundaop)
        elif rip1 == 2:
            apo_cap4p2(acum, puntos, pistas, segundaop)
        elif rip1 == 3:
            clear_shell()
            menu(puntos, pistas, segundaop)


def apo_cap4p2(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 2===============")
    print("\n")

    distancia = random.randint(500, 1500)
    altura_refugio = random.randint(50, 150)
    print(
        f"El refugio está a {distancia} m de distancia y {altura_refugio} m más elevado que la colina desde la que observan."
    )
    resp2 = float(
        input(
            "¿Cuál es el ángulo de elevación desde la colina hasta el refugio? (Responde en grados): "
        ))

    # Solución esperada
    angulo_elevacion = math.degrees(math.atan(altura_refugio / distancia))
    error_margin = 0.1  # Margen de error para respuestas decimales

    if abs(resp2 - angulo_elevacion) <= error_margin:
        acum += 1
        puntos += 10
        print(
            f"¡Correcto! El ángulo de elevación es aproximadamente {angulo_elevacion:.2f}°."
        )
        apo_cap4p3(acum, puntos, pistas, segundaop)
    else:
        print("\n")
        print("Incorrecto.")
        print("\n")
        print(
            f"La respuesta correcta está entre {angulo_elevacion - error_margin:.2f}° y {angulo_elevacion + error_margin:.2f}°."
        )
        print(
            "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
        )
        rip2 = int(input())
        if rip2 == 1:
            if (segundaop >= 1):
                print("\n¡Has utilizado con éxito una segunda oportunidad!\n")
                segundaop -= 1
                enter()
                apo_cap4p2(acum, puntos, pistas, segundaop)
            else:
                print("\n")
                print("No cuentas con segundas oportunidades")
                while (True):
                    print("¿Deseas consultar la tienda? s/n")
                    op = input()
                    if (op.upper() != "S" and op.upper() != "N"):
                        print("Ingresa s/n")
                    if (op.upper() == "N"):
                        clear_shell()
                        break
                    elif (op.upper() == "S"):
                        tienda(puntos, pistas, segundaop)
        elif rip2 == 2:
            apo_cap4p3(acum, puntos, pistas, segundaop)
        elif rip2 == 3:
            clear_shell()
            menu(puntos, pistas, segundaop)


def apo_cap4p3(acum, puntos, pistas, segundaop):
    print("\n")
    enter()
    print("===============Problema 3===============")
    print("\n")

    longitud_cuerda = random.randint(20, 40)
    angulo_pendiente = random.randint(30, 50)
    print(
        f"Sara y tu deben usar una cuerda de {longitud_cuerda} m para bajar una pendiente inclinada {angulo_pendiente}°."
    )
    resp3 = float(
        input(
            "¿Cuál es la distancia vertical que descenderán? (Responde en metros): "
        ))

    # Solución esperada
    longitud = 0
    distancia_vertical = longitud
    distancia_vertical = longitud_cuerda * math.sin(
        math.radians(angulo_pendiente))
    error_margin = 0.1  # Margen de error para respuestas decimales

    if abs(resp3 - distancia_vertical) <= error_margin:
        acum += 1
        puntos += 10
        print(
            f"¡Correcto! La distancia vertical que descenderán es aproximadamente {distancia_vertical:.2f} metros."
        )
        # Aquí podrías continuar con el siguiente capítulo o actividad
        print("Has completado el Capítulo 4.")
        apo_cap5pro1(acum, puntos, pistas, segundaop)
    else:
        print("\n")
        print("Incorrecto.")
        print("\n")
        print(
            f"La respuesta correcta está entre {distancia_vertical - error_margin:.2f} y {distancia_vertical + error_margin:.2f} metros."
        )
        print(
            "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
        )
        rip3 = int(input())
        if rip3 == 1:
            if (segundaop >= 1):
                print("\n¡Has utilizado con éxito una segunda oportunidad!\n")
                segundaop -= 1
                enter()
                apo_cap4p3(acum, puntos, pistas, segundaop)
            else:
                print("\n")
                print("No cuentas con segundas oportunidades")
                while (True):
                    print("¿Deseas consultar la tienda? s/n")
                    op = input()
                    if (op.upper() != "S" and op.upper() != "N"):
                        print("Ingresa s/n")
                    if (op.upper() == "N"):
                        clear_shell()
                        break
                    elif (op.upper() == "S"):
                        tienda(puntos, pistas, segundaop)
        elif rip3 == 2:
            # Continuar con la siguiente sección o capítulo
            apo_cap5pro1(acum, puntos, pistas, segundaop)
        elif rip3 == 3:
            clear_shell()
            menu(puntos, pistas, segundaop)


def apo_cap5pro1(acum, puntos, pistas, segundaop):
    silencio()
    clear_shell()
    print("~~~~~~~~~~CAPÍTULO 5: El Viaje Final~~~~~~~~~")
    print(
        "Has llegado a la última etapa de tu viaje. Sara y tu están a punto de alcanzar su destino final, pero antes de llegar, tendrán que resolver problemas que pondrán a prueba su conocimiento de cálculo. Con cada problema que resuelvas, ayudarás a los protagonistas a dar un paso más cerca de su refugio."
    )
    enter()
    print("==========Problema 1==========")
    print(
        "A medida que se acercan a su destino, el terreno se vuelve más irregular y escarpado. Sara necesita calcular la pendiente de una colina para decidir si es seguro avanzar. Ayúdala calculando la derivada de la función que describe el terreno"
    )
    print("\n")
    sonido_preguntas()
    # Generar coeficientes aleatorios para la función
    x = sp.symbols('x')  # Definir la variable
    coef_f1 = random.randint(1, 5)
    coef_f2 = random.randint(1, 5)
    coef_f3 = random.randint(1, 5)

    funcion = coef_f1 * x**3 - coef_f2 * x**2 + coef_f3 * x
    print(
        f"La función que modela el terreno es f(x) = {coef_f1}x^3 - {coef_f2}x^2 + {coef_f3}x."
    )
    print("Calcula la derivada de la función.")

    # Derivada simbólica
    derivada_funcion = sp.diff(funcion, x)
    derivada_funcion = sp.sympify(derivada_funcion)

    # Generar un valor aleatorio para evaluar la derivada
    valor_x = random.randint(1, 5)
    valor_derivada = derivada_funcion.subs(x, valor_x).evalf()

    i = 0
    max_i = 2
    while i < max_i:
        try:
            resp1 = float(
                input(
                    f"¿Cuál es el valor de la derivada en x = {valor_x}? (Responde en metros por km): "
                ))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        error_margin = 0.5

        if abs(resp1 - valor_derivada) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! El valor de la derivada en x = {valor_x} es aproximadamente {valor_derivada:.2f}."
            )
            apo_cap5pro2(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"La respuesta correcta es aproximadamente {valor_derivada:.2f}."
                )
            else:
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap5pro1(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap5pro2(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap5pro2(acum, puntos, pistas, segundaop):
    clear_shell()
    enter()
    print("==========Problema 2==========")
    print(
        "Después de superar la colina, encuentran un lago que deben bordear. Para estimar el tiempo que les tomará rodearlo, Sara necesita calcular el área bajo una curva que representa la orilla del lago. Ayúdala resolviendo la integral."
    )
    print("\n")
    # Generar coeficientes aleatorios para la función de la integral
    x = sp.symbols('x')
    coef_i1 = random.randint(1, 3)
    coef_i2 = random.randint(1, 3)

    funcion_integral = coef_i1 * x**2 + coef_i2 * x
    print(f"La función es f(x) = {coef_i1}x^2 + {coef_i2}x.")
    print("Calcula la integral de la función desde 0 hasta un valor dado.")

    # Generar el límite superior para la integral
    limite_superior = random.randint(2, 5)
    integral_funcion = sp.integrate(funcion_integral,
                                    (x, 0, limite_superior)).evalf()

    i = 0
    max_i = 2
    while i < max_i:
        try:
            resp2 = float(
                input(
                    f"¿Cuál es el valor de la integral desde 0 hasta {limite_superior}? "
                ))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        error_margin = 1  # Margen más amplio debido a la naturaleza de los cálculos de integrales

        if abs((resp2) - integral_funcion) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! El valor de la integral es aproximadamente {integral_funcion:.2f}."
            )
            apo_cap5pro3(acum, puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(
                    f"La respuesta correcta es aproximadamente {integral_funcion:.2f}."
                )
            else:
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap5pro2(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    apo_cap5pro3(acum, puntos, pistas, segundaop)
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apo_cap5pro3(acum, puntos, pistas, segundaop):
    clear_shell()
    enter()
    print("===========Problema 3==========")
    print(
        "Sara y tu están a punto de cruzar un puente inestable. Antes de cruzarlo, necesitan calcular cuánta variación en su posición será segura. Usa la diferencial para ayudarlos a calcular el desplazamiento y evitar el peligro."
    )
    print("\n")

    # Generar coeficientes aleatorios para la función
    x = sp.symbols('x')
    coef_f1 = random.randint(1, 5)
    coef_f2 = random.randint(1, 5)

    funcion = coef_f1 * x**2 + coef_f2 * x
    derivada_funcion = sp.diff(funcion, x)

    print(
        f"La función que modela el desplazamiento es f(x) = {coef_f1}x^2 + {coef_f2}x."
    )
    print("Calcula la diferencial df para un valor dado de dx.")

    # Generar valores aleatorios para x y dx
    valor_x = random.randint(1, 5)
    dx = random.uniform(0.1, 1.0)  # Valor pequeño de dx
    df = derivada_funcion.subs(
        x, valor_x).evalf() * dx  # Calculamos df = f'(x) * dx

    i = 0
    max_i = 2
    while i < max_i:
        try:
            resp3 = float(
                input(
                    f"¿Cuál es el valor de df cuando x = {valor_x} y dx = {dx:.2f}? "
                ))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        error_margin = 0.5

        if abs(resp3 - df) <= error_margin:
            acum += 1
            puntos += 10
            print(
                f"¡Correcto! El valor de la diferencial df es aproximadamente {df:.2f}."
            )
            print(
                "¡Felicidades! Gracias a tus cálculos precisos, Sara y tu han superado el terreno más traicionero y han cruzado el último obstáculo. Ahora, están seguros dentro del refugio. Gracias a ti, han llegado sanos y salvos a su destino, listos para un nuevo comienzo en este mundo devastado. ¡Gran trabajo completando este viaje épico!"
            )
            enter()
            print("\n")
            ################función puntaje################
            puntaje(acum)
            menu(puntos, pistas, segundaop)
            return
        else:
            i += 1
            print(f"Incorrecto. Te quedan {max_i - i} intentos.")
            if i == max_i:
                print(f"La respuesta correcta es aproximadamente {df:.2f}.")
            else:
                print("\n")
                print("Incorrecto.")
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3.Volver al menú"
                )
                rip3 = int(input())
                if rip3 == 1:
                    if (segundaop >= 1):
                        print(
                            "\n¡Has utilizado con éxito una segunda oportunidad!\n"
                        )
                        segundaop -= 1
                        enter()
                        apo_cap5pro3(acum, puntos, pistas, segundaop)
                    else:
                        print("\n")
                        print("No cuentas con segundas oportunidades")
                        while (True):
                            print("¿Deseas consultar la tienda? s/n")
                            op = input()
                            if (op.upper() != "S" and op.upper() != "N"):
                                print("Ingresa s/n")
                            if (op.upper() == "N"):
                                clear_shell()
                                break
                            elif (op.upper() == "S"):
                                tienda(puntos, pistas, segundaop)
                elif rip3 == 2:
                    #función puntaje
                    puntaje(acum)
                    print()
                elif rip3 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)
                return


def apocalipsis(puntos, name, pistas, segundaop):
    pistas = 0
    segundaop = 0
    silencio()
    clear_shell()
    print("====Haz elegido el camino del Apocalipsis====")
    print(
        "En un mundo post-apocalíptico, donde la tierra ha sido devastada por una",
        end=" ")
    print(
        "enfermedad que convirtió a la mayoría de la población en seres salvajes,",
        end=" ")
    print("sobreviven unos pocos humanos dispersos por el mundo.", end=" ")
    print("Entre ellos están Sara y tú, dos jóvenes que nunca se conocieron",
          end=" ")
    print(
        "antes del fin del mundo, pero cuyas circunstancias los obligaron a ",
        end=" ")
    print(
        "cruzarse en un mundo donde la supervivencia es una lucha constante.",
        end=" ")
    print("\n")
    enter()
    print("~~~~~~~~~~CAPITULO 1~~~~~~~~~~")
    print("\n")
    print(
        "Estás huyendo en medio de una tormenta, buscando refugio encuentras un",
        end=" ")
    print(
        "edificio semidestruido. En tu situación no lo dudas y entras. Los rayos",
        end=" ")
    print("golpean el edificio, lo que ocasiona que algunos escombros caigan.",
          end=" ")
    print(
        "Encuentras una puerta oculta, y por la desesperación decides entrar sin",
        end=" ")
    print(
        "dudar. La puerta está cerrada, golpeas en busca de que se abra y después de",
        end=" ")
    print(
        "un tiempo lo logras, pero no precisamente por tus esfuerzos. Al otro lado de",
        end=" ")
    print(
        "la puerta, hay una chica con un arma apuntando directamente hacia tu cabeza.",
        end=" ")
    print(
        "Decides rogarle por refugio, pues no tienes ningún lugar al cual ir.",
        end=" ")
    print(
        "Aunque desconfiada, ella acepta al ver que no eres alguien peligroso.",
        end=" ")
    print(
        "Después descubres que la chica se llama Sara, una ingeniera solitaria que te",
        end=" ")
    print(
        "cuenta sobre una transmisión de radio reciente, en la que se menciona la",
        end=" ")
    print(
        "existencia de un refugio para sobrevivientes al norte de la ciudad.",
        end=" ")
    print("Juntos, deciden emprender un viaje hacia esa posible de salvación",
          end="\n")
    print("\n")
    enter()
    print("===============Problema 1===============")
    print("\n")
    sonido_preguntas()
    acum = 0  #acumulador de puntaje total FINAL (70%)

    while (True):
        rp1 = random.randint(120, 200)  #rp1 random problema 1
        if (rp1 % 4 == 0):
            break
    print(
        "Sara y tu están preparándose para salir del búnker y viajar al refugio del norte. Sara calcula que les quedan",
        rp1,
        "raciones de comida y deciden que cada uno comerá dos raciones al día."
    )
    print("\n")
    print(
        "Si Sara y tu comen 2 raciones de comida por día cada uno, ¿cuántos días les durarán las raciones?"
    )

    i = 0
    max_i = 2  # Número de intentos permitidos
    sp1 = rp1 / 4  #sp1 = solución problema 1

    while i < max_i:
        try:
            resp1 = float(input(f"¿Cuántos días les durarán las raciones? "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if sp1 == resp1:
            acum += 1
            puntos += 10
            print(f"¡Correcto! Sara y tu tienen raciones para {sp1} días.")
            apo_problema2(acum, puntos, pistas,
                          segundaop)  # Pasar al siguiente problema
            return
        else:
            i += 1
            if i < max_i:
                print(f"Incorrecto. Te quedan {max_i - i} intento(s).")
            else:
                print(f"Incorrecto. Has agotado tus {max_i} intentos.")

                # Menú de opciones después de fallar
                print("\n")
                print(
                    "Seleccione: \n1. Volver a intentarlo \n2. Continuar. \n3. Volver al menú"
                )
                rip1 = int(input())
                if rip1 == 1:
                    continue  # Repite la pregunta
                elif rip1 == 2:
                    apo_problema2(acum, puntos, pistas,
                                  segundaop)  # Continúa al siguiente problema
                    return
                elif rip1 == 3:
                    clear_shell()
                    menu(puntos, pistas, segundaop)  # Volver al menú
                    return


def apocalipsis_elegir(puntos, name, pistas, segundaop):
    silencio()
    print("\n")
    print("Selecciona en que capitulo quieres jugar:")
    print("\nOpciones")
    print("   1      Capitulo 1 (Aritmetica)")
    print(
        "   2      Capitulo 2. (Aljebra) \n   3      Capitulo 3. (Geometria) \n   4      Capitulo 4. (Trigonometria) \n   5      Capitulo 5. (Calculo)"
    ) 
    seleccion = int(input())
    if (seleccion == 1):
        apocalipsis(puntos, name, pistas, segundaop)
    elif (seleccion == 2):
        apo_cap2pro1(puntos, name, pistas, segundaop)
    elif (seleccion == 3):
        apo_cap3pro1(puntos, name, pistas, segundaop)
    elif (seleccion == 4):
        apo_cap4pro1(puntos, name, pistas, segundaop)
    elif (seleccion == 5):
        apo_cap5pro1(puntos, name, pistas, segundaop)
    else:
        print("Por favor ingresa un numero valido")

def apocalipsis_ecap(puntos, pistas, segundaop, name):
    silencio()
    print("\n")
    print("Selecciona en que capitulo quieres jugar:")
    print("\nOpciones")
    print("   1      Capitulo 1 (Aritmetica)")
    print(
        "   2      Capitulo 2. (Aljebra) \n   3      Capitulo 3. (Geometria) \n   4      Capitulo 4. (Trigonometria) \n   5      Capitulo 5. (Calculo)"
    ) 
    seleccion = int(input())
    if (seleccion == 1):
        apocalipsis_ecap1(puntos, name, pistas, segundaop)
    elif (seleccion == 2):
        apo_ecap2(puntos, name, pistas, segundaop)
    elif (seleccion == 3):
        apo_ecap3(puntos, name, pistas, segundaop)
    elif (seleccion == 4):
        apo_ecap4(puntos, name, pistas, segundaop)
    elif (seleccion == 5):
        apo_ecap5(puntos, name, pistas, segundaop)
    else:
        print("Por favor ingresa un numero valido")

def apocalipsis_ecap1(puntos, name, pistas, segundaop):
    print("Seleccioan en que problema quieres continuar:")
    print("\nOpciones")
    print("   1     Problema 1. \n   2     Problema 2. \n   3     Problema 3")

    n = int(input())

    if n == 1:
        apocalipsis(puntos, name, pistas, segundaop)
    elif n == 2:
        apo_problema2(puntos, name, pistas, segundaop)
    elif n == 3:
        apo_problema3(puntos, name, pistas, segundaop)

def apo_ecap2(puntos, name, pistas, segundaop):
    print("Seleccioan en que problema quieres continuar:")
    print("\nOpciones")
    print("   1     Problema 1. \n   2     Problema 2. \n   3     Problema 3")

    n = int(input())

    if n == 1:
        apo_cap2pro1(puntos, name, pistas, segundaop)
    elif n == 2:
        apo_cap2pro2(puntos, name, pistas, segundaop)
    elif n == 3:
        apo_cap2pro3(puntos, name, pistas, segundaop)

def apo_ecap3(puntos, name, pistas, segundaop):
    print("Seleccioan en que problema quieres continuar:")
    print("\nOpciones")
    print("   1     Problema 1. \n   2     Problema 2. \n   3     Problema 3")

    n = int(input())

    if n == 1:
        apo_cap3pro1(puntos, name, pistas, segundaop)
    elif n == 2:
        apo_cap3pro2(puntos, name, pistas, segundaop)
    elif n == 3:
        apo_cap3pro3(puntos, name, pistas, segundaop)

def apo_ecap4(puntos, name, pistas, segundaop):
    print("Seleccioan en que problema quieres continuar:")
    print("\nOpciones")
    print("   1     Problema 1. \n   2     Problema 2. \n   3     Problema 3")

    n = int(input())

    if n == 1:
        apo_cap4pro1(puntos, name, pistas, segundaop)
    elif n == 2:
        apo_cap4p2(puntos, name, pistas, segundaop)
    elif n == 3:
        apo_cap4p3(puntos, name, pistas, segundaop)

def apo_ecap5(puntos, name, pistas, segundaop):
    print("Seleccioan en que problema quieres continuar:")
    print("\nOpciones")
    print("   1     Problema 1. \n   2     Problema 2. \n   3     Problema 3")

    n = int(input())

    if n == 1:
        apo_cap5pro1(puntos, name, pistas, segundaop)
    elif n == 2:
        apo_cap5pro2(puntos, name, pistas, segundaop)
    elif n == 3:
        apo_cap5pro3(puntos, name, pistas, segundaop)


def iniciar_aventura(puntos, pistas, segundaop):
    clear_shell()
    while (True):
        print("Selecciona la temática de tu historia", name, ": ")
        print("1. Apocalipsis")
        #print("2. Piratas")
        #print("3. Futurista")
        oph = int(input())  #oph opción historia
        if (oph != 1 and oph != 2 and oph != 3):
            print(
                "Seleccionar una historia valida dentro del rango mencionado")
        elif (oph == 1):
            apocalipsis_elegir(puntos, name, pistas, segundaop)


#             break
#         elif(oph == 2):
#             piratas()
#             break
#         elif(oph == 3):
#             futurista()
#             break


def main():
    clear_shell()
    sonido_menu()
    print("..::BIENVENIDO AL JUEGO::..")
    puntos = 100
    pistas = 0
    segundaop = 0

    guardar_progreso(puntos, pistas, segundaop)

    menu(puntos, pistas, segundaop)


main()
