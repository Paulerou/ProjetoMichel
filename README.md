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

if _name_ == "_main_":
    create_table()


#Documentação do Código

## Introdução
Este código Python tem como objetivo criar uma tabela chamada "Clientes" em um banco de dados PostgreSQL. Utiliza a biblioteca psycopg2 para se conectar ao banco de dados e executar comandos SQL.

## Requisitos
- Python 3.x
- Biblioteca psycopg2 (instalada via pip install psycopg2)

## Função create_table
A função create_table não recebe nenhum parâmetro e realiza a seguinte operação:

### Funcionamento
1. Tenta conectar ao banco de dados PostgreSQL utilizando as credenciais fornecidas.
2. Abre um cursor para executar comandos SQL.
3. Constrói um comando SQL para criar uma tabela chamada "Clientes" com quatro colunas: id, nome, datadenasc, e telefone.
4. Executa o comando SQL para criar a tabela, mas apenas se ela ainda não existir (CREATE TABLE IF NOT EXISTS).
5. Realiza o commit da transação para efetivar a criação da tabela no banco de dados.
6. Fecha a conexão e imprime uma mensagem de sucesso.

### Exceções
Caso ocorra algum erro durante a execução (por exemplo, falha na conexão ao banco de dados), a função captura exceções do tipo psycopg2.Error e psycopg2.DatabaseError e imprime uma mensagem de erro.

## Uso do Código
O código inclui um bloco if __name__ == "__main__": que chama a função create_table quando o script é executado diretamente. Ao ser executado, o código conecta-se ao banco de dados PostgreSQL e cria a tabela "Clientes" com as colunas especificadas.

*Nota:* Certifique-se de fornecer as credenciais corretas (usuário, senha, host, porta e nome do banco de dados) para a conexão com o banco de dados PostgreSQL.



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

if _name_ == "_main_":
    # Exemplo de uso: excluir o cliente com ID 1
    delete_client(client_id=1)



# Documentação do Código

## Introdução
Este código Python tem como objetivo excluir um cliente específico da tabela "Clientes" em um banco de dados PostgreSQL. Utiliza a biblioteca psycopg2 para se conectar ao banco de dados e executar comandos SQL.

## Requisitos
- Python 3.x
- Biblioteca psycopg2 (instalada via pip install psycopg2)

## Função delete_client
A função delete_client aceita um parâmetro:
- client_id: Identificador único do cliente que será excluído.

### Funcionamento
1. Tenta conectar ao banco de dados PostgreSQL utilizando as credenciais fornecidas.
2. Abre um cursor para executar comandos SQL.
3. Constrói um comando SQL para excluir um cliente específico da tabela "Clientes" com base no ID.
4. Executa o comando SQL para realizar a exclusão.
5. Realiza o commit da transação para efetivar a exclusão dos dados.
6. Fecha a conexão e imprime uma mensagem de sucesso.

### Exceções
Caso ocorra algum erro durante a execução (por exemplo, falha na conexão ao banco de dados), a função captura exceções do tipo psycopg2.Error e psycopg2.DatabaseError e imprime uma mensagem de erro.

## Uso do Código
O código inclui um bloco if __name__ == "__main__": que demonstra um exemplo de uso da função delete_client. Neste exemplo, o cliente com ID 1 é excluído. Para excluir outros clientes, basta chamar a função delete_client com o ID desejado.

*Nota:* Certifique-se de fornecer as credenciais corretas (usuário, senha, host, porta e nome do banco de dados) para a conexão com o banco de dados PostgreSQL.



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

if _name_ == "_main_":
    insert_data()


# Documentação do Código

## Introdução
Este código Python tem como objetivo inserir dados fictícios de clientes em uma tabela chamada "Clientes" em um banco de dados PostgreSQL. Utiliza a biblioteca psycopg2 para se conectar ao banco de dados e executar comandos SQL, além da biblioteca Faker para gerar dados fictícios realistas.

## Requisitos
- Python 3.x
- Biblioteca psycopg2 (instalada via pip install psycopg2)
- Biblioteca Faker (instalada via pip install faker)

## Função insert_data
A função insert_data não recebe nenhum parâmetro e realiza a seguinte operação:

### Funcionamento
1. Cria uma instância da classe Faker para gerar dados fictícios.
2. Tenta conectar ao banco de dados PostgreSQL utilizando as credenciais fornecidas.
3. Abre um cursor para executar comandos SQL.
4. Constrói um comando SQL para inserir 100 registros fictícios na tabela "Clientes" com os campos nome, data de nascimento e telefone.
5. Utiliza o loop for para gerar dados fictícios e executar o comando SQL para cada conjunto de dados.
6. Realiza o commit da transação para efetivar a inserção dos dados no banco de dados.
7. Fecha a conexão e imprime uma mensagem de sucesso.

