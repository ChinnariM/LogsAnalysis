#!/usr/bin/env python3
import psycopg2


def logs_analysis():
    
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

# Question 1
# most viewed article
    popular_article_list = """SELECT articles.title, count(log.path) as viewcount
    FROM articles, log
    WHERE log.path = concat('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY viewcount desc limit 3;"""
    c.execute(popular_article_list)
    most_viewed_article = c.fetchall()
    print("most viewed articles:")
    print("-------------------------")
    for row in most_viewed_article:
        for elem in row:
            print(elem, end=' ')
            print()
    print ('\n')
# Question 2
# Who are the most popular article authors of all time?
    popular_authors_list = """SELECT authors.name, count(log.path) as popularauthor
    FROM authors, articles, log
    WHERE status != '404 NOT FOUND'
    AND articles.author = authors.id
    AND log.path = concat('/article/', articles.slug)
    GROUP BY authors.name
    ORDER BY popularauthor desc;"""
    c.execute(popular_authors_list)
    print("most popular author:")
    print("-------------------------")
    most_popular_authors = c.fetchall()
    for row in most_popular_authors:
        for elem in row:
            print(elem, end=' ')
        print()
    print ('\n')

# Question 3
# On which days did more than 1% of requests lead to errors?
    most_errored_request_day = """SELECT erroredlog.date,
    round ((100*erroredlog.error_count/
    requestlog.request_count),2)
    as percent
    FROM erroredlog, requestlog
    WHERE erroredlog.date = requestlog.date
    AND (erroredlog.error_count) >
    (requestlog.request_count/100)
    ORDER BY percent desc LIMIT 1;"""
    c.execute(most_errored_request_day)
    print("most request Errored Day:")
    print("-------------------------")
    errored_request = c.fetchall()
    for row in errored_request:
        for elem in row:
            print(elem, end=' ')
    print()
    print ('\n')
    c.close()
    db.close()

if __name__ == '__main__':
    logs_analysis()