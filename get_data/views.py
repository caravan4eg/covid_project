from django.views.generic import ListView

import requests
import csv
from api.models import Post, Fact, Project
from datetime import date, timedelta


def get_covid_data():
    """
    Get covid data from API https://api.covid19api.com
    """
    url = 'https://api.covid19api.com/total/dayone/country/belarus'
    response = requests.get(url)

    for item in response.json():
        covid_data = {
            'date': item['Date'],
            'confirmed': item['Confirmed'],
            'deaths': item['Deaths'],
            'recovered': item['Recovered'],
            'tests_made': 0,
        }
        print(covid_data)
        write_covid_db(covid_data)


def write_covid_db(covid_data):
    """
    Write covid data to db Fact model
    """
    covid_fact = Fact(confirmed=covid_data['confirmed'],
                      deaths=covid_data['deaths'],
                      recovered=covid_data['recovered'],
                      published_at=covid_data['date'],
                      tests_made=covid_data['tests_made']
                      )
    if (not Fact.objects.filter(published_at=covid_data['date']).exists()):
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
    """
    Get data from google news api
    Restriction - 1 month ago
    """
    d = date.today() - timedelta(days=25)
    d_str = d.isoformat() + '&'
    url = ('https://newsapi.org/v2/everything?'
           'q=беларусь%20covid&'
           'from=d_str'
           'hl=ru&'
           'gl=RU&'
           'ceid=RU:ru&'
           'sortBy=popularity&'
           'apiKey=a3b7cbcd401248e5876e1dfb8a49e27b'
           )
    r = requests.get(url)
    print(r.json())

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
        write_post_db(data)
    # return render(request, 'index.html')


def write_post_db(data):
    """
    Writes data to db Post model
    """
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
    else:
        print('It\'s OK! We have already this info!')


class HomePageView(ListView):
    """
    Get context for home.html
    """
    model = Post
    template_name = 'home.html'
    get_google_post()
    get_covid_data()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects8'] = Project.objects.all()[:9]
        context['posts8'] = Post.objects.order_by('-published_at')[:8]
        context['posts17'] = Post.objects.order_by('-published_at')[8:17]

        context['facts_last'] = Fact.objects.order_by('-published_at')[0]
        context['facts'] = Fact.objects.all()

        context['last_d'] = context['facts_last'].published_at.day
        context['last_m'] = context['facts_last'].published_at.month
        context['last_y'] = context['facts_last'].published_at.year
        context['loop_times'] = range(1, 8)
        context['i'] = 0

        return context


class BlogPageView(ListView):
    """
    Get context data for Blog page
    """
    model = Post
    context_object_name = 'posts'
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-published_at')
        return context
