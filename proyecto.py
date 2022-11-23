#este programa fue creado como una trivia de diferentes temas

#lista y respuestas de las preguntas segun el tema
#preguntas para matematicas
matematicas=[
    "El resultado del operador logico ^ cuando se tiene falso y falso es: ",
    "El resultado del operador logico v cuando se tiene falso o verdadero es: ", 
    "El resultado de 27-2*(11-15) es: ",
    "En la gerarquia de numeros que se resulve primero: (parentesis-multiplicacion-suma-resta-division-potencia)",
    "El resultado de (7/5)+(2/3)-1 es: ",
    "El resultado de ((-3)^3)+((-2)^3)-((-3)^3)+((-1)^3) es: ",
    "Un triangulo isoceles tiene todos los lados: ",
    "Si 8 litros de gasolina valen 60 dolares, ¿cuantos litros podre comprar con 15 dolares?: (solo el numero)",
    "El monstruo del lago Ness mide 80 metros más la mitad de lo que mide, ¿cuánto mide el monstruo del lago Ness?: (solo numero)",
    "El resultado de 50%3 es: "]

matematicas0=[   
    "El resultado del operador logico ^ cuando se tiene falso y falso es: ",
    "El resultado del operador logico v cuando se tiene falso o verdadero es: ", 
    "El resultado de 27-2*(11-15) es: ",
    "En la gerarquia de numeros que se resulve primero: (parentesis-multiplicacion-suma-resta-division-potencia)",
    "El resultado de (7/5)+(2/3)-1 es: ",
    "El resultado de ((-3)^3)+((-2)^3)-((-3)^3)+((-1)^3) es: ",
    "Un triangulo isoceles tiene todos los lados: ",
    "Si 8 litros de gasolina valen 60 dolares, ¿cuantos litros podre comprar con 15 dolares?: (solo el numero)",
    "El monstruo del lago Ness mide 80 metros más la mitad de lo que mide, ¿cuánto mide el monstruo del lago Ness?: (solo numero)",
    "El resultado de 50%3 es: " ]

respuestasm= ["falso", "verdadero", "35", "parentesis", "16/15", "-9", "iguales", "2", "160", "2" ]
respuestasm0=["falso", "verdadero", "35", "parentesis", "16/15", "-9", "iguales", "2", "160", "2"]

#preguntas para geografia
geografia=[
    "El rio mas largo del mundo es el rio : ",
    "El pais mas pequeño del mundo es: ",
    "El pais mas grande del mundo es: ",
    "La capital de estados unidos es: ",
    "El continente mas grande es: (sin D.C)",
    "En que continente se encuentra australia: ",
    "En que continente se encuentra qatar: ",
    "Cual es la capital de arabia saudita: ",
    "La montaña mas alta del mundo es el: ",
    "El rio mas ancho del mundo es el rio de: "]
geografia0=[
    "El rio mas largo del mundo es el rio : ",
    "El pais mas pequeño del mundo es: ",
    "El pais mas grande del mundo es: ",
    "La capital de estados unidos es: ",
    "El continente mas grande es: (sin D.C)",
    "En que continente se encuentra australia: ",
    "En que continente se encuentra qatar: ",
    "Cual es la capital de arabia saudita: ",
    "La montaña mas alta del mundo es el: ",
    "El rio mas ancho del mundo es el rio de: "
]
respuestasg=["amazonas", "vaticano", "rusia", "wasington", "asia", "oceania", "asia", "riad", "monte everest", "la plata"]
respuestasg0=["amazonas", "vaticano", "rusia", "wasington", "asia", "oceania", "asia", "riad", "monte everest", "la plata"]

#preguntas para quimica
quimica=[
    "El elemto quimico con menor peso es el: ",
    "El nucleo del atomo esta compuesto por: ",
    "Los estados de la materia son: solido, liquido, gaseoso y ...",
    "La quema de madera es un cambio: ",
    "Cual es el simbolo del hierro: (primera en mayuscula)",
    "Los atomos con cargas positivas se llaman: ",
    "La mezcla de agua y arena es una mezcla: ",
    "El elemento mas fundamental para la vida es el: ",
    "Como se llama al cambio de estado gaseoso a liquido: ",
    "El estado donde los atomos estan mas compactos es en el estado: "
]

quimica0=[
    "El elemto quimico con menor peso es el: ",
    "El nucleo del atomo esta compuesto por: ",
    "Los estados de la materia son: solido, liquido, gaseoso y ...",
    "La quema de madera es un cambio: ",
    "Cual es el simbolo del hierro: (primera en mayuscula)",
    "Los atomos con cargas positivas se llaman: ",
    "La mezcla de agua y arena es una mezcla: ",
    "El elemento mas fundamental para la vida es el: ",
    "Como se llama al cambio de estado gaseoso a liquido: ",
    "El estado donde los atomos estan mas compactos es en el estado: "
]

