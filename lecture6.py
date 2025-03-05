import random, pylab

# Configura a largura da linha para os gráficos
pylab.rcParams['lines.linewidth'] = 4
# Configura o tamanho da fonte para os títulos dos eixos
pylab.rcParams['axes.titlesize'] = 20
# Configura o tamanho da fonte para os rótulos dos eixos
pylab.rcParams['axes.labelsize'] = 20
# Configura o tamanho da fonte para os números no eixo X
pylab.rcParams['xtick.labelsize'] = 16
# Configura o tamanho da fonte para os números no eixo Y
pylab.rcParams['ytick.labelsize'] = 16
# Configura o tamanho das marcas no eixo X
pylab.rcParams['xtick.major.size'] = 7
# Configura o tamanho das marcas no eixo Y
pylab.rcParams['ytick.major.size'] = 7
# Configura o tamanho dos marcadores (por exemplo, círculos representando pontos)
# Configura o número de pontos para a legenda
pylab.rcParams['legend.numpoints'] = 1

# Define a classe FairRoulette que simula a roleta justa
class FairRoulette():
    def __init__(self):
        # Cria uma lista de números de 1 a 36 representando as casas da roleta
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        # Define a bola como None inicialmente
        self.ball = None
        # Calcula as odds para as apostas
        self.pocketOdds = len(self.pockets) - 1
        
    def spin(self):
        # Escolhe aleatoriamente uma casa para a bola cair
        self.ball = random.choice(self.pockets)
        
    def betPocket(self, pocket, amt):
        # Verifica se a aposta foi vencedora (pocket == self.ball)
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds  # Retorna o ganho multiplicado pelas odds
        else:
            return -amt  # Retorna a perda do valor apostado

    def __str__(self):
        return 'Fair Roulette'  # Retorna o nome do jogo

# Função para simular várias apostas em uma roleta
def playRoulette(game, numSpins, pocket, bet, toPrint):
    totPocket = 0  # Inicializa o total de retorno
    for i in range(numSpins):
        game.spin()  # Faz a roleta girar
        totPocket += game.betPocket(pocket, bet)  # Soma o retorno da aposta
    if toPrint:
        # Imprime os resultados se toPrint for True
        print(numSpins, 'spins of', game)
        print('Expected return betting', pocket, '=', str(100 * totPocket / numSpins) + '%\n')
    return (totPocket / numSpins)  # Retorna a média do retorno por giro

# Configura a semente para gerar resultados reprodutíveis
random.seed(0)
game = FairRoulette()  # Cria uma instância de uma roleta justa
# Realiza simulações com diferentes números de giros
for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)  # Realiza a aposta na casa 2, apostando 1 unidade

# Classe que representa a roleta europeia, herda de FairRoulette
class EuRoulette(FairRoulette):
    def __init__(self):
        # Chama o construtor da classe pai
        FairRoulette.__init__(self)
        # Adiciona o '0' (casa extra) na lista de casas da roleta
        self.pockets.append('0')
        
    def __str__(self):
        return 'European Roulette'  # Retorna o nome do jogo

# Classe que representa a roleta americana, herda de EuRoulette
class AmRoulette(EuRoulette):
    def __init__(self):
        # Chama o construtor da classe pai
        EuRoulette.__init__(self)
        # Adiciona o '00' (casa extra da roleta americana) na lista de casas
        self.pockets.append('00')
        
    def __str__(self):
        return 'American Roulette'  # Retorna o nome do jogo

# Função para calcular o retorno esperado de uma aposta em diferentes jogos
def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []  # Lista para armazenar os retornos dos diferentes testes
    for t in range(numTrials):
        # Realiza várias simulações
        trialVals = playRoulette(game, trialSize, 2, 1, toPrint)
        pocketReturns.append(trialVals)  # Armazena o retorno de cada simulação
    return pocketReturns  # Retorna a lista de retornos

# Configura a semente para gerar resultados reprodutíveis
random.seed(0)
numTrials = 20  # Número de tentativas para cada jogo
resultDict = {}  # Dicionário para armazenar os resultados
games = (FairRoulette, EuRoulette, AmRoulette)  # Lista de classes de jogos

# Inicializa o dicionário de resultados para cada tipo de roleta
for G in games:
    resultDict[G().__str__()] = []

# Realiza simulações para diferentes números de giros
for numSpins in (1000, 10000, 100000, 1000000):
    print('\nSimulate', numTrials, 'trials of', numSpins, 'spins each')
    # Realiza as simulações para cada tipo de jogo
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials, numSpins, False)
        # Calcula o retorno médio das simulações
        expReturn = 100 * sum(pocketReturns) / len(pocketReturns)
        # Imprime o retorno esperado para cada tipo de roleta
        print('Exp. return for', G(), '=', str(round(expReturn, 4)) + '%')

# Função para calcular a média e o desvio padrão de uma lista de valores
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))  # Calcula a média
    tot = 0.0  # Inicializa a variável para o somatório do desvio
    for x in X:
        tot += (x - mean) ** 2  # Calcula a soma dos quadrados das diferenças
    std = (tot / len(X)) ** 0.5  # Calcula o desvio padrão
    return mean, std  # Retorna a média e o desvio padrão
