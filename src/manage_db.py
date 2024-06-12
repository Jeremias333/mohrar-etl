import pandas as pd


def create_table(cursor):
    # Definir o comando SQL para criar a tabela "projeto" se não existir
    create_table_query = '''CREATE TABLE IF NOT EXISTS projeto (
                                id_projeto INTEGER,
                                nome_projeto TEXT,
                                nome_cliente TEXT,
                                endereço_cliente TEXT,
                                telefone_cliente TEXT,
                                cpf_cliente TEXT,
                                orcamento REAL,
                                orcamento_em TEXT,
                                previsao_entrega_em TEXT,
                                valor_devido REAL,
                                meio_pagamento TEXT,
                                pago BOOLEAN,
                                pago_em TEXT,
                                limite_orcamento INTEGER,
                                material_comprado TEXT,
                                projeto_finalizado_em TEXT,
                                material_comprado_em TEXT,
                                gestor TEXT,
                                observacao TEXT
                            );'''

    # Executar o comando para criar a tabela "projeto"
    cursor.execute(create_table_query)

# def populate_table(cursor, csv_file_path):
#     # Definir o comando SQL para carregar os dados do arquivo CSV para a tabela "banana"
#     copy_query = f'''COPY banana(size, weight, sweetness, softness, harvesttime, ripeness, acidity, quality)
#                     FROM '{csv_file_path}'
#                     DELIMITER ','
#                     CSV HEADER;'''

#     # Executar o comando para carregar os dados do arquivo CSV para a tabela "banana"
#     cursor.execute(copy_query)


def populate_table(cursor, csv_file_path):
    # df = pd.read_csv(csv_file_path)
    copy_query = f'''COPY projeto(id_projeto, nome_projeto, nome_cliente, endereço_cliente,
                    telefone_cliente, cpf_cliente, orcamento, orcamento_em,
                    previsao_entrega_em, valor_devido, meio_pagamento, pago,
                    pago_em, limite_orcamento,
                    material_comprado, projeto_finalizado_em,
                    material_comprado_em, gestor, observacao)
                    FROM '{csv_file_path}'
                    DELIMITER ','
                    CSV HEADER;'''

    # insert_query = '''INSERT INTO projeto (
    #                     id_projeto, nome_projeto, nome_cliente, endereço_cliente, telefone_cliente,
    #                     cpf_cliente, orcamento, orcamento_em, previsao_entrega_em, valor_devido,
    #                     meio_pagamento, pago, pago_em, limite_orcamento, material_comprado,
    #                     projeto_finalizado_em, material_comprado_em, gestor, observacao
    #                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

    # for row in df.itertuples(index=False):
    #     cursor.execute(insert_query, row)
    
    cursor.execute(copy_query)


def drop_table(cursor):
    # Deletar a tabela "projeto" se existir
    drop_table_query = '''DROP TABLE IF EXISTS projeto;'''
    cursor.execute(drop_table_query)


def select_all(cursor):
    # Selecionar todos os registros da tabela "projeto" e exibi-los
    select_query = '''SELECT * FROM projeto;'''
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)
