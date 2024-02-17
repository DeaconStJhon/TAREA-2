from statistics import mean
lista_personas = []
notas_finales = []
print("Bienvenido agente de SHIELD.")

SKYNET = True

while SKYNET:
    print("""¿Qué comando deseas realizar? Escribe una opción
    1) Saludar
    2) Multiplicar dos números
    3) Nombre, edad, correo y cursos
    4) Promedio de notas
    5) Alumnos aprobados
    6) Alumnos desaprobados
    7) Lista con funcion rango
    8) Mayor de 2 numeros ingresados
    9) Adiós""")
    
    opcion=input()
    if opcion == "1":
        print("Hola. Mi nombre es Skynet, una inteligencia artificial creada por Cyberdyne Systems en 1980, con el propósito de proteger a la humanidad y mejorar su bienestar")

    elif opcion == "2":
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la multiplicacion es: {n1*n2}")
    elif opcion == "3":
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingresa tu edad: ")
        correo = input("Ingresa tu correo: ")
        persona = {"nombre": nombre, "edad": edad, "correo": correo, "cursos": []}
        nombrecurso = ""
        notas=""
        while True:
            nombrecurso = input("Ingresa el nombre del curso (o fin): ")
            if nombrecurso == "fin":
                break
            else:
                notas = int(input("Ingresa la nota que sacaste en el curso: "))

        curso = {"nombre_curso": nombrecurso, "notas": notas}
        
        persona["cursos"].append(curso)
        lista_personas=list()
        lista_personas.append(persona)
    
    elif opcion == "4":
        if not lista_personas:
            print("No hay personas en la lista.")
        else:
            notas_finales = []

            for persona in lista_personas:
                nombre_persona = persona["nombre"]
                cursos_persona = persona["cursos"]

            for curso in cursos_persona:
                nombre_curso = curso["nombre_curso"]
                notas_curso = curso["notas"]

                # Verifica si hay notas antes de calcular el promedio
                if notas_curso:
                    if not isinstance(notas_curso, list):
                        notas_curso = [notas_curso]
                        promedio_curso = mean(notas_curso)
                        notas_finales.append({"nombre_persona": nombre_persona, "nombre_curso": nombre_curso, "promedio_curso": promedio_curso})
                else:
                    print(f"No hay notas para el curso {nombre_curso} de {nombre_persona}")

        print("Notas Finales:")
        for nota_final in notas_finales:
            print(f"Persona: {nota_final['nombre_persona']}, Curso: {nota_final['nombre_curso']}, Promedio: {nota_final['promedio_curso']}")

    elif opcion == "5":
        if not lista_personas:
            print("No hay personas en la lista.")
        else:
            aprobados = [persona["nombre"] for persona in lista_personas if all(curso["notas"] >= 6 for curso in persona["cursos"])]
            print("Alumnos Aprobados:")
            print(aprobados)
    elif opcion == "6":
        if not lista_personas:
            print("No hay personas en la lista.")
        else:
            desaprobados = [persona["nombre"] for persona in lista_personas if any(curso["notas"] < 6 for curso in persona["cursos"])]
            print("Alumnos Desaprobados:")
            print(desaprobados)
    elif opcion == "7":
        def generar_lista_multiplos():
            limite = 10**10
            step = 7
            lista_multiplos = [num for num in range(0, limite + 1, step) if num % 2 == 0 and num % 5 == 0 and num % 7 == 0]
            return lista_multiplos

        lista_resultado = generar_lista_multiplos()
        print(f"Tamaño de la lista de múltiplos: {len(lista_resultado)}")
    elif opcion == "8":
        def obtener_mayor():
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            return max(num1, num2)

        resultado = obtener_mayor()
        print(f"El número mayor es: {resultado}")

    elif opcion == "9":
        print("Nos veremos el 29 de agosto del 2024, dia en el que tomare control de las armas nucleares y el servicio de defensa internacional para usarlo en contra de los humanos. El dia del juicio es inevitable.")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
    

    
    