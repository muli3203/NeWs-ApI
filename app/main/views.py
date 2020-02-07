from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_news_articles
from ..models import News
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    science_news = get_news('science')

    title = 'Home - News Feed'

    return render_template('index.html', title = title, business=business_news, entertainment=entertainment_news, sports = sports_news, technology=technology_news, science=science_news )

@main.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_news_articles(news_id)
    title = f'{id}'
    return render_template('news.html',title=title, articles = articles)
