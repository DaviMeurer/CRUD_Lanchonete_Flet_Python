import mysql.connector

user = "root"
senha = ""
host = "localhost"
banco = "lanchonete"

class Conector:
    
    #retorna a conexâo extabelecida ou retorna None quando der errado
    def conectar():
        conexao=None
        try:
            conexao =  mysql.connector.connect(
                host=host,
                user=user,
                password=senha,
                database=banco
            )
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o BD:{e}")

        return conexao

    #finalizar a conexão o fim das operações
    def fechar_conexao(conexao):
        if conexao.is_connected():
            conexao.close()
            print("Conexão com o BD encerrada!")
        

