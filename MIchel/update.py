import psycopg2

def update_client(client_id, new_telefone):
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

                # Comando SQL para atualizar o telefone de um cliente específico
                update_query = "UPDATE Clientes SET telefone = %s WHERE id = %s"

                # Executar o comando SQL para realizar a atualização
                cur.execute(update_query, (new_telefone, client_id))

                # Commit da transação para efetivar a atualização
                conn.commit()

            print("Atualização concluída!")

    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print("Erro ao atualizar dados na tabela 'Clientes':", e)

if __name__ == "__main__":
    # Exemplo de uso: atualizar o telefone do cliente com ID 1 para "987654321"
    update_client(client_id=1, new_telefone="987654321")
