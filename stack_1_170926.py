#!/usr/bin/python

pilha = list()

#read 15 numbers
for i in range(0, 5):

	#le um numero
	num = input("Insert your number please: ")

	#se o numero for par insira-o na pilha sequencial
	if num % 2 == 0:
		pilha.append(num)
		print ('Number {} added in position {}\n'.format(num, len(pilha)-1))

	# se o numero lido for impar retire um numero da pilha sequencial
	else:
		#dummy check if stack is empty
		if len(pilha) == 0:
			continue
		poped_num = pilha.pop()
		print ('Number {} removed in position {}\n'.format(poped_num, len(pilha)))

#Ao final, mostre a pilha
print ('RESULTADO:')
for i, elemento in enumerate(pilha):
	print ('Posicao: {} Conteudo: {}'.format(i, elemento))