function [J grad] = rnaCusto(nn_params, ...
                             input_layer_size, ...
                             hidden_layer_size, ...
                             num_labels, ...
                             X, y, lambda)
%RNACUSTO Implementa a funcao de custo para a rede neural com duas camadas
%voltada para tarefa de classificacao
%   [J grad] = RNACUSTO(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) calcula o custo e gradiente da rede neural. The
%   Os parametros da rede neural sao colocados no vetor nn_params
%   e precisam ser transformados de volta nas matrizes de peso.
%
%   input_layer_size - tamanho da camada de entrada
%   hidden_layer_size - tamanho da camada oculta
%   num_labels - numero de classes possiveis
%   lambda - parametro de regularizacao
%
%   O vetor grad de retorno contem todas as derivadas parciais
%   da rede neural.
%

% Extrai os parametros de nn_params e alimenta as variaveis Theta1 e Theta2.
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Definindo variaveis uteis
m = size(X, 1);
         
% As variaveis a seguir precisam ser retornadas corretamente
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== INSIRA SEU CODIGO AQUI ======================
% Instrucoes: Voce deve completar o codigo a partir daqui 
%               acompanhando os seguintes passos.
%
% (1): Lembre-se de transformar os rotulos Y em vetores com 10 posicoes,
%      onde tera zero em todas posicoes exceto na posicao do rotulo

domain = unique(y);
Y = zeros(size(y,1), size(domain,1));
for i=1:size(domain,1)
  Y(:,i) = (y == i);
end

% (2): Execute a etapa de feedforward e coloque o custo na variavel J.
%      Apos terminar, verifique se sua funcao de custo esta correta,
%      comparando com o custo calculado em ex05.m.

A1 = [ones(size(X,1),1) X];
A2 = sigmoide(A1 * Theta1');
A3 = sigmoide([ones(size(X,1),1) A2] * Theta2');

Jotas = zeros(size(domain,1),1);
for i=1:size(domain,1)
  Jotas(i) = sum((-Y(:,i) .* log(A3(:,i)))-((1-Y(:,i)) .* log((1- A3(:,i)))));
end

J = sum(Jotas) / m;

% (3): Implemente o algoritmo de backpropagation para calcular 
%      os gradientes e alimentar as variaveis Theta1_grad e Theta2_grad.
%      Ao terminar essa etapa, voce pode verificar se sua implementacao 
%      esta correta atraves usando a funcao verificaGradiente.

Delta1 = zeros(size(Theta1_grad));
Delta2 = zeros(size(Theta2_grad));

% ==============
  for i=1:m;
  a1 = [ones(size(X(i,:),1),1) X(i,:)];
  a2 = sigmoide(a1 * Theta1');
  a3 = sigmoide([ones(size(X(i,:),1),1) a2] * Theta2');

  delta3 = a3 - Y(i,:);

  Z2 = a1 * Theta1';
  delta2 = (delta3 * Theta2(:,2:end)) .* gradienteSigmoide(Z2);

  Delta1 = Delta1 + (delta2' * a1);
  Delta2 = Delta2 + (delta3' * [ones(size(X(i,:),1),1) a2]);
end
% ++++++++++++++

Theta1_grad = Delta1 / m;
Theta2_grad = Delta2 / m;

% (4): Implemente a regularizacao na funcao de custo e gradiente.
%

regularization_cost = (sum(sum(Theta1(:,2:end) .^ 2)) + sum(sum(Theta2(:,2:end) .^ 2)))  * (1/(2 * m));

J = J + regularization_cost;

Theta1_grad(:,2:end) = Theta1_grad(:,2:end) +  (Theta1(:,2:end) / m);
Theta2_grad(:,2:end) = Theta2_grad(:,2:end) +  (Theta2(:,2:end) / m);

% -------------------------------------------------------------

% =========================================================================

% Junta os gradientes
grad = [Theta1_grad(:) ; Theta2_grad(:)];

end
