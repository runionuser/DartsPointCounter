# Подсчет всех возможных комбинаций для получения currentNumber очков для игры в дартц
# Учитываются промахи, удвоения, утроения, 25 и 50
# Повторов комбинаций нет
currentNumber = int(input('Введите суммарное количество очков: '))
numbers = [(1, i) for i in range(0, 21)]
numbers2 = [(2, i) for i in range(2, 41, 2)]
numbers3 = [(3, i) for i in range(3, 61, 3)]
allNumbers = numbers + numbers2 + numbers3 + [(4, 25), (4, 50)]
output = ''
uniqueList = []
for i in allNumbers:
    for j in allNumbers:
        for k in allNumbers:
            if i[1] + j[1] + k[1] == currentNumber:
                uniqueList.append(sorted([i, j, k]))

checklist = []
for i in sorted(uniqueList):
    if i not in checklist:
        checklist.append(i)

print(f'Всего возможных комбинаций: {len(checklist)}')

# with open('output.txt', 'w') as file:
#     for i in checklist:
#         file.write('\t'.join(str(item) for item in i) + '\n')
