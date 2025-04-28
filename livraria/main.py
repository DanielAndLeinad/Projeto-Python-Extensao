# -----(main.py)-----

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
from dados import delete_book, delete_user  # Importando funções de exclusão do banco de dados
from view import display_books, display_loans, display_users, insert_book, insert_user, insert_loan, update_return
from view import update_return
print(update_return)

# Cores
co0 = "#5D473A"  # marrom
co1 = "#CBB994"  # bege topo
co2 = "#8A7968"  # menu lateral
co3 = "#4F6D7A"  # botoes azul
co4 = "#6B4226"  # fundo direita
co5 = "#A3B18A"  # verde suave
co6 = "#D9C5B2"  # fundo listas
co10 = "#F2E8CF" # creme

# Janela
janela = Tk()
janela.title("Sistema de Gerenciamento de Livros")
janela.geometry('800x450')
janela.configure(bg=co0)
janela.resizable(False, False)

# Frames
frameTop = Frame(janela, height=60, bg=co1)
frameTop.pack(fill=X)

frameLeft = Frame(janela, width=230, bg=co2)
frameLeft.pack(side=LEFT, fill=Y)

frameRight = Frame(janela, bg=co4)
frameRight.pack(side=RIGHT, expand=True, fill=BOTH)

# Logo e título
img_logo = Image.open('./imgs/logo-livro.png').resize((40, 40))
img_logo = ImageTk.PhotoImage(img_logo)
Label(frameTop, image=img_logo, bg=co1).place(x=10, y=10)
Label(frameTop, text="Sistema de Gerenciamento de Livros", font=('Verdana 16 bold'), bg=co1, fg=co0).place(x=60, y=15)

# Limpar frame principal
def limpar():
    for widget in frameRight.winfo_children():
        widget.destroy()

# Telas

