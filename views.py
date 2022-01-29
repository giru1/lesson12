from app import app, render_template
import functions


SETTINGS_FILE = 'static/settings.json'
CANDIDATE_FILE = 'static/candidates.json'


menu = {'Главная': '/',
        # 'Кандидаты': '/candidate/',
        'Список': '/list',
        'Поиск': '/search',
        'Скилы': '/skill'}


@app.route('/')
def index():
    return functions.settings_json(SETTINGS_FILE, menu)


@app.route('/candidate/<id_candidate>', methods=["POST", "GET"])
def candidate(id_candidate):
    return functions.candidate_info(CANDIDATE_FILE, menu, id_candidate)


@app.route('/list')
def list_candidates():
    return functions.list_url(menu, CANDIDATE_FILE)


@app.route('/search/')
def search():
    return functions.search_url(menu, CANDIDATE_FILE)



@app.route('/skill')
def skill():
    return functions.skill_url(menu, CANDIDATE_FILE)

