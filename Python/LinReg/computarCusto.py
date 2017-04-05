import numpy as np
#function J = computarCusto(X, y, theta)
def computarCusto(X, y, theta):
"""
COMPUTARCUSTO Calcula o custo da regressao linear
   J = COMPUTARCUSTO(X, y, theta) calcula o custo de usar theta como 
   parametro da regressao linear para ajustar os dados de X e y
"""

# Initializa algumas variaveis uteis
#m = length(y); # numero de exemplos de treinamento
	m = len(y); # numero de exemplos de treinamento

# Voce precisa retornar a seguinte variavel corretamente
	J = 0;

# ====================== ESCREVA O SEU CODIGO AQUI ======================
# Instrucoes: Calcule o custo de uma escolha particular de theta.
#             Voce precisa armazenar o valor do custo em J.

	#Parto do principio que a matriz X ja contem o vetor afim

	# X -> Matriz de valores das features das amostras [m x n]
	# Theta -> Vetor de thetas [1 x n]
	# Y -> Vetor de valores reais [m x 1]

	X_times_T = [sum(map(lambda m1, m2: m1 * m2, theta, x)) for x in X]
	XT_minus_sqrd_Y = sum(map(lambda m1, m2: (m1 - m2) ** 2, X_times_T, y))
	J = XT_minus_sqrd_Y / float(2*m)