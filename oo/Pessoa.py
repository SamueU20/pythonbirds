class Pessoa:
     def __init__(self, nome = None, idade=23):
          self.idade = idade
          self.nome = nome

       def cumprimetar(self):
         return f'Olá {id(self)}'


if __name__ == '__main__':
     p = Pessoa('Luciano')
     print(Pessoa.cumprimentar(p))
     print(id(p))
     print(p.cumprimentar())
     print(p.nome)
     p.nome = 'samuel'
     print(p.idade)