import sqlite3

#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

drop_table = '''
    DROP TABLE IF EXISTS clock
    '''

create_table = '''
    CREATE TABLE IF NOT EXISTS clock (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    worker INT (5), 
    clock_in_day VARCHAR (12),
    clock_in_hour VARCHAR (12),
    clock_out_day VARCHAR (12),
    clock_out_hour VARCHAR (12), 
    FOREIGN KEY (worker) REFERENCES funcionario(id) );
'''


#executar o comando SQL com o cursor

cursor.execute(drop_table)
cursor.execute(create_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
