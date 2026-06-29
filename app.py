## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================

## interface grafica que vai rodar a aplicacao como um todo
## arquivo main
import tkinter as tk
from tkinter import ttk, messagebox
from prestador import Prestador
from cep import consultar_cep


class App:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Catalogo de Prestadores de Servico TI")

        self.id_em_edicao = None
        self.prestador = None

        self.frame_menu = tk.Frame(self.janela)
        self.frame_form = tk.Frame(self.janela)
        self.frame_tabela = tk.Frame(self.janela)

        self.montar_menu()
        self.montar_formulario()
        self.montar_tabela()

        self.mostrar_frame(self.frame_menu)

    def montar_menu(self):
        tk.Button(self.frame_menu, text="Adicionar Prestador",
                command=lambda: (self.preparar_formulario(None), self.mostrar_frame(self.frame_form))).pack(pady=10)
                
        tk.Button(self.frame_menu, text="Listar Prestadores",
                command=lambda: self.mostrar_frame(self.frame_tabela)).pack(pady=10)
    def mostrar_frame(self, frame):
        # esconde todos
        self.frame_menu.pack_forget()
        self.frame_form.pack_forget()
        self.frame_tabela.pack_forget()
        # mostra só o pedido
        if(frame == self.frame_tabela):
            self.listar()
        frame.pack(fill="both", expand=True)
    def montar_formulario(self):
        # nome
        self.label_nome = tk.Label(self.frame_form, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.campo_nome = tk.Entry(self.frame_form)
        self.campo_nome.grid(row=0, column=1)
        # tipo de documento
        self.label_tipo_documento = tk.Label(self.frame_form, text="Tipo de Documento:")
        self.label_tipo_documento.grid(row=1, column=0)
        self.campo_tipo_documento = ttk.Combobox(self.frame_form, values=["CPF", "CNPJ"], state="readonly")
        self.campo_tipo_documento.grid(row=1, column=1)
        # documento
        self.label_documento = tk.Label(self.frame_form, text="Documento:")
        self.label_documento.grid(row=2, column=0)  
        self.campo_documento = tk.Entry(self.frame_form)
        self.campo_documento.grid(row=2, column=1)
        # data de nascimento
        self.label_data_nascimento = tk.Label(self.frame_form, text="Data de Nascimento:")
        self.label_data_nascimento.grid(row=3, column=0)
        self.campo_data_nascimento = tk.Entry(self.frame_form)
        self.campo_data_nascimento.grid(row=3, column=1)
        # contato
        self.label_contato = tk.Label(self.frame_form, text="Contato:")
        self.label_contato.grid(row=4, column=0)
        self.campo_contato = tk.Entry(self.frame_form)
        self.campo_contato.grid(row=4, column=1)
        # cep
        self.label_cep = tk.Label(self.frame_form, text="CEP:")
        self.label_cep.grid(row=5, column=0)
        self.campo_cep = tk.Entry(self.frame_form)
        self.campo_cep.grid(row=5, column=1)
        self.botao_buscar_cep = tk.Button(self.frame_form, text="Buscar CEP", command=self.buscar_cep)
        self.botao_buscar_cep.grid(row=5, column=2)
        # uf
        self.label_uf = tk.Label(self.frame_form, text="UF:")
        self.label_uf.grid(row=6, column=0)
        self.campo_uf = ttk.Combobox(self.frame_form, values=[
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
            "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
            "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        ], state="readonly")
        self.campo_uf.grid(row=6, column=1)
        # cidade
        self.label_cidade = tk.Label(self.frame_form, text="Cidade:")
        self.label_cidade.grid(row=7, column=0)
        self.campo_cidade = tk.Entry(self.frame_form)
        self.campo_cidade.grid(row=7, column=1)
        # bairro
        self.label_bairro = tk.Label(self.frame_form, text="Bairro:")
        self.label_bairro.grid(row=8, column=0)
        self.campo_bairro = tk.Entry(self.frame_form)
        self.campo_bairro.grid(row=8, column=1)
        # rua
        self.label_rua = tk.Label(self.frame_form, text="Rua:")
        self.label_rua.grid(row=9, column=0)
        self.campo_rua = tk.Entry(self.frame_form)
        self.campo_rua.grid(row=9, column=1)
        # complemento
        self.label_complemento = tk.Label(self.frame_form, text="Complemento:")
        self.label_complemento.grid(row=10, column=0)
        self.campo_complemento = tk.Entry(self.frame_form)
        self.campo_complemento.grid(row=10, column=1)
        # numero
        self.label_numero = tk.Label(self.frame_form, text="Numero:")
        self.label_numero.grid(row=11, column=0)
        self.campo_numero = tk.Entry(self.frame_form)
        self.campo_numero.grid(row=11, column=1)
        # salvar
        self.botao_salvar = tk.Button(self.frame_form, text="Salvar", command=self.salvar)
        self.botao_salvar.grid(row=12, column=0, columnspan=2)
        # excluir
        self.botao_excluir = tk.Button(self.frame_form, text="Excluir", command=self.excluir)
        self.botao_excluir.grid(row=13, column=0, columnspan=2) 
        # limpar
        self.botao_limpar = tk.Button(self.frame_form, text="Limpar", command=self.limpar)
        self.botao_limpar.grid(row=14, column=0, columnspan=2)
        # voltar
        tk.Button(self.frame_form, text="Voltar",
          command=lambda: self.mostrar_frame(self.frame_menu)).grid(row=15, column=0, columnspan=2)
    def montar_tabela(self):
        self.tree = ttk.Treeview(self.frame_tabela, columns=("ID", "Nome", "Tipo de Documento", "Documento", "Data de Nascimento", "Rua", "Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP", "Contato"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Tipo de Documento", text="Tipo de Documento")
        self.tree.heading("Documento", text="Documento")
        self.tree.heading("Data de Nascimento", text="Data de Nascimento")
        self.tree.heading("Rua", text="Rua")
        self.tree.heading("Numero", text="Numero")
        self.tree.heading("Complemento", text="Complemento")
        self.tree.heading("Bairro", text="Bairro")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.heading("CEP", text="CEP")
        self.tree.heading("Contato", text="Contato")
        self.tree.column("ID", width=40)
        self.tree.column("Nome", width=150)
        self.tree.column("Documento", width=110)
        self.tree.column("Data de Nascimento", width=110)
        self.tree.column("Rua", width=150)
        self.tree.column("Numero", width=50)
        self.tree.column("Complemento", width=150)
        self.tree.column("Bairro", width=150)
        self.tree.column("Cidade", width=150)
        self.tree.column("UF", width=50)
        self.tree.column("CEP", width=110)
        self.tree.column("Contato", width=110)
        self.tree.column("Tipo de Documento", width=110)
        self.tree.grid(row=0, column=0, columnspan=2)

        self.tree.bind("<Double-1>", self.ao_dar_duplo_clique)
        # voltar
        tk.Button(self.frame_tabela, text="Voltar",
          command=lambda: self.mostrar_frame(self.frame_menu)).grid(row=17, column=0, columnspan=2)
    def ao_dar_duplo_clique(self, evento):
        selecao = self.tree.selection()
        if not selecao:
            return
        item = selecao[0]
        id = self.tree.item(item)["values"][0]
        prestador = Prestador(id=id)
        prestador.selectPrestador()
        self.preparar_formulario(prestador)
        self.mostrar_frame(self.frame_form)
    def preparar_formulario(self, prestador):
        self.limpar()

        if prestador is None:
            self.id_em_edicao = None
        else:
            self.id_em_edicao = prestador.id
            self.prestador = prestador
            self.campo_nome.insert(0, prestador.nome)
            self.campo_tipo_documento.set(prestador.tipo_documento)
            self.campo_documento.insert(0, prestador.documento)
            self.campo_data_nascimento.insert(0, prestador.data_nascimento)
            self.campo_rua.insert(0, prestador.rua)
            self.campo_numero.insert(0, prestador.numero)
            self.campo_complemento.insert(0, prestador.complemento)
            self.campo_bairro.insert(0, prestador.bairro)
            self.campo_cidade.insert(0, prestador.cidade)
            self.campo_uf.set(prestador.uf)
            self.campo_cep.insert(0, prestador.cep)
            self.campo_contato.insert(0, prestador.contato)

    def checar_tipo_documento(self, tipo, documento):
        numeros = "".join(c for c in documento if c.isdigit())

        if tipo == "CPF":
            if len(numeros) != 11:
                raise ValueError("CPF deve ter 11 dígitos.")
        elif tipo == "CNPJ":
            if len(numeros) != 14:
                raise ValueError("CNPJ deve ter 14 dígitos.")
        else:
            raise ValueError("Selecione o tipo de documento (CPF ou CNPJ).")
    def salvar(self):
        nome = self.campo_nome.get()
        tipo_documento = self.campo_tipo_documento.get()
        documento = self.campo_documento.get()
        data_nascimento = self.campo_data_nascimento.get()
        rua = self.campo_rua.get()
        numero = self.campo_numero.get()
        complemento = self.campo_complemento.get()
        bairro = self.campo_bairro.get()
        cidade = self.campo_cidade.get()
        uf = self.campo_uf.get()
        cep = self.campo_cep.get()
        contato = self.campo_contato.get()

        try:
            self.checar_tipo_documento(tipo_documento, documento)
        except ValueError as erro:
            messagebox.showerror("Documento inválido", str(erro))
            return 

        prestador = Prestador(nome=nome, tipo_documento=tipo_documento, documento=documento, data_nascimento=data_nascimento, rua=rua, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, uf=uf, cep=cep, contato=contato)

        if self.id_em_edicao is None:
            resultado = prestador.insertPrestador()
            if "sucesso" in resultado.lower():
                messagebox.showinfo("Sucesso", resultado)
            else:
                messagebox.showerror("Erro", resultado)
        else:
            prestador.id = self.id_em_edicao
            resultado = prestador.updatePrestador()
            if "sucesso" in resultado.lower():
                messagebox.showinfo("Sucesso", resultado)
            else:
                messagebox.showerror("Erro", resultado)
        self.limpar()
        self.id_em_edicao = None
        self.listar()
    def excluir(self):
        if self.id_em_edicao is None:
            messagebox.showwarning("Aviso", "Nenhum prestador selecionado.")
            return
        prestador = Prestador(id=self.id_em_edicao)
        resultado = prestador.deletePrestador()
        if "sucesso" in resultado.lower():
            messagebox.showinfo("Sucesso", resultado)
        else:
            messagebox.showerror("Erro", resultado)
        self.limpar()
        self.id_em_edicao = None
        self.listar()
    def listar(self):
        # limpa as linhas antigas primeiro
        for item in self.tree.get_children():
            self.tree.delete(item)
        # agora busca e insere
        prestadores = Prestador.selectTodos()
        for prestador in prestadores:
            self.tree.insert("", "end", values=(prestador.id, prestador.nome, prestador.tipo_documento, prestador.documento, prestador.data_nascimento, prestador.rua, prestador.numero, prestador.complemento, prestador.bairro, prestador.cidade, prestador.uf, prestador.cep, prestador.contato))
    def buscar_cep(self):
        cep = self.campo_cep.get().replace("-", "").strip()        

        try:
            dados = consultar_cep(cep)    
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))  
            return                         
        self.campo_rua.delete(0, tk.END)
        self.campo_rua.insert(0, dados["rua"])
        self.campo_bairro.delete(0, tk.END)
        self.campo_bairro.insert(0, dados["bairro"])
        self.campo_cidade.delete(0, tk.END)
        self.campo_cidade.insert(0, dados["cidade"])
        self.campo_uf.set(dados["uf"])
        self.campo_complemento.delete(0, tk.END)
        self.campo_complemento.insert(0, dados["complemento"])
    def limpar(self):
        self.campo_nome.delete(0, tk.END)
        self.campo_tipo_documento.set("")
        self.campo_documento.delete(0, tk.END)
        self.campo_data_nascimento.delete(0, tk.END)
        self.campo_rua.delete(0, tk.END)
        self.campo_numero.delete(0, tk.END)
        self.campo_complemento.delete(0, tk.END)
        self.campo_bairro.delete(0, tk.END)
        self.campo_cidade.delete(0, tk.END)
        self.campo_uf.set("")
        self.campo_cep.delete(0, tk.END)
        self.campo_contato.delete(0, tk.END)
if __name__ == "__main__":
    janela = tk.Tk()      # cria a janela raiz
    app = App(janela)     # monta sua aplicação dentro dela
    janela.mainloop()     # inicia o loop