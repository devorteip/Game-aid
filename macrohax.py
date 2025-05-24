from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

teclado = Controller()
macro_ativo = False
scroll_lock_ativado = False 

def verificar_scroll_lock():
    """Verifica o estado atual do Scroll Lock (simulado)"""
    return scroll_lock_ativado

def on_press(tecla):
    global macro_ativo

    try:
        if tecla == keyboard.Key.scroll_lock:
            global scroll_lock_ativado
            scroll_lock_ativado = not scroll_lock_ativado
            status = "ATIVADO" if scroll_lock_ativado else "DESATIVADO"
            print(f"\nMacro {status}! (Scroll Lock)")
            return

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
        pass

with keyboard.Listener(on_press=on_press) as listener:
    print("=== MACRO DA TECLA L ===")
    print("Pressione SCROLL LOCK para ativar/desativar o macro")
    print("Status atual: DESATIVADO (Scroll Lock off)")
    print("Quando ATIVADO: 'L' → 'LL' / 'l' → 'll'")
    print("Quando DESATIVADO: Todas teclas funcionam normalmente")
    print("\nPressione ESC para sair...")
    listener.join()
