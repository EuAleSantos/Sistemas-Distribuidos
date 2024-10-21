Tema
Você precisa garantir a sincronização entre as threads; crie um programa que simula uma conta bancária em
Java acessada por diferentes usuários (threads). O programa deve: criar múltiplas threads, onde cada thread representa um usuário realizado uma operação na conta bancária (saque ou deposito); implemente sincronização de threads para evitar que duas threads acessem e modifiquem o saldo da conta simultaneamente. Dica: synchronized / loc
Passos.
Criar uma classe ContaBancaria com métodos para sacar e depositar. Use um controlador de sincronização para garantir que apenas uma thread acesse o saldo da conta por vez. As threads devem realizar operações aleatórias (depósitos ou saques) em um intervalo de tempo. Ex: Thread 1 deposita R$100,00. Thread 2 saca R$50,00. Thread 3 deposita R$200,00. Thread 4 saca R$300,00.
Simule uma operação em um arquivo, o arquivo deverá ser lido e cada thread processará uma linha dele. Exemplo de arquivo:
operacao, valor
depositar, 200
sacar, 100
depositar, 300
No fim, apresente o resultado de todas as operações.
Exemplo de arquivo de entrada
operacao,valor
depositar,345
sacar,-678
depositar,999
sacar,-999
depositar,0
sacar,123
depositar,-456
sacar,789
depositar,-234
sacar,567
depositar,-890
sacar,321
depositar,-654
sacar,987
depositar,-111
sacar,222
depositar,-333
sacar,444
depositar,-555
sacar,666
