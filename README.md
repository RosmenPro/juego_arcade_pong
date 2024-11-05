
# Juego de Pong en Python

Este proyecto es una implementación del clásico juego Pong en Python utilizando la librería `turtle`. Permite que dos jugadores compitan entre sí, eligiendo el estilo de juego: por puntuación, por tiempo, o en modo libre.

## Características

- **Multijugador local**: Dos jugadores controlan las paletas con teclas específicas.
- **Tres estilos de juego**:
  - **Por puntuación**: Gana el primer jugador en alcanzar una puntuación máxima.
  - **Por tiempo**: El jugador con mayor puntuación al finalizar el tiempo gana.
  - **Libre**: Juega sin límite de tiempo ni puntuación.
- **Colisiones realistas** con las paredes y las paletas.

## Requisitos

Para ejecutar este proyecto necesitas tener instalado:

- Python 3.x
- Librería `turtle` (generalmente incluida en las instalaciones estándar de Python)

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener Python instalado en tu sistema.
3. No necesitas instalar bibliotecas adicionales, ya que `turtle` viene con Python por defecto.

## Ejecución

1. Abre una terminal o un entorno de desarrollo.
2. Ejecuta el script principal:

   ```bash
   python pong.py
   ```

3. Sigue las instrucciones en pantalla para ingresar los nombres de los jugadores y seleccionar el estilo de juego.


## Controles del Juego
   * **Jugador 1:** Usa las teclas W para mover la paleta hacia arriba y S para moverla hacia abajo.
   * **Jugador 2:** Usa las teclas de flecha ↑ para mover la paleta hacia arriba y ↓ para moverla hacia abajo.

## Estilos de Juego
   * **Puntuación:** Los jugadores definen una puntuación máxima, y el juego finaliza cuando uno de los jugadores la alcanza.
   * **Tiempo:** Los jugadores definen una duración para el juego, y al finalizar, el jugador con más puntos gana.
   * **Libre:** Juega sin límite de tiempo ni puntuación.

## Estructura del Código
   * **Función principal:** Inicializa las paletas, la pelota, y maneja las colisiones y el movimiento.
   * **Funciones auxiliares:**
       * **pedir_nombres:** Solicita los nombres de los jugadores.
       * **elegir_estilo_juego:** Permite seleccionar el estilo de juego.
       * **paleta_izquierda_arriba, paleta_izquierda_abajo, paleta_derecha_arriba, paleta_derecha_abajo:** Controlan el movimiento de las paletas.
       * **verificar_fin_juego:** Comprueba si se cumplen las condiciones para finalizar el juego.

## Futuras Mejoras
   * Implementar la opcion de dar mas velocidad gradual a la pelota
   * Imprimir ganador por pantalla no en terminal
   * Mostrar reloj de tiempo faltante en opcion por tiempo y quizas reloj de tiempo jugado en las otras opciones
   * Añadir sonidos de efectos cuando la pelota colisiona o se anota un punto.
   * Implementar un menú de inicio y una interfaz gráfica más avanzada.
   
## Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor abre un issue o un pull request.

---

# Pong Game in Python

This project is an implementation of the classic Pong game in Python using the turtle library. It allows two players to compete against each other by choosing the style of play: by score, by time, or in free mode.

## Features

- Local multiplayer: Two players control the paddles with specific keys.
- Three styles of play:
  - By score: The first player to reach a maximum score wins.
  - By time: The player with the highest score when time runs out wins.
  - Free: Play without time or score limits.
- Realistic collisions with the walls and paddles.

## Requirements

To run this project you need to have installed:

- Python 3.x
- Turtle library (usually included in standard Python installations)

## Installation

1. Clone this repository or download the project files.
2. Make sure you have Python installed on your system.
3. You don’t need to install additional libraries, as turtle comes with Python by default.

## Execution

1. Open a terminal or development environment.
2. Run the main script:

   ```bash
   python pong.py
   ```

3. Follow the on-screen instructions to enter the players' names and select the style of play.
## Game Controls
* **Player 1**: Use the W key to move the paddle up and the S key to move it down.
* **Player 2**: Use the ↑ arrow key to move the paddle up and the ↓ arrow key to move it down.

## Game Styles
* **Score**: Players set a maximum score, and the game ends when one of the players reaches it.
* **Time**: Players set a duration for the game, and at the end, the player with the most points wins.
* **Free**: Play without time or score limits.

## Code Structure
* **Main function**: Initializes the paddles, the ball, and manages collisions and movement.
* **Auxiliary functions**: 
  * **request_names**: Asks for the players' names.
  * **choose_game_style**: Allows selection of the game style.
  * **left_paddle_up, left_paddle_down, right_paddle_up, right_paddle_down**: Control the movement of the paddles.
  * **check_game_over**: Checks if the conditions to end the game are met.

## Future Improvements
* Implement an option to gradually increase the ball's speed.
* Display the winner on the screen, not just in the terminal.
* Show a countdown timer in the time option and perhaps a timer for the total time played in other options.
* Add sound effects when the ball collides or when a point is scored.
* Implement a start menu and a more advanced graphical interface.

## Contributions
Contributions are welcome. If you find any issues or have suggestions for improvements, please open an issue or a pull request.

