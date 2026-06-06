from random import choice, randint
from time import sleep
from pathlib import Path

from pygame import mixer


class CaixaSom:
    '''
    Classe que contém tudo necessário para tocas as músicas e efeitos sonoros de Chaves.
    Inicie chamando o método init()!
    
    Attributes:
        musicas (Path): Caminho para a pasta onde estão as músicas.
        efeitos (Path): Caminho para a pasta onde estão os efeitos.
        lista_musicas (list[Path]): Lista de todas músicas presentes na pasta de músicas.
        musica_atual (str | None): Musica que está tocando nesse momento.
    '''

    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        return cls._instancia
    
    def __init__(self):
        self.musicas = Path(__file__).parent / 'musicas'
        self.efeitos = Path(__file__).parent / 'efeitos'

        self.lista_musicas = [f.name for f in self.musicas.iterdir() if f.is_file()]

        self.musica_atual = None

    def init(self):
        '''
        Inicia o mixer do pygame para que seja possível tocar músicas e efeitos.
        '''
        if not mixer.get_init():
            mixer.init()

    def tocar_musica(self, id_musica: int | None = None, pausa: float =5) -> None:
        '''
        Toca uma música por id ou aleatória do Seriado Chaves
        
        Args:
            id_musica (optional): ID de alguma música do Chaves.
            pausa (optional): Quantos segundos de pausa após a música começar a tocar.
        
        Returns:
            Retorna uma música presente na playslist de músicas dos Chaves, ou uma conversa entre os moradores se as músicas forem roubadas
        '''

        if len(self.lista_musicas) < 1:
            self._roubaram_musicas()
            return

        if id_musica is None:
            id_musica = randint(0, len(self.lista_musicas) - 1)

        self.musica_atual = self.lista_musicas[id_musica]
        mixer.music.load(self.musicas / self.lista_musicas[id_musica])
        mixer.music.play()

        sleep(pausa)

    def _roubaram_musicas(self) -> None:
        '''
        Conversa entre os moradores da vila sobre alguém ter roubado as músicas.
        '''

        # definição de personagens
        chiquinha = '\033[1;31mCh\033[1;33mi\033[1;32mqui\033[1;33mn\033[1;31mha:\033[m'
        seu_madruga = '\033[1;34mSeu Madruga:\033[m'
        chaves = '\033[1;32mChaves:\033[m'

        conversa(seu_madruga, 'Estamos sem as músicas.', 1)
        conversa(chiquinha, 'Já empenhou de novo?', 1)
        conversa(seu_madruga, 'Eu não empenhei nada. Roubaram!', 1)
        conversa(chiquinha, 'Não, lá!', 1)
        conversa(seu_madruga, 'Sim, lá!', 1)
        conversa(chiquinha, 'Ai, lá!', 3)
        
        conversa(chaves, 'Seu Madruga, eu sei quem roubou as músicas.', 1)
        conversa(seu_madruga, 'Quem?!', 1)
        conversa(chaves, 'Um ladrão!', 0)

        self.som_risada()

        sleep(2)
        conversa(seu_madruga, 'Maravilhoso!', 0.8, fluxo=True)
        conversa('', 'Barbaridade!', 1, fluxo=True)
        conversa('', 'Nunca imaginei que você fosse tão inteligente, Chaves!', 1, fluxo=True)
        conversa('', 'Que Beleza!', 2)
        conversa(chaves, 'E também sei quem é o ladrão.', 1)
        conversa(seu_madruga, 'Quem é, Chaves?!', 1)
        conversa(chaves, 'O que roubou as músicas!', 0)

        self.som_risada()
        
        sleep(1)
    
    def pausar_musica(self):
        mixer.music.stop()

    def som_risada(self, pausa: float = 2):
        '''
        Chama um efeito sonoro de risada.
        
        Args:
            pausa (float, optional): Quantos segundos de pausa após o efeito começar a tocar.
            
        Returns:
            Um som de risada do Chaves.
        '''
        risada = mixer.Sound(self.efeitos / 'risada-de-fundo-chaves.mp3')
        risada.play()
        sleep(pausa)

    def som_pancada(self, pausa: float = 2):
        '''
        Chama um efeito sonoro de pancada.
        
        Args:
            pausa (float, optional): Quantos segundos de pausa após o efeito começar a tocar.
            
        Returns:
            Um som de pancada do Chaves.
        '''
        risada = mixer.Sound(self.efeitos / 'som-de-pancada-do-chaves.mp3')
        risada.play()
        sleep(pausa)


def citacao_aleatoria() -> dict[str, str]:
    '''
    Retorna uma citação aleatória do seriado Chaves
    '''
    citacoes = [
                {'citacao': 'Sabe qual o animal que come com o rabo? Todos, porque eles não podem tirar o rabo para comer.', 'autor': 'Chaves'},
                {'citacao': 'Pra aprender uma língua estrangeira você tem que primeiro estudar anatomia, porque anatomia estuda o corpo e a língua faz parte dele.', 'autor': 'Seu Madruga'},
                {'citacao': 'O trabalho não é ruim. Ruim é ter de trabalhar!', 'autor': 'Seu Madruga'},
                {'citacao': 'A vingança nunca é plena, mata a alma e envenena.', 'autor': 'Seu Madruga'},
                {'citacao': 'Quero ver, Outra vez, Seus olhinhos de noite serena.', 'autor': 'Seu Madruga'},
                {'citacao': 'Entre os chifres do touro!', 'autor': 'Chiquinha'}
                ]

    return choice(citacoes)

def conversa(personagem: str, fala: str, pausa: float, fluxo: bool =False) -> None:
    '''
    Imprime a fala de algum personagem.
    
    Args:
        personagem (str): Nome do personagem.
        fala (str): A fala do personagem.
        pausa (float): Quantos segundos de pausa para leitura da fala do personagem.
        fluxo (bool): Se a fala é completa, ou apenas uma parte, que será seguida por outra fala do mesmo personagem
    '''
    end = '' if fluxo else '\n'

    print(f'{(personagem + ' ') if personagem else personagem}{fala}{' ' if fluxo else ''}', end=end, flush=fluxo)
    sleep(pausa)

def acao(personagem: str, acao: str, pausa: float, fluxo: bool =False) -> None:
    '''
    Imprime a ação de algum personagem em negrito.

    Args:
        personagem (str): Nome do personagem.
        acao (str): A ação do personagem.
        pausa (float): Quantos segundos de pausa para leitura da fala do personagem.
        fluxo (bool): Se a fala é completa, ou apenas uma parte, que será seguida por outra fala do mesmo personagem
    '''
    conversa(personagem, f'\033[1m{acao}\033[m', pausa, fluxo)
