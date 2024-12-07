import flet as ft
from database.conector import Conector
from controllers.produto_controller import ProdutoController

def produto_view(pg):
    conexao = Conector.conectar()
    elementos = []

    if conexao != None:
        produtos = ProdutoController.listar(conexao)

        pg.snack_bar = ft.SnackBar(ft.Text("Conexão estabelecida!"))
        pg.snack_bar.open = True

        tf_desc = ft.TextField(label="Descrição")
        tf_valor = ft.TextField(label="Valor")
        tf_qtd = ft.TextField(label="Quantidade")
        bt_salvar = ft.ElevatedButton("Salvar")

        divisor = ft.Divider(height=5)
        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Produto")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Quantidade"))
            ],
            rows=[]
        )

        dt_rows = []
        for produto in produtos:
            dt_row = ft.DataRow(cells=[
                    ft.DataCell(ft.Text(produto.cod)),
                    ft.DataCell(ft.Text(produto.descricao)),
                    ft.DataCell(ft.Text(produto.preco)),
                    ft.DataCell(ft.Text(produto.qtd))
                ])
            dt_rows.append(dt_row)
        tabela.rows = dt_rows

        elementos.append(tf_desc)
        elementos.append(tf_valor)
        elementos.append(tf_qtd)
        elementos.append(bt_salvar)
        elementos.append(divisor)
        elementos.append(tabela)

    else:
        pg.snack_bar = ft.SnackBar(ft.Text("Falha na Conexão!"))
        pg.snack_bar.open = True

    return ft.Column(
        elementos
)