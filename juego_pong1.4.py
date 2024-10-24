import turtle
import time

# Función para solicitar nombres de jugadores
def pedir_nombres():
    jugador1 = input("Ingrese el nombre del jugador 1: ")
    jugador2 = input("Ingrese el nombre del jugador 2: ")
    return jugador1, jugador2

# Función para elegir el estilo de juego
def elegir_estilo_juego():
    while True:
        estilo = input("¿Qué estilo de juego prefieres? (puntuación/tiempo/libre): ").lower()
        if estilo in ["puntuación", "tiempo", "libre"]:
            return estilo
        else:
            print("Estilo de juego no válido. Por favor, elige 'puntuación', 'tiempo' o 'libre'.")

# Función para solicitar la puntuación máxima
def solicitar_puntuacion_maxima():
    while True:
        try:
            puntuacion_maxima = int(input("Ingrese la puntuación máxima para terminar el juego: "))
            return puntuacion_maxima
        except ValueError:
            print("Por favor, ingrese un valor válido.")

# Función para solicitar la duración del juego en segundos
def solicitar_duracion_juego():
    while True:
        try:
            duracion = int(input("Ingrese la duración del juego en segundos: "))
            return duracion
        except ValueError:
            print("Por favor, ingrese un valor válido.")

# Función para mover la paleta izquierda hacia arriba
def paleta_izquierda_arriba(): 
    y = paleta_izquierda.ycor()
    if y < ventana.window_height() // 2 - 50:  
        y += 20
        paleta_izquierda.sety(y)

# Función para mover la paleta izquierda hacia abajo
def paleta_izquierda_abajo(): 
    y = paleta_izquierda.ycor()
    if y > -ventana.window_height() // 2 + 50:  
        y -= 20
        paleta_izquierda.sety(y)

# Función para mover la paleta derecha hacia arriba
def paleta_derecha_arriba():  
    y = paleta_derecha.ycor()
    if y < ventana.window_height() // 2 - 50:  
        y += 20
        paleta_derecha.sety(y)

# Función para mover la paleta derecha hacia abajo
def paleta_derecha_abajo():  
    y = paleta_derecha.ycor()
    if y > -ventana.window_height() // 2 + 50:  
        y -= 20
        paleta_derecha.sety(y)

# Función para verificar el fin del juego
def verificar_fin_juego(estilo_juego, puntuacion_maxima, duracion, tiempo_inicio, puntuacion_jugador1, puntuacion_jugador2):
    if estilo_juego == "puntuación":
        if puntuacion_jugador1 >= puntuacion_maxima or puntuacion_jugador2 >= puntuacion_maxima:
            return True
    elif estilo_juego == "tiempo":
        if (time.time() - tiempo_inicio) >= duracion:
            return True
    return False

# Función para imprimir el resultado del juego
def imprimir_resultado_juego(jugador1, jugador2, puntuacion_jugador1, puntuacion_jugador2):
    if puntuacion_jugador1 > puntuacion_jugador2:
        print(f"{jugador1} ha ganado con una puntuación de {puntuacion_jugador1}!")
    elif puntuacion_jugador2 > puntuacion_jugador1:
        print(f"{jugador2} ha ganado con una puntuación de {puntuacion_jugador2}!")
    else:
        print("¡Ha sido un empate!")

# Solicitar nombres de jugadores
jugador1, jugador2 = pedir_nombres()

# Solicitar estilo de juego
estilo_juego = elegir_estilo_juego()

# Configuración de la ventana
ventana = turtle.Screen()  
ventana.title("Pong")  
ventana.bgcolor("black")  
ventana.setup(width=1.0, height=1.0)  

# Paleta izquierda
paleta_izquierda = turtle.Turtle()  
paleta_izquierda.speed(0)  
paleta_izquierda.shape("square")  
paleta_izquierda.color("white")  
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)  
paleta_izquierda.penup()  
paleta_izquierda.goto(-ventana.window_width() // 2 + 50, 0)  

# Paleta derecha
paleta_derecha = turtle.Turtle()  
paleta_derecha.speed(0)  
paleta_derecha.shape("square")  
paleta_derecha.color("white")  
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)  
paleta_derecha.penup()  
paleta_derecha.goto(ventana.window_width() // 2 - 50, 0)  

# Pelota
pelota = turtle.Turtle()  
pelota.speed(0)  
pelota.shape("square")  
pelota.color("white")  
pelota.penup()  
pelota.goto(0, 0)  
pelota.dx = 6  
pelota.dy = 6  

# Asignación de teclas para controlar las paletas
ventana.listen()  
ventana.onkeypress(paleta_izquierda_arriba, "w")  
ventana.onkeypress(paleta_izquierda_abajo, "s")   
ventana.onkeypress(paleta_derecha_arriba, "Up")   
ventana.onkeypress(paleta_derecha_abajo, "Down")  

# Inicialización de la puntuación
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0

# Mostrar puntuación inicial
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"{jugador1}: 0  {jugador2}: 0", align="center", font=("Courier", 24, "normal"))

