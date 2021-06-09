from flask import render_template
from . import main
@main.app_errorhandler(FourOwFour)
def (error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html'),FourOwFour
