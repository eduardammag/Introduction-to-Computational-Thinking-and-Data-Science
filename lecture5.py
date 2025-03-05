import random, pylab

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1

# Classe Location: Representa uma localização no plano com coordenadas x e y
class Location(object):
    def __init__(self, x, y):
        """x e y são números representando as coordenadas"""
        self.x = x
        self.y = y

    # Método para mover a localização
    def move(self, deltaX, deltaY):
        """deltaX e deltaY são números que alteram as coordenadas"""
        return Location(self.x + deltaX, self.y + deltaY)

    # Método para obter a coordenada x
    def getX(self):
        return self.x

    # Método para obter a coordenada y
    def getY(self):
        return self.y

    # Método para calcular a distância de outra localização
    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    # Representação em string da localização
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

# Classe Field: Representa o campo onde os bêbados podem se mover
class Field(object):
    def __init__(self):
        self.drunks = {}  # Dicionário para armazenar os bêbados e suas localizações
        
    # Método para adicionar um bêbado no campo
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')  # Garante que não haverá duplicação de bêbados
        else:
            self.drunks[drunk] = loc
            
    # Método para mover um bêbado no campo
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')  # Verifica se o bêbado está no campo
        xDist, yDist = drunk.takeStep()  # Obtém o passo a ser dado pelo bêbado
        # Atualiza a localização do bêbado usando o método move
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
        
    # Método para obter a localização de um bêbado
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')  # Verifica se o bêbado está no campo
        return self.drunks[drunk]

# Classe Drunk: Representa um bêbado com nome
class Drunk(object):
    def __init__(self, name = None):
        """Assume que name é uma string"""
        self.name = name

    # Representação em string do bêbado
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

# Classe UsualDrunk: Representa um bêbado que se move aleatoriamente em quatro direções
class UsualDrunk(Drunk):
    def takeStep(self):
        # O bêbado pode escolher entre quatro direções (cima, baixo, direita, esquerda)
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

# Classe MasochistDrunk: Representa um bêbado que se move de maneira diferente
class MasochistDrunk(Drunk):
    def takeStep(self):
        # O bêbado pode escolher entre quatro direções com distâncias diferentes
        stepChoices = [(0.0,1.1), (0.0,-0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

# Função walk: Realiza uma caminhada de um bêbado e retorna a distância final
def walk(f, d, numSteps):
    """Assume: f é um Field, d é um Drunk em f, e numSteps é um inteiro >= 0.
       Move d numSteps vezes e retorna a distância entre o local final e o início"""
    start = f.getLoc(d)  # Obtém a localização inicial
    for s in range(numSteps):  # Move o bêbado numSteps vezes
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))  # Retorna a distância entre o ponto de partida e o final
    
# Função simWalks: Simula múltiplas caminhadas e retorna as distâncias finais
def simWalks(numSteps, numTrials, dClass):
    """Assume numSteps um inteiro >= 0, numTrials um inteiro > 0, dClass uma subclasse de Drunk
       Simula numTrials caminhadas de numSteps passos cada.
       Retorna uma lista das distâncias finais para cada tentativa"""
    Homer = dClass('Homer')
    origin = Location(0, 0)  # Posição inicial
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)  # Adiciona o bêbado ao campo
        distances.append(round(walk(f, Homer, numSteps), 1))  # Realiza a caminhada e armazena a distância
    return distances

# Função drunkTest: Testa várias caminhadas para um tipo específico de bêbado
def drunkTest(walkLengths, numTrials, dClass):
    """Assume walkLengths uma sequência de inteiros >= 0
         numTrials um inteiro > 0, dClass uma subclasse de Drunk
       Para cada número de passos em walkLengths, executa simWalks com numTrials caminhadas e imprime os resultados"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))
        
# Função simAll: Executa simulações para vários tipos de bêbados e tamanhos de caminhada
def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()  # Escolhe o estilo de gráfico
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)  # Plota os resultados

    # Configurações do gráfico
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')

# Função simDrunk: Simula as caminhadas de um bêbado e retorna a distância média
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / len(trials)
        meanDistances.append(mean)
    return meanDistances

# Função OddField: Um campo com buracos (wormholes) que transportam o bêbado para outra posição
class OddField(Field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc  # Cria buracos no campo

    # Método moveDrunk sobrescrito para movimentar o bêbado, considerando os buracos
    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]  # Transporta o bêbado para um novo local se cair em um buraco
            
# Função traceWalk: Realiza a caminhada considerando o campo com buracos e plota os resultados
def traceWalk(fieldKinds, numSteps):
    styleChoice = styleIterator(('b+', 'r^', 'ko'))
    for fClass in fieldKinds:
        d = UsualDrunk()
        f = fClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))  # Adiciona as localizações durante a caminhada
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)  # Plota o caminho

    # Configurações do gráfico
    pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'best')
