import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6
    
    def button_clicked(e):

        if tfnombre.value==tfpassword.value:
            dlg = ft.AlertDialog(title=ft.Text("Usuario y contraseña coinciden"))
            page.dialog = dlg
            dlg.open = True
            page.update()
        else:
            dlg = ft.AlertDialog(title=ft.Text("Usuario y contraseña NO coinciden"))
            page.dialog = dlg
            dlg.open = True
            page.update()
        page.update()

    #Fin --- Ejercicio 6


    #Ejercicio 2
    img = ft.Image(src=f"Logo.png",width=200,height=200)
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250
    tfnombre = ft.TextField(label="Nombre")

    #Ejercicio 4
    tfpassword= ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    #Fin --- Ejercicio 4


    #Ejercicio 5
    btnEntrar=ft.ElevatedButton("Entrar", icon="park_rounded",color="blue",on_click=button_clicked)
    #Fin-- Ejercicio 5


    page.add(img,tfnombre, tfpassword, btnEntrar)
    

ft.app(target=main,assets_dir="fotos")