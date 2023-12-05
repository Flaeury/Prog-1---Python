import flet as ft
# Importar


def main(page):
    # Definir a função principal chamando o argumento PAGE, do framework

    # Sempre chamar o flet, o que é estranho...
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    # Chamando atos, como o click do botão.
    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
