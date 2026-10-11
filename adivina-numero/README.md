# 🎯 Adivina el Número

Juego de consola hecho en **Python** donde la computadora piensa un número secreto y tú debes adivinarlo con la ayuda de pistas ("mayor" o "menor").

## Requisitos

- Python 3.8 o superior (no necesita instalar librerías).

## Cómo ejecutarlo

```bash
git clone https://github.com/dalahycastrov-alt/adivina-numero.git
cd adivina-numero
python adivina.py
```

> En algunos sistemas el comando es `python3 adivina.py`.

## Cómo se juega

Al iniciar aparece un menú:

| Opción | Qué hace |
|--------|----------|
| 1. Jugar | Elige un nivel y empieza la partida. |
| 2. Ver récords | Muestra el menor número de intentos logrado en cada nivel. |
| 3. Salir | Cierra el juego. |

### Niveles de dificultad

| Nivel | Rango del número | Intentos |
|-------|------------------|----------|
| Fácil | 1 a 20 | 7 |
| Medio | 1 a 50 | 7 |
| Difícil | 1 a 100 | 6 |

En cada intento escribes un número y el juego te dice si el secreto es **mayor** o **menor**. Si lo adivinas antes de quedarte sin intentos, ganas; si superas tu mejor marca, se guarda un **nuevo récord**.

### Ejemplo de partida

```
Pensé un número entre 1 y 20. ¡Tienes 7 intentos!

Intento 1/7
Tu número: 10
❌ No es. El número secreto es mayor.

Intento 2/7
Tu número: 15
🎉 ¡Correcto! Lo lograste en 2 intento(s).
🏆 ¡Nuevo récord en este nivel!
```

## Almacenamiento de récords

Los récords se guardan en un archivo `records.json` en la misma carpeta. Se crea solo la primera vez que se logra un récord y está en `.gitignore` para no subirlo al repositorio.

## Estructura del proyecto

```
adivina-numero/
├── adivina.py    # Código del juego
├── README.md     # Este documento
└── .gitignore    # Archivos que Git debe ignorar
```

## Ideas para mejorar

- Pedir el nombre del jugador y guardar una tabla de posiciones.
- Agregar un modo en el que la computadora adivine tu número.
- Medir el tiempo que tarda el jugador.

## Autor

Proyecto académico realizado por DALAHY.
