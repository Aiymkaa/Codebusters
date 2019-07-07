from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .forms import HomeForm

f="https://api.vk.com/method/"
e="&access_token=96d6bbee0c4494772c06e61b6600138a1c59cee164d8748166c45f521b37e35e59bd804be3e18dab7adae&v=5.101"

id='1'
posts=requests.get(f+'wall.get?owner_id='+id+e).json()
profile_photo=requests.get(f+'photos.get?owner_id='+id+'&album_id=profile'+e).json()
profile=requests.get(f+'users.get?user_ids='+id+e).json()
posts_array=posts['response']['items']
post_all_likes=0
for i in posts_array:
    post_all_likes+=i['likes']['count']
post_all_reposts=0
for i in posts_array:
    post_all_likes+=i['reposts']['count']

friends=requests.get(f+'friends.get?fields=sex,country&user_id='+id+e).json()
male_friends=0
female_friends=0

for i in friends['response']['items']:
    if i['sex']==1:
        female_friends+=1
    else:
        male_friends+=1


col_countries=dict()

for i in friends['response']['items']:
    if 'country' in i:
        if i['country']['title'] in col_countries:
            col_countries[i['country']['title']]+=1
        else:
            col_countries[i['country']['title']]=1
online=0
offline=0

for i in friends['response']['items']:
    if i['online']==1:
        online+=1
    else:
        offline+=1
context={
    'posts_size': posts['response']['count'],
    'profile_photo': profile_photo['response']['items'][0]['sizes'][0]['url'],
    'first_name': profile['response'][0]['first_name'],
    'last_name': profile['response'][0]['last_name'],
    'post_all_likes': post_all_likes,
    'average_posts_likes': int(post_all_likes/posts['response']['count']),
    'average_posts_reposts': int(post_all_reposts/posts['response']['count']),
    'number_of_friends': friends['response']['count'],
    'male_friends': male_friends,
    'female_friends': female_friends,
    'col_countries': col_countries,
    'online': online,
    'offline': offline,
    'id': id
}
def home(request):
    if request.method == 'POST':
        form=HomeForm(request.POST)
        if form.is_valid():
            global id,context,posts,profile_photo,profile,posts_array,post_all_likes,post_all_reposts,friends,male_friends,female_friends,col_countries,online,offline,context
            id = form.cleaned_data.get('post')
            context['id']=id
            posts=requests.get(f+'wall.get?owner_id='+id+e).json()
            profile_photo=requests.get(f+'photos.get?owner_id='+id+'&album_id=profile'+e).json()
            profile=requests.get(f+'users.get?user_ids='+id+e).json()
            posts_array=posts['response']['items']
            post_all_likes=0
            for i in posts_array:
                post_all_likes+=i['likes']['count']
            post_all_reposts=0
            for i in posts_array:
                post_all_likes+=i['reposts']['count']

            friends=requests.get(f+'friends.get?fields=sex,country&user_id='+id+e).json()
            male_friends=0
            female_friends=0

            for i in friends['response']['items']:
                if i['sex']==1:
                    female_friends+=1
                else:
                    male_friends+=1


            col_countries=dict()

            for i in friends['response']['items']:
                if 'country' in i:
                    if i['country']['title'] in col_countries:
                        col_countries[i['country']['title']]+=1
                    else:
                        col_countries[i['country']['title']]=1
            online=0
            offline=0

            for i in friends['response']['items']:
                if i['online']==1:
                    online+=1
                else:
                    offline+=1
            context={
                'posts_size': posts['response']['count'],
                'profile_photo': profile_photo['response']['items'][0]['sizes'][0]['url'],
                'first_name': profile['response'][0]['first_name'],
                'last_name': profile['response'][0]['last_name'],
                'post_all_likes': post_all_likes,
                'average_posts_likes': int(post_all_likes/posts['response']['count']),
                'average_posts_reposts': int(post_all_reposts/posts['response']['count']),
                'number_of_friends': friends['response']['count'],
                'male_friends': male_friends,
                'female_friends': female_friends,
                'col_countries': col_countries,
                'online': online,
                'offline': offline,
                'id': id
            }
            return redirect('about')
    else:
        form=HomeForm()
    context['form']=form
    return render(request,'home/home.html', context)

def about(request):

    return render(request,'home/proba.html', context)
