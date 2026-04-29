class operacoes:
    
    def __init__(self):
        self.num1 = 0.0
        self.count = 0
        self.operator = ""
    
    def soma(a, b):
        if b == "+":
            return a
        return float(a) + float(b)
    
    def subtracao(a, b):
        if b == "-":
            return a
        return float(a) - float(b)