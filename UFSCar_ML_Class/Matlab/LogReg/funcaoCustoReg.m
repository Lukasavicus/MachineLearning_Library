function [J, grad] = funcaoCustoReg(theta, X, y, lambda)
%FUNCAOCUSTOREG Calcula o custo da regressao logistica com regularizacao
%   J = FUNCAOCUSTOREG(theta, X, y, lambda) calcula o custo de usar theta 
%   como parametros da regressao logistica para ajustar os dados de X e y 

% Initializa algumas variaveis uteis
m = length(y); % numero de exemplos de treinamento

% Voce precisa retornar as seguintes variaveis corretamente
J = 0;
grad = zeros(size(theta));

% ====================== ESCREVA O SEU CODIGO AQUI ======================
% Instrucoes: Calcule o custo de uma escolha particular de theta.
%             Voce precisa armazenar o valor do custo em J.
%             Calcule as derivadas parciais e encontre o valor do gradiente
%             para o custo com relacao ao parametro theta
%
% Obs: grad deve ter a mesma dimensao de theta
%

%termo_regularizacao = (lambda / (2 * m)) * (theta' * theta);                   % Considera o theta(0)
termo_regularizacao = (lambda / (2 * m)) * ((theta' * theta) - (theta(1) ^ 2));

J = (-((1/m) * ((y' * log(sigmoid(X*theta))) + ((1 - y') * log(1 - sigmoid(X*theta))))) + termo_regularizacao);

grad = (((1/m) * (X' * (sigmoid(X * theta) - y))) + ((lambda/m) * theta));  
grad(1) = grad(1) - ((lambda/m) * theta(1));
% =============================================================

end
