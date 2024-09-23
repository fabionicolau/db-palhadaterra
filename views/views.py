# views/main_view.py

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from models import models


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PALHA DA TERRA")
        self.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self)
        self.tab_clientes = ttk.Frame(tab_control)
        self.tab_produtos = ttk.Frame(tab_control)

        tab_control.add(self.tab_clientes, text="Clientes")
        tab_control.add(self.tab_produtos, text="Produtos")
        tab_control.pack(expand=1, fill="both")

        self.create_clientes_tab()

        self.create_produtos_tab()

    def create_clientes_tab(self):
        frame = self.tab_clientes

        btn_inserir = tk.Button(
            frame, text="Criar Cliente", command=self.inserir_cliente
        )
        btn_inserir.pack(pady=5)

        btn_listar = tk.Button(
            frame, text="Listar Clientes", command=self.listar_clientes
        )
        btn_listar.pack(pady=5)

        btn_atualizar = tk.Button(
            frame, text="Atualizar Cliente", command=self.atualizar_cliente
        )
        btn_atualizar.pack(pady=5)

        btn_deletar = tk.Button(
            frame, text="Deletar Cliente", command=self.deletar_cliente
        )
        btn_deletar.pack(pady=5)

    def inserir_cliente(self):
        janela = ClienteForm(self, titulo="Criar Cliente")
        self.wait_window(janela)

    def listar_clientes(self):
        clientes = models.ler_clientes()
        if clientes:
            janela = Listagem(
                self,
                titulo="Lista de Clientes",
                dados=clientes,
                colunas=["id", "nome", "endereco", "telefone"],
            )
            self.wait_window(janela)
        else:
            messagebox.showinfo("Lista de Clientes", "Nenhum cliente encontrado.")

    def atualizar_cliente(self):
        id_cliente = simpledialog.askinteger(
            "Atualizar Cliente", "Digite o ID do cliente:"
        )
        if id_cliente:
            cliente = self.obter_cliente_por_id(id_cliente)
            if cliente:
                janela = ClienteForm(
                    self,
                    titulo="Atualizar Cliente",
                    dados=cliente,
                    id_registro=id_cliente,
                )
                self.wait_window(janela)
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")

    def deletar_cliente(self):
        id_cliente = simpledialog.askinteger(
            "Deletar Cliente", "Digite o ID do cliente:"
        )
        if id_cliente:
            resposta = messagebox.askyesno(
                "Confirmação",
                f"Tem certeza que deseja deletar o cliente com ID {id_cliente}?",
            )
            if resposta:
                models.deletar_cliente(id_cliente)
                messagebox.showinfo("Deletar Cliente", "Cliente deletado com sucesso.")

    def obter_cliente_por_id(self, id_cliente):
        clientes = models.ler_clientes()
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                return cliente
        return None

    def create_produtos_tab(self):
        frame = self.tab_produtos

        btn_inserir = tk.Button(
            frame, text="Criar Produto", command=self.inserir_produto
        )
        btn_inserir.pack(pady=5)

        btn_listar = tk.Button(
            frame, text="Listar Produtos", command=self.listar_produtos
        )
        btn_listar.pack(pady=5)

        btn_atualizar = tk.Button(
            frame, text="Atualizar Produto", command=self.atualizar_produto
        )
        btn_atualizar.pack(pady=5)

        btn_deletar = tk.Button(
            frame, text="Deletar Produto", command=self.deletar_produto
        )
        btn_deletar.pack(pady=5)

    def inserir_produto(self):
        janela = ProdutoForm(self, titulo="Criar Produto")
        self.wait_window(janela)

    def listar_produtos(self):
        produtos = models.ler_produtos()
        if produtos:
            janela = Listagem(
                self,
                titulo="Lista de Produtos",
                dados=produtos,
                colunas=["id", "nome", "descricao", "preco", "quantidade"],
            )
            self.wait_window(janela)
        else:
            messagebox.showinfo("Lista de Produtos", "Nenhum produto encontrado.")

    def atualizar_produto(self):
        id_produto = simpledialog.askinteger(
            "Atualizar Produto", "Digite o ID do produto:"
        )
        if id_produto:
            produto = self.obter_produto_por_id(id_produto)
            if produto:
                janela = ProdutoForm(
                    self,
                    titulo="Atualizar Produto",
                    dados=produto,
                    id_registro=id_produto,
                )
                self.wait_window(janela)
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

    def deletar_produto(self):
        id_produto = simpledialog.askinteger(
            "Deletar Produto", "Digite o ID do produto:"
        )
        if id_produto:
            resposta = messagebox.askyesno(
                "Confirmação",
                f"Tem certeza que deseja deletar o produto com ID {id_produto}?",
            )
            if resposta:
                models.deletar_produto(id_produto)
                messagebox.showinfo("Deletar Produto", "Produto deletado com sucesso.")

    def obter_produto_por_id(self, id_produto):
        produtos = models.ler_produtos()
        for produto in produtos:
            if produto["id"] == id_produto:
                return produto
        return None


