import matplotlib.pyplot as plt

#function visualizarDados(X, Y)
def visualizarDados(X, Y):
	"""
	VIZUALIZARDADOS Plota as amostras X de acordo com as classe em Y 
	em uma nova figura
	VIZUALIZARDADOS(X,Y) plota os exemplos positivos como sinais '+' e os
	os exemplos negativos como sinais 'o'. Assume-se que X eh uma matriz
	Mx2.
	"""

	# Plota exemplos das classes positivas e negativas em um plot 2D, usando
	# a opcao 'k+' para exemplos positivos e 'ko' para os negativos

	# Encontra os indices das amostras positivas (pos) e negativas (neg)
	# pos = find(Y==1); neg = find(Y == 0);
	pos = [i for i, yi in enumerate(Y) if not yi]
	neg = [i for i, yi in enumerate(Y) if yi]


	# Plota as amostras
	#plot(X(pos, 1), X(pos, 2), 'b+','LineWidth', 2, 'MarkerSize', 7);
	#plot(X(neg, 1), X(neg, 2), 'ko', 'MarkerFaceColor', 'r', 'MarkerSize', 7);

	plot_pos = [X[i] for i in pos]
	plot_neg = [X[i] for i in neg]

	# Cria uma nova figura
	fig = plt.figure()

	# To create separadly the plot graphic from data 'pos' and after the data 'neg'
	sub_fig = fig.add_subplot(111)

	sub_fig.scatter([ppi[0] for ppi in plot_pos], [ppi[1] for ppi in plot_pos], c='r', marker='o', label = 'Iris Setosa/Virginica (+)')
	sub_fig.scatter([pni[0] for pni in plot_neg], [pni[1] for pni in plot_neg], c='b', marker='+', linewidth=2, label = 'Iris Versicolour (-)')

	plt.xlabel('Comprimento da petala (cm)');
	plt.ylabel('Largura da petala (cm)');

	plt.title('Plot 2D da base de dados Iris')
	plt.legend(loc='upper left')

	#plt.scatter([plot_pos[:][0], plot_neg[:][0]], [plot_pos[:][1], plot_neg[:][1]], c=['r', 'b'])

	plt.show()