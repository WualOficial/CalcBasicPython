class operacoes:
    
    def __init__(self):
        self.num1 = 0.0
        self.count = 0
        self.operator = ""
    
    def soma(a, b):
        if b == "+":
            return a
        return a + b
    
    def subtracao(a, b):
        if b == "-":
            return a
        if b < 0:
            return a + b #Subtrair um número negativo é o mesmo que somar o valor positivo 
        else:
            return a - b
        
    def multiplicacao(a, b):
        if b == "*":
            return a
        return a * b
    def divisao(a, b):
        if b == "/":
            return a
        return a / b