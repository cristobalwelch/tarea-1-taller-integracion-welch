from flask import Flask, render_template, url_for, redirect, request
from methods import all_episodes, episode_information, character_name, character_information, episode_name, location_information, text_search
from searchbar import SearchForm

app = Flask(__name__)

@app.route('/')
def main_page():
    episodes = all_episodes()
    return render_template('home.html', posts=episodes)

@app.route('/episodes/<string:id>')
def episodes(id):
    episode_info = episode_information(id)
    return render_template('episode.html', information=episode_info)

@app.route('/characters/<string:id>')
def characters(id):
    character_info = character_information(id)
    return render_template('character.html', information=character_info)

@app.route('/locations/<string:id>')
def locations(id):
    location_info = location_information(id)
    return render_template('location.html', information=location_info)

@app.route('/search_results/<string:query>')
def search_results(query):
    search_info = text_search(query)
    return render_template('search.html', information=search_info)

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        print(f'Post Method IN BRAH')
        req = request.form.to_dict()
        print(f'REQ: {req}')
        search_info = text_search(req['query'])
    return render_template('search.html', information=search_info)

if __name__ == '__main__':
    app.run(debug=True)
