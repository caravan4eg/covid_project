from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

import requests
import csv
from api.models import Post, Fact, Project


def get_covid_data():
    url = 'https://api.covid19api.com/total/dayone/country/belarus'
    response = requests.get(url)

    for item in response.json():
        covid_data = {
            'date': item['Date'],
            'confirmed': item['Confirmed'],
            'deaths': item['Deaths'],
            'recovered': item['Recovered']
        }
        print(covid_data)
        write_covid_db(covid_data)


def write_covid_db(covid_data):
    covid_fact = Fact(country='Беларусь',
                      confirmed=covid_data['confirmed'],
                      deaths=covid_data['deaths'],
                      recovered=covid_data['recovered'],
                      published_at=covid_data['date']
                      )
    if (not Fact.objects.filter(published_at=covid_data['date'])):
        covid_fact.save()
    else:
        print('It\'s OK! We have already this record!')


def write_google_post_csv(data):
    with open('output/post.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
                        data['source_name'],
                        data['author'],
                        data['title'],
                        data['url'],
                        data['img_main_url'],
                        data['published_at'],
                        # data['content'],
                        data['description'],
                        ))


def get_google_post():
    url = ('https://newsapi.org/v2/everything?'
           'q=беларусь%20covid&'
           'from=2020-04-01&'
           'hl=ru&'
           'gl=RU&'
           'ceid=RU:ru&'
           'sortBy=popularity&'
           'apiKey=a3b7cbcd401248e5876e1dfb8a49e27b'
           )
    r = requests.get(url)

    for article in r.json()['articles']:
        data = {
            'source_name': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'url': article['url'],
            'img_main_url': article['urlToImage'],
            'published_at': article['publishedAt'],
            'content': article['content'],
            'description': article['description']
        }
        print(data)
        write_post_db(data)
    # return render(request, 'index.html')


def write_post_db(data):
    post = Post(source_name=data['source_name'],
                author=data['author'],
                title=data['title'],
                url=data['url'],
                img_main_url=data['img_main_url'],
                published_at=data['published_at'],
                description=data['description'])
    # check if we have already this post
    if (not Post.objects.filter(title__icontains=data['title'])) or \
            (not Post.objects.filter(url__icontains=data['url'])):
        post.save()
    else:
        print('It\'s OK! We have already this info!')


class HomePageView(ListView):
    model = Project
    # context_object_name = 'posts'
    template_name = 'home.html'
    # get new posts from News Google API
    ##get_google_post()
    # get new covid data from https://api.covid19api.com
    ##get_covid_data()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects8'] = Project.objects.all()[:8]
        context['posts8'] = Post.objects.order_by('-published_at')[:7]
        context['facts_last'] = Fact.objects.order_by('-measured_at')[0]

        context['last_d'] = context['facts_last'].measured_at.day
        context['last_m'] = context['facts_last'].measured_at.month
        context['last_y'] = context['facts_last'].measured_at.year
        context['loop_times'] = range(1, 8)
        context['i'] = 0

        return context


def demo(request):
    return render(request, 'demo-medical.html')
