#1. Oracle DB
#2. Python Lib(bibliotecas | API)
#3. DB details
#4. Driver cx_Oracle
'''
Módulos Python
- cx_Oracle - Oracle Database
- pyodbc - Microsoft SQL server
- pymsql - MySQL
- Psycopg2 - PostgreSQL


Como criar a conexao
1. importar o driver cx_Oracle
2. Estabelecer uma conexão entre o python e o banco de dados
3. Criar um cursor (objeto para executar queries e obter resultados após a execução)
'''

import cx_Oracle

#create connection

conn = cx_Oracle.connect(user="rm99708", password="180105", host="oracle.fiap.com.br/orcl")

print(conn.version)

#create cursor

cursor = conn.cursor()

#create table

sql_create = """
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER()
);
"""

#execute query
cursor.execute(sql_create)
print('Tabela criada!')

#fechar conexao
conn.close()

#fechar o cursor
cursor.close()
