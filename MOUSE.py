import pyautogui

print('Posicione o MOUSE')

pyautogui.sleep(3)
x, y = pyautogui.position()
print("Posicao atual do mouse:")
print("x = "+str(x)+" y = "+str(y))
