import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="palha_da_terra",
            password="123123",
            database="palhadaterra",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")
        return None
