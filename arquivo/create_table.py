import sqlite3

#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

#id integer pk
#utilizador text not null unique
#password text not null

create_table = '''
    CREATE TABLE IF NOT EXISTS funcionario (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, primeiro_nome VARCHAR(50), ultimo_nome VARCHAR(50), data_nascimento DATE, 
    numero_cartao_cidadao VARCHAR(20), nib INT(20), nacionalidade VARCHAR(50), salario_iliquido DECIMAL(10, 2) 
    CHECK (salario_iliquido >= 820.00), nivel_escolaridade VARCHAR(50), cargo VARCHAR(20) CHECK (cargo IN ('funcionario', 'administrador')) );
'''


#executar o comando SQL com o cursor

cursor.execute(create_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()