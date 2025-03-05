import random, pylab, numpy

# Configurações para melhorar a estética do gráfico
#set line width
pylab.rcParams['lines.linewidth'] = 4  # Define a espessura das linhas no gráfico
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20  # Define o tamanho da fonte para os títulos dos eixos
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20  # Define o tamanho da fonte para os rótulos dos eixos
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16  # Define o tamanho da fonte dos números no eixo x
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16  # Define o tamanho da fonte dos números no eixo y
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7  # Define o tamanho dos "ticks" (marcadores) no eixo x
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7  # Define o tamanho dos "ticks" (marcadores) no eixo y
#set size of markers
pylab.rcParams['lines.markersize'] = 10  # Define o tamanho dos marcadores nas linhas do gráfico
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1  # Define o número de pontos a serem mostrados na legenda

# Bloco de código comentado que cria um gráfico simples de temperatura ao longo do tempo.
#temps = [98.6, 99, 99.5, 99.3, 100, 99.9, 100.5]
#times = range(3,10)
#pylab.plot(times, temps)  # Cria o gráfico com o tempo no eixo x e a temperatura no eixo y
#pylab.xlabel('Time')  # Rótulo do eixo x
#pylab.ylabel('Oral Temperature')  # Rótulo do eixo y
#pylab.title('A Bout with the Flu')  # Título do gráfico
#pylab.ylim(97,102)  # Define o intervalo do eixo y

# Configurações para o experimento de simulação
random.seed(0)  # Define a semente para o gerador de números aleatórios
numCasesPerYear = 36000  # Número de casos por ano
numYears = 3  # Número de anos
stateSize = 10000  # Tamanho do estado
communitySize = 10  # Tamanho de uma comunidade
numCommunities = stateSize // communitySize  # Número total de comunidades

# Simulação de um experimento
numTrials = 100  # Número de tentativas
numGreater = 0  # Contador para as tentativas em que a região 111 tem mais de 143 casos
for t in range(numTrials):
    locs = [0] * numCommunities  # Inicializa a lista de casos por comunidade
    for i in range(numYears * numCasesPerYear):  # Para cada caso (em 3 anos)
        locs[random.choice(range(numCommunities))] += 1  # Escolhe uma comunidade aleatória e incrementa o número de casos
    if locs[111] >= 143:  # Verifica se a comunidade 111 tem pelo menos 143 casos
        numGreater += 1  # Incrementa o contador se a condição for atendida

# Calcula a probabilidade estimada de a região 111 ter pelo menos 143 casos
prob = round(numGreater / numTrials, 4)  
print('Est. probability of region 111 having at least 143 cases =', prob)

# Bloco de código comentado que avalia a probabilidade de alguma região ter pelo menos 143 casos
#numTrials = 100
#anyRegion = 0
#for trial in range(numTrials):
#    locs = [0]*numCommunities
#    for i in range(numYears*numCasesPerYear):
#        locs[random.choice(range(numCommunities))] += 1
#    if max(locs) >= 143:  # Verifica se alguma comunidade tem pelo menos 143 casos
#        anyRegion += 1
#print(anyRegion)
#aProb = round(anyRegion / numTrials, 4)  # Calcula a probabilidade estimada
#print('Est. probability of some region having at least 143 cases =', aProb)
