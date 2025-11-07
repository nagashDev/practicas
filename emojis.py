import time
import os

# Estados de ánimo de la mascota (ASCII)
estados = [
"""
 ╔╦═══╦╗
 ║ ^ᴥ^ ║
 ╚╦═══╦╝
  ˶   ˵
""",
"""
 ╔╦═══╦╗
 ║ TᴥT ║
 ╚╦═══╦╝
  ˶   ˵
""",
"""
 ╔╦═══╦╗
 ║ xᴥx ║
 ╚╦═══╦╝
  ︶   ︶
""",
"""
 ╔╦═══╦╗
 ║ •ᴥ• ║
 ╚╦═╦═╦╝
  ˶🍗˵
""",
"""
 ╔╦═══╦╗
 ║ -ᴥ- ║
 ╚╦═══╦╝
  ˶ Z˵
"""
]

# Recorremos con un for
for estado in estados:
    os.system("cls" if os.name == "nt" else "clear")  # limpia pantalla
    print(estado)
    time.sleep(1.5)  # espera 1.5 seg antes de pasar al siguiente
