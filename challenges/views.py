from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


MONTHLY_CHALLENGES = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 mins every day!',
}


def monthly_challenge(request, month):
    challenge = MONTHLY_CHALLENGES.get(month)
    if challenge is not None:
        return HttpResponse(challenge)
    return HttpResponseNotFound('This month is not supported!')
