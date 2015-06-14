from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
#from django.db.models import get_app, get_models, get_model for 1.6, deprecated in 1.7
from django.apps import apps
from wine.models import *

# Create your views here.

def home(request):
    return render_to_response('base.html',)
                              
def default(request):
    return HttpResponseRedirect('/spiritwine/home/')
def getAllModels():
    app = apps.get_app('wine')
    models = apps.get_models(app)
    return models
def getModels(request, wineType):
    wine_classes = []
    for model in getAllModels():
        if (model._meta.verbose_name in wineType):
            wine_classes.append({
                                  'model_name': model._meta.verbose_name,
                                  'model_table': model._meta.db_table,
                                  'model_object': model.objects.all()
                                  }) 
    return wine_classes
def redwine(request):
    redwine = ['malbec', 'sirah', 'pinot noir', 'shiraz', 'claret', 'vranac', 'merlot', 'cordial',
               'grenache', 'french', 'cabernet sauvignon', 'pinotage', 'zinfandel', 'burgundy']
    return render_to_response('redwine.html',
                              {'model_classes': getModels(request, redwine)}
                              )

def whitewine(request):
    whitewine = ['pinot grigio', 'blanc', 'chardonnay', 'bordeaux', 'sangria',
                 'riesling']
    return render_to_response('whitewine.html',
                              {'model_classes': getModels(request, whitewine)}
                              )
def rosewine(request):
    rosewine = ['rose']
    return render_to_response('rosewine.html',
                              {'model_classes': getModels(request, rosewine)}
                              )
def champagne(request):
    champagne = ['champagne']
    return render_to_response('champagne.html',
                              {'model_classes': getModels(request, champagne)}
                              )
def dessertwine(request):
    dessertwine = ['plum', 'chocolate', 'moscato', 'sherry', 'port', 'creams', 'marsala']
    return render_to_response('dessertwine.html',
                              {'model_classes': getModels(request, dessertwine)}
                              )
def liquor(request):
    liquor = ['anise', 'vermouth', 'pisco', 'brandy', 'tequila', 'cognac', 'vodka',
              'gin', 'liqueur', 'rum', 'vodka', 'sake', 'whiskey']
    return render_to_response('liquor.html',
                              {'model_classes': getModels(request, liquor)}
                              )
def showwine(request, model_name, object_name, object_id):
    model = apps.get_model('wine', model_name.replace(" ", ""))
    return render_to_response('showwine.html',
                             {
                              'model_name': model_name,
                              'object': model.objects.get(name=object_name, id=object_id)
                              })
def viewType(request, type_name):
    typewine = [type_name]
    return render_to_response('typewine.html',
                              {'model_classes': getModels(request, typewine),
                               'type_name': type_name
                               })

def catagory(request, catagory_name):
    funcToCall = globals()[catagory_name]
    return funcToCall(request)