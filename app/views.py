
from flask import render_template
from app import app
from app.request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_sources=get_news('business')
    # tech_sources=get_news('technology')
    # sports_sources=get_news('sports')
    
    
    title='news app'
    # headlines=headlines
    return render_template('index.html',title=title,business=business_sources)

    # ,technology=tech_sources,sports=sports_sources