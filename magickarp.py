from testejoy import definircoordenadas
import pydirectinput
import tkinter as tk
from threading import Thread
from pynput.keyboard import Listener
import time
import pyautogui
import keyboard
import sys
from PIL import Image
import pytesseract
from PIL import ImageGrab
from PIL import ImageDraw
from PIL import ImageTk


class COORDENADAS:

    def on_close(self):
        self.stop_bot()
        self.root.quit()
        self.root.destroy()
        
    def __init__(self, root):
        self.root = root
        self.root.title("Coordenadas")
        
        self.running = False  
        self.help_button_pressed = False
        
        self.status_label = tk.Label(root, text="COORDENADAS DOS PIXELS", font=("Arial Black", 16), fg="blue")
        self.status_label.grid(pady=1, row=0, column=0, columnspan=2)
        
        '''-----------------------------------------------------------------------------------------------------------------'''
        self.botaoc1 = tk.Button(root, text="Definir coordenada 1:", font=("Helvetica", 14), command=self.COORDENADA1)
        self.botaoc1.grid(pady=1, column=0, row=1)
        
        self.mostrar1 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA1)
        self.mostrar1.grid(pady=1, column=1 ,row=1)
       
        self.coordenada1 = tk.Label(root, text="Coordenada 1: ", font=("Helvetica", 14))
        self.coordenada1.grid(pady=1)
        
        self.texto_coordenada1 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        
        self.texto_coordenada1.grid()
        
        self.update_texto_coordenada1(Coordenadas1)
        
        '''-----------------------------------------------------------------------------------------------------------------'''
        self.botaoc2 = tk.Button(root, text="Definir coordenada 2:", font=("Helvetica", 14), command=self.COORDENADA2)
        self.botaoc2.grid(pady=1,column=0, row=4)
        
        self.mostrar2 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA2)
        self.mostrar2.grid(pady=1, column=1 ,row=4)

        self.coordenada2 = tk.Label(root, text="Coordenada 2: ", font=("Helvetica", 14))
        self.coordenada2.grid(pady=1)
        
        self.texto_coordenada2 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada2.grid()
        self.update_texto_coordenada2(Coordenadas2)
        
        '''-----------------------------------------------------------------------------------------------------------------'''
        self.botaoc3 = tk.Button(root, text="Definir coordenada 3:", font=("Helvetica", 14), command=self.COORDENADA3)
        self.botaoc3.grid(pady=1,column=0, row=7)
        
        self.mostrar3 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA3)
        self.mostrar3.grid(pady=1, column=1 ,row=7)
        
        self.coordenada3 = tk.Label(root, text="Coordenada 3: ", font=("Helvetica", 14))
        self.coordenada3.grid(pady=1)
        
        self.texto_coordenada3 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada3.grid()
        self.update_texto_coordenada3(Coordenadas3)
        '''-----------------------------------------------------------------------------------------------------------------'''
        self.botaoc4 = tk.Button(root, text="Definir coordenada 4:", font=("Helvetica", 14), command=self.COORDENADA4)
        self.botaoc4.grid(pady=1, column=0 ,row=10)
        
        self.mostrar4 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA4)
        self.mostrar4.grid(pady=1, column=1 ,row=10)
        
        self.coordenada4 = tk.Label(root, text="Coordenada 4: ", font=("Helvetica", 14))
        self.coordenada4.grid(pady=1)
        
        self.texto_coordenada4 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada4.grid()
        self.update_texto_coordenada4(Coordenadas4) 
        '''-----------------------------------------------------------------------------------------------------------------'''
        
        self.botaoc5 = tk.Button(root, text="Definir coordenada 5:", font=("Helvetica", 14), command=self.COORDENADA5)
        self.botaoc5.grid(pady=1, column=0 ,row=13)
        
        self.mostrar5 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA5)
        self.mostrar5.grid(pady=1, column=1 ,row=13)
        
        self.coordenada5 = tk.Label(root, text="Coordenada 5: ", font=("Helvetica", 14))
        self.coordenada5.grid(pady=1)
        
        self.texto_coordenada5 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada5.grid()
        self.update_texto_coordenada5(Coordenadas5) 
        
        '''-----------------------------------------------------------------------------------------------------------------'''
        
        self.botaoc6 = tk.Button(root, text="Definir coordenada 6:", font=("Helvetica", 14), command=self.COORDENADA6)
        self.botaoc6.grid(pady=1, column=0 ,row=16)
        
        self.mostrar6 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA6)
        self.mostrar6.grid(pady=1, column=1 ,row=16)
        
        self.coordenada6 = tk.Label(root, text="Coordenada 6: ", font=("Helvetica", 14))
        self.coordenada6.grid(pady=1)
        
        self.texto_coordenada6 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada6.grid()
        self.update_texto_coordenada6(Coordenadas6)
        
        '''-----------------------------------------------------------------------------------------------------------------'''
        
        self.botaoc7 = tk.Button(root, text="Definir coordenada 7:", font=("Helvetica", 14), command=self.COORDENADA7)
        self.botaoc7.grid(pady=1, column=0 ,row=19)
        
        self.mostrar7 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA7)
        self.mostrar7.grid(pady=1, column=1 ,row=19)
        
        self.coordenada7 = tk.Label(root, text="Coordenada 7: ", font=("Helvetica", 14))
        self.coordenada7.grid(pady=1)
        
        self.texto_coordenada7 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada7.grid()
        self.update_texto_coordenada7(Coordenadas7)
        #COPIAR AQUI
        
        '''-----------------------------------------------------------------------------------------------------------------'''
                
        # Criação do Frame para os botões
        button_frame = tk.Frame(root)
        button_frame.grid(row=22, column=0, columnspan=3, pady=1, sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        # Primeiro botão
        self.botaoc8 = tk.Button(button_frame, text="Ret1", font=("Helvetica", 14), command=self.COORDENADA8)
        self.botaoc8.grid(row=0, column=0, sticky="ew")

        # Segundo botão
        self.botaoc9 = tk.Button(button_frame, text="Ret2", font=("Helvetica", 14), command=self.COORDENADA9)
        self.botaoc9.grid(row=0, column=1, sticky="ew")

        
        self.coordenadas8 = tk.Label(root, text="Coordenadas Retangulo: ", font=("Helvetica", 14))
        self.coordenadas8.grid(pady=1,column=0 ,row=23)
        
        self.mostrar8 = tk.Button(root, text="View", font=("Helvetica", 14), command=self.MOSTRARCOORDENADA8)
        self.mostrar8.grid(pady=1, column=1 ,row=23)
        
        self.texto_coordenada8 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.texto_coordenada8.grid()
        self.update_texto_coordenada8(str(Coordenadas8) + "  " + str(Coordenadas9))
    
    #Label final pra n ficar feio
        self.labelfinal = tk.Label(root, text=" ", font=("Helvetica", 14))
        self.labelfinal.grid(pady=1)
        
    def reset_bot(self):
        self.running = False
        #COPIAR AQUI
        self.texto_coordenada1.delete(1.0, tk.END)
        self.texto_coordenada2.delete(1.0, tk.END)
        self.texto_coordenada3.delete(1.0, tk.END)
        self.texto_coordenada4.delete(1.0, tk.END)
        self.texto_coordenada5.delete(1.0, tk.END)
        self.texto_coordenada6.delete(1.0, tk.END)
        self.texto_coordenada7.delete(1.0, tk.END)
        self.texto_coordenada8.delete(1.0, tk.END)
        '''-----------------------------------------------------------------------------------------------------------------'''
  
    def COORDENADA1(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada1)
        thread.start()

    def obter_coordenada1(self):
        global Coordenadas1
        Coordenadas1 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada1(Coordenadas1)
        
    def MOSTRARCOORDENADA1(self):
        pyautogui.moveTo(Coordenadas1, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
        
    def COORDENADA2(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada2)
        thread.start()
        
    def obter_coordenada2(self):
        global Coordenadas2
        Coordenadas2 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada2(Coordenadas2)       

    def MOSTRARCOORDENADA2(self):
        pyautogui.moveTo(Coordenadas2, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
        
    def COORDENADA3(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada3)
        thread.start()
        
    def obter_coordenada3(self):
        global Coordenadas3
        Coordenadas3 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada3(Coordenadas3)    

    def MOSTRARCOORDENADA3(self):
        pyautogui.moveTo(Coordenadas3, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
    def COORDENADA4(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada4)
        thread.start()
        
    def obter_coordenada4(self):
        global Coordenadas4
        Coordenadas4 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada4(Coordenadas4)

    def MOSTRARCOORDENADA4(self):
        pyautogui.moveTo(Coordenadas4, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
        
    def COORDENADA5(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada5)
        thread.start()
    
    def obter_coordenada5(self):
        global Coordenadas5
        Coordenadas5 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada5(Coordenadas5)
        
    def MOSTRARCOORDENADA5(self):
        pyautogui.moveTo(Coordenadas5, duration=1)   
    '''-----------------------------------------------------------------------------------------------------------------'''
        
    def COORDENADA6(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada6)
        thread.start()
        
    def obter_coordenada6(self):
        global Coordenadas6
        Coordenadas6 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada6(Coordenadas6)
        
    def MOSTRARCOORDENADA6(self):
        pyautogui.moveTo(Coordenadas6, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
    
    def COORDENADA7(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada7)
        thread.start()
    
    def obter_coordenada7(self):
        global Coordenadas7
        Coordenadas7 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada7(Coordenadas7)
        
    def MOSTRARCOORDENADA7(self):
        pyautogui.moveTo(Coordenadas7, duration=1)
    #COPIAR AQUI
    '''-----------------------------------------------------------------------------------------------------------------'''
    def COORDENADA8(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada8)
        thread.start()
    
    def obter_coordenada8(self):
        global Coordenadas8, Coordenadas9
        Coordenadas8 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada8(str(Coordenadas8) + "  " + str(Coordenadas9))
    
    def COORDENADA9(self):
        # Iniciar uma nova thread para executar a função definircoordenadas()
        thread = Thread(target=self.obter_coordenada9)
        thread.start()
    
    def obter_coordenada9(self):
        global Coordenadas9
        Coordenadas9 = definircoordenadas()
        # Atualizar o widget de texto com as coordenadas obtidas
        self.update_texto_coordenada8(str(Coordenadas8) + "  " + str(Coordenadas9))

    def MOSTRARCOORDENADA8(self):
        pyautogui.moveTo(Coordenadas8, duration=1)
        pyautogui.moveTo(Coordenadas9, duration=1)
    '''-----------------------------------------------------------------------------------------------------------------'''
    
    def update_texto_coordenada1(self, step):
        if self.texto_coordenada1.winfo_exists():  # Verifica se o widget ainda existe
            self.texto_coordenada1.delete(1.0, tk.END)
            self.texto_coordenada1.insert(tk.END, str(step))
            self.texto_coordenada1.tag_configure("center", justify='center')
            self.texto_coordenada1.tag_add("center", "1.0", "end")
            
    def update_texto_coordenada2(self, step):
        if self.texto_coordenada2.winfo_exists():  # Verifica se o widget ainda existe
            self.texto_coordenada2.delete(1.0, tk.END)
            self.texto_coordenada2.insert(tk.END, str(step))
            self.texto_coordenada2.tag_configure("center", justify='center')
            self.texto_coordenada2.tag_add("center", "1.0", "end")
        
    def update_texto_coordenada3(self, step):
        if self.texto_coordenada3.winfo_exists():  # Verifica se o widget ainda existe
            self.texto_coordenada3.delete(1.0, tk.END)
            self.texto_coordenada3.insert(tk.END, str(step))
            self.texto_coordenada3.tag_configure("center", justify='center')
            self.texto_coordenada3.tag_add("center", "1.0", "end")

    def update_texto_coordenada4(self, step):
        if self.texto_coordenada4.winfo_exists():  # Verifica se o widget ainda existe
            self.texto_coordenada4.delete(1.0, tk.END)
            self.texto_coordenada4.insert(tk.END, str(step))
            self.texto_coordenada4.tag_configure("center", justify='center')
            self.texto_coordenada4.tag_add("center", "1.0", "end")

    def update_texto_coordenada5(self, step):
        if self.texto_coordenada5.winfo_exists():
            self.texto_coordenada5.delete(1.0, tk.END)
            self.texto_coordenada5.insert(tk.END, str(step))
            self.texto_coordenada5.tag_configure("center", justify='center')
            self.texto_coordenada5.tag_add("center", "1.0", "end")
    
    def update_texto_coordenada6(self, step):
        if self.texto_coordenada6.winfo_exists():
            self.texto_coordenada6.delete(1.0, tk.END)
            self.texto_coordenada6.insert(tk.END, str(step))
            self.texto_coordenada6.tag_configure("center", justify='center')
            self.texto_coordenada6.tag_add("center", "1.0", "end")

    def update_texto_coordenada7(self, step):
        if self.texto_coordenada7.winfo_exists():
            self.texto_coordenada7.delete(1.0, tk.END)
            self.texto_coordenada7.insert(tk.END, str(step))
            self.texto_coordenada7.tag_configure("center", justify='center')
            self.texto_coordenada7.tag_add("center", "1.0", "end")
    
    def update_texto_coordenada8(self, step):
        if self.texto_coordenada8.winfo_exists():
            self.texto_coordenada8.delete(1.0, tk.END)
            self.texto_coordenada8.insert(tk.END, str(step))
            self.texto_coordenada8.tag_configure("center", justify='center')
            self.texto_coordenada8.tag_add("center", "1.0", "end")
        
        
    def stop_bot(self):
        self.reset_bot()
        
    #COPIAR AQUI

def SETTINGSCOORDENADAS(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    global Coordenadas1, Coordenadas2, Coordenadas3, Coordenadas4, Coordenadas5, Coordenadas6, Coordenadas7, Coordenadas8, Coordenadas9
    Coordenadas1 = c1
    Coordenadas2 = c2
    Coordenadas3 = c3
    Coordenadas4 = c4
    Coordenadas5 = c5
    Coordenadas6 = c6
    Coordenadas7 = c7
    Coordenadas8 = c8
    Coordenadas9 = c9
    root = tk.Tk()
    app = COORDENADAS(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  
    root.wm_attributes("-topmost", 1)  # Definir a janela como sempre no topo
    root.mainloop()
    return Coordenadas1, Coordenadas2, Coordenadas3, Coordenadas4, Coordenadas5, Coordenadas6, Coordenadas7, Coordenadas8, Coordenadas9