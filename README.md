
# Análise de Logs

## Descrição do Projeto

O projeto tem como intuito construir uma ferramenta interna de relatórios que usará informações do banco de dados para descobrir de que tipo de artigos os leitores do site de jornal mais gostam.
O projeto consiste de uma camada de banco de dados onde é feito as queries. A camada (report.py) que chama as funções de banco de dados obtém o resultado e imprime no console do programa o resultado.

Esse projeto se encontra hospedado no Heroku com a mesma base de dados para os testes e em uma versão web.

https://wesley-log-report.herokuapp.com/

## Pré-Requisitos

**Necessário ter a vm do vagrant e o script de banco de dados disponibilizado no curso**

**Para a configuração do ambiente em que esse projeto roda, seguir instruções nesse link: (Créditos a Udacity)**

1. Estamos usando ferramentas chamadas [Vagrant](https://www.vagrantup.com/) e [VirtualBox](https://www.virtualbox.org/wiki/Downloads) para instalar e gerenciar a VM.

    https://classroom.udacity.com/nanodegrees/nd004-br/parts/302d2209-30c1-4b9e-8615-2a1f4a5ee7c6/modules/e4147fc0-3658-48bf-8a6c-542fa272d0cd/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0

2. Baixar e extrair o diretório de configuração da VM:

    https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip

3. Baixar e extrair o arquivo de dados que será populado a base na pasta vagrant dentro do diretório de configuração:

    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Após concluído a instalação do Vagrant, VirtualBox do passo 1, a extração do arquivo do passo 2 e baixado o arquivo de dados.

- Entrar na VM com `vagrant ssh`
- Trocar para diretório /vagrant
- Executar `psql -d news -f newsdata.sql`. Este comando populará e montará a base de dados.

## Passo-a-passo para executar o projeto localmente

- Entrar na pasta do vagrant
- Baixar o projeto  
`git clone https://github.com/wkoyama/prj3-udacity-logs-report.git`
- Subir a VM com `vagrant up`
- Acessar a vm com `vagrant ssh`
- Trocar para diretório `cd /vagrant/prj3-udacity-logs-report`
- Executar o programa com `python src/report.py`

## Observação

O projeto está configurado para executar no ambiente de produção.
Para executar local é necessário alterar algumas coisas no arquivo `src/reportsdb.py`:

Trocar a linha
```DATABASE_URL = os.environ['DATABASE_URL']```
para 
```DATABASE_URL = "news"```

E as chamadas 
```db = psycopg2.connect(DATABASE_URL, sslmode='require')```
para 
```db = psycopg2.connect(database=DATABASE_URL)```

### Arquivo SQL

O arquivo `queries de projeto de log.sql` demonstra as queries usadas no programa com suas respectivas perguntas. Para essa V1 optei por uma implementação sem view e funcional. Acredito que com a View deverá melhorar um pouco mais a performance.