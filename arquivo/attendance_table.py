import sqlite3

#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

#id integer pk
#utilizador text not null unique
#password text not null
drop_table = '''
    DROP TABLE IF EXISTS attendance
    '''
create_table = '''
    CREATE TABLE IF NOT EXISTS attendance(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    worker INT (5),
    day VARCHAR (20),
    description VARCHAR (150),
    FOREIGN KEY (worker) REFERENCES employee (id)
     );
'''


#executar o comando SQL com o cursor

cursor.execute(drop_table)
cursor.execute(create_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
