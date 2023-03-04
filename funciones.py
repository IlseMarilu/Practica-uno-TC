from collections import Counter
import math

def sinacento(string):
    string = string.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')\
        .replace('à','a').replace('è','e').replace('ì','i').replace('ò','o').replace('ù','u').replace('ü','u').replace('ö','o')
    return string


def entropy(lst):
    freq = Counter(lst)
    probs = [freq[c]/len(lst) for c in freq]
    return -sum(p * math.log(p, 2) for p in probs)

def informacion(probabilidad):
    info = math.log(1/probabilidad, 2)
    return info

