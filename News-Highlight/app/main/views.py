from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_news
from ..models import Source,news

#views
@main.route("/")
def index():
    '''
    view root page and returns the index page
    '''

    # Getting sources
    sources = get_sources('sources')

    return render_template('index.html', sources = sources)

@main.route('/news/<id>')
def articles(id):
    '''
    Veiwing of the page with news which returns the source details and the data
    '''

    news = get_news(id)
    title = f'{id}'

    return render_template('news.html', id = id, news = news)
