from django.shortcuts import render, render_to_response, RequestContext, HttpResponsePermanentRedirect
from django.utils import simplejson
import operator
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your views here.

json_data = open(os.path.join(os.path.dirname(BASE_DIR), "static", "data", "movies.json"))
obj = simplejson.load(json_data)
movies = obj["movies"]
context = {'movies': movies }
    
def home(request):
    return render_to_response("landing_page.html", context, context_instance=RequestContext(request))

def details(request):
    return render_to_response("movie_details.html", context, context_instance=RequestContext(request))

def popularity(request):
    ordered = sorted(movies, key=operator.itemgetter('ratings'), reverse=True)
    context = {'movies': ordered }
    return render_to_response("landing_page.html", context, context_instance=RequestContext(request))

def freshness(request):
    ordered = sorted(movies, key=operator.itemgetter('release_dates'), reverse=True)
    context = {'movies': ordered }
    return render_to_response("landing_page.html", context, context_instance=RequestContext(request))

def MPAA(request):
    ordered = sorted(movies, key=operator.itemgetter('mpaa_rating'))
    context = {'movies': ordered }
    return render_to_response("landing_page.html", context, context_instance=RequestContext(request))