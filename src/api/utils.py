import requests, json

def crawl_data(handle):
    crawled_data = requests.get('https://codeforces.com/api/user.info?handles='+handle).json()
    user = {}
    user['handle'] = handle
    user['rating'] = crawled_data['result'][0]['rating']
    user['rank'] = crawled_data['result'][0]['rank']
    return user

def generate_card(user):
    return true