### Exceções
Caso ocorra algum erro durante a execução (por exemplo, falha na conexão ao banco de dados), a função captura exceções do tipo psycopg2.Error e psycopg2.DatabaseError e imprime uma mensagem de erro.

## Uso do Código
O código inclui um bloco if __name__ == "__main__": que chama a função insert_data quando o script é executado diretamente. Ao ser executado, o código conecta-se ao banco de dados PostgreSQL, gera dados fictícios para 100 clientes e os insere na tabela "Clientes".

*Nota:* Certifique-se de fornecer as credenciais corretas (usuário, senha, host, porta e nome do banco de dados) para a conexão com o banco de dados PostgreSQL.



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


# Documentação do Código

## Introdução
Este código Python tem como objetivo recuperar e exibir todos os registros da tabela "Clientes" em um banco de dados PostgreSQL. Utiliza a biblioteca psycopg2 para se conectar ao banco de dados e executar comandos SQL.

## Requisitos
- Python 3.x
- Biblioteca psycopg2 (instalada via pip install psycopg2)

## Função select_all_clients
A função select_all_clients não recebe nenhum parâmetro e realiza a seguinte operação:

### Funcionamento
1. Tenta conectar ao banco de dados PostgreSQL utilizando as credenciais fornecidas.
2. Abre um cursor para executar comandos SQL.
3. Constrói um comando SQL para selecionar todos os registros da tabela "Clientes".
4. Executa o comando SQL para selecionar os dados.
5. Recupera os resultados utilizando o método fetchall() do cursor.
6. Exibe os resultados na saída padrão (console).

### Exceções
Caso ocorra algum erro durante a execução (por exemplo, falha na conexão ao banco de dados), a função captura exceções do tipo psycopg2.Error e psycopg2.DatabaseError e imprime uma mensagem de erro.

## Uso do Código
O código inclui um bloco if __name__ == "__main__": que chama a função select_all_clients quando o script é executado diretamente. Ao ser executado, o código conecta-se ao banco de dados PostgreSQL, recupera todos os registros da tabela "Clientes" e os exibe na saída padrão.

*Nota:* Certifique-se de fornecer as credenciais corretas (usuário, senha, host, porta e nome do banco de dados) para a conexão com o banco de dados PostgreSQL.




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

if _name_ == "_main_":
    # Exemplo de uso: atualizar o telefone do cliente com ID 1 para "987654321"
    update_client(client_id=1, new_telefone="987654321")


# Documentação do Código

## Introdução
Este código Python tem como objetivo realizar a atualização do número de telefone de um cliente em uma tabela chamada "Clientes" em um banco de dados PostgreSQL. O código utiliza a biblioteca psycopg2 para se conectar ao banco de dados e executar comandos SQL.

## Requisitos
- Python 3.x
- Biblioteca psycopg2 (instalada via pip install psycopg2)

## Função update_client
A função update_client aceita dois parâmetros:
- client_id: Identificador único do cliente cujo telefone será atualizado.
- new_telefone: Novo número de telefone que será atribuído ao cliente.

### Funcionamento
1. Tenta conectar ao banco de dados PostgreSQL utilizando as credenciais fornecidas.
2. Abre um cursor para executar comandos SQL.
3. Constrói um comando SQL para atualizar o número de telefone do cliente específico na tabela "Clientes".
4. Executa o comando SQL com os parâmetros fornecidos (novo telefone e ID do cliente).
5. Realiza o commit da transação para efetivar a atualização.
6. Fecha a conexão e imprime uma mensagem de sucesso.

### Exceções
Caso ocorra algum erro durante a execução (por exemplo, falha na conexão ao banco de dados), a função captura exceções do tipo psycopg2.Error e psycopg2.DatabaseError e imprime uma mensagem de erro.

## Uso do Código
O código inclui um bloco if __name__ == "__main__": que demonstra um exemplo de uso da função update_client. Neste exemplo, o telefone do cliente com ID 1 é atualizado para "987654321". Para utilizar a função com outros clientes ou números de telefone, basta chamar a função update_client com os parâmetros desejados.

*Nota:* Certifique-se de fornecer as credenciais corretas (usuário, senha, host, porta e nome do banco de dados) para a conexão com o banco de dados PostgreSQL.
