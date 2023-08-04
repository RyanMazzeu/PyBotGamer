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
from magickarp import SETTINGSCOORDENADAS



def is_dialog_present(dialog_positions, dialog_color, tolerance=10): #VERIFICA SE TEM A CAIXA DE DIALOGO DA JOY
    for pos in dialog_positions:
        screenshot = pyautogui.screenshot(region=(pos[0], pos[1], 1, 1))
        pixel_color = screenshot.getpixel((0, 0))
        if all(abs(pixel_color[i] - dialog_color[i]) <= tolerance for i in range(3)):
            return True
    return False

def printar_retangulo(x1, y1, x2, y2, teste):
    # Capturar somente a região dentro do retângulo delimitado pelas coordenadas
    tela = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # Salvar a imagem capturada como um arquivo PNG
    tela.save(teste, "PNG")

# Coordenadas do retângulo (x1, y1) -> (x2, y2)
retangulo1 = (418, 144)
retangulo2 = (1402, 240)

quantidade = 0

# Coordenadas da pokebola
pokeball_x = 10
pokeball_y = 10

# Pixels para controle de cor
coordenadaCP = (1720, 253)
coordenadaLago = (675, 160)
coordenadaNado = (1707, 136)
coordenadaSweet = (1619, 464)

dialog_color = (253, 253, 253)  # Cor do diálogo (branco)
npc_dialog_positions = [(540, 135), (950, 114), (1354, 126)]  #COORDENADA

def load_pokeball_image(angle):
    pokeball_image = Image.open("pokeball.png")
    pokeball_image = pokeball_image.resize((30, 30), Image.LANCZOS)
    rotated_image = pokeball_image.rotate(angle)
    return ImageTk.PhotoImage(rotated_image)



