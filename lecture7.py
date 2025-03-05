import random, pylab, numpy  # Importando bibliotecas necessárias para o código: random para gerar números aleatórios, pylab para gráficos, e numpy para cálculos numéricos.

#set line width
pylab.rcParams['lines.linewidth'] = 4  # Define a largura das linhas nos gráficos
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20  # Define o tamanho da fonte para os títulos dos eixos
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20  # Define o tamanho da fonte para os rótulos dos eixos
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16  # Define o tamanho da fonte para os números no eixo x
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16  # Define o tamanho da fonte para os números no eixo y
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7  # Define o tamanho das marcas principais no eixo x
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7  # Define o tamanho das marcas principais no eixo y
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1  # Define o número de pontos para a legenda

class FairRoulette():  # Classe para simular a roleta justa
    def __init__(self):  # Inicializa a classe
        self.pockets = []  # Lista para armazenar os números da roleta
        for i in range(1, 37):  # Adiciona números de 1 a 36 na roleta
            self.pockets.append(i)
        self.ball = None  # Inicializa a bola como None
        self.pocketOdds = len(self.pockets) - 1  # Apostas na roleta são baseadas no número de bolsos

    def spin(self):  # Método para girar a roleta
        self.ball = random.choice(self.pockets)  # Escolhe aleatoriamente um número da roleta

    def betPocket(self, pocket, amt):  # Método para apostar em um bolso específico
        if str(pocket) == str(self.ball):  # Se a aposta for no número sorteado
            return amt * self.pocketOdds  # Retorna o valor da aposta multiplicado pelas odds
        else:
            return -amt  # Se o número sorteado não for o apostado, retorna o valor negativo da aposta

    def __str__(self):  # Método para representar a roleta como string
        return 'Fair Roulette'  # Retorna o nome da roleta justa

def playRoulette(game, numSpins, pocket, bet, toPrint):  # Função para jogar a roleta
    totPocket = 0  # Inicializa o total acumulado de ganhos/perdas
    for i in range(numSpins):  # Loop para girar a roleta várias vezes
        game.spin()  # Gira a roleta
        totPocket += game.betPocket(pocket, bet)  # Acumula o ganho ou perda da aposta
    if toPrint:  # Se toPrint for True, imprime o resultado
        print(numSpins, 'spins of', game)  # Exibe o número de giros e o nome do jogo
        print('Expected return betting', pocket, '=',\
              str(100 * totPocket / numSpins) + '%\n')  # Exibe o retorno esperado da aposta
    return (totPocket / numSpins)  # Retorna o retorno médio

def findPocketReturn(game, numTrials, trialSize, toPrint):  # Função para simular múltiplos testes de apostas
    pocketReturns = []  # Lista para armazenar os resultados de cada teste
    for t in range(numTrials):  # Para cada teste
        trialVals = playRoulette(game, trialSize, 2, 1, toPrint)  # Joga a roleta e obtém o retorno
        pocketReturns.append(trialVals)  # Armazena o retorno de cada teste
    return pocketReturns  # Retorna todos os resultados dos testes

def getMeanAndStd(X):  # Função para calcular a média e o desvio padrão de uma lista
    mean = sum(X) / float(len(X))  # Calcula a média
    tot = 0.0  # Inicializa a soma para o cálculo da variância
    for x in X:  # Para cada valor em X
        tot += (x - mean) ** 2  # Soma a diferença ao quadrado de cada valor da média
    std = (tot / len(X)) ** 0.5  # Calcula o desvio padrão
    return mean, std  # Retorna a média e o desvio padrão

#random.seed(1)  # Define a semente para gerar números aleatórios (comentado)
#dist, numSamples = [], 1000000  # Inicializa a lista de distribuição e o número de amostras
#
#for i in range(numSamples):  # Para cada amostra
#    dist.append(random.gauss(0, 100))  # Gera uma amostra de uma distribuição normal com média 0 e desvio padrão 100
#    
#weights = [1/numSamples] * len(dist)  # Define os pesos para cada amostra
#v = pylab.hist(dist, bins=100,  # Cria o histograma da distribuição
#               weights=[1/numSamples] * len(dist))  # Normaliza o histograma

