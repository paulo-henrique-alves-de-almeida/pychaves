'''
Exeções customizadas com citações do Seriado Chaves.

Chame inicializar() para ativar.
'''
import sys


class CustomExceptions:
    '''Customização de exceções com citações do seriado Chaves'''
    def __init__(self):
        self.personagens = {
            'chaves': '\033[1;32mChaves:\033[m',
            'madruga': '\033[1;34mSeu Madruga:\033[m',
            'florinda': '\033[1;38;2;255;105;180mDona Florinda:\033[m',
            'quico': '🧢 \033[1mQuico:\033[m',
            'barriga': '\033[1;38;2;139;69;19mSeu Barriga:\033[m'
            }

        self.traducoes = {
            'AttributeError': f'{self.personagens['chaves']} Carne de burro não é transparente!',
            'KeyboardInterrupt': f'{self.personagens['chaves']} Tá bom, mas não se irrite! \U0001F614',
            'IndexError': 'Tinha que ser o Chaves de novo!',
            'ValueError': f'{self.personagens['quico']} Gentalha! Gentalha!',
            'KeyError': f'{self.personagens['chaves']} Eu sou o Chaves, e você é o... o...?',
            'ZeroDivisionError': f'{self.personagens['chaves']} Ai, que burro! Dá zero pra ele!',
            'SystemExit': f'{self.personagens['chaves']} Era melhor ter ido ver o filme do Pelé!',
            'TabError': f'{self.personagens['chaves']} Foi sem querer querendo...',
            'SyntaxError': f'{self.personagens['chaves']} Foi sem querer querendo...',
            'RecursionError': f'{self.personagens['chaves']} E zás, e aí eu fazia assim, e depois assim...',
            'TypeError': f'{self.personagens['florinda']} Vamos tesouro, não se misture com essa gentalha!',
            'NameError': f'{self.personagens['chaves']} Eu sou o Chaves, e você é o... o...?',
            'FileNotFoundError': 'Cadê o Quico? O Quico sumiu!',
            'ModuleNotFoundError': f'\n{self.personagens['barriga']} Seu Madruga está?\n{self.personagens['quico']} Por parte de quem?\n{self.personagens['barriga']} Está ou não está?!\n{self.personagens['quico']} NÃO!!!\n{self.personagens['barriga']} OBRIGADO!\n{self.personagens['quico']} De nada!!!',
            'ImportError': f'{self.personagens['chaves']} Eu sou o Chaves, e você é o... o...?',
            'RuntimeError': f'{self.personagens['chaves']} Ninguém tem paciência comigo!',
            'TimeoutError': f'{self.personagens['chaves']} Ninguém tem paciência comigo!',
            'FileExistsError': f'{self.personagens['madruga']} Se já sabe, então por que pergunta?',
            'ConnectionRefusedError': f'{self.personagens['madruga']} Não está!!!',
            'ConnectionAbortedError': f'{self.personagens['chaves']} Digo... digo... É que me escapuliu!',
            'NotImplementedError': f'{self.personagens['florinda']} O que pensa que está fazendo?!',
            'PermissionError': f'{self.personagens['madruga']} Digo... digo... é que eu esqueci de pagar o aluguel!',
            'UnicodeDecodeError': f'{self.personagens['madruga']} Que que foi, que que foi, que que há?!',
            'UnicodeEncodeError': f'{self.personagens['madruga']} Que que foi, que que foi, que que há?!',
            'UnicodeError': f'{self.personagens['madruga']} Que que foi, que que foi, que que há?!',
            'UnicodeTranslateError': f'{self.personagens['madruga']} Que que foi, que que foi, que que há?!'
        }

    def hook(self, exctype, value):
        name = exctype.__name__
        msg = self.traducoes.get(name, f"Erro: {value}")
        
        print(f'\033[1;31m{name}:\033[m {msg}')

def inicializar():
    handler = CustomExceptions()
    sys.excepthook = handler.hook


class ChavesException(Exception):
    '''Classe base para Exceptions de Chaves'''
    pass


class AiQueBurroException(ChavesException):
    '''Para quando alguma burrice acontece.'''
    pass


class NinguemTemPacienciaException(ChavesException):
    '''Para quando alguma ação demora muito.'''


class FilmePeleException(ChavesException):
    '''Para quando era melhor ter ido ver o filme do Pelé.'''
    pass


class SemQuererQuerendo(ChavesException):
    '''Para quando algo acontece sem querer.'''
    pass


class NaoDeu(ChavesException):
    '''Para quando algo não funciona.'''
    pass


if __name__ == '__main__':
    import builtins

    inicializar()

    print('\033[1mErros:\033[m\n')
    todas_excecoes = [
        obj for obj in dir(builtins) 
        if isinstance(getattr(builtins, obj), type) and issubclass(getattr(builtins, obj), BaseException)
    ]

    for e in todas_excecoes:
        print(e)
