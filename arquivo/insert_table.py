import sqlite3

#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela

#id integer pk
#utilizador text not null unique
#password text not null

insert_table = '''
    INSERT INTO funcionario (primeiro_nome, ultimo_nome, data_nascimento, numero_cartao_cidadao, nib, nacionalidade, salario_iliquido, nivel_escolaridade, cargo)VALUES
    ('Ana', 'Pereira', '1985-02-10', '12345678', '1234-5678-9012-3456-7890', 'Portuguesa', 1000.00, '12º ano', 'funcionario'),
    ('Pedro', 'Silva', '1988-07-25', '98765432', '9876-5432-1098-7654-3210', 'Portuguesa', 1200.00, 'Ensino Superior', 'administrador'),
    ('Marta', 'Ribeiro', '1992-11-15', '34567890', '1111-2222-3333-4444-5555', 'Portuguesa', 900.00, '12º ano', 'funcionario'), 
    ('Rui', 'Santos', '1980-05-20', '87654321', '5555-4444-3333-2222-1111', 'Portuguesa', 1300.00, 'Ensino Superior', 'administrador'),
    ('Carla', 'Oliveira', '1995-08-03', '23456789', '2222-3333-4444-5555-6666', 'Portuguesa', 850.00, '12º ano', 'funcionario'),     
    ('João', 'Ferreira', '1983-01-22', '76543210', '6666-5555-4444-3333-2222', 'Portuguesa', 1100.00, 'Ensino Superior', 'administrador'),     
    ('Sofia', 'Costa', '1990-04-18', '45678901', '3333-4444-5555-6666-7777', 'Portuguesa', 950.00, '12º ano', 'funcionario'),     
    ('Ricardo', 'Rodrigues', '1987-09-12', '65432109', '7777-6666-5555-4444-3333', 'Portuguesa', 1250.00, 'Ensino Superior', 'administrador'),     
    ('Inês', 'Mendes', '1986-12-05', '56789012', '4444-5555-6666-7777-8888', 'Portuguesa', 880.00, '12º ano', 'funcionario'),     
    ('Luís', 'Araújo', '1998-02-28', '32109876', '8888-7777-6666-5555-4444', 'Portuguesa', 1050.00, 'Ensino Superior', 'administrador'),     
    ('Filipa', 'Martins', '1993-06-08', '67890123', '5555-4444-3333-2222-1111', 'Portuguesa', 900.00, '12º ano', 'funcionario'),     
    ('António', 'Pinto', '1984-10-30', '54321098', '1111-2222-3333-4444-5555', 'Portuguesa', 1150.00, 'Ensino Superior', 'funcionario'),     
    ('Beatriz', 'Gomes', '1991-03-16', '78901234', '2222-3333-4444-5555-6666', 'Portuguesa', 870.00, '12º ano', 'funcionario'),     
    ('Hugo', 'Cunha', '1989-08-11', '43210987', '6666-5555-4444-3333-2222', 'Portuguesa', 1220.00, 'Ensino Superior', 'funcionario'),    
    ('Lara', 'Ramos', '1994-01-24', '89012345', '3333-4444-5555-6666-7777', 'Portuguesa', 920.00, '12º ano', 'funcionario'),     
    ('Daniel', 'Sousa', '1981-04-02', '10987654', '7777-6666-5555-4444-3333', 'Portuguesa', 1350.00, 'Ensino Superior', 'funcionario'),
    ('Catarina', 'Almeida', '1982-07-19', '23456789', '4444-5555-6666-7777-8888', 'Portuguesa', 880.00, '12º ano', 'funcionario'),     
    ('Miguel', 'Fernandes', '1997-11-10', '54321098', '8888-7777-6666-5555-4444', 'Portuguesa', 1050.00, 'Ensino Superior', 'funcionario'),   
    ('Raquel', 'Vieira', '1996-03-03', '65432109', '5555-4444-3333-2222-1111', 'Portuguesa', 900.00, '12º ano', 'funcionario'),     
    ('Gonçalo', 'Carvalho', '1987-05-15', '78901234', '1111-2222-3333-4444-5555', 'Portuguesa', 1150.00, 'Ensino Superior', 'funcionario'),     
    ('Eva', 'Moreira', '1992-09-28', '12345678', '2222-3333-4444-5555-6666', 'Portuguesa', 870.00, '12º ano', 'funcionario'),     
    ('Alexandre', 'Pires', '1988-12-20', '98765432', '6666-5555-4444-3333-2222', 'Portuguesa', 1220.00, 'Ensino Superior', 'funcionario'),     
    ('Tatiana', 'Lopes', '1995-02-13', '34567890', '3333-4444-5555-6666-7777', 'Portuguesa', 920.00, '12º ano', 'funcionario'),     
    ('Nuno', 'Machado', '1983-06-06', '87654321', '7777-6666-5555-4444-3333', 'Portuguesa', 1350.00, 'Ensino Superior', 'funcionario')
'''


#executar o comando SQL com o cursor

cursor.execute(insert_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
