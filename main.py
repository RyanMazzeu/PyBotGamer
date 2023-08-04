import tkinter as tk  # Importa a biblioteca tkinter para criação da interface gráfica
from tkinter import messagebox  # Importa a função messagebox da biblioteca tkinter
from PIL import Image, ImageTk  # Importa as classes Image e ImageTk da biblioteca PIL (Python Imaging Library)
import subprocess

class JanelaRolavel(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)            
        
        # cria um canvas e uma barra de rolagem para rolá-lo:
        rolagem = tk.Scrollbar(self, orient=tk.VERTICAL)
        rolagem.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=rolagem.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        rolagem.config(command=self.canvas.yview)

        # reseta a visão:
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # cria um frame dentro do canvas
        # para que seja rolado junto com ele:
        self.conteudo =  tk.Frame(self.canvas)
        self.id_conteudo = self.canvas.create_window(
            0, 0, window=self.conteudo, anchor=tk.NW)

        # cria eventos para detectar mudanças no canvas
        # e sincronizar com a barra de rolagem:
        self.conteudo.bind('<Configure>', self._configurar_conteudo)
        self.canvas.bind('<Configure>', self._configurar_canvas)

    def _configurar_conteudo(self, evento):
            # atualiza a barra de rolagem para o tamanho do frame de conteudo:
            tamanho = (
                self.conteudo.winfo_reqwidth(),
                self.conteudo.winfo_reqheight()
            )
            self.canvas.config(scrollregion="0 0 %s %s" % tamanho)
            if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
                # atualizar tambem a largura do canvas para caber o conteudo:
                self.canvas.config(width=self.conteudo.winfo_reqwidth())

    def _configurar_canvas(self, evento):
        if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
            # atualizar tambem a largura do conteudo para preencher o canvas:
            self.canvas.itemconfigure(
                self.id_conteudo, width=self.canvas.winfo_width())

def start_bot(comando):
    messagebox.showinfo("Bot", comando)  # Exibe uma caixa de mensagem com o texto do comando

def criar_creditos_frame():
    global creditos_frame
    creditos_frame = tk.Frame(app, bg="black")  # Cria o frame de créditos com fundo preto
    creditos_label = tk.Label(creditos_frame, text="Créditos:\n\nRYAN ALVES MAZZEU", fg="white", bg="black", font=("Helvetica", 14))  # Cria o label de créditos com o texto e fonte especificados
    creditos_label.pack(pady=50)  # Exibe o label de créditos com padding y igual a 50

    voltar_botao = tk.Button(creditos_frame, text="Voltar", command=voltar_menu_inicial, bg="black", fg="white", width=10)  # Cria o botão "Voltar" com o comando para voltar ao menu inicial e fundo preto, texto branco e largura 10
    voltar_botao.pack()  # Exibe o botão "Voltar"


