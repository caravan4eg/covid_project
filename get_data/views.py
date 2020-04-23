from django.shortcuts import render
from django.http import HttpResponse
import requests
import csv
from api.models import Post


def write_csv(data):
    with open('output/post.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
                        data['source_name'],
                        data['author'],
                        data['title'],
                        data['url'],
                        data['img_url'],
                        data['published_at'],
                        # data['content'],
                        data['description'],
                        ))


def get_data(request):
    url = ('https://newsapi.org/v2/everything?'
           'q=беларусь%20covid&'
           'from=2020-04-20&'
           'hl=ru&'
           'gl=RU&'
           'ceid=RU:ru&'
           'sortBy=popularity&'
           'apiKey=a3b7cbcd401248e5876e1dfb8a49e27b'
           )
    r = requests.get(url)
    print('*'*30, r.json()['totalResults'])

    for article in r.json()['articles']:
        data = {
            'source_name': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'url': article['url'],
            'img_url': article['urlToImage'],
            'published_at': article['publishedAt'],
            'content': article['content'],
            'description': article['description']
        }
        print(data)
        write_csv(data)
        # write_db(data)
    return render(request, 'index.html')


def write_db(data):
    post = Post(source_name=data['source_name'],
                author=data['author'],
                title=data['title'],
                url=data['url'],
                img_url=data['img_url'],
                published_at=data['published_at'],
                description=data['description'])
    # check if we have already this post
    if (not Post.objects.filter(title__icontains=data['title'])) or \
            (not Post.objects.filter(url__icontains=data['url'])):
        post.save()
