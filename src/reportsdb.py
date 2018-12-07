import datetime, psycopg2, os

# DBNAME = "forum"

# def get_posts():
#   """Return all posts from the 'database', most recent first."""
#   db = psycopg2.connect(database=DBNAME)
#   c = db.cursor()
#   c.execute("select content, time from posts order by time desc")
#   posts = c.fetchall()
#   db.close()
#   return posts
  
DATABASE_URL = os.environ['DATABASE_URL']

def get_most_popular_articles():
  """Return the three most popular articles from the 'database', most recent first."""
  
  query = """select a.title, count(l.*) as view
            from articles a, log l
            where l.path like '%' || a.slug || '%'
            group by a.slug, a.title
            order by view desc
            limit 3;"""

  db = psycopg2.connect(DATABASE_URL, sslmode='require')
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()

def get_authors_popular():
  """Add a post to the 'database' with the current timestamp."""

  query = """select aut.name, count(l.*) as view
            from articles a, log l, authors aut
            where a.author = aut.id and l.path like '%' || a.slug || '%'
            group by aut.name, a.slug
            order by view desc
            limit 3;"""

  db = psycopg2.connect(DATABASE_URL, sslmode='require')
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()

def get_greater_day_with_error():
  """Add a post to the 'database' with the current timestamp."""

  query = """select 
            to_char(date_trunc('day', time),'Month DD, YYYY') as date,
            round( (count(lg.status) * 100)::decimal / Total.total ,2) || ' %' as errors
            from log lg, (
                    select 
                    count(l.status) as total,
                    date_trunc('day', l.time) as date
                    from log l
                    where l.status like '200%'
                    group by date_trunc('day', l.time), l.status
                    order by date_trunc('day', l.time) desc ) Total
            where lg.status not like '200%' and Total.date = date_trunc('day', lg.time)
            group by date_trunc('day', lg.time), status, Total.total
            having abs( (count(lg.status) * 100)::decimal / Total.total ) >= 1
            order by round( (count(lg.status) * 100)::decimal / Total.total ,2) desc, date_trunc('day', lg.time) desc;"""

  db = psycopg2.connect(DATABASE_URL, sslmode='require')
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()