respuestasq=["hidrogeno", "protones y neutrones", "plasma", "quimico", "Fe", "cationes", "heterogenea", "carbono", "condensación", "solido"]
respuestasq0=["hidrogeno", "protones y neutrones", "plasma", "quimico", "Fe", "cationes", "heterogenea", "carbono", "condensación", "solido"]

puntaje=0
npregunta=1
print ("Bienvenido a esta trivia, por favor escriba su nombre")

nombre=input("Nombre: ")

jugar=input("¿Quiere jugar a una trivia?: ")  #loop para que el juego se repita hasta que el usuario quiera
while jugar == "si":

    print ("Hola, "+ nombre + " por favor escriba el tema que de la trivia")
    print ("(matematica)-(geografia)-(quimica)")

    tema=input()

    if tema == "matematica":   #inicia las preguntas de matemicas

        print("El tema escogido es: matematica")

        print("-----------------------------------------------------------------------------------------------------------")

        print("Inicio de la trivia")
        print("Respuestas en minuscula")

        for i in matematicas:

            print("Pregunta numero: ", npregunta)
            print(i)
            npregunta=npregunta+1
            res=input()
            for b in respuestasm:
                if res==b:
                    print("Respuesta correcta")
                    respuestasm.remove(b)
                    puntaje=puntaje+1
                    break
                else:
                    print("Respuesta equivocada, la respuesta era: ", b)
                    respuestasm.remove(b)
                    break #fin de las preguntas

    if tema=="geografia":    #inicio de las preguntas de geografia
        print("El tema escogido es: geografia")

        print("-----------------------------------------------------------------------------------------------------------")

        print("inicio de la trivia")
        print("Respuestas en minuscula")

        for i in geografia:

            print("Pregunta numero: ", npregunta)
            print(i)
            npregunta=npregunta+1
            res=input()
            for b in respuestasg:
                if res==b:
                    print("Respuesta correcta")
                    respuestasg.remove(b)
                    puntaje=puntaje+1
                    break
                else:
                    print("Respuesta equivocada, la respuesta era: ", b)
                    respuestasg.remove(b)
                    break       #fin preguntas

    if tema=="quimica":         #inicio de las preguntas de quimica
        print("El tema escogido es: quimica")
                
        print("-----------------------------------------------------------------------------------------------------------")

        print("inicio de la trivia")
        print("Respuestas en minuscula")

        for i in quimica:

            print("Pregunta numero: ", npregunta)
            print(i)
            npregunta=npregunta+1

            res=input()
            for b in respuestasq:
                if res==b:
                    print("Respuesta correcta")
                    respuestasq.remove(b)
                    puntaje=puntaje+1
                    break
                else:
                    print("Respuesta equivocada, la respuesta era: ", b)
                    respuestasq.remove(b)
                    break       #fin preguntas

    print(nombre, " su puntaje en la trivia de ", tema, " es: ", puntaje)

    añadir=input("Le gustaria añadir alguna pregunta a la trivia?: ") #esto permite al usuario añadir preguntas
    if añadir=="si":
        cambio=input("¿A que trivia quiere añadir una pregunta? (matematica)-(geografia)-(quimica): ")

        if cambio=="matematica":
            preguntan=input("Escriba la pregunta que quiere añadir: ")
            respuesta=input("Escriba la respuesta a la pregunta: ")
            matematicas0.append(preguntan)
            respuestasm0.append(respuesta)
            print ("la pregunta y fue añadida a la trivia de ", cambio)
        
        if cambio=="geografia":
            preguntan=input("Escriba la pregunta que quiere añadir: ")
            respuesta=input("Escriba la respuesta a la pregunta: ")
            geografia0.append(preguntan)
            respuestasg0.append(respuesta)
            print ("la pregunta y fue añadida a la trivia de ", cambio)

        if cambio=="quimica":
            preguntan=input("Escriba la pregunta que quiere añadir: ")
            respuesta=input("Escriba la respuesta a la pregunta: ")
            quimica0.append(preguntan)
            respuestasq0.append(respuesta)
            print ("la pregunta y fue añadida a la trivia de ", cambio)       #fin del añadido

    #lo que sigue restablece los valores de preguntas y respuestas, ademas de añadir las que el usuario puso
    matematicas=matematicas0
    respuestasm=respuestasm0
    geografia=geografia0
    respuestasg=respuestasg0
    quimica=quimica0
    respuestasq=respuestasq0
    npregunta=0
    puntaje=0


    jugar=input("¿Quiere volver a jugar?: ") #esto decide si el loop continua o termina



    

print("gracias por jugar")
