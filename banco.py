## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================

import sqlite3


class Banco:
    def __init__(self) -> None:
        self.conexao = sqlite3.connect("prestador.db")
        self.createTable()

    def createTable():
        c = self.conexao.cursor()

        c.execute(""""create table if not exists prestadores(
        id integer primary key autoincrement,
        nome text,
        data_nasc text,
        endereco text,
        contato integer,
        tipo_doc text,
        doc integer)""")

        self.conexao.commit()
        c.close()
