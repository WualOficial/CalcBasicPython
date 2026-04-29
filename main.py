import flet as ft
from calculadora import operacoes

def main(page: ft.Page):
    page.title = "CALC BASIC PYTHON FLET"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    calc = operacoes()
    text = ft.Text("0", size=40, weight=ft.FontWeight.BOLD)

    def update_display(value):
        if calc.count == 0:
            if value == "." and "." in text.value:
                text.value = text.value
                
                #SOMA
            elif value == "+" and text.value != "+":
                if calc.num1 == 0.0:
                    calc.num1 = float(text.value)
                    text.value = "0"
                    calc.operator = "+"
                    
                else:
                    resultado = operacoes.soma(calc.num1, float(text.value))
                    calc.num1 = resultado 
                    text.value = resultado
                    calc.count = 1
                    
                 #SUBTRAÇÃO   
            elif value == "-":
                if text.value == "0":
                    text.value = value
                else:
                    if calc.num1 == 0.0:
                        calc.num1 = float(text.value)
                        text.value = "0"
                        calc.operator = "-"
                    else:
                        resultado = operacoes.subtracao(calc.num1, float(text.value))
                        calc.num1 = resultado 
                        text.value = resultado
                        calc.count = 1
            else:
                text.value = text.value + value if text.value != "0" else value
                
        else: #Zera Contadores e sinal operador para nova operação
            text.value = value
            calc.count = 0
            calc.operator = ""
            
        page.update()
        
    def fazer_conta():
        update_display(value = calc.operator)
        
    def clear_display():
        text.value = "0"
        calc.num1 = 0.0
        page.update()
        

    row1 = ft.Row(controls=[ft.ElevatedButton("1", on_click=lambda e: update_display("1")), ft.ElevatedButton("2", on_click=lambda e: update_display("2")), ft.ElevatedButton("3", on_click=lambda e: update_display("3"))],alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Row(controls=[ft.ElevatedButton("4", on_click=lambda e: update_display("4")), ft.ElevatedButton("5", on_click=lambda e: update_display("5")), ft.ElevatedButton("6", on_click=lambda e: update_display("6"))],alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row(controls=[ft.ElevatedButton("7", on_click=lambda e: update_display("7")), ft.ElevatedButton("8", on_click=lambda e: update_display("8")), ft.ElevatedButton("9", on_click=lambda e: update_display("9"))],alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Row(controls=[ft.ElevatedButton("0", on_click=lambda e: update_display("0")), ft.ElevatedButton(".", on_click=lambda e: update_display(".")), ft.ElevatedButton("=", on_click=lambda e: fazer_conta())],alignment=ft.MainAxisAlignment.CENTER)
    row5 = ft.Row(controls=[ft.ElevatedButton("C", on_click=lambda e: clear_display()), ft.ElevatedButton("-", on_click=lambda e: update_display("-")),ft.ElevatedButton("+", on_click=lambda e: update_display("+"))],alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        text,
        row1,
        row2,
        row3,
        row4,
        row5
    
    )
    
    

if __name__ == "__main__":
    ft.run(main)