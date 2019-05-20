from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source,Article

#views
@main.route("/")
def index():
    '''
    view root page and returns the index page
    '''

    # Getting sources
    sources = get_sources('sources')

    return render_template('index.html', sources = sources)

@main.route('/articles/<id>')
def articles(id):
    '''
    Veiwing of the page with articles which returns the source details and the data
    '''

    articles = get_articles(id)
    title = f'{id}'

    return render_template('articles.html', id = id, articles = articles)
