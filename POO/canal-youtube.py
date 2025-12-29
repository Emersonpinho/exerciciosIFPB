from symtable import Class


class Canal:
    #metedo construtor / metodo magico
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []

    def postar(self, video):
        if video in self.videos:
            print('Esse video ja foi postado')
            return
        self.videos.append(video)

    def __str__(self):
        return f'Canal: {self.nome}\nDescrição: {self.descricao}\nInscritos: {self.inscritos}'

# herança
class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property # indica que determinado metodo é uma propriedade
    def equipe(self):
        return self._equipe

    # encapsulamento
    def adicionar_mebro(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f'O membro {membro} já está na equipe!')

    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f'O membro {membro} não está na equipe!')


class Vidio:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

        self.visualizacao = 0
        self.like = 0
        self.deslike = 0
        self.comentarios = []

    def __repr__(self):
        return f'<{self.titulo}>'

    def assistir(self):
        self.visualizacao += 1

    def like(self):
        self.like += 1

    def deslike(self):
        self.deslike += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def info(self):
         print(f'Vidio: {self.titulo}\nDescrição: {self.descricao}\n{self.visualizacao} Visualizações\n{self.like} Likes\n{self.deslike} Deslikes\nComentarios: {self.comentarios}')

lanCode = Canal('lanCode', 'Canal legalzinho para estudar programação', '2M')
cursoEmVidio =  Canal('Curso em vídio', 'Paixão por ensinar', '44M')
duolingo = CanalEmpresarial('Duolingo', 'Ingres', 'Tantos milhoes')

vidioPoo = Vidio('Python Poo', 'Entenda de uma vez por todas!')
vidioSkill = Vidio('Desenvolva skills em programação!', 'Entenda tudo sobre skills')

cursoEmVidio.postar(vidioPoo)
cursoEmVidio.postar(vidioSkill)
print(cursoEmVidio.videos)

'''print(f'Membros atuais: {duolingo.equipe}')
duolingo.adicionar_mebro('Pedro')
print(f'Membros atuais: {duolingo.equipe}')
duolingo.adicionar_mebro('André')
duolingo.remover_membro('Pedro')
duolingo.adicionar_mebro('João')
print(f'Membros atuais: {duolingo.equipe}')'''
