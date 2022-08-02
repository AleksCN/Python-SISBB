import pyautogui
import pyperclip
import pygetwindow

nome_excel = 'CHAVES - Excel'
nome_sisbb = 'pw3270:A - 170.66.50.244'

janela_excel = pygetwindow.getWindowsWithTitle(nome_excel)[0]
janela_sisbb = pygetwindow.getWindowsWithTitle(nome_sisbb)[0]

i = 1

while i < 25172:

    janela_sisbb.activate()
    pyautogui.moveTo(193, 138, 0.3)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('esc')

    # DECLARA A CHAVE
    VALIDADOR_LOCALIZADO = pyperclip.paste()
    VALIDADOR = " ATCM2051"

    while VALIDADOR == VALIDADOR_LOCALIZADO:

        # COPIA A CHAVE F
        janela_excel.activate()
        pyautogui.press('F2')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        pyautogui.press('left')

        # COLA A CHAVE F
        janela_sisbb.activate()
        pyautogui.press('down', presses=3)
        pyautogui.press('right', presses=16)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        # FAZ A VALIDAÇÃO
        pyautogui.moveTo(193, 138, 0.3)
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')

        VALIDADOR_LOCALIZADO = pyperclip.paste()

        if VALIDADOR == VALIDADOR_LOCALIZADO:
            janela_excel.activate()
            pyautogui.write('INATIVO')
            pyautogui.press('right')
            pyautogui.press('down')
            janela_sisbb.activate()
        else:
            print(f'continuando... {i}')

    else:
        # COPIA O NOME
        pyautogui.press('down', presses=3)
        pyautogui.press('right', presses=28)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O NOME NO EXCEL
        pyautogui.write('ATIVO')
        pyautogui.press('right', presses=2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('right')
        janela_sisbb.activate()

        # COPIA O NÚMERO DO DDD
        pyautogui.press('down', presses=7)
        pyautogui.sleep(0.1)
        pyautogui.press('left', presses=7)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O DDD
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        pyautogui.press('right')
        pyautogui.sleep(0.1)
        janela_sisbb.activate()

        # COPIA O NÚMERO DE TRABALHO
        pyautogui.press('right', presses=5)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right', presses=8)
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O NÚMERO DE TRABALHO NO EXCEL
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        pyautogui.press('right')
        pyautogui.sleep(0.1)
        janela_sisbb.activate()

        # COPIA O SEGUNDO NÚMERO DE TRABALHO
        pyautogui.press('right', presses=4)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right', presses=8)
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O SEGUNDO NÚMERO DE TRABALHO
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        pyautogui.press('right')
        pyautogui.sleep(0.1)
        janela_sisbb.activate()

        # COPIA O TERCEIRO NÚMERO DE TRABALHO
        pyautogui.press('right', presses=4)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right', presses=8)
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O TERCEIRO NÚMERO DE TRABALHO
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('right')
        janela_sisbb.activate()

        # COPIA O NÚMERO DO TELEFONE RESIDENCIAL
        pyautogui.press('down')
        pyautogui.sleep(0.1)
        pyautogui.press('left', presses=33)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right', presses=9)
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O NÚMERO DO TELEFONE RESIDENCIAL
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        pyautogui.press('right')
        pyautogui.sleep(0.1)
        janela_sisbb.activate()

        # COPIA O NÚMERO DO CELULAR'
        pyautogui.press('down')
        pyautogui.press('left', presses=9)
        pyautogui.keyDown('shiftright')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('right', presses=9)
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('shiftleft')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        janela_excel.activate()

        # COLA O NÚMERO DO CELULAR
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        janela_sisbb.activate()

        # VOLTAR PARA O INICIO
        pyautogui.sleep(0.1)
        pyautogui.press('F3')
        pyautogui.sleep(0.1)

        # PRÓXIMA CHAVE
        janela_excel.activate()
        pyautogui.press('down')
        pyautogui.press('left', presses=7)

    i = i + 1

else:
    print('CABOU')
