import sys
import os
import string
import pickle


filtered_tags = set(string.punctuation)
filtered_tags.add(u'\u201d')
filtered_tags.add(u'\u201c')
filtered_tags.add(u'\u2019')
filtered_tags.add('...')
model_file = 'model.pkl'

with open(os.path.join(os.path.dirname(__file__), model_file), 'rb') as fin:
    model = pickle.load(fin)

def word2features(sent, i, is_training):
    word = sent[i][0] if is_training else sent[i]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        # 'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'word[:1].isdigit()': word[:1].isdigit(),
        'word[:3].isupper()': word[:3].isupper(),
        #       'word.indict()': word in vi_words,
        'word.isfiltered': word in filtered_tags,
        }
    if i > 0:
        word1 = sent[i - 1][0] if is_training else sent[i - 1]
        features.update({
        '-1:word.lower()': word1.lower(),
        '-1:word.istitle()': word1.istitle(),
        '-1:word[:1].isdigit()': word1[:1].isdigit(),
        '-1:word[:3].isupper()': word1[:3].isupper(),
        })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1][0] if is_training else sent[i + 1]
        features.update({
        '+1:word.lower()': word1.lower(),
        '+1:word.istitle()': word1.istitle(),
        '+1:word[:1].isdigit()': word1[:1].isdigit(),
        '+1:word.isupper()': word1.isupper(),
        })          
    else:
        features['EOS'] = True

    return features


def sent2features(sent, is_training):
    return [word2features(sent, i, is_training) for i in range(len(sent))]


def postagging(str):
    return postagging_tokens(str.split(' '))


def postagging_tokens(tokens):
    labels = model.predict([sent2features(tokens, False)])
    return tokens, labels[0]



