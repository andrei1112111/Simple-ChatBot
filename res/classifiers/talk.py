# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator
from pandas import read_csv
import numpy as np

file = read_csv('res/classifiers/good.tsv', sep='\t')
vectorizer = TfidfVectorizer()
vectorizer.fit(file.context_0)
matrix_big = vectorizer.transform(file.context_0)

svd = TruncatedSVD(n_components=300)
svd.fit(matrix_big)
matrix_small = svd.transform(matrix_big)


def softmax(x):
    proba = np.exp(-x)
    return proba / sum(proba)


class NeighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature=1.0):
        self.k, self.temperature = k, temperature

    def fit(self, x, y):
        self.tree = BallTree(x)
        self.y = np.array(y)

    def predict(self, x):
        distances, indices = self.tree.query(x, return_distance=True, k=self.k)
        result = []
        for distance, index in zip(distances, indices):
            result.append(np.random.choice(index, p=softmax(distance * self.temperature)))
        return self.y[result]


ns = NeighborSampler()
ns.fit(matrix_small, file.reply)
pipe = make_pipeline(vectorizer, svd, ns)
