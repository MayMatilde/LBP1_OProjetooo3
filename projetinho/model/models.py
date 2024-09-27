class Livro:
    def __init__(self, id, nome, autor, gosto, ):
        self.nome = nome
        self.autor = autor
        self.gosto = gosto 
        self.id = id

listaLivros = []

def AddLivros( nome, autor, gosto,):
    id = len(listaLivros) + 1
    novo_livro = Livro (id, nome, autor, gosto,)
    listaLivros.append(novo_livro)
