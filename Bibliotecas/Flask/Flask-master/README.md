# Flask
Topics of flask for study

## Flask framework 


## Python Web if flask introduction

### Intro


```
pip install flask
excalidraw/ figma - design
render - deploy
planetscale - cloud
```


* from flask import Flask
* criar um objeto app = Flask()
* criar uma rota @app.route('/')
* definir uma função para rota
* verificar se name possui valor main - if __name__ == "main"
* __name__ é uma variável que guarda o local onde o app principal foi gerado
* Possível passar valores para host e debug
* host = '0.0.0.0' - rede particular deixa aplicação visível para outros dispositivos
* debug = True permite desenvolver em tempo de execução

  ### HTML, CSS e Flask

* templates folder - criar pasta do projeto que guarda a documentação em html
* static folder - criar pasta do projeto que guarda a documentação css
* render_template("nome.html") - método que retorna na função a documentação html passada

  ### dynamic data using jinja templates

* Prover argumentos para o render_template("nome.html", parâmetro = estrutura de dados)
* utilizar no html a sintaxe {{}} para passar os paramêtros do render template para o o doc.html
* lista = []; tuple =(); dict = {}... render_template("nome.html", parâmetro = lista)
```HTML
 {%for i in parâmetro%}
 <li>{i}</li>
 {% endfor %}

 {{}} >> renderizar
 {%%} >> expressões lógicas
  ```
* Reutilizar código html 

  ```HTML
  
  {% include 'nome.html' %}
  ```
* para desenvolver rotas json, utilizar jsonify - retorna os dados passados como parâmetro

### Deploying to the Cloud with Render

* web service - aplicações integradas com banco de dados
* configurações : gerar arquivo requirements.txt
* passar no deploy: start command gunicorn app:app

### Cloud MySQL Database Setup
* gerar database no planetscale
* pegar host; user e password
* passar infos para conectar no mysql workbench.
* criar e popular tabelas com comando ddl e dml

### DB Connection with SQLAlchemy 
<a href="https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples">Passo a Passo</a>

### Display DB Data on Web Page

```python 
def querydb():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        list_jobs = []
        for row in result:
            list_jobs.append(dict(row._asdict()))
        return list_jobs

@app.route("/")
def home():
    return render_template("index.html", jobs=querydb())

```

```HTML
<div class="container text-center">
<h4 class="text-center mt-4">Open Positions</h4>
</div>


{%for job in jobs%}
<ul>
    <hr>
<!--        key['value']-->
    <div class="container lh-1">
        <div class="row">
            <div class="col-md-10 ">
                <p >Job_id: {{job['id']}}</p>
            </div>
            <div class="col-md-10">
                <p>Title: {{ job['title'] }}</p>
            </div>
            <div class="col-md-10">
                <p>Location: {{ job['location'] }}</p>
            </div>
            <div class="col-md-10">
                <p>Salary: {{ job['salary'] }} R$</p>
            </div>
            <div class="col-md-2">
                <div class="well">
                <button type="button" class="btn btn-outline-primary position-absolute  translate-middle ">Apply</button>
                </div>
            </div>
        </div>
    </div>
</ul>
{%endfor%}
<div class="d-grid gap-2 d-md-flex justify-content-md-center">

    <div class="container text-center ">
  <button class=" btn btn-primary me-md-2" type="button">Contact us</button>
        <p class="mt-4">Copyright 2023, ApplyJobs</p>
</div>


</div>

```

### Dynamic Database-Driven Pages


```python
def queryjobydb(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._asdict())

@app.route("/api/jobs")
def homeJson():
    jobs = querydb()
    return jsonify(jobs)

obs. /<id> - permite passar parâmtro id para a função chamada na rota - buscada com where no db e retorna como dicionário a linha do id passado
```
