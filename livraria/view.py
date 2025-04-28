import sqlite3
from dados import create_tables  # chamando para garantir que o banco está criado

# Garantir que as tabelas sejam criadas
create_tables()

# Conectar ao banco de dados
def connect():
    return sqlite3.connect('livraria.db')

# Função para inserir livro
def insert_book(titulo, autor, editora, ano_publicacao, ISBN):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO livros (titulo, autor, editora, ano_publicacao, ISBN) VALUES (?, ?, ?, ?, ?)',
                   (titulo, autor, editora, ano_publicacao, ISBN))
    conexao.commit()
    conexao.close()

# Função para inserir usuário
def insert_user(nome, sobrenome, endereco, telefone, email):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, sobrenome, endereco, telefone, email) VALUES (?, ?, ?, ?, ?)',
                   (nome, sobrenome, endereco, telefone, email))
    conexao.commit()
    conexao.close()

# Função para inserir empréstimo
def insert_loan(livro_id, usuario_id, data_emprestimo, data_devolucao=None):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)',
                   (livro_id, usuario_id, data_emprestimo, data_devolucao))
    conexao.commit()
    conexao.close()

# Mostrar todos os livros cadastrados
def display_books():
    conexao = connect()
    livros = conexao.execute('SELECT * FROM livros').fetchall()
    conexao.close()
    return livros

# Mostrar todos os usuários cadastrados
def display_users():
    conexao = connect()
    usuarios = conexao.execute('SELECT * FROM usuarios').fetchall()
    conexao.close()
    return usuarios

# Mostrar todos os empréstimos ativos
def display_loans():
    conexao = connect()
    emprestimos = conexao.execute('''
        SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo
        FROM emprestimos
        JOIN livros ON emprestimos.livro_id = livros.id
        JOIN usuarios ON emprestimos.usuario_id = usuarios.id
        WHERE emprestimos.data_devolucao IS NULL
    ''').fetchall()
    conexao.close()
    return emprestimos

# Atualizar devolução de um livro
def update_return(emprestimo_id, data_devolucao):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('UPDATE emprestimos SET data_devolucao = ? WHERE id = ?', (data_devolucao, emprestimo_id))
    conexao.commit()
    conexao.close()