def show_credits():
    titulo_label.destroy()
    global frame_info
    frame_info = tk.Frame(app, bg="black") 
    if info_frame.winfo_exists() and info_frame.winfo_ismapped():
        info_frame.pack_forget()
    
    # Esconde os elementos do menu 
    for widget in botoes_frame.winfo_children():
        widget.pack_forget()
    image_label.pack_forget()
    # 
    # Cria novamente o frame de créditos
    criar_creditos_frame()
    # Exibe o frame de créditos no centro da tela
    creditos_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def show_info():
    titulo_label.destroy()
    
    if creditos_frame.winfo_exists() and creditos_frame.winfo_ismapped():
        creditos_frame.pack_forget()

    for widget in botoes_frame.winfo_children():
        widget.pack_forget()
    image_label.pack_forget()

    # Cria uma instância da JanelaRolavel para exibir as informações
    info_texto = """
Instruções de Uso do Bot POKEMMO:
                                                                                                                   
Bem-vindo ao Bot POKEMMO, uma ferramenta criada por 
Ryan Alves Mazzeu para auxiliar os jogadores na bus-
ca por Pokémons Shinys no jogo. Este bot está em fase
de testes e foi desenvolvido com o intuito de tornar
a caça aos Pokémon Shinys uma tarefa mais prática e
eficiente.


Aqui vão algumas instruções:
*Desativar o flash pré batalhas*
--------------Bot de Hunting de Shiny Magikarp---------------

Bem-vindo ao Manual de Instruções para o Bot de Hunting
de Shiny Magikarp! Este bot é projetado para ajudá-lo a
caçar Pokémons Shiny no jogo POKEMMO, especificamente o
Magikarp Shiny, de forma mais prática e eficiente.
Antes de utilizar o bot, é necessário configurar o game
seguindo os requisitos abaixo:

1. Posicionamento Inicial:
Certifique-se de que o seu personagem esteja posicionado
inicialmente no Centro Pokémon (CP) de Sootopolis, de 
frente para a Nurse Joy. Isso é importante para garantir
o correto funcionamento do bot durante as etapas de caça.

2. Spawn do Teleport:
Verifique se o spawn do Teleport está configurado para o 
mesmo Centro Pokémon (Sootopolis). O Teleport será utili
zado para retornar ao CP após as sessões de caça e é 
essencial para otimizar o processo.

3. Sweet Scent:
Tenha a habilidade Sweet Scent com pelo menos 30 cargas 
disponíveis. Essa habilidade deve estar posicionada no 
atalho da tecla "6" no seu teclado. O bot utilizará o 
Sweet Scent para atrair Pokémon para a batalha durante 
a caça.

4. Teleport:
Certifique-se de que o Teleport esteja posicionado no 
atalho da tecla "7" no seu teclado. Essa habilidade será
usada para retornar rapidamente ao CP após cada sessão
de caça.

Agora que você configurou corretamente o seu game com os
requisitos acima, siga os passos abaixo para utilizar o 
Bot de Hunting de Shiny Magikarp:

Passo 1: Iniciar o Bot

• Ao abrir o bot, você será apresentado à tela inicial.
• Clique no botão "Iniciar Bot" para ativar o bot.

Passo 2: Execução do Bot

•O bot realizará automaticamente as etapas de caça pro
gramadas.
•Durante a execução, você pode acompanhar o progresso do 
bot na área de informações exibida na tela.

Passo 3: Verificação de Shiny

•Após cada batalha, o bot verificará automaticamente se 
um Pokémon Shiny foi encontrado.
•Caso o bot detecte um Pokémon Shiny, ele encerrará aut
omaticamente a execução e exibirá a mensagem "TEM SHINY".
•Caso contrário, o bot continuará a busca por Pokémons
Shiny.

Passo 4: Interromper o Bot

•Para interromper o bot durante a execução, clique no bo
tão "Parar Bot".
•O bot encerrará a execução atual e retornará ao estado 
inicial.

Passo 5: Consultar Quantidade de Tentativas

•Durante ou após a execução, o bot exibirá a quantidade 
de tentativas de batalha realizadas desde o início da caça.
•A quantidade será atualizada a cada sessão de caça
bem-sucedida.

Importante:

•Certifique-se de que o jogo esteja em tela cheia durante 
a execução do bot.
•Mantenha o foco na janela do jogo para garantir o correto 
funcionamento do bot.

Com este manual de instruções, você está pronto para uti
lizar o Bot de Hunting de Shiny Magikarp. Boa caçada e boa 
sorte na busca por Pokémons Shiny!

    """ + '\n'  

    # Cria um novo frame para agrupar o frame rolável e o botão
    global frame_info
    frame_info = tk.Frame(app, bg="black")
    frame_info.pack()

    info_janela = JanelaRolavel(frame_info, bg="black", bd=0)

    # Configuração do frame conteudo para ter fundo preto
    info_janela.conteudo.configure(bg="black")

    info_label = tk.Label(info_janela.conteudo, text=info_texto, fg="white", bg="black", font=("Helvetica", 14))
    info_label.pack(pady=0)

    # Exibe o frame de informações rolável no centro do frame_info
    info_janela.pack(side=tk.TOP, pady=10)

    # Cria o botão "Voltar" com fundo preto e texto branco
    voltar_botao = tk.Button(frame_info, text="Voltar", command=voltar_menu_inicial, bg="black", fg="white", width=10)
    voltar_botao.pack(pady=10)

    # Exibe o frame_info no centro da tela
    frame_info.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def voltar_menu_inicial():
    global frame_info

    # Esconde o frame de créditos
    if creditos_frame.winfo_exists():
        creditos_frame.pack_forget()
        creditos_frame.destroy()

    # Esconde o frame de informações
    if info_frame.winfo_exists():
        info_frame.pack_forget()
        info_frame.destroy()

    # Exclui o frame que contém o frame rolável e o botão
    if frame_info.winfo_exists():
        frame_info.pack_forget()
        frame_info.destroy()

    menu_inicial()

    
def BOT_MAGIKARP():
    arquivo1 = "MagickarpBOT.py"
    # Executar o código do arquivo1.py    
    with open(arquivo1, "r") as file:
        code = file.read()
        subprocess.Popen(["python", arquivo1])  

