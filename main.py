import flet as ft
from views.produto_view import produto_view

def main(pg:ft.Page):
    pg.title = "Restaurante Siri Cascudo"
    pg.window_width=700
    pg.window_height=700
    pg.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    pg.auto_scroll = ft.ScrollMode.AUTO

    def chama_produto(e):
        coluna = produto_view(pg)
        pg.clean()
        pg.add(coluna)

    pg.add(
        ft.ElevatedButton("Produtos", on_click = chama_produto)
    )

ft.app(target=main)