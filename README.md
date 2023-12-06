# ProjetoMichel
**Projeto em python, com o código comentado**
import psycopg2

def create_table():
    """
    Esta função cria uma tabela chamada 'Clientes' no banco de dados PostgreSQL.
    A tabela tem as seguintes colunas:
        - id: um número inteiro que serve como chave primária.
        - nome: uma string que armazena o nome do cliente.
        - datadenasc: uma data que armazena a data de nascimento do cliente.
        - telefone: uma string que armazena o número de telefone do cliente.
    Se a tabela já existir, a função não fará nada.
    """

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

if _name_ == "_main_":
    create_table()




import psycopg2

def delete_client(client_id):
    """
    Esta função exclui um cliente específico da tabela 'Clientes' no banco de dados PostgreSQL.
    A função recebe um argumento:
        - client_id: um número inteiro que representa o ID do cliente a ser excluído.
    A função executa um comando SQL DELETE para excluir o cliente com o ID especificado.
    Se ocorrer um erro durante a exclusão, a função imprimirá uma mensagem de erro.
    """

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

if _name_ == "_main_":
    # Exemplo de uso: excluir o cliente com ID 1
    delete_client(client_id=1)

Aqui está a documentação para o seu código:

python
import psycopg2
from faker import Faker

def insert_data():
    """
    Esta função insere 100 registros de dados falsos na tabela 'Clientes' no banco de dados PostgreSQL.
    Os dados falsos são gerados usando a biblioteca Faker e incluem:
        - nome: um nome completo gerado aleatoriamente.
        - datadenasc: uma data de nascimento gerada aleatoriamente para uma pessoa com idade entre 18 e 90 anos.
        - telefone: um número de telefone gerado aleatoriamente.
    A função executa um comando SQL INSERT para cada registro gerado e efetiva a inserção de dados com um commit.
    Se ocorrer um erro durante a inserção, a função imprimirá uma mensagem de erro.
    """

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

if _name_ == "_main_":
    select_all_clients()


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
        # Imprimir o erro se houver um problema ao selecionar dados na tabela 'Clientes'
        print("Erro ao selecionar dados na tabela 'Clientes':", e)

if _name_ == "_main_":
    # Chamar a função select_all_clients se este script for o módulo principal
    select_all_clients()




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
        # Imprimir o erro se houver um problema ao atualizar dados na tabela 'Clientes'
        print("Erro ao atualizar dados na tabela 'Clientes':", e)

if _name_ == "_main_":
    # Exemplo de uso: atualizar o telefone do cliente com ID 1 para "987654321"
    update_client(client_id=1, new_telefone="987654321")
