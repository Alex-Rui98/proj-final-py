import sqlite3

#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

drop_table = '''
    DROP TABLE IF EXISTS employee
    '''

create_table = '''
    CREATE TABLE IF NOT EXISTS employee (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(50), last_name VARCHAR(50), date_birth DATE, 
    document_number VARCHAR(20), nib INT(20), nationality VARCHAR(50), gross_salary DECIMAL(10, 2) 
    CHECK (gross_salary >= 820.00), level_education VARCHAR(50), perms VARCHAR(20) CHECK (perms IN ('employee', 'administrator')), password VARCHAR(32));
'''


#executar o comando SQL com o cursor


cursor.execute(drop_table)
cursor.execute(create_table)
#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
