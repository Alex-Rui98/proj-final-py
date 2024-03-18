import sqlite3

#ligar à base de dados
conn = sqlite3.connect('clock.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

#id integer pk
#utilizador text not null unique
#password text not null

create_table = '''
    CREATE TABLE IF NOT EXISTS clock (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    worker INT (5), 
    clock_in DATATIME,
    clock_out DATATIME, 
    FOREIGN KEY (worker) REFERENCES funcionario(id) );
'''


#executar o comando SQL com o cursor

cursor.execute(create_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
