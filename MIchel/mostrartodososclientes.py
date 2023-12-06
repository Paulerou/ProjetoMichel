import psycopg2

def select_all_clients():
    try:
        # Conectar ao banco de dados PostgreSQL usando o context manager
        with psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
            port="5450",
            database="postgres"
        ) as conn:

            # Abrir um cursor para executar comandos SQL
            with conn.cursor() as cur:

                # Comando SQL para selecionar todos os registros da tabela Clientes
                select_query = "SELECT * FROM Clientes"

                # Executar o comando SQL para selecionar dados
                cur.execute(select_query)

                # Recuperar os resultados
                rows = cur.fetchall()

                # Exibir os resultados
                print("Registros na tabela 'Clientes':")
                for row in rows:
                    print(row)

    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print("Erro ao selecionar dados na tabela 'Clientes':", e)

if __name__ == "__main__":
    select_all_clients()
