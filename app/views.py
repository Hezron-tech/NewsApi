
from flask import render_template
from app import app
from app.request import get_news,article_source,get_category

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_sources=get_news('business')
    tech_sources=get_news('technology')
    sports_sources=get_news('sports')
    
    
    title='news app'
    # headlines=headlines
    return render_template('index.html',title=title,business=business_sources,technology=tech_sources,sports=sports_sources)

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )

@app.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)    