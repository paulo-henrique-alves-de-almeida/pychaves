# PYCHAVES
Uma biblioteca feita em referência ao seriado Chaves (originalmente El Chavo del Ocho). Para deixar sua experiência programando em Python um pouco mais engraçada.

Sempre adorei Chaves, então criar essa biblioteca foi uma experiência muito divertida, principalmente ao escrever as interações entre persoagens como classes.

---

## 💻 Exemplo
Como utilizar uma função da biblioteca:
```python
from pychaves import Chaves

chaves = Chaves() # Instancia a classe Chaves para entrar na vila
print(chaves.calc('1 + 1'))
# Retorno: "Mas essa é muito fácil, faça uma mais difícil!"
```

---

## 🔩 Instalação
Para instalar a biblioteca utilizando `pip`, digite esse comando em seu terminal:

`pip install pychaves`

---

## Personagens

### Chaves
É o principal personagem do seriado e a classe que possui mais métodos.
Veja seus **métodos listados abaixo:**

- **calc:** Recebe uma string com equação e possui chance de realizá-la ou pedir uma mais difícil.
- **eh_privado:** Checa se uma variável é privada e retorna uma citação.
- **checar_erro:** Decorator que captura qualquer erro e retorna uma citação.
- **fazer_silencio:** Faz silêncio, mas algo acontece.
- **falar:** Chaves fala alguma palavra errado e brigam com ele.
- **guardar_lista:** Seu Madruga pede para Chaves guardar uma lista, mas ele some com tudo.
- **desenhar:** Transforma um arquivo de imagem em arte ASCII e o chama de Xinforimpola.

### Seu Madruga
**Métodos:**

- **verificar_acao:** Decorator que adiciona um comentário de Seu Madruga após a ação ser realizada.
- **checar_emoji:** Verifica se é um emoji perigoso.
- **responder_barriga:** Dá uma resposta a Seu Barriga, mas acaba trocando algumas palavras.
- **pancada:** Dá uma pancada em algum morador da vila.

### Quico
**Métodos:**

- **exist:** Verifica se uma variável existe.
- **chamar_mae:** Chama sua mãe e Dona Florinda dá um tapa em Seu Madruga.
- **outra_vez:** Reações às interações estranhamente repetitivas entre Dona Florinda e Professor Girafales.

### Seu Barriga
**Métodos:**

- **responder:** Analisa uma resposta.
- **cobra_aluguel:** Cobra o aluguel de algum morador da vila.

### Girafales
**Métodos:**

- **tatatata:** Demonstra sua raiva de forma característica.

### Dona Florinda
**Métodos:**

- **punir_madruga:** Dá um tapa em Seu Madruga

### Pópis
Está presente apenas para guardar o estilo do nome de seu personagem.

---

## 📜 Depedências
Ao instalar a biblioteca, também é preciso instalar as seguintes bibliotecas para total funcionamento (essas são instaladas automaticamente com `pip` ao instalar a biblioteca):

- `emoji`
- `pygame`
- `simpleeval`
- `ascii_magic`

---

Essa biblioteca tem como objetivo principal o humor.

Sugestões são aceitas.