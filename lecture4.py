import random

# Função que simula o lançamento de um dado de 6 faces
def rollDie():
    """Retorna um número inteiro aleatório entre 1 e 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

# Função para testar a rolagem do dado 'n' vezes
def testRoll(n=10):
    """Lança um dado 'n' vezes e imprime o resultado"""
    result = ''
    for i in range(n):
        result += str(rollDie())  # Concatena o resultado das jogadas
    print(result)

# Define uma semente para a geração de números aleatórios, garantindo reprodutibilidade
random.seed(0)

# Simulação para estimar a probabilidade de um evento específico em lançamentos de dados
def runSim(goal, numTrials, txt):
    """Executa uma simulação para verificar a probabilidade de obter uma sequência específica ao rolar dados"""
    total = 0  # Contador de sucessos
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())  # Concatena os valores das jogadas
        if result == goal:  # Verifica se a sequência gerada é igual ao objetivo
            total += 1
    
    # Cálculo da probabilidade teórica
    print('Probabilidade teórica de', txt, '=', round(1 / (6 ** len(goal)), 8))
    # Cálculo da probabilidade estimada pela simulação
    estProbability = round(total / numTrials, 8)
    print('Probabilidade estimada de', txt, '=', estProbability)

# Exemplo: Estimar a probabilidade de obter '11111' em 1000 testes
# runSim('11111', 1000, '11111')

# Função que verifica se há pelo menos 'numSame' pessoas fazendo aniversário no mesmo dia
def sameDate(numPeople, numSame):
    """Simula aniversários e verifica se pelo menos 'numSame' pessoas fazem aniversário no mesmo dia"""
    possibleDates = range(366)  # Lista com os 366 dias possíveis do ano (inclui anos bissextos)
    birthdays = [0] * 366  # Lista que armazena a quantidade de pessoas que fazem aniversário em cada dia
    
    # Atribui um dia de nascimento aleatório para cada pessoa
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1  # Incrementa o contador do dia escolhido
    
    # Verifica se há pelo menos 'numSame' pessoas no mesmo dia
    return max(birthdays) >= numSame

# Função que estima a probabilidade de pelo menos 'numSame' pessoas compartilharem aniversário
def birthdayProb(numPeople, numSame, numTrials):
    """Calcula a probabilidade estimada de pelo menos 'numSame' pessoas compartilharem a mesma data de nascimento"""
    numHits = 0  # Contador de casos bem-sucedidos
    for t in range(numTrials):
        if sameDate(numPeople, numSame):  # Verifica se a condição foi satisfeita
            numHits += 1
    return numHits / numTrials  # Retorna a proporção de sucessos

import math  # Importa a biblioteca para cálculos matemáticos

# Teste da probabilidade de aniversários compartilhados para diferentes números de pessoas
for numPeople in [10, 20, 40, 100]:
    print('Para', numPeople,
          'a probabilidade estimada de compartilhar aniversário é',
          birthdayProb(numPeople, 2, 10000))
    
    # Cálculo da probabilidade real baseada em teoria combinatória
    numerator = math.factorial(366)
    denom = (366 ** numPeople) * math.factorial(366 - numPeople)
    print('Probabilidade real para N =', numPeople, '=',
          1 - numerator / denom)
