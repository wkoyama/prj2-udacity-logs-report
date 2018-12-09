#!/usr/bin/env python3

import datetime
import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']


def get_most_popular_articles():
    """Return the three most popular articles from the 'database',
       most recent first."""

    query = """select a.title, count(l.*) as view
                from articles a, log l
                where l.path like '%' || a.slug
                group by a.slug, a.title
                order by view desc
                limit 3;"""

    db = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def get_authors_popular():
    """Return the three most popular authors from the 'database',
       most recent first."""

    query = """select aut.name, count(l.*) as view
            from articles a, log l, authors aut
            where a.author = aut.id and l.path like '%' || a.slug
            group by aut.name, a.slug
            order by view desc
            limit 3;"""

    db = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def get_greater_day_with_error():
    """Return the list of days that having more than 1% of errors,
       most recent first."""

    query = """select
            to_char(date_trunc('day', time),'Month DD, YYYY') as date,
            round(
              (count(lg.status) * 100)::decimal / Total.total
              ,2) || ' %' as errors
            from log lg, (
                    select
                    count(l.status) as total,
                    date_trunc('day', l.time) as date
                    from log l
                    group by date_trunc('day', l.time)
                    order by date_trunc('day', l.time) desc ) Total
            where lg.status not like '200%'
            and Total.date = date_trunc('day', lg.time)
            group by date_trunc('day', lg.time), status, Total.total
            having abs( (count(lg.status) * 100)::decimal / Total.total ) >= 1
            order by round(
              (count(lg.status) * 100)::decimal / Total.total
              ,2) desc,
            date_trunc('day', lg.time) desc;"""

    db = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()
