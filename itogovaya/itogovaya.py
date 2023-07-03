import requests

def isMagnes():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "magnes".encode() in res.content

def isGenres():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "genres".encode() in res.content

def isDimensions():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "dimensions".encode() in res.content

def isTiny():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "tiny".encode() in res.content

def isCoul():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "coul".encode() in res.content

print("Is Magnes?", isMagnes())

print("Is Genres?", isGenres())

print("Is Dimensions?", isDimensions())

print("Is Tiny?", isTiny())

print("Is Coul?", isCoul())



