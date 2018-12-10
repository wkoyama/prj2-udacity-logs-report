--Quais são os três artigos mais populares de todos os tempos?
select a.title, count(l.*) as view
from articles a, log l 
where l.path like '%' || a.slug
group by a.slug, a.title
order by view desc
limit 3;

--Quem são os autores de artigos mais populares de todos os tempos? 
select aut.name, count(l.*) as view
from articles a, log l, authors aut
where a.author = aut.id and l.path like '%' || a.slug
group by aut.name
order by view desc
limit 3;

--Em quais dias mais de 1% das requisições resultaram em erros?
select 
to_char(date_trunc('day', time),'Month DD, YYYY') as date,
round( (count(lg.status) * 100)::decimal / Total.total ,2) || ' %' as errors
from log lg, (
        select 
        count(l.status) as total,
        date_trunc('day', l.time) as date
        from log l
        group by date_trunc('day', l.time)
        order by date_trunc('day', l.time) desc ) Total
where lg.status not like '200%' and Total.date = date_trunc('day', lg.time)
group by date_trunc('day', lg.time), status, Total.total
having abs( (count(lg.status) * 100)::decimal / Total.tonumtal ) >= 1
order by round( (count(lg.status) * 100)::decimal / Total.total ,2) desc, date_trunc('day', lg.time) desc;