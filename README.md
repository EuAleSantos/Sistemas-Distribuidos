Desenvolva um sistema em qualquer linguagem de programação que contemple a seguinte arquitetura de sistema distribuído e que seja deployado em algum serviço cloud:



Requisitos
1) Deverá ser desenvolvido um microserviço ("Microserviço 1") como cliente em que receberá requisições HTTP em um endpoint chamado "POST /pagar"

2) Deverá ser desenvolvido um microserviço ("Microserviço 2") como servidor em que receberá requisições HTTP do microserviço 1 no endpoint "POST /notificar" 

3) Este microserviço 2 deverá postar uma mensagem em um tópico de mensageria (Ex. AWS SQS ou Rabbit MQ) 

4) Ambos os serviços deverão ter um Dockerfile ou docker-compose e um arquivo README explicando como subir os serviços 

Referências

Rabbit MQ: https://engineering.3ap.ch/post/rabbitmq-vs-pubsub-part-2/

GC Rabbit MQ: https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/rabbitmq?hl=pt-br

Como subir AWS localmente: https://thomasdacosta.com.br/2023/02/16/spring-boot-localstack-usando-o-aws-sqs/ 

Documentação da localstack: https://github.com/localstack/localstack?tab=readme-ov-file

PONTOS

REQUISITO 1 = 2,5

REQUISITO 2  = 2,5

REQUISITO 3 = 2,5

REQUISITO 4 = 2,5

ENVIAR UM ÚNICO ARQUIVO .ZIP CONTENDO O README E AS APLICAÇOES BEM COMO A EXPLICAÇÃO DE COMO EXECUTAR. TAMBÉM DEVERÁ CONTER O DOCKER-COMPOSE.

Enviar atribuições
Arquivos a serem enviados
(0) arquivo(s) a ser(em) enviado(s)

Depois de carregar, você deve clicar em Enviar para concluir o envio.
