#O programa deverá apresentar um menu de opções ao usuário: 
#1 –inscrição: ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados da inscrição. 
#O código do voucher deve ser preenchido automaticamente pelo sistema, e o usuário não deve ter a opção de alterar esse código
#2 – visualizar inscrição: ao selecionar essa opção, o programa deverá imprimir, na tela, para cada reserva, todos os dados dessa inscrição.
#Caso nenhuma inscrição tenha sido cadastrada ao selecionar essa opção, o programa deverá exibir a mensagem “nenhuma inscrição cadastrada”
#0 – Encerrar: ao selecionar essa opção, o programa se encerra.



op = 1 #será a opção de controle do loop, mas começa com 1

#sempre que se adicionar uma nova inscrição, cont terá incremento
#Isso garante que cada nova inscrição tenha um número único e sequencial
cont = 0
dic = {} #declarando dicionário que vai armazenar inscrição
#programa vai rodar em loop até usuário entrar com zero quando solicitado
while(op != 0):
    print('\n')
    print('---------- FICHA DE INSCRIÇÃO ----------')
    print('Escolha uma das opções abaixo\n')

    print('1 - inscrição')
    print('2 - visualizar inscrição')
    print('0 - encerrar')
    op = int(input()) #espera entrada do usuário
    #validação da entrada
    if(op > 2 or op < 0):
        print('Operação inválida')
        continue
    #se entrada do usuário for 1 vai haver solicitação dos dados
    if(op == 1):
        nome = input('Nome: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        curso = input('Curso: ')
        cont=cont+1 #contador será acrescido de 1 para gerar voucher
        #dicionário vai associar os campos com as chaves entradas pelo usuário
        dic = {'Voucher' : cont,
            'Nome' : nome,
            'Email' : email,
            'Telefone' : telefone,
            'Curso' : curso}
#se usuário escolher a op 2, vai haver verificação se existe já um dicionário criado. Em caso positive vai percorrer o dicionário existente com um for e printar os dados do último inscrito. Caso contrário vai avisar que não há inscrição.
    elif(op == 2):
        if(dic):
            for x in dic.keys():
                print(f'{x} : {dic[x]}')
        else:
            print('Nenhuma inscrição registrada')
    else:
        break
