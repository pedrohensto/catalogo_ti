## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================

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
            c.execute("select * from prestadores where id=?", (id,))
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.tipo_documento = linha[2]
                self.documento = linha[3]
                self.data_nascimento = linha[4]
                self.rua = linha[5]
                self.numero = linha[6]
                self.complemento = linha[7]
                self.bairro = linha[8]
                self.cidade = linha[9]
                self.uf = linha[10]
                self.cep = linha[11]
                self.contato = linha[12]
            c.close()
            return "Busca feita com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na busca do prestador"
