from exceptions import FilmePeleException, NinguemTemPacienciaException
from acoes import CaixaSom, conversa, acao

from random import choice, randint
from time import sleep
from typing import Callable
from functools import wraps
from abc import ABC, abstractmethod

from emoji import emojize
from simpleeval import simple_eval


class Morador(ABC):
    @abstractmethod
    def _pagar_aluguel(self):
        pass


class Chaves(Morador):
    '''
    Faz ações ligadas ao personagem Chaves.
    
    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
        alterego (str): Chapolin Colorado.
    '''
    def __init__(self):
        self.nome = '\033[1;32mChaves:\033[m'
        self.alterego = '\033[1;31mC\033[1;33mh\033[1;31ma\033[1;33mp\033[1;31mo\033[1;33ml\033[1;31mi\033[1;33mn\033[1;31m:\033[m'

    def calc(self, equacao: str) -> str:
        '''
        Gosta de equações difíceis.

        Args:
            equacao (str): equação a ser calculada.
        
        Returns:
            Se a equação for fácil, retorna uma string falando que a equação é fácil e pede uma mais difícil.
            Se não for uma equação, não entende e retorna que saberia fazer com maçãs.
            Se for difícil, retorna a equação resolvida
        '''
        chance = randint(1, 4)

        if chance == 4:
            try:
                return simple_eval(equacao)
            except:
                return f'{self.nome} Eu sabia essa era com maçãs!'
        
        return f'{self.nome} Mas essa é muito fácil, faça outra mais difícil!'

    def eh_privado(self, variavel: str) -> bool | dict[str, str | bool]:
        '''
        Checa se uma variável é privada.

        Args:
            variavel (str): Variável que será verificada.
        
        Returns:
            False, se a função não for privada. Caso contrário, retorna um dicionário com uma citação e True. 
        '''
        try:
            if variavel.startswith('_') or variavel.startswith('__'):
                return {'citacao': f'{self.nome} Carne de burro não é transparente!', 'private': True}
        except AttributeError:
            return {'citacao': f'{self.nome} Carne de burro não é transparente!', 'private': True}
        else:
            return False

    def checar_erro(self, func: Callable) -> Callable:
        '''
        (Decorator)
        Chaves verifica se a função ou método possui algum erro.
        
        Args:
            func (Callable): Função que será verificada.
            args (tuple): argumentos da função, que serão desempacotados.
            kwargs (dict): argumentos da função com chave, que serão desempacotados.
        
        Returns:
            Retornar um erro, caso a função tenha erro, e retorna uma string com uma citação caso não tenha.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                raise FilmePeleException(f'{self.nome} Era melhor ter ido ver o filme do Pelé!')
            else:
                citacoes = [f'{self.alterego} Todos os meus movimentos são friamente calculados!', f'{self.alterego} Não contavam com minha astúcia!']
                print(choice(citacoes))
                return
        return wrapper

    def fazer_silencio(self, girafales: Girafales) -> None:
        '''
        Faz silêncio... mas algo acontece

        Args:
            girafales (Girafales): Instãncia da classe Girafales
        '''
        sleep(1.5)
        conversa(self.nome, '[...] o professor linguiça!', 1.2)

        # toca som de risada
        som = CaixaSom() 
        som.init()
        som.som_risada()
        del som

        girafales.tatatata()

    def falar(self, palavra: str, vezes: int = 3) -> None:
        '''
        Pede para Chaves falar alguma palavra.
        
        Args:
            palavra (str): A palavra que tentará ser dita por Chaves.
            vezes (int): Quantas vezes Chaves confirmará a palavra certa.
        
        Returns:
            Retorna um erro porque ninguém tem paciência com o Chavinho :(
        '''
        palavra = palavra.capitalize()
        index = randint(0, len(palavra) - 1)
        alfabeto = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '', ' ']
        palavra_mudada = palavra.replace(palavra[index], choice(alfabeto)).capitalize()

        conversa(self.nome, palavra_mudada, 1)
        if palavra_mudada != palavra:
            conversa('', f'Se diz: {palavra}!', 1)

            if palavra.lower() == 'não sei':
                conversa(self.nome, 'Se não sabe por que fica corrigindo os outros?', 0)
                som = CaixaSom()
                som.init()
                som.som_risada()
                return
            
            for _ in range(0, vezes):
                sleep(1)
                conversa(self.nome, 'E como eu disse?', 1)
                conversa('', f'{palavra_mudada}!', 1)
                conversa(self.nome, 'E como é?', 1)
                conversa('', f'{palavra}!', 0)

            print(emojize(':angry_face:'))
            
            raise NinguemTemPacienciaException(f'{self.nome} Ninguém tem paciência comigo! {emojize(':disappointed_face:')}')
    
    def guardar_lista(self, lista: list, seu_madruga: Madruga, conversa_pre: bool =True) -> list[None]:
        '''
        Seu Madruga pede para Chaves guardar uma lista... O que poderia acontecer?
        
        Args:
            lista (list): A lista que será guardada por Chaves enquanto Seu Madruga está fora.
            seu_madruga (Madruga): Instância da classe Madruga
            conversa_pre (bool, optional): Se True, mostra a conversa que acontece antes de Chaves tomar conta da lista.
        
        Returns:
            Retorna uma lista (list) vazia, porque Chaves comprou tudo.
        '''
        if type(lista) == list:
            # conversa que acontece antes de Chaves tomar conta da lista
            if conversa_pre:
                conversa(seu_madruga.nome, 'CHAVES!', 0.6, fluxo=True)
                conversa('', 'Vem cá!', 0.3, fluxo=True)
                conversa('', 'Vem cá, Chaves, Chaves, Chaves!', 1, fluxo=True)
                conversa('', 'Vem aqui!', 0.5, fluxo=True)
                conversa('', 'Não me faça gritar!', 0.8, fluxo=True)
                conversa('', 'Vem, Chavinho!', 0.3, fluxo=True)
                conversa('', 'Venha, vem, vem!', 1.6)
                conversa(self.nome, 'O senhor não vai me bater?', 2)
                
                som = CaixaSom()
                som.init()
                som.som_risada()

                conversa(seu_madruga.nome, 'Chavinho, você quer ganhar mil cruzeiros?', 1)
                conversa(self.nome, 'Mil Cruzeiros?!', 1)
                conversa(seu_madruga.nome, 'Isso mesmo!', 1)
                conversa(self.nome, 'Sim, sim, sim!', 1)
                conversa(seu_madruga.nome, 'Olha, é que eu o posto um pouquinho e eu queria que tomasse conta.', 1.5)
                conversa(self.nome, 'Onde é que o senhor vai?', 1)
                conversa(seu_madruga.nome, 'Eu vou passar um telegrama.', 1)
                conversa(self.nome, 'E o dinheiro que o senhor vai me dar dá pra comprar um churro?', 1.5)
                conversa(seu_madruga.nome, 'Sim, sim.', 0.5)
                conversa(self.nome, 'Um churro gostosisisissímo custa mil cruzeiros, não é?!', 1)
                conversa(seu_madruga.nome, 'Sim, sim, sim, sim! Mas-', 1)
                conversa(self.nome, 'Um churro açucaradinho e douradinho?!', 1)
                conversa(seu_madruga.nome, 'Sim, sim, sim! Dá Licença!', 0)
                som.som_risada()
                sleep(1)
                del som

            # Chaves tomando conta da lista
            from random import random

            for item in lista:
                compras = ['Madruga', item]
                frases_seu_madruga = [
                                    f'Claro, Chavinho, foi por isso que te dei o dinheiro! Aqui está o {item}.',
                                    'Que que foi, que que foi, que que há! Claro que sim!',
                                    f'Aqui está o {item}.'
                                    ]

                print()
                compra = randint(0, 1)
                conversa(self.nome,
                         f'Seu {compras[compra].capitalize() if type(compras[compra]) == str else compras[compra]}, ',
                         0, fluxo=True)
                compras.pop(compra)
                conversa('', f'me vende {compras[0]}, por favor?', random())
                conversa('\033[1;34mChaves:', f'{choice(frases_seu_madruga)}\033[m', random())
                acao(self.nome, 'Dá o dinheiro', random())
                conversa('\033[1;34mChaves:', f'Põe o {item}\033[m', random())

        return []

    def desenhar(self, caminho_imagem: str, girafales: Girafales) -> None:
        '''
        Pede para Chaves fazer um desenho de ximforimpola.

        Args:
            caminho_imagem (str): Caminho de um arquivo de imagem
            girafales (Girafales): Instância da classe Girafales
        '''
        import ascii_magic
        imagem_ascii = ascii_magic.from_image(caminho_imagem)
        imagem_ascii.to_terminal()
        sleep(1)

        conversa(girafales.nome, 'O que representa?', 1)
        conversa(self.nome, 'Uma xinforimpola.', 2)
        conversa(girafales.nome, 'Uma o quê?', 1)
        conversa(self.nome, 'Xinforimpola!', 3.5)
        conversa(girafales.nome, 'E o que é isso?', 1)
        conversa(self.nome, 'Uma coisa que eu inventei.', 1.5, True)
        conversa('', 'Esse aí é igualzinho, não é verdade?', 1)
        conversa(girafales.nome, 'Exatamente igual!', 2.5, True)
        conversa('', 'Bem, eu vou lhe dar 6.', 1.5)
        conversa(self.nome, 'Por quê?! Pela exatização, o senhor deveria me dar 10!', 0)

    def _pagar_aluguel(self) -> bool:
        '''
        Tenta pagar o aluguel, mas não tem dinheiro... mas algo acontece
        
        Returns:
            False
        '''
        # toca música triste para sensibilizar o público
        som = CaixaSom()
        som.init()
        som.tocar_musica(0, 0)

        conversa(self.nome, f'Tá bom, mas não se irrite! {emojize(':pensive_face:')}', 1)

        return False


class Madruga(Morador):
    '''
    Faz ações ligadas ao personagem Seu Madruga.
    
    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = '\033[1;34mSeu Madruga:\033[m'

    def verificar_acao(self, func: Callable) -> Callable:
        '''
        Seu Madruga vigia uma função e fala o que acha sobre isso.

        Returns:
            Função com a opinião de Seu Madruga.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            print(f'{self.nome} Se soubesse que tinha mandado um idiota fazer isso, tinha ido eu mesmo.')

        return wrapper

    def checar_emoji(self, emoji: str) -> str:
        '''
        Verifica um emoji.
        
        Args:
            emoji: emoji que será verificado
        
        Returns:
            Retorna o emoji ou um alerta de perigo.
        '''
        emoji = emoji.strip()
        if (emoji.lower() == ':skull_and_crossbones:') or (emoji.lower() == ':skull:') or (emoji == '\U0001F480') or (emoji == '\u2620') or (emoji == '💀') or (emoji == '☠️'):
            return f'{self.nome} {emojize(emoji.lower())} Essa caveira significa prerigo, entenderam bem? PRE-RI-GO! {emojize(emoji.lower())}'
        
        return emojize(emoji)
    
    def responder_barriga(self, resposta: str, seu_barriga: Barriga) -> None:
        '''
        Tenta responder Seu Barriga, mas se enrola com as palavras.
        
        Args:
            resposta: O que será respondido.
            seu_barriga (Barriga): Instância da classe Barriga.
        
        Returns:
            Retorna uma conversa (levemente desconfortável, mas engraçada) entre Seu Barriga e Seu Madruga.
        '''
        resposta_separada = resposta.split(' ')
        index_palavra = randint(0, len(resposta_separada) - 1)
        conversa(seu_barriga.nome, 'Vim cobrar os 14 meses de alguel que me deve!', 1)
        
        for index, palavra in enumerate(resposta_separada):
            nome = self.nome if index == 0 else ''
            espaco = '' if index == len(resposta_separada) - 1 else ' '
            if index == index_palavra:
                conversa(nome, f'Barriga{espaco}', 0, fluxo=True)
            else:
                conversa(nome, f'{palavra}{espaco}', 0, fluxo=True)
        conversa('', f', Seu {resposta_separada[index_palavra].capitalize()}!', 0)
    
    def pancada(self, morador: Chaves | Quico | Barriga | Girafales | Florinda) -> None:
        '''
        Seu Madruga fica nervoso e dá uma pancada em alguém.
        
        Args:
            morador (Chaves | Quico | Barriga | Girafales | Florinda):
                Instância da classe de algum morador da vila. Se for outro tipo de objeto, dá um tapa no nada.
        
        Returns:
            Depois do tapa, consequências podem acontecer.
        '''

        # dá a pancada
        som = CaixaSom()
        som.init()
        som.som_pancada()
        del som

        if type(morador).__name__ == 'Barriga':
            conversa(self.nome, 'Me Barriga, seu Desculpe!', 1)

            morador.cobrar_aluguel(self)
        
        if type(morador).__name__ == 'Girafales':
            morador.tatatata()

        if type(morador).__name__ == 'Quico':
            conversa(morador.nome, 'Você não vai com a minha cara?!', 0.5)
            acao(morador.nome, 'Choro Quiquístico', 1.5)

            morador.chamar_mae(self)

        if type(morador).__name__ == 'Chaves':
            conversa(morador.nome, 'Pipipipipipi!', 1)
            conversa(self.nome, 'Só não te dou outra porque-', 1)
            conversa(morador.nome, '\033[1;31mSaiu da vida\033[m', 0)

            del morador
    
    def _pagar_aluguel(self) -> bool:
        '''
        Resiste ou aceita pagar os 14 meses de aluguel atrasados.
        
        Returns:
            True ou False
        '''
        chance = randint(1, 2)
        sleep(1)

        match chance:
            case 1:
                conversa(self.nome, 'Que que foi, que que foi, que que há?!', 0)
                return False

            case 2:
                conversa(self.nome, 'Devemos perdoar as ofensas, devemos perdoar as afrontas. Devemos perdoar os aluguéis atrasados.', 0)
                return True
        
        return True


class Quico(Morador):
    '''
    Faz ações ligadas ao personagem Quico.
    
    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = f'{emojize(':billed_cap:')}\033[1mQuico:\033[m'

    def exist(self, variavel=None) -> bool:
        '''
        Verifica se uma variável existe.
        
        Args:
            variavel (optional): Uma variável qualquer.
        
        Returns:
            Retorna True ou False (bool) se a variável existir
        '''
        if variavel:
            conversa(self.nome, 'Já chegou o disco voador!', 0)
            return True
        
        return False
    
    def chamar_mae(self, mamae: Florinda, madruga: Madruga, reclamacao: str ='MAMÃE!!!') -> None:
        '''
        Chama a Dona Florinda para dar um tapa em Seu Madruga.
        
        Args:
            mamae (Florinda): Instância de Dona Florinda, sua mamãe.
            madruga (Madruga): Instância do Seu Madruga.
            reclamacao (str, optional): A reclamação que Quico fará para chamar sua mãe.
        
        Returns:
            Deleta a instância de Seu Madruga.
            Se a instância passada de Seu Madruga não for o Seu Madruga, retorna None.
        '''
        conversa(self.nome, reclamacao, 2)

        mamae.punir_madruga(madruga)
    
    def outra_vez(self, florinda: Florinda, girafales: Girafales) -> None:
        '''
        Reações às interações estranhamente repetitivas entre Dona Florinda e Professor Girafales.
        
        Args:
            florinda (Florinda): Instância da classe Florinda.
            girafales (Girafales): Instância da classe Girafales.
        '''

        conversa(florinda.nome, 'Ah, que milagre o senhor por aqui!', 1.5)
        conversa(girafales.nome, 'Vim lhe trazer este humilde presentinho.', 1.5)
        acao(girafales.nome, 'Entrega flores', 1.5)
        conversa(self.nome, 'Outra vez flores?!', 2)

        som = CaixaSom()
        som.init()
        som.som_risada()

        conversa(florinda.nome, 'Tesouro!', 1.5)
        conversa(self.nome, 'Ai, mamãe, mas o professor parece que não sabe comprar outra coisa!', 1, fluxo=True)
        conversa('', 'Sempre', 1, fluxo=True)
        for _ in range(3):
            conversa('', 'Flores!', 1, fluxo=True)
        sleep(1)
        print()

        conversa(florinda.nome, 'Ah, mas acontece-', 0.8)
        conversa(self.nome, 'Ah, mas por que um dia ele não traz chocolates?!', 1, fluxo=True)

        som.som_risada()

        conversa('', 'Outro caramelos?!', 1, fluxo=True)
        conversa('', 'Outro dia um relógio de ouro?!', 1, fluxo=True)
        conversa('', 'Outro dia um casaco de pele?!', 1, fluxo=True)
        conversa('', 'Outro dia um carro último tipo?!', 1, fluxo=True)
        conversa('', 'Enfim?!', 4)
        conversa(florinda.nome, 'Ah, não ligue para ele, professor Girafales! É que o Quico adora fazer piadas!', 3.5)
        conversa(girafales.nome, 'Eu já percebi!', 2.5)
        conversa(florinda.nome, 'Mas não gostaria de entrar e tomar uma xícara de café?', 1.5)
        conversa(self.nome, 'Outra vez café?!', 1.5)
        conversa(florinda.nome, 'Tesouro!', 1.5)
        conversa(self.nome, 'É por isso que ele sempre te traz só flores!', 1.5)
        
        som.som_risada()
        del som

    def _pagar_aluguel(self, mae: Florinda, popis: Popis) -> bool:
        '''
        Chama sua mãe para pagar o aluguel.

        Args:
            mae (Florinda): Instância da classe Florinda, sua mãe.
            popis (Popis): Instância da classe Popis
        
        Returns:
            True
        '''
        sleep(1)
        conversa(self.nome, 'Você não vai com a minha cara?!', 0)
        conversa(popis.nome, 'Conta tudo pra sua mãe, Quico!', 1)
        mae._pagar_aluguel()

        return True


class Florinda(Morador):
    '''
    Faz ações ligada à personagem Dona Florinda.

    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = '\033[1;38;2;255;105;180mDona Florinda:\033[m'
    
    def punir_madruga(self, madruga: Madruga) -> None:
        '''
        Dá um tapa em Seu Madruga.
        
        Args:
            madruga (Madruga): Instância da classe Madruga
        '''
        if type(madruga).__name__ == 'Madruga':
            # dá a pancada
            som = CaixaSom()
            som.init()
            som.som_pancada()

            conversa(self.nome, 'E da próxima vez ', 1, fluxo=True)
            conversa('', 'faça isso com a sua vó!', 1)
            del som
            conversa(madruga.nome, '\033[1;31mSaiu da vila.\033[m', 0)
            del madruga
    
    def _pagar_aluguel(self) -> bool:
        '''
        Paga o Aluguel
        
        Returns:
            True
        '''
        acao(self.nome, 'Paga o aluguel.', 0)

        return True


class Barriga:
    '''
    Faz ações ligadas ao personagem Seu Barriga.
    
    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = '\033[1;38;2;139;69;19mSeu Barriga:\033[m'

    def responder(self, pergunta: str, resposta: str) -> None:
        '''
        Imprime uma pergunta e uma resposta.
        
        Args:
            pergunta (str): Uma pergunta.
            resposta (str): Uma resposta. Não recomendado responder com outra pergunta.
        '''
        print(f'Pergunta: {pergunta}')
        sleep(1)
        print(f'Resposta: {resposta}')

        if '?' in resposta:
            sleep(1)
            conversa(self.nome, 'Apenas um idiota responde uma pergunta com outra pergunta.', 0)
    
    def cobrar_aluguel(self, morador: Morador) -> None:
        '''
        Usa seu poder para cobrar o aluguel dos moradores.
        
        Args:
            morador: instância da classe do morador da vila.
        
        Returns:
            Deleta usuários que não podem pagar o aluguel.
        '''
        conversa(self.nome, 'Pague o aluguel!', 1)

        if type(morador).__name__ not in ['Madruga', 'Quico', 'Florinda', 'Chaves']:
            conversa(f'\033[1m{morador.nome if hasattr(morador, 'nome') else type(morador)}:\033[m', '...', 0)
            return
        
        morador_pagar_aluguel = morador._pagar_aluguel()
        if not morador_pagar_aluguel:
            if type(morador).__name__ == 'Chaves':
                conversa(morador.nome, '\033[1;31mS', 0.5, fluxo=True)
                conversa('', 'a', 0.5, fluxo=True)
                conversa('', 'i', 0.5, fluxo=True)
                conversa('', 'u', 0.5, fluxo=True)
                conversa('', ' ', 0.2, fluxo=True)
                conversa('', 'd', 0.5, fluxo=True)
                conversa('', 'a', 0.5, fluxo=True)
                conversa('', ' ', 0.2, fluxo=True)
                conversa('', 'v', 0.5, fluxo=True)
                conversa('', 'i', 0.5, fluxo=True)
                conversa('', 'l', 0.5, fluxo=True)
                conversa('', 'a', 0.5, fluxo=True)
                conversa('', '.', 1, fluxo=True)
                conversa('', '.', 1, fluxo=True)
                conversa('', '.\033[m', 1)
                conversa(self.nome, 'Chaves, ', 1, fluxo=True)
                conversa('', 'Pode voltar...', 2)
                
                som = CaixaSom()
                som.pausar_musica()
                del som

                conversa(morador.nome, 'Ju- ju- ju- ju- jura? E zás-', 0)
            else:
                conversa(morador.nome, '\033[1;31msaiu da vila...\033[m', 0)
                del morador


class Girafales:
    '''
    Faz ações ligadas ao personagem Professor Girafales.

     Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = ('\033[1;33mProfessor Girafales:\033[m')
    
    def tatatata(self) -> None:
        '''
        Demonstra sua raiva de forma característica.
        '''
        conversa(self.nome, '', 0, fluxo=True)
        for _ in range(0, 5):
            conversa('', 'TÁ!', 0.7, fluxo=True)
        print()


class Popis:
    '''
    Ligada à personagem Pópis.

    Attributes:
        nome (str): Nome do personagem para ser chamado, já com cores características.
    '''
    def __init__(self) -> None:
        self.nome = '\033[1;38;2;255;182;193mPópis:\033[m'



if __name__ == '__main__':
    seu_barriga = Barriga()
    seu_madruga = Madruga()
    chaves = Chaves()
    quico = Quico()
    girafales = Girafales()
    dona_florinda = Florinda()
    popis = Popis()