def tela_cadastrar_livro():
    limpar()
    Label(frameRight, text="Cadastrar Livro", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    campos = ["Título", "Autor", "Editora", "Ano de Publicação", "ISBN"]
    entradas = []

    for campo in campos:
        Label(frameRight, text=f"{campo}:", font=('Verdana 10'), bg=co4, fg=co10).pack(pady=2)
        entry = Entry(frameRight, width=40)
        entry.pack()
        entradas.append(entry)

    def salvar():
        # Inserir livro na base de dados
        livro = tuple(e.get() for e in entradas)
        if all(livro):  # Verifica se todos os campos foram preenchidos
            insert_book(*livro)  # Chama a função para salvar no banco
            print(f"Livro cadastrado: {livro}")
            for e in entradas:
                e.delete(0, END)  # Limpa os campos
            Label(frameRight, text="Livro cadastrado com sucesso!", font=('Verdana 10'), bg=co4, fg='green').pack(pady=5)
        else:
            Label(frameRight, text="Preencha todos os campos!", font=('Verdana 10'), bg=co4, fg='red').pack(pady=5)

    Button(frameRight, text="Salvar Livro", font=('Verdana 10 bold'), bg=co5, command=salvar).pack(pady=10)

def tela_cadastrar_usuario():
    limpar()
    Label(frameRight, text="Cadastrar Usuário", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    campos = ["Nome", "Sobrenome", "Endereço", "Telefone", "Email"]
    entradas = []

    for campo in campos:
        Label(frameRight, text=f"{campo}:", font=('Verdana 10'), bg=co4, fg=co10).pack(pady=2)
        entry = Entry(frameRight, width=40)
        entry.pack()
        entradas.append(entry)

    def salvar():
        # Inserir usuário na base de dados
        usuario = tuple(e.get() for e in entradas)
        if all(usuario):  # Verifica se todos os campos foram preenchidos
            insert_user(*usuario)  # Chama a função para salvar no banco
            print(f"Usuário cadastrado: {usuario}")
            for e in entradas:
                e.delete(0, END)  # Limpa os campos
            Label(frameRight, text="Usuário cadastrado com sucesso!", font=('Verdana 10'), bg=co4, fg='green').pack(pady=5)
        else:
            Label(frameRight, text="Preencha todos os campos!", font=('Verdana 10'), bg=co4, fg='red').pack(pady=5)

    Button(frameRight, text="Salvar Usuário", font=('Verdana 10 bold'), bg=co5, command=salvar).pack(pady=10)

def tela_realizar_emprestimo():
    limpar()
    Label(frameRight, text="Realizar Empréstimo", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    Label(frameRight, text="ID do Livro:", bg=co4, fg=co10).pack()
    livro_id = Entry(frameRight)
    livro_id.pack()

    Label(frameRight, text="ID do Usuário:", bg=co4, fg=co10).pack()
    usuario_id = Entry(frameRight)
    usuario_id.pack()

    def emprestar():
        hoje = datetime.datetime.now().strftime('%Y-%m-%d')
        if livro_id.get() and usuario_id.get():
            try:
                insert_loan(int(livro_id.get()), int(usuario_id.get()), hoje)
                print(f"Empréstimo realizado: Livro ID {livro_id.get()}, Usuário ID {usuario_id.get()}, Data {hoje}")
                Label(frameRight, text="Empréstimo realizado com sucesso!", font=('Verdana 10'), bg=co4, fg='green').pack(pady=5)
                livro_id.delete(0, END)
                usuario_id.delete(0, END)
            except Exception as e:
                print(f"Erro ao realizar empréstimo: {e}")
                Label(frameRight, text="Erro ao realizar empréstimo!", font=('Verdana 10'), bg=co4, fg='red').pack(pady=5)
        else:
            Label(frameRight, text="Preencha todos os campos!", font=('Verdana 10'), bg=co4, fg='red').pack(pady=5)

    Button(frameRight, text="Emprestar", font=('Verdana 10 bold'), bg=co5, command=emprestar).pack(pady=10)

def tela_devolver_livro():
    limpar()
    Label(frameRight, text="Devolver Livro", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    Label(frameRight, text="ID do Empréstimo:", bg=co4, fg=co10).pack()
    emprestimo_id = Entry(frameRight)
    emprestimo_id.pack()

    def devolver():
        hoje = datetime.datetime.now().strftime('%Y-%m-%d')
        # Lógica de devolução (substitua pela lógica real)
        print(f"Livro devolvido: Empréstimo ID {emprestimo_id.get()} em {hoje}")
        emprestimo_id.delete(0, END)

    Button(frameRight, text="Devolver", font=('Verdana 10 bold'), bg=co5, command=devolver).pack(pady=10)

# Tela para excluir livros
def tela_excluir_livro():
    limpar()
    Label(frameRight, text="Excluir Livro", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    Label(frameRight, text="ID do Livro:", font=('Verdana 10'), bg=co4, fg=co10).pack(pady=5)
    livro_id = Entry(frameRight, width=40)
    livro_id.pack()

    def excluir():
        if livro_id.get():
            delete_book(int(livro_id.get()))
            print(f"Livro com ID {livro_id.get()} excluído.")
            livro_id.delete(0, END)

    Button(frameRight, text="Excluir Livro", font=('Verdana 10 bold'), bg='red', fg='white', command=excluir).pack(pady=10)

# Tela para excluir usuários
def tela_excluir_usuario():
    limpar()
    Label(frameRight, text="Excluir Usuário", font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    Label(frameRight, text="ID do Usuário:", font=('Verdana 10'), bg=co4, fg=co10).pack(pady=5)
    usuario_id = Entry(frameRight, width=40)
    usuario_id.pack()

    def excluir():
        if usuario_id.get():
            delete_user(int(usuario_id.get()))
            print(f"Usuário com ID {usuario_id.get()} excluído.")
            usuario_id.delete(0, END)

    Button(frameRight, text="Excluir Usuário", font=('Verdana 10 bold'), bg='red', fg='white', command=excluir).pack(pady=10)

# Funções de Exibição

def tabela_com_scroll(titulo, colunas, dados, deletar_callback=None):
    limpar()
    Label(frameRight, text=titulo, font=('Verdana 16 bold'), bg=co4, fg=co10).pack(pady=10)

    frameLista = Frame(frameRight, bg=co6)
    frameLista.pack(expand=True, fill=BOTH, padx=20, pady=10)

    tv = ttk.Treeview(frameLista, columns=colunas, show='headings')
    tv.pack(side=LEFT, expand=True, fill=BOTH)

    for col in colunas:
        tv.heading(col, text=col)
        tv.column(col, anchor=CENTER, width=120)

    scroll_y = Scrollbar(frameLista, orient=VERTICAL, command=tv.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    tv.configure(yscrollcommand=scroll_y.set)

    scroll_x = Scrollbar(frameRight, orient=HORIZONTAL, command=tv.xview)
    scroll_x.pack(fill=X)
    tv.configure(xscrollcommand=scroll_x.set)

    for item in dados:
        tv.insert('', 'end', values=item)

    if deletar_callback:
        def deletar():
            selecionado = tv.selection()
            if selecionado:
                item = tv.item(selecionado[0])['values'][0]
                deletar_callback(item)
                tv.delete(selecionado[0])

        Button(frameRight, text="Deletar", font=('Verdana 10 bold'), bg='red', fg='white', command=deletar).pack(pady=10)

# Telas de visualizar

def tela_visualizar_livros():
    tabela_com_scroll("Livros", ["ID", "Título", "Autor", "Editora", "Ano", "ISBN"], display_books(), delete_book)

def tela_visualizar_usuarios():
    tabela_com_scroll("Usuários", ["ID", "Nome", "Sobrenome", "Endereço", "Telefone", "Email"], display_users(), delete_user)

def tela_visualizar_emprestimos():
    def devolver_emprestimo(emprestimo_id):
        hoje = datetime.datetime.now().strftime('%Y-%m-%d')
        update_return(emprestimo_id, hoje)  # Atualiza a devolução no banco de dados
        print(f"Empréstimo ID {emprestimo_id} devolvido em {hoje}")
        tela_visualizar_emprestimos()  # Atualiza a tela após a devolução

    emprestimos = display_loans()  # Obtém os empréstimos do banco de dados
    tabela_com_scroll(
        "Empréstimos Ativos",
        ["ID", "Título do Livro", "Nome do Usuário", "Sobrenome", "Data do Empréstimo"],
        emprestimos,
        devolver_emprestimo
    )

# Botões do menu
botoes = [
    ("Cadastrar Livro", tela_cadastrar_livro),
    ("Cadastrar Usuário", tela_cadastrar_usuario),
    ("Realizar Empréstimo", tela_realizar_emprestimo),
    ("Devolver Livro", tela_devolver_livro),
    ("Visualizar Livros", tela_visualizar_livros),
    ("Visualizar Usuários", tela_visualizar_usuarios),
    ("Visualizar Empréstimos", tela_visualizar_emprestimos),  # Novo botão
    ("Excluir Livro", tela_excluir_livro),
    ("Excluir Usuário", tela_excluir_usuario)
]

for texto, comando in botoes:
    Button(frameLeft, text=texto, font=('Verdana 10 bold'), width=25, bg=co3, fg="white", command=comando).pack(pady=5)

# Primeira tela aberta
tela_cadastrar_livro()

# Mainloop
janela.mainloop()
