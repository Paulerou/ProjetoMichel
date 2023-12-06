import psycopg2

def create_table():
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

                # Comando SQL para criar uma tabela
                create_table_query = """
                    CREATE TABLE IF NOT EXISTS Clientes (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(100),
                        datadenasc DATE,
                        telefone VARCHAR(100)
                    )
                """

                # Executar o comando SQL para criar a tabela
                cur.execute(create_table_query)

                # Commit da transação para efetivar a criação da tabela
                conn.commit()

            print("Tabela criada com sucesso!")

    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print("Erro ao criar a tabela 'Clientes':", e)

if __name__ == "__main__":
    create_table()
