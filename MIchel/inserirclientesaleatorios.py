import psycopg2
from faker import Faker

def insert_data():
    fake = Faker()

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

                # Comando SQL para inserir 100 pessoas aleatórias
                insert_query = """
                    INSERT INTO Clientes (nome, datadenasc, telefone) VALUES (%s, %s, %s)
                """

                # Gerar e inserir 100 registros aleatórios
                for _ in range(100):
                    nome = fake.name()
                    datadenasc = fake.date_of_birth(minimum_age=18, maximum_age=90)
                    telefone = fake.phone_number()

                    # Executar o comando SQL para inserir dados
                    cur.execute(insert_query, (nome, datadenasc, telefone))

                # Commit da transação para efetivar a inserção de dados
                conn.commit()

            print("Inserção de dados concluída!")

    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print("Erro ao inserir dados na tabela 'Clientes':", e)

if __name__ == "__main__":
    insert_data()