def menu_inicial():
    global titulo_label
    titulo_label = tk.Label(app, text="POKEMMO BOT", font=("Helvetica", 20, "bold"), fg="red", bg="black")  # Cria o label de título com texto "POKEMMO BOT", fonte "Helvetica" tamanho 20 em negrito, cor vermelha e fundo preto
    titulo_label.pack(pady=20, anchor=tk.N)  # Exibe o label de título com padding y igual a 20 e alinhamento norte (topo)
    image_label.pack(side=tk.RIGHT, padx=10, pady=10)  # Exibe o label da imagem alinhado à direita com padding x e y igual a 10
    botoes_frame.pack(side=tk.LEFT, padx=10)  # Exibe o frame de botões alinhado à esquerda com padding x igual a 10
    titulo_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)  # Exibe o label de título no centro da tela
    
    for i in range(4):
        if i == 1:
            botao = tk.Button(botoes_frame, text=comandos[i], command=BOT_MAGIKARP, bg="black", fg="white", width=35, height=2)
        elif i == 2:
            botao = tk.Button(botoes_frame, text=comandos[i], command=show_info, bg="black", fg="white", width=35, height=2)
        elif i == 3:
            botao = tk.Button(botoes_frame, text=comandos[i], command=show_credits, bg="black", fg="white", width=35, height=2)
        else:
            botao = tk.Button(botoes_frame, text=comandos[i], command=lambda comando=comandos[i]: start_bot(comando), bg="black", fg="white", width=35, height=2)
        botao.pack(pady=20)  # Cria e exibe os botões no frame de botões

comandos = [
    "Futuro Bot",
    "SHINY MAGIKARP (SOOTOPOLIS)",
    "Instruções",
    "Créditos",
]

###########################DADOS##############################################################################################################################################################################

app = tk.Tk()  # Cria a instância do aplicativo
app.title("POKEMMO BOT")  # Define o título da janela
app.iconbitmap("pokeball.ico")  # Define o ícone da janela


app.resizable(False, False)  # Impede o redimensionamento da janela
app.configure(bg="black")  # Define a cor de fundo da janela como preto

largura_janela = 600
altura_janela = 400
app.geometry(f"{largura_janela}x{altura_janela}")  # Define o tamanho da janela
#titulo_label.pack(pady=20, anchor=tk.N)  # Exibe o label de título com padding y igual a 20 e alinhamento norte (topo)

image_path = "Shiny Charizard.jpg"
image = Image.open(image_path)  # Abre a imagem do Charizard
image = image.resize((300, 294))  # Redimensiona a imagem para o tamanho desejado
photo = ImageTk.PhotoImage(image)  # Converte a imagem em um objeto PhotoImage para uso no tkinter
image_label = tk.Label(app, image=photo, bg="black")  # Cria o label da imagem com a imagem do Charizard e fundo preto
#image_label.pack(side=tk.RIGHT, padx=10, pady=10)  # Exibe o label da imagem alinhado à direita com padding x e y igual a 10

botoes_frame = tk.Frame(app, bg="black")  # Cria o frame para os botões com fundo preto
#botoes_frame.pack(side=tk.LEFT, padx=10)  # Exibe o frame de botões alinhado à esquerda com padding x igual a 10

creditos_frame = tk.Frame(app, bg="black")  # Cria o frame de créditos com fundo preto
creditos_label = tk.Label(creditos_frame, text="Créditos:\n\nInsira aqui os créditos e informações\nque deseja mostrar.", fg="white", bg="black", font=("Helvetica", 14))  # Cria o label de créditos com o texto e fonte especificados

info_frame = tk.Frame(app, bg="black")  # Cria o frame de créditos com fundo preto
info_label = tk.Label(info_frame, text="Créditos:\n\nInsira aqui os créditos e informações\nque deseja mostrar.", fg="white", bg="black", font=("Helvetica", 14))  # Cria o label de créditos com o texto e fonte especificados


voltar_botao = tk.Button(creditos_frame, text="Voltar", command=voltar_menu_inicial, bg="black", fg="white", width=10)  # Cria o botão "Voltar" com o comando para voltar ao menu inicial e fundo preto, texto branco e largura 10
voltar_botao.pack()  # Exibe o botão "Voltar"

########################################################################################## BOT ##############################################################################################################


menu_inicial()  # Exibe o menu inicial

app.mainloop()  # Inicia o loop principal do aplicativo
