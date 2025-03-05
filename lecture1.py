class Food(object):  # Define a classe Food para representar um alimento
    def __init__(self, n, v, w):  # Construtor da classe, inicializa nome, valor e calorias
        self.name = n  # Nome do alimento
        self.value = v  # Valor associado ao alimento (por exemplo, satisfação)
        self.calories = w  # Custo do alimento em calorias
    
    def getValue(self):  # Retorna o valor do alimento
        return self.value
    
    def getCost(self):  # Retorna o custo em calorias do alimento
        return self.calories
    
    def density(self):  # Retorna a densidade do alimento (valor/calorias)
        return self.getValue() / self.getCost()
    
    def __str__(self):  # Representação em string do alimento
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    """Cria uma lista de objetos Food a partir de listas de nomes, valores e calorias.
       names: lista de strings com os nomes dos alimentos
       values: lista de valores numéricos
       calories: lista de custos em calorias
       Retorna uma lista de objetos Food."""
    menu = []  # Inicializa uma lista vazia para armazenar os alimentos
    for i in range(len(values)):  # Itera sobre os índices das listas
        menu.append(Food(names[i], values[i], calories[i]))  # Cria um objeto Food e adiciona à lista
    return menu  # Retorna a lista de alimentos


def greedy(items, maxCost, keyFunction):
    """Algoritmo guloso para selecionar os melhores alimentos dentro de uma restrição de custo.
       items: lista de objetos Food
       maxCost: limite máximo de calorias
       keyFunction: função usada para ordenar os alimentos
       Retorna uma tupla (lista de itens selecionados, valor total dos itens)."""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)  # Ordena os itens com base na keyFunction (maior primeiro)
    result = []  # Lista para armazenar os itens selecionados
    totalValue, totalCost = 0.0, 0.0  # Inicializa valor e custo totais
    
    for i in range(len(itemsCopy)):  # Itera sobre os itens ordenados
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:  # Verifica se pode adicionar o item sem ultrapassar o limite
            result.append(itemsCopy[i])  # Adiciona o item à lista de escolhidos
            totalCost += itemsCopy[i].getCost()  # Atualiza o custo total
            totalValue += itemsCopy[i].getValue()  # Atualiza o valor total
    
    return (result, totalValue)  # Retorna a lista de itens escolhidos e o valor total acumulado


def testGreedy(items, constraint, keyFunction):
    """Testa o algoritmo guloso com uma determinada função chave.
       items: lista de objetos Food
       constraint: limite máximo de calorias
       keyFunction: critério de ordenação"""
    taken, val = greedy(items, constraint, keyFunction)  # Chama o algoritmo guloso
    print('Total value of items taken =', val)  # Exibe o valor total obtido
    for item in taken:  # Exibe cada item escolhido
        print('   ', item)


def testGreedys(foods, maxUnits):
    """Executa testes do algoritmo guloso com diferentes estratégias de ordenação.
       foods: lista de objetos Food
       maxUnits: limite máximo de calorias."""
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)  # Ordenação por valor absoluto
    
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1 / x.getCost())  # Ordenação por menor custo (invertido)
    
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)  # Ordenação por densidade (valor/calorias)

# Listas de alimentos, valores e calorias
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]  # Lista de valores dos alimentos
calories = [123, 154, 258, 354, 365, 150, 95, 195]  # Lista de calorias dos alimentos

foods = buildMenu(names, values, calories)  # Cria a lista de objetos Food

# Testa o algoritmo guloso com diferentes estratégias de ordenação
testGreedys(foods, 1000)
