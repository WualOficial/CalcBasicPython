class operacoes:
    
    def __init__(self):
        self.num1 = 0.0
        self.count = 0
    
    def soma(a, b):
        if b in ["+", "-","/","*"]:
            return a
        return float(a) + float(b)