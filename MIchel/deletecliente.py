import psycopg2

def delete_client(client_id):
    try:
        # Conectar ao banco de dados PostgreSQL usando o context manager
        with psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
            port="5440",
            database="postgres"
        ) as conn:

            # Abrir um cursor para executar comandos SQL
            with conn.cursor() as cur:

                # Comando SQL para excluir um cliente específico
                delete_query = "DELETE FROM Clientes WHERE id = %s"

                # Executar o comando SQL para realizar a exclusão
                cur.execute(delete_query, (client_id,))

                # Commit da transação para efetivar a exclusão
                conn.commit()

            print("Exclusão concluída!")

    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print("Erro ao excluir dados na tabela 'Clientes':", e)

if __name__ == "__main__":
    # Exemplo de uso: excluir o cliente com ID 1
    delete_client(client_id=1)