class PokemonBotApp:
    
    def show_help(self, event=None):
        if not self.help_button_pressed:  # Executa somente quando o botão é pressionado pela primeira vez
            self.help_button_pressed = True  
            global coordenadaCP, coordenadaLago, coordenadaNado, coordenadaSweet, npc_dialog_positions, retangulo1, retangulo2
            coordenadaCP, coordenadaLago, coordenadaNado, coordenadaSweet, npc_dialog_positions[0], npc_dialog_positions[1], npc_dialog_positions[2],retangulo1,retangulo2 = SETTINGSCOORDENADAS(coordenadaCP, coordenadaLago, coordenadaNado, coordenadaSweet, npc_dialog_positions[0], npc_dialog_positions[1], npc_dialog_positions[2], retangulo1, retangulo2)
        else:
            self.help_button_pressed = False
        

    def update_pokeball(self):
        if(self.pokeball_label.winfo_exists() == True):
            self.current_image_index = (self.current_image_index + 1) % len(self.pokeball_images)
            self.pokeball_label.config(image=self.pokeball_images[self.current_image_index])
            self.root.after(50, self.update_pokeball)
        
    def on_close(self):
        self.stop_bot()
        self.root.destroy()
        
    def __init__(self, root):
        self.pokeball_images = [load_pokeball_image(angle) for angle in range(360, 0, -60)]
        self.current_image_index = 0
        self.root = root
        self.root.title("Hunting Magikarp Bot")
        self.root.iconbitmap("magikarp.ico")  # Define o ícone da janela
        self.running = False  
        self.help_button_pressed = False
        
        self.status_label = tk.Label(root, text="Bot desligado", font=("Helvetica", 16), fg="red")
        self.status_label.pack(pady=10)

        self.start_stop_button = tk.Button(root, text="Iniciar Bot", font=("Helvetica", 14), command=self.toggle_bot)
        self.start_stop_button.pack(pady=10)

        self.help_button = tk.Button(root, text="?", font=("Helvetica", 14), command=self.show_help)
        self.help_button.place(x=10, y=10)
    
        self.step_label = tk.Label(root, text="Etapa atual: ", font=("Helvetica", 14))
        self.step_label.pack(pady=5)

        self.step_text = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.step_text.pack()
        
        self.adicional_label = tk.Label(root, text="Subetapa: ", font=("Helvetica", 14))
        self.adicional_label.pack(pady=10)

        self.adicional_text = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.adicional_text.pack()
        
        self.adicional_text2 = tk.Text(root, width=30, height=3, font=("Helvetica", 12), wrap=tk.WORD)
        self.adicional_text2.pack()
        
        self.adicional_text3 = tk.Text(root, width=30, height=1, font=("Helvetica", 12), wrap=tk.WORD)
        self.adicional_text3.pack()
    

        
    def reset_bot(self):
        self.running = False
        self.adicional_text.delete(1.0, tk.END)
        self.adicional_text2.delete(1.0, tk.END)
        self.adicional_text3.delete(1.0, tk.END)
        self.step_text.delete(1.0, tk.END)
        if hasattr(self, "pokeball_label") and self.pokeball_label.winfo_exists():
            self.pokeball_label.destroy() 
        self.status_label.config(text="Bot desligado", fg="red")
        self.start_stop_button.config(text="Iniciar Bot")

    def toggle_bot(self):
        if self.running:
            self.reset_bot()
        else:
            self.running = True
            
            self.pokeball_label = tk.Label(root, image=self.pokeball_images[self.current_image_index])
            self.pokeball_label.pack()
            self.update_pokeball()

            self.start_stop_button.config(text="Parar Bot")
            self.status_label.config(text="Bot funcionando", fg="green")
            self.bot_thread = Thread(target=self.bot_loop)
            self.bot_thread.start()
            

    def update_step_text(self, step):
        self.step_text.delete(1.0, tk.END)
        self.step_text.insert(tk.END, step)
        
    def update_adicional_text(self, adicional):
        self.adicional_text.delete(1.0, tk.END)
        self.adicional_text.insert(tk.END, adicional)
        
    def update_adicional_text2(self, adicional2):
        self.adicional_text2.delete(1.0, tk.END)
        self.adicional_text2.insert(tk.END, adicional2)
        
    def update_adicional_text3(self, adicional3):        
        self.adicional_text3.delete(1.0, tk.END)
        self.adicional_text3.insert(tk.END, adicional3)

    def bot_loop(self):
        
        def read_number_from_file(file_path):
            with open(file_path, "r") as file:
                number = int(file.read())
            return number

        def write_number_to_file(file_path, number):
            with open(file_path, "w") as file:
                file.write(str(number))
        
        file_path = 'QUANTIDADE.txt'  # Substitua pelo caminho do seu arquivo de texto
        quantidade = read_number_from_file(file_path)
        
        self.update_adicional_text3("QUANTIDADE: " + str(quantidade))
        try:
            while self.running:
                self.update_step_text("Restaurando Pokemons...")
                time.sleep(1)
                self.restore_pokemons() #revisado e pausa bonitinho
                    
                if not self.running:
                    break

                self.update_step_text("Saindo do CP...")
                time.sleep(1)
                self.exit_cp() #revisado e pausa bonitinho

                if not self.running:
                    break
                
                self.update_step_text("Indo para o lago...")
                time.sleep(1)
                self.go_to_lake()

                if not self.running:
                    break

                self.update_step_text("Nadando...")
                time.sleep(1)
                self.swim()
                
                
                time.sleep(1)
                if not self.running:
                    break
                
                for i in range(0, 6):
                    if not self.running:
                        break
                    
                    self.update_step_text("Usando Sweet Scent...")
                    time.sleep(1)
                    self.use_sweet_scent()
                        
                    self.update_step_text("Batalhando pela {}ª vez...".format(i+1))
                    time.sleep(1)
                    self.battle()
                        
                    write_number_to_file(file_path, quantidade+5)
                    quantidade = quantidade + 5
                    self.update_adicional_text3("QUANTIDADE: " + str(quantidade))

                if not self.running:
                    break
                
                self.update_step_text("Voltando para o CP...")
                time.sleep(1)
                self.return_to_cp()
                '''    
                if not self.running:
                    break
                '''  
                self.update_step_text("Concluído! Aguardando próxima execução.")
                time.sleep(1)  # Aguardar um tempo antes de recomeçar
                    
        except KeyboardInterrupt:
            self.stop_bot()
            
    aux = 0
    def restore_pokemons(self):
        # Posição do CP
        color = pyautogui.screenshot().getpixel(coordenadaCP) #COORDENADA DO CP
        self.update_adicional_text("Verificando se voltou para o CP...")
        while(color[0]>5 or color[1]>5 or color[2]>5): #VERIFICANDO SE VOLTOU PARA O CP OU NÃO
            time.sleep(1)
            color = pyautogui.screenshot().getpixel(coordenadaCP)
            '''
            '''
            if not self.running:
                break
            ''''''
        self.adicional_text.delete(1.0, tk.END)
        
        if self.running:
            self.adicional_text.insert(tk.END, "Conversando com a JOY...")
            
        
        # Posições dos possíveis diálogos
        
        restore_started = False  # Variável de controle para indicação da restauração iniciada
        self.z_pressed = False # Variável de controle para indicação da tecla "Z" pressionada
        primeira = True 
        while True:
            ''''''
            if not self.running:
                break
            ''''''
            dialog_present = is_dialog_present(npc_dialog_positions, dialog_color)
            
            if(primeira):
                while(dialog_present == False):
                    dialog_present = is_dialog_present(npc_dialog_positions, dialog_color)
                    keyboard.press('z')
                    time.sleep(0.1)
                    keyboard.release('z')
                    primeira = False
                    if not self.running:
                        break
                    
            if(dialog_present):
                    keyboard.press('z')
                    self.z_pressed = True
            else:
                if self.z_pressed:
                    keyboard.release('z')
                    self.z_pressed = False
                    restore_started = True
                
        # Verifica se a restauração foi concluída e atualiza a label correspondente
            if restore_started and not dialog_present:
                aux = aux + 1
            else:
                aux = 0
            time.sleep(0.1)  # Aguarda um curto intervalo antes de atualizar novamente
            if(aux==5):
                self.adicional_text.delete(1.0, tk.END) 
                break
            

    
    def exit_cp(self):
        self.update_adicional_text("Saindo do CP...")
        aux = 0
        while(pyautogui.screenshot().getpixel(coordenadaCP)[0]<5 or pyautogui.screenshot().getpixel(coordenadaCP)[1]<5 or pyautogui.screenshot().getpixel(coordenadaCP)[2]<5):  
        #COORDENADA
            if not self.running:
                    break
            
            keyboard.press('s')
            time.sleep(0.1)
            keyboard.release('s')
            time.sleep(0.1)
            aux = aux + 1
            if(aux==20):
                break
            
 
        pass

    def go_to_lake(self):
        self.update_adicional_text("Indo para o lago...")
        aux = 0
        #COORDENADA
        while(pyautogui.screenshot().getpixel(coordenadaLago)[0]>80):
            
            if not self.running:
                break
            
            keyboard.press('s')
            time.sleep(0.1)
            keyboard.release('s')
            aux = aux + 1
            if(aux==20):
                break
            
            
        pass

    def swim(self):
        self.update_adicional_text("De volta ao lago...")
        time.sleep(1)
        aux = 0
        #COORDENADA
        while(pyautogui.screenshot().getpixel(coordenadaNado)[0]>100 or pyautogui.screenshot().getpixel(coordenadaNado)[1]>100 or pyautogui.screenshot().getpixel(coordenadaNado)[2]>100):
            
            if not self.running:
                break
            
            keyboard.press('z')
            time.sleep(0.1)
            keyboard.release('z')
            time.sleep(0.1)
            aux = aux + 1
            if(aux==20):
                break

        self.update_adicional_text("Nadando...")
        pass

    def use_sweet_scent(self):
        time.sleep(1) 
        aux = 0 
        self.update_adicional_text("Preparando...")
        #COORDENADA SWEET SCENT
        while(pyautogui.screenshot().getpixel(coordenadaSweet)[0]<230 or pyautogui.screenshot().getpixel(coordenadaSweet)[1]<230 or pyautogui.screenshot().getpixel(coordenadaSweet)[2]<230):
            
            if not self.running:
                break
            
            keyboard.press('6')
            time.sleep(0.1)
            keyboard.release('6')
            time.sleep(0.1)
            self.update_adicional_text("Usando o Sweet Scent...")
            if(aux==20):
                break
    
        pass

    def battle(self):
        self.update_adicional_text("Esperando a partida normalizar...")
        #COORDENADA
        while(pyautogui.screenshot().getpixel(coordenadaSweet)[0]<230 or pyautogui.screenshot().getpixel(coordenadaSweet)[1]<230 or pyautogui.screenshot().getpixel(coordenadaSweet)[2]<230):
            time.sleep(0.1)
            '''
            if not self.running:
                break
            '''
        if self.running:
            self.update_adicional_text("VERIFICANDO SHINY...")
            teste = "teste.png"
            # Chamar a função para capturar e salvar somente o retângulo delimitado pelas coordenadas
            printar_retangulo(retangulo1[0], retangulo1[1], retangulo2[0], retangulo2[1], teste)
            
            # Defina o caminho para o executável do Tesseract (caso não esteja no PATH)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            # Caminho da imagem com texto que deseja realizar OCR
            image_path = 'teste.png'

            # Abra a imagem usando a biblioteca PIL
            img = Image.open(image_path)

            # Realize OCR na imagem
            resultado = pytesseract.image_to_string(img, lang='por')
            # Imprima o resultado do OCR
            resultado = resultado.replace(' ', '')
            resultado = resultado.replace('\n', '')
            resultado = resultado.lower()
            self.update_adicional_text2(resultado)
    
            if('shi' in resultado or 'hiny' in resultado):
                self.update_adicional_text("TEM SHINY")
                sys.exit()
            else:
                self.update_adicional_text("NÃO TEM SHINY")
                time.sleep(3)
                self.update_adicional_text("Saindo da partida...")
                pyautogui.moveTo(770,733, duration=1)
                pyautogui.click()

            while(pyautogui.screenshot().getpixel(coordenadaSweet)[0]>230 and pyautogui.screenshot().getpixel(coordenadaSweet)[1]>230 and pyautogui.screenshot().getpixel(coordenadaSweet)[2]>230):
                self.update_adicional_text("SAINDO DA PARTIDA...")
                time.sleep(0.1)
                #COORDENADA
            
            pass

    def return_to_cp(self):
        aux = 0
        self.update_adicional_text("Voltando para o CP...")
        #COORDENADA
        while(pyautogui.screenshot().getpixel(coordenadaCP)[0]>5 or pyautogui.screenshot().getpixel(coordenadaCP)[1]>5 or pyautogui.screenshot().getpixel(coordenadaCP)[2]>5):            
            keyboard.press('7')
            time.sleep(0.1)
            keyboard.release('7')
            time.sleep(0.1)
            
        pass

    def stop_bot(self):
        self.reset_bot()
        if hasattr(self, "bot_thread") and self.bot_thread.is_alive():
            self.bot_thread.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonBotApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  
    root.wm_attributes("-topmost", 1)  # Definir a janela como sempre no topo
    root.mainloop()