## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================

import sqlite3


class Banco:
    def __init__(self) -> None:
        self.conexao = sqlite3.connect("prestador.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists prestadores(
                        id integer primary key autoincrement,
                        nome text, tipo_documento text, documento text,
                        data_nascimento text, rua text, numero text,
                        complemento text, bairro text, cidade text,
                        uf text, cep text, contato text)""")
        self.conexao.commit()
        c.close()
