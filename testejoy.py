import pydirectinput
import tkinter as tk
from threading import Thread
import time
import pyautogui
import subprocess
from pynput import keyboard
import queue

def obter_coordenadas_mouse():
    encerrar_listener = False
    listener = None  
    # Variável para armazenar as coordenadas do botão A
    coordenadas_mouse = None

    # Variável para controlar se o listener está em execução ou não
    listener_executando = False

    # Variável para controlar a saída do loop do listener
    def fechar():
        global encerrar_listener
        nonlocal listener_executando
        root1.destroy()  # Fecha a janela
        time.sleep(0.1)  # Pequeno atraso para garantir que a janela foi fechada corretamente
        #if listener_executando:
        #   listener.stop()  # Interrompe o listener manualmente

    def get_keypress_position_and_color(callback):
        nonlocal listener_executando
        global listener
        listener_executando = True

        def on_press(key):
            nonlocal coordenadas_mouse

            try:
                if key.char == 'a':
                    x, y = pyautogui.position()
                    coordenadas_mouse = (x, y)
                    callback('A', x, y)
            except AttributeError:
                if key == keyboard.Key.esc:
                    fechar()
                    return False

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

    # Exemplo de como utilizar a função
    def print_button_position(button_name, x, y):
        valor['text'] = "COORDENADAS: "+str((x, y))
    # Criando a interface gráfica com tkinter
    root1 = tk.Tk()
    root1.title("Coordenadas do Botão A")
    root1.wm_attributes("-topmost", 1)
    titulo = tk.Label(root1, text="Obter Coordenadas do Botão A")
    titulo.pack(padx=10, pady=10)
    valor = tk.Label(root1, text="COORDENADAS: "+str(coordenadas_mouse))
    valor.pack(padx=10, pady=10)
    label = tk.Label(root1, text="Pressione a tecla 'a' para definir as coordenadas do botão A.")
    label.pack(padx=10, pady=10)
    label2 = tk.Label(root1, text="Pressione a tecla 'ESC' para confirmar o valor de A.")
    label2.pack(padx=10, pady=10)

    # Define a função de fechamento da janela
    root1.protocol("WM_DELETE_WINDOW", fechar)  # Define a ação quando a janela é fechada

    # Inicia o listener de eventos de teclado em uma thread separada
    thread_teclado = Thread(target=get_keypress_position_and_color, args=(print_button_position,))
    thread_teclado.start()

    root1.mainloop()
    
    #return coordenadas_mouse
    #print(coordenadas_mouse)
    return coordenadas_mouse


def VAR1(queue):
    global coordenadas_a 
    coordenadas_a = obter_coordenadas_mouse()
    queue.put(coordenadas_a)

class Teste:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste")
        self.running = False

        self.status_label = tk.Label(root, text="COORDENADA", font=("Helvetica", 16))
        self.status_label.pack(pady=10)

        self.step_label = tk.Label(root, text="VALOR ATUAL", font=("Helvetica", 12))
        self.step_label.pack(pady=5)

        self.step_text = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.step_text.pack()
        
        self.start_stop_button = tk.Button(root, text="DEFINIR VARIAVEL", font=("Helvetica", 14), command=self.VAR1)
        self.start_stop_button.pack(pady=10)
        
        self.queue = queue.Queue()
        
    def update_step_text(self, step):
        self.step_text.delete(1.0, tk.END)
        self.step_text.insert(tk.END, step)

    def VAR1(self):
        thread = Thread(target=VAR1, args=(self.queue,))
        thread.start()
        self.check_queue()

    def check_queue(self):
        try:
            global coordenadas_a
            coordenadas_a = self.queue.get_nowait()
            if(coordenadas_a):
                coordenadas_a = coordenadas_a
            else:
                coordenadas_a = (0, 0)
            self.update_step_text(coordenadas_a)
        except queue.Empty:
            self.root.after(0, self.check_queue)  # Agendamos a próxima verificação após 100ms

    
def on_closing(root):
    global coordenadas_a
    root.quit()

def definircoordenadas():
    root = tk.Tk()
    app = Teste(root)
    global coordenadas_a
    coordenadas_a = (0, 0)
    root.protocol("WM_DELETE_WINDOW", on_closing(root))
    root.wm_attributes("-topmost", 1)  # Definir a janela como sempre no topo
    root.mainloop()
    return coordenadas_a

