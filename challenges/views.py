from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.


MONTHLY_CHALLENGES = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def select_month(request):
    print(MONTHLY_CHALLENGES)
    return render(request, 'challenges/index.html', {'challenges': MONTHLY_CHALLENGES})


def monthly_challenge(request, month):
    try:
        challenge = MONTHLY_CHALLENGES[month]
        return render(request, 'challenges/challenge.html', {
            # context for template
            'text': challenge,
            'month': month,
        })
    except KeyError:
        raise Http404()


def monthly_challenge_by_month_number(request, month: int):
    months = list(MONTHLY_CHALLENGES.keys())
    try:
        redirect_month = months[month-1]
        url = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(url)
    except IndexError:
        return HttpResponseNotFound('This month is not supported!')
