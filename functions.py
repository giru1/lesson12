import json
import pprint
from utils import read_file
import requests

from flask import render_template, request


def settings_json(file, menu):
    """

    :param file:
    :param menu:
    :return:
    """
    settings = read_file(file)
    if settings['online']:
        status = 'Приложение работает'
        color_status = 'green'
    else:
        status = 'Приложение не работает'
        color_status = 'red'
    return render_template('index.html', status=status, color=color_status, menu=menu)


def candidate_info(file, menu, id_candidate):
    """

    :param id_candidate:
    :param file:
    :param menu:
    :return:
    """
    candidate_full_info = {}
    for candidate in read_file(file):
        for key, value in candidate.items():
            if key == 'id' and value == int(id_candidate):
                candidate_full_info = candidate
    return render_template('candidate.html', menu=menu,
                           candidate_full_info=candidate_full_info)


def list_url(menu, file):
    """

    :param menu:
    :param file:
    :return:
    """
    candidates = read_file(file)
    # pprint.pprint((candidates))
    return render_template('list.html', menu=menu, candidates=candidates)


def search_url(menu, file):
    """

    :param menu:
    :param file:
    :return:
    """

    candidates = []
    letter = request.args.get('letter')
    if letter is None:
        letter = ''
    for candidate in read_file(file):
        for key, value in candidate.items():
            if key == 'name' and letter.lower() in value.lower():
                candidates.append(candidate)
    count = len(candidates)

    return render_template('search.html',
                           menu=menu,
                           count=count,
                           candidates=candidates,
                           letter=letter
                           )


def skill_url(menu, file):
    candidates_skill = []

    skill = request.args.get('skill')
    if skill is None:
        skill = ''
    for candidate in read_file(file):
        for key, value in candidate.items():
            if key == 'skills' and skill in value:
                candidates_skill.append(candidate)
    pprint.pprint(candidates_skill)
    count = len(candidates_skill)
    return render_template('skill.html',
                           menu=menu,
                           count=count,
                           skill=skill,
                           candidates=candidates_skill)
