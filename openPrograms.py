import webbrowser
import time
import pyautogui

# Abre o Google no navegador padrão
webbrowser.open("https://www.google.com")

# Aguarda o navegador abrir e carregar a página
time.sleep(5)

# Digita "youtube" no campo de pesquisa e pressiona Enter
pyautogui.write("youtube")
pyautogui.press("enter")

# Aguarda os resultados de pesquisa carregarem
time.sleep(3)

# Acha a posição do primeiro link - você pode precisar ajustar essas coordenadas
# Uma maneira de obter as coordenadas é usar o pyautogui.displayMousePosition() em um script separado
# para encontrar a posição correta do primeiro link
first_link_position = (310, 323)  # Substitua (x, y) pelas coordenadas do primeiro link

# Move o cursor para o primeiro link e clica
pyautogui.moveTo(first_link_position[0], first_link_position[1], duration=1)
pyautogui.click()

# Espera alguns segundos para ver o resultado
time.sleep(5)