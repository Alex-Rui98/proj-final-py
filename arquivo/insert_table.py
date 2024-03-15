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
    INSERT INTO funcionario (primeiro_nome, ultimo_nome, data_nascimento, numero_cartao_cidadao, nib, nacionalidade, salario_iliquido, nivel_escolaridade, cargo, password)VALUES
    ('Pedro', 'Silva', '1988-07-25', '98765432', 98765432109876543210, 'Portuguesa', 1200.00, 'Ensino Superior', 'administrador','86456da16bf304fd7a097be7eabe06e64e84298b591d49ba0ad56e6c45fa974d'),
    ('Ana', 'Pereira', '1985-02-10', '12345678', 12345678901234567890, 'Portuguesa', 1000.00, '12º ano', 'funcionario','c98f69f7d264bb767b0c4b3520a19f4f91212169678c977e47f0bd5c3a827db6' ),
    ('Marta', 'Ribeiro', '1992-11-15', '34567890', 11112222333344445555, 'Portuguesa', 900.00, '12º ano', 'funcionario','7a7bf024a1668dfbb66ede886b3060f39ae78cd08f5a87e7143406db9dc0cb22'), 
    ('Rui', 'Santos', '1980-05-20', '87654321', 55554444333322221111, 'Portuguesa', 1300.00, 'Ensino Superior', 'administrador','5d7af36961980052899a821d6ab0ab976666d20e9fd33c194be84e7d42c84f2a'),
    ('Carla', 'Oliveira', '1995-08-03', '23456789', 22223333444455556666, 'Portuguesa', 850.00, '12º ano', 'funcionario', '5d992469ebf186cfa87bc2547bde39772987612fb2f4dea01323d44d91bf84f6'),     
    ('João', 'Ferreira', '1983-01-22', '76543210', 66665555444433332222, 'Portuguesa', 1100.00, 'Ensino Superior', 'administrador'. 'ebfe8fec61db93ad3b4aaf4a259cef8bbe2601856b5076428c17745f4dbdddbf'),     
    ('Sofia', 'Costa', '1990-04-18', '45678901', 33334444555566667777, 'Portuguesa', 950.00, '12º ano', 'funcionario', '473132aebd3f348ca05c22e14751de48bcf49489a4cec8ba088f86d172bc4ba2'),     
    ('Ricardo', 'Rodrigues', '1987-09-12', '65432109', 77776666555544443333, 'Portuguesa', 1250.00, 'Ensino Superior', 'administrador', 'c42d5ce03e5984d12671b4131020db998e6165625af216a8c0198977badf06c9'),     
    ('Inês', 'Mendes', '1986-12-05', '56789012', 44445555666677778888, 'Portuguesa', 880.00, '12º ano', 'funcionario', '9cf33e645cd8208f510b1d36589640bb7625239d04d1dfc8f3c085e855fb47d7'),     
    ('Luís', 'Araújo', '1998-02-28', '32109876', 88887777666655554444, 'Portuguesa', 1050.00, 'Ensino Superior', 'administrador', 'd0dc58e6080d568cd2e1278c97bad75f0090ab90c4ec12918313387fd607e995'),     
    ('Filipa', 'Martins', '1993-06-08', '67890123', 55554444333322221111, 'Portuguesa', 900.00, '12º ano', 'funcionario', 'dcea08f9646ef4126552ca3c18e085b696d99be3cc7d1fcd0b081c7a6a669982'),     
    ('António', 'Pinto', '1984-10-30', '54321098', 11112222333344445555, 'Portuguesa', 1150.00, 'Ensino Superior', 'funcionario', '9237279dafe8aeffb2001569749e73129c0cdf369ab3fee45a80e0ad8f68c3ad'),     
    ('Beatriz', 'Gomes', '1991-03-16', '78901234', 22223333444455556666, 'Portuguesa', 870.00, '12º ano', 'funcionario', '18fa6fa144e1175d249157ff866d89311b01006eb28542bb9544416eba83d812'),     
    ('Hugo', 'Cunha', '1989-08-11', '43210987', 66665555444433332222, 'Portuguesa', 1220.00, 'Ensino Superior', 'funcionario', '82a3f7afd4654a6b47a95048b6b65dc8395fe8d7437215bdebe38124f5e157ab'),    
    ('Lara', 'Ramos', '1994-01-24', '89012345', 33334444555566667777, 'Portuguesa', 920.00, '12º ano', 'funcionario', '43626230d59d5dbfcdd8f9aacf5b8239165580b899e1c28255a9ea1df5f9dbc4'),     
    ('Daniel', 'Sousa', '1981-04-02', '10987654', 77776666555544443333, 'Portuguesa', 1350.00, 'Ensino Superior', 'funcionario', '2d9308a22546e6bfd6f4322737f4a4d32f3e43d9a62586ae062712d0694feb3b'),
    ('Catarina', 'Almeida', '1982-07-19', '23456789', 44445555666677778888, 'Portuguesa', 880.00, '12º ano', 'funcionario', 'cef57d4951fc70046b2f62e7403984825289daa0feb6155fca6cf0e3a960b2a9'),     
    ('Miguel', 'Fernandes', '1997-11-10', '54321098', 88887777666655554444, 'Portuguesa', 1050.00, 'Ensino Superior', 'funcionario', '45f2170b1421aea7948c561b9e4f08d65335dbcd0f600076010d4e8220e3333a'),   
    ('Raquel', 'Vieira', '1996-03-03', '65432109', 55554444333322221111, 'Portuguesa', 900.00, '12º ano', 'funcionario', 'cff6e1d8515ecf97aee8a266b8b6cf91ffb0c6188ab609c44a6a5b25c2e64478'),     
    ('Gonçalo', 'Carvalho', '1987-05-15', '78901234', 11112222333344445555, 'Portuguesa', 1150.00, 'Ensino Superior', 'funcionario', '0d645ea5cbb178850f76c5fdd94ffd8e96fa993a8acfd82c53377d4141d2378f'),     
    ('Eva', 'Moreira', '1992-09-28', '12345678', 22223333444455556666, 'Portuguesa', 870.00, '12º ano', 'funcionario', '74f06b6f3567eededfa6c451edbe8a4c65fdfa6e52ac69f47a95eb19e3b4f981'),     
    ('Alexandre', 'Pires', '1988-12-20', '98765432', 66665555444433332222, 'Portuguesa', 1220.00, 'Ensino Superior', 'funcionario', '8ba106c6d6f0920f2aea56d1d331d092e8837f68c7844dc009f22270cd9c8321'),     
    ('Tatiana', 'Lopes', '1995-02-13', '34567890', 33334444555566667777, 'Portuguesa', 920.00, '12º ano', 'funcionario', 'ce434a816ddcb10fb55e1c0ed914a50573781f8fc4270cb1155ae50db0d39e8f'),     
    ('Nuno', 'Machado', '1983-06-06', '87654321', 77776666555544443333, 'Portuguesa', 1350.00, 'Ensino Superior', 'funcionario', 'd44b0b8751bf78fa6b5200d11f4c5f8b92042b1f1a0d4fcc4daefeb87d1fa11')
'''


#executar o comando SQL com o cursor

cursor.execute(insert_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
