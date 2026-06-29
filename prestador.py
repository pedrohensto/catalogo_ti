## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================
import sqlite3
from banco import Banco


## criacao da classe Prestador, principal classe da aplicacao
## metodos de CRUD definidos na propria classe (eh um pouco de anti-pattern, mas simplifica o codigo)
class Prestador:
    def __init__(
        self,
        id=0,
        nome="",
        tipo_documento="",
        documento="",
        data_nascimento="",
        rua="",
        numero="",
        complemento="",
        bairro="",
        cidade="",
        uf="",
        cep="",
        contato="",
    ):
        self.id = id
        self.nome = nome
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.data_nascimento = data_nascimento
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.contato = contato

    ## na doc do sqlite3 eh recomendado passar os valores como values ?
    ## ja que passa direto das variaveis python e evita ataques de sqlinjection
    ## esse pattern foi usado em todas as operacoes do CRUD

    ## outro detalhe que vale mencao foi o sqlite3.Error que eh a classe padrao
    ## das exceptions do sqlite

    def insertPrestador(self) -> None:
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "insert into prestadores "
                "(nome, tipo_documento, documento, data_nascimento, rua, "
                "numero, complemento, bairro, cidade, uf, cep, contato) "
                "values (?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    self.nome,
                    self.tipo_documento,
                    self.documento,
                    self.data_nascimento,
                    self.rua,
                    self.numero,
                    self.complemento,
                    self.bairro,
                    self.cidade,
                    self.uf,
                    self.cep,
                    self.contato,
                ),
            )
            banco.conexao.commit()
            c.close()
            return "Prestador cadastrado com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na insercao do prestador"

    def updatePrestador(self) -> None:
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "update prestadores set nome=?, tipo_documento=?, "
                "documento=?, data_nascimento=?, rua=?, numero=?, "
                "complemento=?, bairro=?, cidade=?, uf=?, cep=?, contato=? "
                "where id=?",
                (
                    self.nome,
                    self.tipo_documento,
                    self.documento,
                    self.data_nascimento,
                    self.rua,
                    self.numero,
                    self.complemento,
                    self.bairro,
                    self.cidade,
                    self.uf,
                    self.cep,
                    self.contato,
                    self.id,
                ),
            )
            banco.conexao.commit()
            c.close()
            return "Prestador atualizado com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na alteracao do prestador"

    def deletePrestador(self) -> None:
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from prestadores where id=?", (self.id,))
            banco.conexao.commit()
            c.close()
            return "Prestador excluido com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na exclusao do prestador"

    def selectPrestador(self) -> None:
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from prestadores where id=?", (self.id,))
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.data_nascimento = linha[2]               
                self.rua = linha[3]
                self.numero = linha[4]
                self.complemento = linha[5]
                self.bairro = linha[6]
                self.cidade = linha[7]
                self.uf = linha[8]
                self.cep = linha[9]
                self.contato = linha[10]
                self.tipo_documento = linha[11]
                self.documento = linha[12]
                
            c.close()
            return "Busca feita com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na busca do prestador"

    @staticmethod
    def selectTodos():
        banco = Banco()
        lista = []
        try:
            c = banco.conexao.cursor()
            c.execute("select * from prestadores")   # sem where = todos
            for linha in c:
                p = Prestador()
                p.id = linha[0]
                p.nome = linha[1]
                p.data_nascimento = linha[2]
                p.rua = linha[3]
                p.numero = linha[4]
                p.complemento = linha[5]
                p.bairro = linha[6]
                p.cidade = linha[7]
                p.uf = linha[8]
                p.cep = linha[9]
                p.contato = linha[10]
                p.tipo_documento = linha[11]
                p.documento = linha[12]
                lista.append(p)
            c.close()
            return lista
        except sqlite3.Error:
            return []
