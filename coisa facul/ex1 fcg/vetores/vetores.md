**Descrição do exercício:**

Realize a lista de exercícios abaixo. Você pode utilizar a linguagem de programação que desejar. Ao finalizar, envie o código-fonte (arquivo(s) do código) ou um arquivo .zip contendo todos os códigos desenvolvidos.

Especifique as classes vet2, vet3 e vet4 para a representação de vetores de tamanho 2, 3 e 4, respectivamente. Cada classe deve representar um vetor com a quantidade correta de posições (2, 3 ou 4 valores numéricos).

*Essas classes deverão possuir:*

Atributos de classe do tipo float para cada posição do vetor:
x e y para vet2 (representando as duas posições do vetor);
x, y e z para vet3 (representando as três posições do vetor);
x, y, z e w para vet4 (representando as quatro posições do vetor).
Método construtor padrão, sem parâmetros, que deve inicializar (zerar) todos os valores do vetor (ou seja, todos os atributos devem começar com valor 0.0).
Método que retorna o tamanho (magnitude/comprimento) do vetor, calculado a partir dos seus valores.
Método que normaliza o vetor (ou seja, deve ajustar o vetor para que seu tamanho seja igual a 1, mantendo a direção original).
Métodos para adição e subtração de outro vetor. Esses métodos deverão:
Receber por parâmetro outro vetor do mesmo tipo da classe (por exemplo, vet2 com vet2);
Somar ou subtrair, posição por posição, os valores do vetor recebido com os valores do vetor atual.
Método para a multiplicação do vetor por um escalar recebido por parâmetro (multiplicar cada posição do vetor por esse valor numérico).
Método para a divisão do vetor por um escalar recebido por parâmetro (dividir cada posição do vetor por esse valor numérico).
Método para cálculo do produto escalar do vetor por outro vetor recebido por parâmetro. Esse método deverá:
Receber um vetor do mesmo tipo;
Calcular o produto escalar entre os dois vetores;
Retornar o resultado como um valor numérico (float).
Método que retorna uma nova cópia do vetor atual (ou seja, deve criar e retornar um novo objeto com os mesmos valores do vetor original).
Método que retorna um vetor (array/lista) de float contendo os valores atuais do vetor (na mesma ordem dos atributos).