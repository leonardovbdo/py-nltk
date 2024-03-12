from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

LINGUAGEM = 'portuguese'

def iniciar():
    iniciado, classificacoes, palavras_de_parada = False, None, None

    try:
        palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))

        classificacoes = {}
        for (palavra, classificacao) in floresta.tagged_words():
            classificacoes[palavra.lower()] = classificacao

        iniciado = True    
    except Exception as e:
        print(f"ocorreu um erro acessando o nltk: {str(e)}")

    return iniciado, classificacoes, palavras_de_parada

def obter_tokens(texto):
    tokens = word_tokenize(texto, LINGUAGEM)

    return tokens

def imprimir_tokens(tokens):
    for token in tokens:
        print(token)
    print("\n")

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def classificar_gramaticamente(tokens, classificacao):
    for token in tokens:
        classificacao = classificacoes[token]
        print(f"{token} é um(a) {classificacao}")

TEXTO = "a verdadeira generosidade para com o futuro consiste em dar tudo ao presente" #albert camus

if __name__ == "__main__":
    iniciado, classificacoes, palavras_de_parada = iniciar()
    if iniciado:
        tokens = obter_tokens(TEXTO)
        imprimir_tokens(tokens)

        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        #imprimir_tokens(tokens)

        classificar_gramaticamente(tokens, classificacoes)