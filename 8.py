

list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))
print('Уникальные в первом множестве:',set(list_1),'.')
print('Уникальные во втором множестве:',set(list_2),'.')
set_union = set.union(set(list_1), set(list_2))
set_interseption = set.intersection(set(list_1), set(list_2))
print('Уникальные для объединения этих списков', set_union ,'.')
print('Содержащиеся в двух списках', set_interseption ,'.')

