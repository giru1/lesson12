import json
import pprint
import requests

from flask import render_template, request


def settings_json(file, menu):
    with open(file) as f:
        settings = json.load(f)
    if settings['online']:
        status = 'Приложение работает'
        color_status = 'green'
    else:
        status = 'Приложение не работает'
        color_status = 'red'
    return render_template('index.html', status=status, color=color_status, menu=menu)


def candidate_list(file, menu):

    with open(file) as f:
        candidates = json.load(f)
    pprint.pprint((candidates))
    candidate_name = request.args.get('candidate_name')
    candidate_full_info = {}
    for candidate in candidates:
        for key, value in candidate.items():
            if value == candidate_name:
                candidate_full_info = candidate
    print(candidate_full_info)

    return render_template('candidate.html', menu=menu,
                           candidates=candidates,
                           candidate_full_info=candidate_full_info)


