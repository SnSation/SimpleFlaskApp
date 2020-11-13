from .import app
from flask import render_template, request, redirect, url_for
import requests

from .models import User, Post

# empty route/home route
@app.route('/', methods=['GET']) # listening for activity
def index():
    users = [
        User(1, 'Derek', 'Hawkins', 'derekh@codingtemple.com'),
        User(2, 'Ripal', 'Patel', 'ripalp@codingtemple.com'),
        User(3, 'Sam', 'Davitt', 'samd@codingtemple.com')
    ]

    posts = [
        Post(1, 'This is the first blog post.'),
        Post(2, 'This is the second blog post.'),
        Post(3, 'This is the third blog post.')
    ]
    context = {
        'users': users,
        'posts': posts
    }
    return render_template('index.html', **context)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon').lower()
        pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        if pokemon_data.status_code != 200:
             context = {
                'pokemon':
                    {
                        'name' : 'Pokemon Not Found',
                        'type' : "?",
                        'height': "?",
                        'weight': "?",
                        'ability': "?",
                        'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/201.png'
                    }
             }
        else:
            pokemon_data = pokemon_data.json()
            context = {
                'pokemon':
                    {
                        'name' : pokemon_data['species']['name'].title(),
                        'type' : [x['type']['name'].title() for x in pokemon_data['types']],
                        'height':pokemon_data['height'],
                        'weight':pokemon_data['weight'],
                        'ability':pokemon_data['abilities'][0]['ability']['name'].title(),
                        'image':pokemon_data['sprites']['front_default']
                    }
            
            }
    else:
        context = {
            'pokemon': []
        }
    return render_template('projects.html', **context)

@app.route('/python', methods=['GET'])
def python():
    return render_template('python.html')

@app.route('/web_design', methods=['GET'])
def web_design():
    return render_template('web_design.html')

@app.route('/ergast', methods=['GET', 'POST'])
def ergast():
    if request.method == 'POST':
        year = request.form.get('year')
        data = requests.get(f'https://ergast.com/api/f1/{year}/5/driverStandings.json').json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        context = {
            'racers': data
        }
    else:
        context = {
            'racers': []
        }
    return render_template('ergast.html', **context)