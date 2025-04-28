# -----(dados.py)-----

import sqlite3  # importando biblioteca SQLite

# conectar ao banco de dados
# função que conecta ao banco, se não existir cria

def connect():
    return sqlite3.connect('livraria.db')

# criar tabelas
# essa função vai criar as tabelas livros, usuarios e emprestimos se não existirem

def create_tables():
    conexao = connect()
    cursor = conexao.cursor()

    # criando tabela livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            editora TEXT,
            ano_publicacao INTEGER,
            ISBN TEXT
        )
    ''')

    # criando tabela usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            endereco TEXT,
            telefone TEXT,
            email TEXT
        )
    ''')

    # criando tabela emprestimos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER,
            usuario_id INTEGER,
            data_emprestimo TEXT,
            data_devolucao TEXT,
            FOREIGN KEY (livro_id) REFERENCES livros(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    ''')

# Função para deletar livro
def delete_book(livro_id):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
    conexao.commit()
    conexao.close()
    reset_table("livros")  # Reseta os IDs após exclusão

# Função para resetar IDs da tabela
def reset_table(table_name):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = ?', (table_name,))
    conexao.commit()
    conexao.close()

# Função para deletar usuário
def delete_user(usuario_id):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
    conexao.commit()
    conexao.close()
    reset_table("usuarios")  # Reseta os IDs após exclusão
