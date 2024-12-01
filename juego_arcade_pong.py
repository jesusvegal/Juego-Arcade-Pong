import turtle

# --- CONSTANTES ---
# Estas constantes permiten modificar fácilmente los parámetros del juego
SCREEN_WIDTH = 800           # Ancho de la pantalla
SCREEN_HEIGHT = 600          # Altura de la pantalla
PADDLE_MOVE_DISTANCE = 30    # Distancia que se mueve la paleta con cada tecla
BALL_SPEED = 0.8             # Velocidad inicial de la pelota
BALL_SPEED_INCREMENT = 0.1   # Incremento de velocidad por cada punto
PADDLE_WIDTH = 6             # Altura de las paletas
PADDLE_LENGTH = 1            # Grosor de las paletas

# --- FUNCIONES ---
# Función para configurar la ventana principal del juego
def setup_window():
    """
    Configura la ventana principal del juego con parámetros predefinidos.
    :return: Objeto `Screen` configurado.
    """
    window = turtle.Screen()
    window.title("Juego Arcade Pong - Python")
    window.bgcolor("black")
    window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    window.tracer(0)  # Desactiva actualizaciones automáticas para mejorar rendimiento
    return window

# Función para crear una paleta
def create_paddle(x_pos):
    """
    Crea una paleta en una posición horizontal específica.
    :param x_pos: Coordenada X donde se ubicará la paleta.
    :return: Objeto `Turtle` configurado como paleta.
    """
    paddle = turtle.Turtle()
    paddle.speed(0)  # Velocidad de animación máxima
    paddle.shape("square")  # Forma de la paleta
    paddle.color("white")  # Color de la paleta
    paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)  # Tamaño
    paddle.penup()  # Evita que la paleta dibuje al moverse
    paddle.goto(x_pos, 0)  # Posición inicial
    return paddle

# Función para crear la pelota
def create_ball():
    """
    Crea la pelota en el centro de la pantalla con velocidad inicial.
    :return: Objeto `Turtle` configurado como pelota.
    """
    ball = turtle.Turtle()
    ball.speed(0)  # Velocidad de animación máxima
    ball.shape("circle")  # Forma de la pelota
    ball.color("white")  # Color de la pelota
    ball.penup()  # Evita que la pelota dibuje al moverse
    ball.goto(0, 0)  # Posición inicial
    ball.dx = BALL_SPEED  # Velocidad horizontal inicial
    ball.dy = -BALL_SPEED  # Velocidad vertical inicial
    return ball

# Función para crear el marcador
def create_score_pen():
    """
    Crea el marcador para mostrar las puntuaciones en pantalla.
    :return: Objeto `Turtle` configurado como marcador.
    """
    pen = turtle.Turtle()
    pen.speed(0)  # Velocidad de animación máxima
    pen.color("white")  # Color del marcador
    pen.penup()  # Evita que dibuje al moverse
    pen.hideturtle()  # Oculta la "tortuga" para mostrar solo texto
    pen.goto(0, SCREEN_HEIGHT / 2 - 40)  # Posición del marcador en la pantalla
    return pen

# Actualización del marcador
def update_score(pen, score_a, score_b):
    """
    Actualiza el marcador en pantalla con las puntuaciones actuales.
    :param pen: Objeto `Turtle` utilizado como marcador.
    :param score_a: Puntuación del jugador A.
    :param score_b: Puntuación del jugador B.
    """
    pen.clear()  # Limpia el marcador anterior
    pen.write(f"Jugador A: {score_a}  Jugador B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Movimiento de paletas
def move_paddle_up(paddle):
    """
    Mueve la paleta hacia arriba si no sobrepasa el límite superior.
    :param paddle: Objeto `Turtle` que representa la paleta.
    """
    y = paddle.ycor()
    if y < (SCREEN_HEIGHT / 2) - 50:  # Límite superior
        paddle.sety(y + PADDLE_MOVE_DISTANCE)

def move_paddle_down(paddle):
    """
    Mueve la paleta hacia abajo si no sobrepasa el límite inferior.
    :param paddle: Objeto `Turtle` que representa la paleta.
    """
    y = paddle.ycor()
    if y > -(SCREEN_HEIGHT / 2) + 50:  # Límite inferior
        paddle.sety(y - PADDLE_MOVE_DISTANCE)

# --- INICIALIZACIÓN ---
# Configuración de la ventana
window = setup_window()

# Creación de elementos del juego
paddle_a = create_paddle(-350)
paddle_b = create_paddle(350)
ball = create_ball()
pen = create_score_pen()

# Variables de puntuación
score_a = 0
score_b = 0
update_score(pen, score_a, score_b)

# Asignación de teclas
window.listen()
window.onkeypress(lambda: move_paddle_up(paddle_a), "w")  # Jugador A: tecla "W"
window.onkeypress(lambda: move_paddle_down(paddle_a), "s")  # Jugador A: tecla "S"
window.onkeypress(lambda: move_paddle_up(paddle_b), "Up")  # Jugador B: flecha arriba
window.onkeypress(lambda: move_paddle_down(paddle_b), "Down")  # Jugador B: flecha abajo

# --- BUCLE PRINCIPAL ---
while True:
    window.update()

    # Movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Rebote en los bordes superior e inferior
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 10:
        ball.sety((SCREEN_HEIGHT / 2) - 10)
        ball.dy *= -1
    if ball.ycor() < -(SCREEN_HEIGHT / 2) + 10:
        ball.sety(-(SCREEN_HEIGHT / 2) + 10)
        ball.dy *= -1

    # Punto para el jugador B
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = abs(ball.dx)
        score_b += 1
        BALL_SPEED += BALL_SPEED_INCREMENT
        update_score(pen, score_a, score_b)

    # Punto para el jugador A
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -abs(ball.dx)
        score_a += 1
        BALL_SPEED += BALL_SPEED_INCREMENT
        update_score(pen, score_a, score_b)

    # Rebote en las paletas
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1.1  # Incrementa velocidad
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1.1  # Incrementa velocidad
