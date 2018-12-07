# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# 
# A buggy web service in need of a database.
import bleach
import os
from flask import Flask, request, redirect, url_for

from reportsdb import get_most_popular_articles, get_authors_popular, get_greater_day_with_error

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Relatórios</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <style>
        h1, form { 
            text-align: center; 
        }
        textarea { 
            width: 400px; 
            height: 100px; 
        }
        div.post { 
            border: 1px solid #999;
            padding: 10px 10px;
            margin: 10px 20%%; 
        }
        hr.postbound { 
            width: 50%%; 
        }
        em.date { 
            color: #999;
        }
    </style>
  </head>
  <body class="container">
    <div class="jumbotron">
        <h1>Relatórios</h1>
    </div>
    
    <nav class="nav nav-pills nav-justified">
        <a class="flex-sm-fill text-sm-center nav-item nav-link" href="/most-popular-articles">Três artigos mais populares</a>
        <a class="flex-sm-fill text-sm-center nav-item nav-link" href="/most-popular-authors">Três autores mais populares</a>
        <a class="flex-sm-fill text-sm-center nav-item nav-link" href="/greater-day-with-errors">Dias com mais de 1%% de erros</a>
    </nav>

    <main class="container mx-auto mt-4 text-center">
        <section>
            %s
        </section>
    </main>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    <script>
        $('.nav-item').on('click', function (e) {
            $('.nav-item').tab('dispose');
            $(this).tab('show');
        });
    </script>

  </body>
</html>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "" #.join(POST % (date, bleach.clean(text)) for text, date in get_posts())
  html = HTML_WRAP % posts
  return html

@app.route('/most-popular-articles', methods=['GET'])
def popular_articles():
  '''Main page of the forum.'''
  
  HEAD_POPULAR_ARTICLES = '''\
    <table class="table table-bordered">
        <thead class="thead-dark">
            <tr>
                <th scope="col">Title</th>
                <th scope="col">Views</th>
            </tr>
        </thead>
        %s
    </table>
  '''

  POPULAR_ARTICLES = '''
    <tbody>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </tbody>
  '''

  posts = "".join(POPULAR_ARTICLES % (title, view) for title, view in get_most_popular_articles())
  posts = HEAD_POPULAR_ARTICLES % posts
  html = HTML_WRAP % posts
  return html

@app.route('/most-popular-authors', methods=['GET'])
def popular_authors():
  '''Main page of the forum.'''
  
  HEAD_POPULAR_AUTHORS = '''\
    <table class="table table-bordered">
        <thead class="thead-dark">
            <tr>
                <th scope="col">Author</th>
                <th scope="col">Views</th>
            </tr>
        </thead>
        %s
    </table>
  '''

  POPULAR_AUTHORS = '''
    <tbody>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </tbody>
  '''

  posts = "".join(POPULAR_AUTHORS % (author, view) for author, view in get_authors_popular())
  posts = HEAD_POPULAR_AUTHORS % posts
  html = HTML_WRAP % posts
  return html

@app.route('/greater-day-with-errors', methods=['GET'])
def report_errors():
  '''Main page of the forum.'''
  
  HEAD_REPORT_ERRORS = '''\
    <table class="table table-bordered">
        <thead class="thead-dark">
            <tr>
                <th scope="col">Date</th>
                <th scope="col">Errors</th>
            </tr>
        </thead>
        %s
    </table>
  '''

  REPORT_ERRORS = '''
    <tbody>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </tbody>
  '''

  posts = "".join(REPORT_ERRORS % (date, errors) for date, errors in get_greater_day_with_error())
  posts = HEAD_REPORT_ERRORS % posts
  html = HTML_WRAP % posts
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8000')))

