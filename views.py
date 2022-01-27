from app import app
import functions


SETTINGS_FILE = 'settings.json'
CANDIDATE_FILE = 'candidates.json'


menu = {'Главная': '/',
        'Кандидаты': '/candidate',
        'Кандидат1ы': '/candidate',
        'Задача 3': '/lesson3',
        'Задача 4': '/lesson4',
        'Авторизация': '/authorization'}



@app.route('/')
def index():
    return functions.settings_json(SETTINGS_FILE, menu)



@app.route('/candidate/', methods=["POST", "GET"])
def candidate():
    return functions.candidate_list(CANDIDATE_FILE, menu)
#
#
# @app.route('/list')
# def list():
#     return render_template('list.html')
#
#
# @app.route('/search?name=<x>')
# def search():
#     return render_template('search.html')
#
#
# @app.route('/skill/<x>')
# def skill():
#     return render_template('skill.html')


if __name__ == '__main__':
    app.run(debug=True)

