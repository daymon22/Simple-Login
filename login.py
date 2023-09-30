import mysql.connector
import hashlib

# Função para conectar à base de dados
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="logindb"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar à base de dados: {erro}")
        return None

# Função para calcular o hash SHA-256 de uma senha
def calcular_hash(senha):
    sha256 = hashlib.sha256()
    sha256.update(senha.encode('utf-8'))
    return sha256.hexdigest()

# Função para registar um novo utilizador
def registar():
    conexao = conectar_bd()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            username = input("Digite o nome de utilizador: ")
            
            # Verificar se o nome de utilizador já existe
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                print("Nome de utilizador já existe. Escolha outro nome de utilizador.")
            else:
                password = calcular_hash(input("Digite a senha: "))
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                conexao.commit()
                print("Registo bem-sucedido!")
        except mysql.connector.Error as erro:
            print(f"Erro ao registar utilizador: {erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


# Função para verificar o login
def verificar_login():
    conexao = conectar_bd()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            username = input("Digite o nome de utilizador: ")
            password = calcular_hash(input("Digite a senha: "))
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user is not None:
                print("Login bem-sucedido!")
            else:
                print("Utilizador ou senha incorretos")
        except mysql.connector.Error as erro:
            print(f"Erro ao verificar login: {erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

# Função para redefinir a senha com base no nome de utilizador
def redefinir_senha():
    conexao = conectar_bd()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            username = input("Digite o nome de utilizador: ")
            
            # Solicitar a senha atual do utilizador
            current_password = input("Digite a senha atual: ")
            current_password_hash = calcular_hash(current_password)
            
            # Verifica se o utilizador existe na base de dados e se a senha atual está correta
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, current_password_hash))
            user = cursor.fetchone()
            if user is not None:
                # Se a senha atual estiver correta, solicitar a nova senha
                new_password = input("Digite a nova senha: ")
                # Atualize a senha do utilizador
                hashed_password = calcular_hash(new_password)
                cursor.execute("UPDATE users SET password = %s WHERE username = %s", (hashed_password, username))
                conexao.commit()
                print("Senha redefinida com sucesso!")
            else:
                print("Nome de utilizador não encontrado ou senha atual incorreta")
        except mysql.connector.Error as erro:
            print(f"Erro ao redefinir senha: {erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

# Menu
while True:
    print("Escolha uma opção:")
    print("1 - Registar")
    print("2 - Verificar Login")
    print("3 - Redefinir Senha")
    print("0 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        registar()
    elif opcao == "2":
        verificar_login()
    elif opcao == "3":
        redefinir_senha()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
                
'''
A linha cursor = conexao.cursor() cria um objeto de cursor que é usado para,
executar consultas SQL no banco de dados MySQL.


Fetchone - é usado para recuperar a próxima linha de um resultado de uma consulta SQL,
executada em um banco de dados usando um cursor.
'''