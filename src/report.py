#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import reportsdb


def popular_articles():
    #     '''Invoke popular articles.'''
    header = ["Titulo", "Visualizações"]
    data = reportsdb.get_most_popular_articles()
    drawTable(header, data)


def popular_authors():
    #     '''Invoke the popular authors.'''
    header = ["Autor", "Visualizações"]
    data = reportsdb.get_authors_popular()
    drawTable(header, data)


def report_errors():
    #     '''Find the das with more than 1% of errors'''
    header = ["Data", "Erros"]
    data = reportsdb.get_greater_day_with_error()
    drawTable(header, data)


def drawTable(header, data):
    print("\n__________________________________________________")
    print("{0:^{fill}} | {1:^}".format(*header, fill=33))
    print("__________________________________________________")
    for row in data:
        print("{0:<{fill}} | {1:^}".format(*row, fill=33))
    print("__________________________________|_______________")


popular_articles()
popular_authors()
report_errors()
