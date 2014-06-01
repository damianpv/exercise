import urllib
import json
from urllib2 import urlopen
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from .models import Friend

# Home page
def home_view(request):

    return render(request, 'home/home.html')

def json_view(request):
    response_data = {
        "age": 0,
        "id": "motorola-xoom-with-wi-fi",
        "imageUrl": "img/phones/motorola-xoom-with-wi-fi.0.jpg",
        "name": "Motorola XOOM\u2122 with Wi-Fi",
        "snippet": "The Next, Next Generation\r\n\r\nExperience the future with Motorola XOOM with Wi-Fi, the world's first tablet powered by Android 3.0 (Honeycomb)."
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Profile page
def profile_view(request):

    social_user = request.user.social_auth.filter(
        provider='facebook',
        ).first()

    if social_user:
        url_friends = u'https://graph.facebook.com/{0}/' \
              u'friends?fields=id,name,location,picture' \
              u'&access_token={1}'.format(
                social_user.uid,
                social_user.extra_data['access_token'],
            )
        url_profile = u'https://graph.facebook.com/me?' \
                u'access_token={0}'.format(
                    social_user.extra_data['access_token'],
            )

        # https://graph.facebook.com/100001950528740/friends?fields=id,name,location,picture&access_token=CAADcvSC2groBAP3liS70z8KKm9DBZA1CdrKfaemU7SnqPlNS4jVxWQom8FhHNVOSPwNQypr0zUXcffG6dyjcT5OfONm29VmCh0qjIysQ4j7klPNtyZClu9pkpZAGFcuZAB8liobFgaYgz3SfCOEQkUyEGyIpPYoNc4AcNhJJROfHlgLxTaGn

        # https://graph.facebook.com/4172831015054/friends?fields=id,name,location,picture&access_token=CAAKuILeFZADcBAGEbZALpudXWSGqZAcNSe3kc0CWQrVFRvnxvE5ngl7R1hJB5OCqYspXEtmmeiZCzl2XSZAHG35MYNH040bSwST1EsodU1wNQ9DZCJabv5UWLQeLkInIwl4FkHZAXJAVzp3ol5qeOWl4y5GovAOhQH4vOliruJ4802ydBtNTVhus0ccYlrXLSEZD

        profile = json.load(urllib.urlopen(url_profile))

        friends = json.loads(urlopen(url_friends).read())

        current_user = request.user
        user = User.objects.get(pk=current_user.id)

        for friend in friends['data']:
            try:
                update = Friend.objects.get(fb_id=friend['id'], user=user)
                update.full_name = friend['name']
                update.photo = friend['picture']['data']['url']
                update.save()
            except:
                new_friend = Friend()
                new_friend.user = user
                new_friend.fb_id = friend['id']
                new_friend.full_name = friend['name']
                new_friend.photo = friend['picture']['data']['url']
                new_friend.save()

    ctx = {
        'profile': profile,
    }

    return render(request, 'home/profile.html', ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')






