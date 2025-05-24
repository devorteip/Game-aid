from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

teclado = Controller()
macro_ativo = False
scroll_lock_ativado = False  # Estado inicial do Scroll Lock

def verificar_scroll_lock():
    """Verifica o estado atual do Scroll Lock (simulado)"""
    # Nota: pynput não pode ler estados de LED, então simulamos com uma variável
    return scroll_lock_ativado

def on_press(tecla):
    global macro_ativo

    try:
        # Verifica se é Scroll Lock sendo pressionado
        if tecla == keyboard.Key.scroll_lock:
            global scroll_lock_ativado
            scroll_lock_ativado = not scroll_lock_ativado
            status = "ATIVADO" if scroll_lock_ativado else "DESATIVADO"
            print(f"\nMacro {status}! (Scroll Lock)")
            return

        # Se Scroll Lock estiver DESLIGADO e for 'L'
        if not verificar_scroll_lock() and tecla.char.lower() == 'l' and not macro_ativo:
            print("Tecla 'L' pressionada. Duplicando...")
            macro_ativo = True
            
            if tecla.char.isupper():
                teclado.press(Key.shift)
                teclado.tap('l')
                teclado.release(Key.shift)
            else:
                teclado.tap('l')
            
            time.sleep(0.05)
            macro_ativo = False
            
    except AttributeError:
        pass  # Ignora teclas especiais

with keyboard.Listener(on_press=on_press) as listener:
    print("=== MACRO DA TECLA L ===")
    print("Pressione SCROLL LOCK para ativar/desativar o macro")
    print("Status atual: DESATIVADO (Scroll Lock off)")
    print("Quando ATIVADO: 'L' → 'LL' / 'l' → 'll'")
    print("Quando DESATIVADO: Todas teclas funcionam normalmente")
    print("\nPressione ESC para sair...")
    listener.join()