class ClienteForm(tk.Toplevel):
    def __init__(self, parent, titulo="Cliente", dados=None, id_registro=None):
        super().__init__(parent)
        self.title(titulo)
        self.id_registro = id_registro
        self.create_widgets(dados)

    def create_widgets(self, dados):
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text="Endereço:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)

        self.nome_entry = tk.Entry(self)
        self.endereco_entry = tk.Entry(self)
        self.telefone_entry = tk.Entry(self)

        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        self.endereco_entry.grid(row=1, column=1, padx=10, pady=5)
        self.telefone_entry.grid(row=2, column=1, padx=10, pady=5)

        if dados:
            self.nome_entry.insert(0, dados["nome"])
            self.endereco_entry.insert(0, dados["endereco"])
            self.telefone_entry.insert(0, dados["telefone"])

        btn_salvar = tk.Button(self, text="Salvar", command=self.salvar_cliente)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

    def salvar_cliente(self):
        dados = {
            "nome": self.nome_entry.get(),
            "endereco": self.endereco_entry.get(),
            "telefone": self.telefone_entry.get(),
        }
        if not all(dados.values()):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        if self.id_registro:
            models.atualizar_cliente(self.id_registro, dados)
            messagebox.showinfo("Atualizar Cliente", "Cliente atualizado com sucesso.")
        else:
            models.inserir_cliente(dados)
            messagebox.showinfo("Inserir Cliente", "Cliente inserido com sucesso.")
        self.destroy()


class ProdutoForm(tk.Toplevel):
    def __init__(self, parent, titulo="Produto", dados=None, id_registro=None):
        super().__init__(parent)
        self.title(titulo)
        self.id_registro = id_registro
        self.create_widgets(dados)

    def create_widgets(self, dados):
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text="Descrição:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Preço:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self, text="Quantidade:").grid(row=3, column=0, padx=10, pady=5)

        self.nome_entry = tk.Entry(self)
        self.descricao_entry = tk.Entry(self)
        self.preco_entry = tk.Entry(self)
        self.quantidade_entry = tk.Entry(self)

        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        self.descricao_entry.grid(row=1, column=1, padx=10, pady=5)
        self.preco_entry.grid(row=2, column=1, padx=10, pady=5)
        self.quantidade_entry.grid(row=3, column=1, padx=10, pady=5)

        if dados:
            self.nome_entry.insert(0, dados["nome"])
            self.descricao_entry.insert(0, dados["descricao"])
            self.preco_entry.insert(0, str(dados["preco"]))
            self.quantidade_entry.insert(0, str(dados["quantidade"]))

        btn_salvar = tk.Button(self, text="Salvar", command=self.salvar_produto)
        btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

    def salvar_produto(self):
        try:
            dados = {
                "nome": self.nome_entry.get(),
                "descricao": self.descricao_entry.get(),
                "preco": float(self.preco_entry.get()),
                "quantidade": int(self.quantidade_entry.get()),
            }
            if not dados["nome"] or not dados["descricao"]:
                messagebox.showwarning("Atenção", "Preencha todos os campos.")
                return

            if self.id_registro:
                models.atualizar_produto(self.id_registro, dados)
                messagebox.showinfo(
                    "Atualizar Produto", "Produto atualizado com sucesso."
                )
            else:
                models.inserir_produto(dados)
                messagebox.showinfo("Inserir Produto", "Produto inserido com sucesso.")
            self.destroy()
        except ValueError:
            messagebox.showerror(
                "Erro", "Preço e Quantidade devem ser valores numéricos."
            )


class Listagem(tk.Toplevel):
    def __init__(self, parent, titulo="Listagem", dados=None, colunas=None):
        super().__init__(parent)
        self.title(titulo)
        self.create_widgets(dados, colunas)

    def create_widgets(self, dados, colunas):
        tree = ttk.Treeview(self, columns=colunas, show="headings")
        for coluna in colunas:
            tree.heading(coluna, text=coluna.capitalize())
            tree.column(coluna, anchor="center")

        for item in dados:
            valores = [item[coluna] for coluna in colunas]
            tree.insert("", tk.END, values=valores)

        tree.pack(expand=True, fill="both")