#print('Fraction within ~200 of mean =',  # Imprime a fração de valores dentro de 200 da média
#      sum(v[0][30:70]))  # Soma os valores dentro do intervalo de ~200 ao redor da média

# Definição da função gaussiana
def gaussian(x, mu, sigma):  
    factor1 = (1.0 / (sigma * ((2 * pylab.pi) ** 0.5)))  # Fator de normalização
    factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))  # Função gaussiana
    return factor1 * factor2  # Retorna o valor da função gaussiana

xVals, yVals = [], []  # Inicializa as listas para os valores de x e y
mu, sigma = 0, 1  # Define a média e o desvio padrão da distribuição normal
x = -4  # Valor inicial de x
while x <= 4:  # Para valores de x entre -4 e 4
    xVals.append(x)  # Adiciona o valor de x à lista
    yVals.append(gaussian(x, mu, sigma))  # Calcula o valor de y pela função gaussiana
    x += 0.05  # Incrementa x em 0.05

pylab.plot(xVals, yVals)  # Plota a distribuição normal
pylab.title('Normal Distribution, mu = ' + str(mu) + ', sigma = ' + str(sigma))  # Adiciona título ao gráfico

# Definição da função checkEmpirical para verificar as frações dentro de múltiplos desvios padrão
def checkEmpirical(numTrials):
    for t in range(numTrials):  # Para cada teste
        mu = random.randint(-10, 10)  # Gera um valor aleatório para a média
        sigma = random.randint(1, 10)  # Gera um valor aleatório para o desvio padrão
        print('For mu =', mu, 'and sigma =', sigma)  # Exibe os valores de mu e sigma
        for numStd in (1, 1.96, 3):  # Para diferentes números de desvios padrão
            area = scipy.integrate.quad(gaussian,  # Calcula a área sob a curva da gaussiana
                                        mu - numStd * sigma,
                                        mu + numStd * sigma,
                                        (mu, sigma))[0]  # Realiza a integração
            print(' Fraction within', numStd,  # Exibe a fração dentro do número de desvios padrão
                  'std =', round(area, 4))

#checkEmpirical(3)  # Comentado, mas seria utilizado para realizar o teste empírico

# Teste do Teorema Central do Limite
# Função para simular o lançamento de dados e calcular a média das somas
def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []  # Lista para armazenar as médias
    for i in range(numRolls // numDice):  # Para cada número de lançamentos
        vals = 0  # Inicializa a soma das faces
        for j in range(numDice):  # Para cada dado
            vals += 5 * random.random()  # Gera um valor aleatório para cada dado
        means.append(vals / float(numDice))  # Adiciona a média à lista
    pylab.hist(means, numBins, color=color, label=legend,  # Plota o histograma das médias
               weights=[1 / len(means)] * len(means),  # Normaliza os valores do histograma
               hatch=style)  # Define o estilo da marcação
    return getMeanAndStd(means)  # Retorna a média e o desvio padrão

mean, std = plotMeans(1, 1000000, 19, '1 die', 'b', '*')  # Lança 1 dado
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)  # Exibe a média e o desvio padrão
mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')  # Lança 50 dados
print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)  # Exibe a média e o desvio padrão
pylab.title('Rolling Continuous Dice')  # Título do gráfico
pylab.xlabel('Value')  # Rótulo do eixo x
pylab.ylabel('Probability')  # Rótulo do eixo y
pylab.legend()  # Exibe a legenda

# Simula o Teorema Central do Limite com o FairRoulette
numTrials = 1000000  # Número de tentativas
numSpins = 200  # Número de giros
game = FairRoulette()  # Cria uma instância de roleta justa

means = []  # Lista para armazenar as médias dos retornos
for i in range(numTrials):  # Para cada tentativa
    means.append(findPocketReturn(game, 1, numSpins, False)[0])  # Armazena o retorno médio de cada tentativa

pylab.hist(means, bins=19,  # Plota o histograma dos retornos médios
           weights=[1 / len(means)] * len(means), color='b')  # Normaliza e adiciona a cor azul
pylab.title('Fair Roulette')  # Título do gráfico
pylab.xlabel('Return')  # Rótulo do eixo x
pylab.ylabel('Probability')  # Rótulo do eixo y
pylab.show()  # Exibe o gráfico
