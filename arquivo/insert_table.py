import sqlite3


#ligar à base de dados
conn = sqlite3.connect('func.db')

#criar um cursor

cursor = conn.cursor()

#comando SQL para criar tabela


insert_table = '''
    INSERT INTO employee (first_name, last_name, date_birth, document_number, nib, nationality, gross_salary, level_education, perms, password)VALUES
    ('Pedro', 'Silva', '1988-07-25', '98765432', 98765432109876543210, 'Portuguesa', 1200.00, 'Ensino Superior', 'administrator','ada5b3b51e6bd3b8637a30ddc7286b24:a4dfd09bf299c1e7c0307d587f7b655dd9cae15f8668857b3e50ab50c1cce803'),
    ('Ana', 'Pereira', '1985-02-10', '12345678', 12345678901234567890, 'Portuguesa', 1000.00, '12º ano', 'employee','a6170cc9c0b57f8822c395a5db2b714f:206109854b0c51a50f8748caf893143488b47b67c759dbe59c9f5d41a4f46007' ),
    ('Marta', 'Ribeiro', '1992-11-15', '34567890', 11112222333344445555, 'Portuguesa', 900.00, '12º ano', 'employee','4b68365f5ad8105e023d9beb63459868:e21b69c0685c3f97217b99151e0f731983b822c9494ebbe53ef2f2a7b5e266e5'), 
    ('Rui', 'Santos', '1980-05-20', '87654321', 55554444333322221111, 'Portuguesa', 1300.00, 'Ensino Superior', 'employee','f2b73609ccecd972a81d422a8f192702:d3f8f8fcb3a8fab33f0dd5abbcb2f2b7a1959abe60c4c7176bcb26a2e739dec3'),
    ('Carla', 'Oliveira', '1995-08-03', '23456789', 22223333444455556666, 'Portuguesa', 850.00, '12º ano', 'employee', '89bcfa4470594b427313db1b5250a0c0:60244267483c28086752da3148b64c11e0be48911ba2c84bcea28a39b7af6f1e'),     
    ('João', 'Ferreira', '1983-01-22', '76543210', 66665555444433332222, 'Portuguesa', 1100.00, 'Ensino Superior', 'administrator', '2295f3e6b71139689f9e8f795b8ae86e:216d656bc12353daa5eb4fd724b0a7624912f53d8ff83063576c5555d8ee38fa'),     
    ('Sofia', 'Costa', '1990-04-18', '45678901', 33334444555566667777, 'Portuguesa', 950.00, '12º ano', 'employee', '184e4d6475c65e4f4f2fa58b72d5a686:1ea6e640c70f9d8a5527129ebb4bf56482f2a54916f8e896825033906a438410'),     
    ('Ricardo', 'Rodrigues', '1987-09-12', '65432109', 77776666555544443333, 'Portuguesa', 1250.00, 'Ensino Superior', 'administrator', '68299c715d6c82c08e8c01e024c1e417:5e7e45b1e9453e816e869b65273803a447a7aca344c70f83c9a38a9584132dc6'),     
    ('Inês', 'Mendes', '1986-12-05', '56789012', 44445555666677778888, 'Portuguesa', 880.00, '12º ano', 'employee', '1ddb066cf3d76217226529c189f5e614:eb1ac2b9e0c16360da12755eeb870d336d8e25a549a6edf326fe7adc4780eb25'),     
    ('Luís', 'Araújo', '1998-02-28', '32109876', 88887777666655554444, 'Portuguesa', 1050.00, 'Ensino Superior', 'administrator', '550be36047b3349cf60f6fa22128e70c:421842d2ad94ad3d43af349902018cf710f4b458883c3950e87cdbca281fa811'),     
    ('Filipa', 'Martins', '1993-06-08', '67890123', 55554444333322221111, 'Portuguesa', 900.00, '12º ano', 'employee', '913a1098580dbc32a85ace12f787e524:7adfd7a364496525d0fab6fa5b2928b20f12cf00c65d0ca8ff2dac52d72db0dc'),     
    ('António', 'Pinto', '1984-10-30', '54321098', 11112222333344445555, 'Portuguesa', 1150.00, 'Ensino Superior', 'employee', '6c455a481a1397eeaa1bbf198d68b4a9:7ff522a99ef9888b1fb62a0e68d3f900315f134a4e971869012b3ed10ec0bbcf'),     
    ('Beatriz', 'Gomes', '1991-03-16', '78901234', 22223333444455556666, 'Portuguesa', 870.00, '12º ano', 'employee', '1680cf90434e9c41a8da22627c984a60:b3a3defaae16ae6535d3b2f6002097b970ff7e6ea8552eb9a1751e5f7f6527e4'),     
    ('Hugo', 'Cunha', '1989-08-11', '43210987', 66665555444433332222, 'Portuguesa', 1220.00, 'Ensino Superior', 'employee', 'a4bf8eaea6c82c3e01aa697b9378d36c:bd7d464ce271b29af021d563e1d57aad1ec2be1275cbd3fc01ded53c396fbd2d'),    
    ('Lara', 'Ramos', '1994-01-24', '89012345', 33334444555566667777, 'Portuguesa', 920.00, '12º ano', 'employee', '22914a2a5d356a6beea338a644eabd08:15e4c2e13f8559076ccf5c0df5d177c710e68e877ab4e991fd4fb66dfc18cf1e'),     
    ('Daniel', 'Sousa', '1981-04-02', '10987654', 77776666555544443333, 'Portuguesa', 1350.00, 'Ensino Superior', 'employee', 'f9be33c700d0e7fba7ae8a970e095ea6:29160489c0675e25888bf2fce3d56d607135fbdaf3e7b2419e0186450412f943'),
    ('Catarina', 'Almeida', '1982-07-19', '23456789', 44445555666677778888, 'Portuguesa', 880.00, '12º ano', 'employee', 'e60f74b62030b858adc50e21da0e44de:835408e98efeaca5dc8cfbfa4c9881c3b70a992229b62931c6838ce37176a8df'),     
    ('Miguel', 'Fernandes', '1997-11-10', '54321098', 88887777666655554444, 'Portuguesa', 1050.00, 'Ensino Superior', 'employee', '37c5eae630a16b5ffaaa2c16e1ff358c:18735ae3f313806048b832d86ddd0d6d8ffccf94f5756cd6de3914d65d928a87'),   
    ('Raquel', 'Vieira', '1996-03-03', '65432109', 55554444333322221111, 'Portuguesa', 900.00, '12º ano', 'employee', '599d3b633ab288d79c2b254e447c9543:56aedbacd7d8a013bef2c897f2cfe5dab21f90890cdb5d11af520460f1c830f1'),     
    ('Gonçalo', 'Carvalho', '1987-05-15', '78901234', 11112222333344445555, 'Portuguesa', 1150.00, 'Ensino Superior', 'employee', '6e94a5c0d1f818e89ba0eb48035c4208:b243410bf9fb58491c7174ce066883e9c9dd6e1aa09312783c5c8b69ada5a85e'),     
    ('Eva', 'Moreira', '1992-09-28', '12345678', 22223333444455556666, 'Portuguesa', 870.00, '12º ano', 'employee', 'f9a026f300ed72f0bbb8946d1e2dc4ba:d4a4ee4eb8eb6b685d7c4d4d47bac65464e0d2a96dfde2e2f05288fddc14b532'),     
    ('Alexandre', 'Pires', '1988-12-20', '98765432', 66665555444433332222, 'Portuguesa', 1220.00, 'Ensino Superior', 'employee', '4dbb532ed927e8d244c8469b0ea942e0:5b677a08340bccd94e67eba6650a3d34aed4b3b556a35666d744958cadf5b041'),     
    ('Tatiana', 'Lopes', '1995-02-13', '34567890', 33334444555566667777, 'Portuguesa', 920.00, '12º ano', 'employee', 'fcaac5515e35829ca5befaeeb11563b7:f2d0dd71109c4a79748dafe7c84098bbaaf9043e9f030f403eb56e562f76b628'),     
    ('Nuno', 'Machado', '1983-06-06', '87654321', 77776666555544443333, 'Portuguesa', 1350.00, 'Ensino Superior', 'employee', '1b56b789473fd9456588478c2c1690c0:304b9b8e414573d1054a10856f0e3d1616054ae2a70584a479e3b39a8d05d215')
'''


#executar o comando SQL com o cursor

cursor.execute(insert_table)

#guardar com um commit
conn.commit()

#fechar a ligação
conn.close()
