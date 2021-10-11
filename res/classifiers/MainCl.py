from textblob.classifiers import NaiveBayesClassifier
import pickle

data = [
    ('', ''),
    ('погода', 'weather'),
    ('погода на завтра', 'weather@1'),
    ('погода в', 'weather@city'),
    ('погода на завтра в', 'weather@1@city'),
    ('погода на сегодня', 'weather'),
    ('погода на сегодня в', 'weather@city'),
    ('погода в на завтра', 'weather@1@city'),
    ('музыка', 'music'),
    ('включи музыку', 'music'),
    ('включи рок', 'music'),
    ('проиграй рок', 'music'),
    ('включи рок музыку', 'music'),
    ('привет', 'hi'),
    ('здравствуй', 'hi'),
    ('доброе утро', 'hi@0'),
    ('добрый день', 'hi@1'),
    ('добрый вечер', 'hi@2'),
    ('доброй ночи', 'hi@3')
]
cl = NaiveBayesClassifier(data)

with open('main.pickle', 'wb') as f:
    pickle.dump(cl, f)
