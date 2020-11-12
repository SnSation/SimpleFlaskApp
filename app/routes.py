from .import app

# empty route/home route
@app.route('/', methods=['GET']) # listening for activity
def index():
    return 'Home Page'