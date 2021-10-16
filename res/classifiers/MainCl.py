# -*- coding: utf-8 -*-
from fuzzywuzzy.process import extract as find

music = [{
    'text': [
        'музыка',
        'включи музыку'
    ],
    'label': 'музыка'
}]

weather = [{
    'text': [
        'погода',
        'погода на сегодня'
    ],
    'label': 'погода'
}, {
    'text': [
        'погода на завтра'
    ],
    'label': 'погода на завтра'
}, {
    'text': [
        'погода в ',
        'погода на сегодня в ',
        'погода в на'
    ],
    'label': 'погода в городе'
}, {
    'text': [
        'погода на завтра в ',
        'погода в коробке на завтра'
    ],
    'label': 'погода в городе на завтра'
}]
intents = [music, weather]


def classify(text):
    res = []
    for intent in intents:
        for unit in intent:
            res.append((find(text, [i for i in unit['text'] if
                                    len(i.split()) == len(text.split()) or len(i.split()) + 1 == len(text.split()) or len(
                                        i.split()) - 1 == len(text.split())], limit=1), unit['label']))

    print(res)
    res = [i for i in res if i[0] != []]
    res = max(res, key=lambda x: x[0][0][1])
    res = res[1] if int(res[0][0][1]) >= 70 else 'False'
    return res
