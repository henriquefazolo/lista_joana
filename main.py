'''
Considere a lista de compras de Joana e faça o que se pede:

lista_de_compras = [“batata”, “arroz”, “feijão”, “macarrão”, “detergente”]

Mostre na tela o tamanho da lista.
Joana descobriu que não precisa de arroz, mas sim de jiló. Realize a substituição do item.
Joana encontrou um detergente na sua cozinha, elimine o item.
Joana se lembrou que precisa de abacates. Realize a inserção do item na lista
Mostre todos os itens de forma individual utilizando um comando FOR.

'''

lista_de_compras = ['batata', 'arroz', 'feijão', 'macarrão', 'detergente']
print(f'Tamanho da lista : {len(lista_de_compras)} itens.')

lista_de_compras = ['jiló' if value == 'arroz' else value for value in lista_de_compras]

lista_de_compras.remove('detergente')

lista_de_compras.append('abacates')

for i in lista_de_compras:
    print(i)



