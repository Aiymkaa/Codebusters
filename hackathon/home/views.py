from django.shortcuts import render
from django.http import HttpResponse
import requests

ac_token="https://api.vk.com/method/friends.get?count=2&order=name&access_token=876d707ba75c8d580488e5e4d846929c562b3164f7409bec974f89084a327b6c594aec645c46dadfc9cfc&v=5.101"
method="friends.get"
r=requests.get('https://api.instagram.com/v1/users/self/?access_token=2893092593.beb5943.97ea7966157f413aa098836e3bd27b7e').json()
context={
    'name': r['data']['username'],
    'follows': r['data']['counts']['follows'],
    'followed_by': r['data']['counts']['followed_by'],
    'photo': r['data']['profile_picture']
}

def home(request):
    return render(request,'home/home.html', context)
