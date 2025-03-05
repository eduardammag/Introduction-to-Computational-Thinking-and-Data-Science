import random

class Food(object):
    """Representa um item de comida com nome, valor nutricional e calorias."""
    def __init__(self, n, v, w):
        self.name = n  # Nome do alimento
        self.value = v  # Valor do alimento (satisfação ou benefício)
        self.calories = w  # Custo em calorias
    
    def getValue(self):
        """Retorna o valor do alimento."""
        return self.value
    
    def getCost(self):
        """Retorna o custo do alimento em calorias."""
        return self.calories
    
    def density(self):
        """Retorna a densidade do alimento (valor por caloria)."""
        return self.getValue() / self.getCost()
    
    def __str__(self):
        """Retorna uma string representando o alimento."""
        return f"{self.name}: <{self.value}, {self.calories}>"


def buildMenu(names, values, calories):
    """Cria uma lista de objetos Food a partir de listas de nomes, valores e calorias."""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    """Implementa um algoritmo guloso para selecionar itens dentro de um limite de calorias.
       Ordena os itens com base em uma função-chave e seleciona os mais vantajosos até atingir o limite."""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)  # Ordena os itens por critério especificado
    result = []  # Lista dos itens selecionados
    totalValue, totalCost = 0.0, 0.0  # Inicializa o valor total e o custo total
    
    for item in itemsCopy:
        if (totalCost + item.getCost()) <= maxCost:  # Verifica se ainda há espaço
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    
    return (result, totalValue)  # Retorna os itens escolhidos e o valor total


def testGreedy(items, constraint, keyFunction):
    """Testa o algoritmo guloso com diferentes funções-chave."""
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)


def testGreedys(foods, maxUnits):
    """Executa o algoritmo guloso com diferentes estratégias de escolha."""
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


# Definição de itens de comida para o teste
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)  # Testa o algoritmo guloso com um limite de 750 calorias
