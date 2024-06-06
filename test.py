import pyautogui

print("Move o cursor para a posição do primeiro link e pressione Ctrl+C para sair.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual do mouse: ({x}, {y})", end="\r")
except KeyboardInterrupt:
    print("\nFinalizado.")