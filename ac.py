from pynput.mouse import Button, Controller, Listener
import time
import threading

version = 0.2
mouse = Controller()

activation_button = Button.right
is_holding = False
click_delay = 0.05

def autoclick_loop():
    while True:
        if is_holding:
            mouse.click(Button.right)
            time.sleep(click_delay)
        else:
            time.sleep(0.01)

def on_click(x, y, button, pressed):
    global is_holding
    
    if button == activation_button:
        is_holding = pressed
        if pressed:
            print("Iniciando autoclick (segure o botão)")
        else:
            print("Parando autoclick")

def main():
    global activation_button, click_delay
    
    print("Bem Vindo ao Visca Auto Clicker (HOLD MODE)")
    print(f"Versão: {version}")
    print("         CARREGANDO SISTEMA. . .")
    time.sleep(0.5)
    
    print("\nOpções de botão de ativação:")
    print("   MBLEFT       MBRIGHT")
    print("     (1)          (2)")
    print("   MBSIDE1      MBSIDE2")
    print("     (3)          (4)")
    
    try:
        choice = int(input('Qual botão de ativação? >> '))
        if choice == 1:
            activation_button = Button.left
        elif choice == 2:
            activation_button = Button.right
        elif choice == 3:
            activation_button = Button.button8
        elif choice == 4:
            activation_button = Button.button9
        else:
            print("Opção inválida! Usando botão esquerdo padrão")
    except ValueError:
        print("Entrada inválida! Usando botão esquerdo padrão")

    try:
        cps = float(input('Quantos clicks por segundo? >> '))
        click_delay = 1 / cps if cps > 0 else 0.05
    except ValueError:
        print("Valor inválido! Usando 20 CPS padrão")
        click_delay = 0.05
    
    click_thread = threading.Thread(target=autoclick_loop, daemon=True)
    click_thread.start()
    
    print("\nModo HOLD ativado! Segure o botão para clicar.")
    print(f"Config: {1/click_delay:.1f} CPS | Botão: {activation_button}")
    print("Pressione Ctrl+C para sair")
    
    with Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nDesligando autoclicker...")

if __name__ == "__main__":
    main()
