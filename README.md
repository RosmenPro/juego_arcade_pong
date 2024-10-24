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
   * ##Jugador 1:## Usa las teclas W para mover la paleta hacia arriba y S para moverla hacia abajo.
   * ##Jugador 2:## Usa las teclas de flecha ↑ para mover la paleta hacia arriba y ↓ para moverla hacia abajo.

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
