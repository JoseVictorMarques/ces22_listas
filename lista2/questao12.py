import sys

class Birds:
    def __init__(self):
        pass

class Duck(Birds):
    def quack(self):
        return "Duck can quacks"

class Swan(Birds):
    def quack(self):
        return "Swan can quacks"

class Goose(Birds):
    def quack(self):
        return "Goose can quacks"
    
class Chicken(Birds):
    pass


def quack_test(birds):
    for b in birds:
        try:
            yield b.quack()
        except AttributeError:
            pass
    

#Teste
birds= {'duck': Duck(), 'swan': Swan(), 'goose': Goose(), 'chicken': Chicken() }
print([b for b in quack_test(birds.values())])

