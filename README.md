
# Análise de Logs

Esse projeto se encontra hospedado no Heroku com a mesma base de dados para os testes.

https://wesley-log-report.herokuapp.com/

## Passo-a-passo para executar o projeto localmente

 **Necessário ter a vm do vagrant e o script de banco de dados disponibilizado no curso**

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