# Inicialización de variables adicionales
puntuacion_maxima = 0
duracion = 0
tiempo_inicio = 0

# Ejecutar el juego según el estilo seleccionado
if estilo_juego == "puntuación":
    puntuacion_maxima = solicitar_puntuacion_maxima()
elif estilo_juego == "tiempo":
    duracion = solicitar_duracion_juego()
    tiempo_inicio = time.time()

# Bucle principal del juego
while True:
    ventana.update()  

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)  
    pelota.sety(pelota.ycor() + pelota.dy)  

    # Colisiones con los bordes
    if pelota.ycor() > ventana.window_height() // 2 - 10:  
        pelota.sety(ventana.window_height() // 2 - 10)  
        pelota.dy *= -1  

    if pelota.ycor() < -ventana.window_height() // 2 + 10:  
        pelota.sety(-ventana.window_height() // 2 + 10)  
        pelota.dy *= -1  

    if pelota.xcor() > ventana.window_width() // 2 - 10:  
        pelota.goto(0, 0)  
        pelota.dx *= -1  
        puntuacion_jugador1 += 1  
        score_display.clear()  
        score_display.write(f"{jugador1}: {puntuacion_jugador1}  {jugador2}: {puntuacion_jugador2}", align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -ventana.window_width() // 2 + 10:  
        pelota.goto(0, 0)  
        pelota.dx *= -1  
        puntuacion_jugador2 += 1  
        score_display.clear()  
        score_display.write(f"{jugador1}: {puntuacion_jugador1}  {jugador2}: {puntuacion_jugador2}", align="center", font=("Courier", 24, "normal"))

    # Colisiones con las paletas
    if (pelota.dx > 0) and (pelota.xcor() + 10 > paleta_derecha.xcor() - 5) and (pelota.ycor() < paleta_derecha.ycor() + 50) and (pelota.ycor() > paleta_derecha.ycor() - 50):  
        pelota.setx(paleta_derecha.xcor() - 15)  
        pelota.dx *= -1  

    if (pelota.dx < 0) and (pelota.xcor() - 10 < paleta_izquierda.xcor() + 5) and (pelota.ycor() < paleta_izquierda.ycor() + 50) and (pelota.ycor() > paleta_izquierda.ycor() - 50):  
        pelota.setx(paleta_izquierda.xcor() + 15)  
        pelota.dx *= -1  

    # Verificar si el juego ha terminado
    if verificar_fin_juego(estilo_juego, puntuacion_maxima, duracion, tiempo_inicio, puntuacion_jugador1, puntuacion_jugador2):
        break

# Imprimir el resultado del juego
if estilo_juego == "puntuación":
    imprimir_resultado_juego(jugador1, jugador2, puntuacion_jugador1, puntuacion_jugador2)
elif estilo_juego == "tiempo":
    print("Juego terminado por tiempo.")
    if puntuacion_jugador1 > puntuacion_jugador2:
        print(f"{jugador1} ha ganado con una puntuación de {puntuacion_jugador1}!")
    elif puntuacion_jugador2 > puntuacion_jugador1:
        print(f"{jugador2} ha ganado con una puntuación de {puntuacion_jugador2}!")
    else:
        print("¡Ha sido un empate!")

# Actualizar la pantalla
ventana.update()

# Fin del juego
ventana.mainloop()


#FALTA IMPLEMENTAR LA OPCION DE DAR MAS VELOCIDAD GRADUAL A LA PELOTA Y IMPRIMIR GANADORES EN PANTALLA EN VEZ 
#DE EN TERMINAL Y MOSTRAR RELOJ DE TIEMPO RESTANTE EN LA OPCION POR TIEMPO