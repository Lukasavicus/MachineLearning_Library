import matplotlib.pyplot as plt

#function plotarDados(x, y)
def plotarDados(x, y):
	"""
	PLOTARDADOS Plota os pontos de dados x e y em uma nova figura
	   PLOTARDADOS(x,y) plota pontos de dados e seta os rotulos x e y da
	   figura com "Populacao" e "Resultado orcamentario", respectivamente.
	"""

	#figure; # abre uma nova figura em uma janela

	# ====================== ESCREVA O SEU CODIGO AQUI ======================
	# Instrucoes: Plota os dados de treinamento em um grafico usando os comandos 
	#               "figure" e "plot". Seta o rotulo dos eixos usando os comandos
	#               "xlabel" e "ylabel". Assuma que a populacao e o resultado 
	#               orcamentario sao passados nas variaveis x e y, como 
	#               argumentos desta funcao.
	#
	# Dica: Voce pode usar a opcao 'bx' do comando plot para obter simbolos que
	#       parecem xis azuis. Alem disso, voce pode aumentar o tamanhos
	#       dos simbolos usando plot(..., 'bx', 'MarkerSize', 10);

	# Cria uma nova figura
	fig = plt.figure()

	# To create separadly the plot graphic from data 'pos' and after the data 'neg'
	sub_fig = fig.add_subplot(111)

	sub_fig.scatter(x, y, c='b', marker='x')

	plt.xlabel('Populacao');
	plt.ylabel('Resultado orcamentario');

	plt.title('Plot 2D da base de dados Populacao x Resultado Orcamentario')
	#plt.legend(loc='upper left')

	#plt.scatter([plot_pos[:][0], plot_neg[:][0]], [plot_pos[:][1], plot_neg[:][1]], c=['r', 'b'])

	plt.show()
