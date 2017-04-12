## Universidade Federal de Sao Carlos - UFSCar, Sorocaba
#
#  Disciplina: Aprendizado de Máquina
#  Prof. Tiago A. Almeida
#
#  Exercicio 2 - Regressao Linear
#
#  Instrucoes
#  ----------
#
#  Este arquivo contem o codigo que auxiliara no desenvolvimento do
#  exercicio. Voce precisara completar as seguintes funcoes:ns:
#
#     plotarDados.m
#     gradienteDescente.m
#     computarCusto.m
#
#  Voce nao podera criar nenhuma outra funcao. Apenas altere as rotinas
#  fornecidas.
#
# Dados:
#   x refere-se ao tamanho da populacao (x 10.000 pessoas)
#   y refere-se a arrecadacao (x R$ 100.000,00)
#

## Inicializacao
#clear ; close all; clc


## ======================= Parte 1: Plotando dados =======================
import csv
import plotarDados as pd
import computarCusto as cc
import gradienteDescente as gd

#fprint('Plotando dados ...\n')
print('Plotando dados ...\n')
#data = load('ex02Dados.txt')
file = open('ex02Dados.csv', 'r')
csv_reader = csv.reader(file)
list_reader = list(csv_reader)
#X = data(:, 1); y = data(:, 2)
X = [float(li[0]) for li in list_reader]
y = [float(li[1]) for li in list_reader]
#m = length(y); # numero de exemplos de treinamento
m = len(y); # numero de exemplos de treinamento

# Plotando os Dados
# VOCE PRECISA COMPLETAR O CODIGO PLOTARDADOS.M
pd.plotarDados(X, y);

#fprint('\nPrograma pausado. Pressione enter para continuar.\n\n');
#pause;


## =================== Parte 2: Gradiente descente ===================
#fprint('Calculando Gradiente Descente ...\n')
print('Calculando Gradiente Descente ...\n')

#X = [ones(m, 1), data(:,1)]; # Adicionar uma coluna de 1s em x
X = zip([1 for x in X], X) # Adicionar uma coluna de 1s em x
#theta = zeros(2, 1); # Inicializa parâmetros que serao ajustados
theta = [0, 0] # Inicializa parâmetros que serao ajustados

# Algumas configuracoes do gradiente descente
iteracoes = 1500;
alpha = 0.01;

# calcula e exibe o custo inicial
# VOCE PRECISA COMPLETAR O CODIGO COMPUTARCUSTO.M
J = cc.computarCusto(X, y, theta);
#fprint('Custo inicial: ');
print('Custo inicial: ')
#fprint('#f\n', J);
print('%f\n' % J)

# chama o metodo do gradiente descente
# VOCE PRECISA COMPLETAR O CODIGO GRADIENTEDESCENTE.M
[theta, J_historico] = gd.gradienteDescente(X, y, theta, alpha, iteracoes);

# imprime o valor de Theta
#fprint('Theta encontrado pelo gradiente descendente: ');
print('Theta encontrado pelo gradiente descendente: ')
#fprint('#f #f \n', theta(1), theta(2));
print('%f %f \n' % (theta(1), theta(2)))

# Plota o regressor linear
#hold on; # mantem o plot anterior
plot(X(:,2), X*theta, 'r-', 'LineWidth', 2);
legend('Dados de treinamento', 'Regressor linear')
#hold off

#fprint('\nPrograma pausado. Pressione enter para continuar.\n\n');
#pause;

# Plota o grafico de convergencia do gradiente descente
# O valor sempre devera ser decrescente ou igual no decorrer das iteracoes
figure;
plot(1:numel(J_historico), J_historico, 'b-', 'LineWidth', 2);
title('Convergencia do Gradiente Descendente');
xlabel('# iteracoes');
ylabel('Custo J');

# Prediz resultados orcamentarios para cidades com populacao de 40.000 e
# 70.000 habitantes
predict1 = [1, 4] *theta;
#fprint('Para populacao = 40.000, resultado orcamentario previsto = #f\n',...
print('Para populacao = 40.000, resultado orcamentario previsto = %f\n' % \
    predict1*100000)
predict2 = [1, 8] * theta;
#fprint('Para populacao = 80.000, resultado orcamentario previsto = #f\n',...
print('Para populacao = 80.000, resultado orcamentario previsto = %f\n' % \
    predict2*100000);

#fprint('\nPrograma pausado. Pressione enter para continuar.\n\n');
#pause;


## ============= Parte 3: Visualizando J(theta_0, theta_1) =============
#fprint('Visualizando J(theta_0, theta_1) ...\n')
print('Visualizando J(theta_0, theta_1) ...\n')

# Grade sobre a qual J sera calculado
theta0_vals = linspace(-10, 10, 100);
theta1_vals = linspace(-1, 4, 100);

# Initializa J_vals em uma matriz de 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals));

# Calcula todos os valores de J_vals
for i = 1:length(theta0_vals)
    for j = 1:length(theta1_vals)
	  t = [theta0_vals(i); theta1_vals(j)];    
	  J_vals(i,j) = computarCusto(X, y, t);
    end
end


# Devido a forma como meshgrid trabalha com o comando surf, eh preciso 
# transpor J_vals antes de chamar surf, ou entao os eixos serao invertidos
#J_vals = J_vals'

# Plota a superficie
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0'); ylabel('\theta_1'); zlabel('Custo J');

#fprint('\nPrograma pausado. Pressione enter para continuar.\n\n');
print('\nPrograma pausado. Pressione enter para continuar.\n\n');
pause;

#fprint('Visualizando o contorno de J(theta_0, theta_1) ...\n')
print('Visualizando o contorno de J(theta_0, theta_1) ...\n')

# Plota o contorno
figure;
# Plota J_vals como 15 linhas de contorno espacadas logaritimicamente entre
# 0.01 e 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0'); ylabel('\theta_1');
#hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);

#fprint('\nPrograma pausado. Pressione enter para continuar.\n\n');
#pause;


## ============= Parte 4: Predizendo o valor de novos dados =============

#fprint('Predizendo o valor de novos dados...\n\n')
print('Predizendo o valor de novos dados...\n\n')

popSize = input('Informe o tamanho da populacao (x 10.000) ou -1 para SAIR: ');

while (popSize ~= -1)

    predict = [1, popSize] *theta; # Faz a predicao usando theta encontrado
    
    #fprint('Para populacao = #d, resultado orcamentario previsto = #f\n\n',...
    print('Para populacao = #d, resultado orcamentario previsto = %f\n\n' % \
        popSize*10000, predict*100000);
    
    popSize = input('Informe o tamanho da populacao (x 10.000) ou -1 para SAIR: ');
end


## Finalizacao
#close all; clear all;
