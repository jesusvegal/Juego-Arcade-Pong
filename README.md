# 🏓 **Juego Arcade Pong - Python** 🏓

¡Bienvenido al clásico juego de **Pong** desarrollado en Python usando la librería `turtle`! Este juego es una versión sencilla y divertida en la que dos jugadores se enfrentan controlando paletas para evitar que la pelota pase al campo contrario. ¿Estás listo para el desafío?

## 🎮 **Características del Juego**

- **Control para dos jugadores**: Cada jugador puede mover su paleta de arriba a abajo para intentar bloquear la pelota.
- **Marcador en tiempo real**: El puntaje de ambos jugadores se muestra en la parte superior de la pantalla.
- **Colisiones realistas**: La pelota rebota contra las paredes superior e inferior, y las paletas de los jugadores. Si la pelota cruza un lado, el oponente anota un punto.
- **Movimiento continuo**: La pelota se mueve constantemente, y se acelera ligeramente con cada rebote en las paletas.

## 📦 **Tecnologías Utilizadas**

Este juego ha sido construido utilizando **Python** y la librería **turtle**, que permite crear gráficos simples y controlar objetos en una ventana gráfica.

- **Python 3.x**: Lenguaje de programación.
- **Turtle Graphics**: Librería gráfica de Python para crear la ventana del juego, las paletas, la pelota y el marcador.

## ⚙️ **Requisitos**

Para ejecutar el juego, necesitas tener instalado:

- Python 3.x (cualquier versión reciente).
- La librería **turtle**, que generalmente viene preinstalada con Python.

## 📜 **Cómo Jugar**

1. **Inicio del Juego**: Al ejecutar el archivo `pong.py`, se abrirá una ventana de juego donde podrás ver el marcador y las paletas.
2. **Control de las Paletas**:
   - **Jugador A** (izquierda):  
     - Mueve la paleta hacia arriba con la tecla **"W"**.
     - Mueve la paleta hacia abajo con la tecla **"S"**.
   - **Jugador B** (derecha):  
     - Mueve la paleta hacia arriba con la tecla de flecha **↑**.
     - Mueve la paleta hacia abajo con la tecla de flecha **↓**.
3. **Objetivo**: El objetivo es evitar que la pelota pase por tu campo. Cada vez que la pelota cruza al campo contrario, el jugador contrario anota un punto.
4. **Marcador**: En la parte superior de la pantalla, se muestra el puntaje actual de ambos jugadores.
5. **Rebote de la Pelota**: 
   - La pelota rebota en las paredes superior e inferior.
   - Si la pelota colisiona con las paletas, cambia de dirección y aumenta ligeramente su velocidad.
6. **Puntuación**: Si la pelota cruza el borde izquierdo (punto para el jugador B) o el borde derecho (punto para el jugador A), el juego reinicia la pelota al centro.


