#Esse programa substitui as vogais do nome digitado por caracteres selecionados ao percorrer uma lista e comparar valores

#recebe o nome do usuário
nome = input('Digite um nome: ')

#passa tudo pra caixa alta para tratar melhor os dados
nome = nome.upper()

#cria uma lista com as letras do nume inserido pelo usuário
lista = []

#percorre cada item da lista (cada letra) e procura as vogais para substituir por caracteres específicos e codificar
for i in nome:
    if(i == 'A'):
        lista.append('@')
        continue
    elif(i == 'E'):
        lista.append('&')
        continue
    elif(i == 'I'):
        lista.append('!')
        continue
    elif(i == 'O'):
        lista.append('#')
        continue
    elif(i == 'U'):
        lista.append('*')
        continue
    else:
        lista.append(i)
        continue

#variável cripto recebe a lista como uma string só
cripto = "".join(lista)
print(nome)
print(cripto)
