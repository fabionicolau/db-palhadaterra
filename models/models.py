from connection.db_connection import get_connection


def inserir_cliente(payload):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nome, endereco, telefone) VALUES (%s, %s, %s)"
        try:
            cursor.execute(
                sql, (payload["nome"], payload["endereco"], payload["telefone"])
            )
            conn.commit()
            print("Cliente inserido com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def ler_clientes():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM clientes"
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao ler clientes: {e}")
            return []
        finally:
            cursor.close()
            conn.close()


def atualizar_cliente(id, payload):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE clientes SET nome=%s, endereco=%s, telefone=%s WHERE id=%s"
        try:
            cursor.execute(
                sql, (payload["nome"], payload["endereco"], payload["telefone"], id)
            )
            conn.commit()
            print("Cliente atualizado com sucesso.")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def deletar_cliente(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM clientes WHERE id=%s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            print("Cliente deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def inserir_produto(payload):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(
                sql,
                (
                    payload["nome"],
                    payload["descricao"],
                    payload["preco"],
                    payload["quantidade"],
                ),
            )
            conn.commit()
            print("Produto inserido com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def ler_produtos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM produtos"
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao ler produtos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()


def atualizar_produto(id_produto, payload):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE produtos SET nome=%s, descricao=%s, preco=%s, quantidade=%s WHERE id=%s"
        try:
            cursor.execute(
                sql,
                (
                    payload["nome"],
                    payload["descricao"],
                    payload["preco"],
                    payload["quantidade"],
                    id_produto,
                ),
            )
            conn.commit()
            print("Produto atualizado com sucesso.")
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def deletar_produto(id_produto):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM produtos WHERE id=%s"
        try:
            cursor.execute(sql, (id_produto,))
            conn.commit()
            print("Produto deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
