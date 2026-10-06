#9 - Crie um programa com uma variável número qualquer. Depois, crie uma variável chute pedindo para o usuário  digitar um numero. Na sequencia, crie uma condição para saber se o chute é igual a variável. Caso seja igual exiba uma mensagem "Você acertou" , se for diferente exiba a a mensagem "Você errou"
#num = 7
#penalti = int(input("Digite um número: "))
#if penalti == num:
    #print("Acerto miseravi")
#else:
    #print("Erroooooooooooou")

#num = 10 
#penalti = int(input('Digite um número'))
#if penalti == num:
    #print ('acerto miseravi')
#elif penalti > num:
    #print ('erooooooooooou longe')
#elif penalti < num:
    #print ('erooooooooooou tá humilde hein')

#num = 30

#while num <= 10:
    #print(num)
    #num = num + 1
    #num +=1

num_secreto = 1200

total_tentativas = 5
while total_tentativas > 0 :
    chute = int(input('Digite seu número'))
    print(f'Você digitou :{chute}')
    num_certo = num_secreto == chute
    num_maior = chute > num_secreto
    num_menor = chute < num_secreto

    if num_certo:
        print('acerto mizeravi')
        break
    elif num_maior:
        print('erooooooooou longe')
    else:
        print('erooooooooou tá humilde hein')

    total_tentativas = total_tentativas - 1
else:
    print(f'Número de tentativas excedidas. O número secreto era:{num_secreto}')