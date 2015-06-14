from django.shortcuts import render, render_to_response
from django.db.models import get_app, get_models, get_model
import wine.views
from django.db.models import Q
# Create your views here.

def search(request):
    errors = []
    objects = []
    wines = []
    num = 0
    if 'q' in request.GET:
        t = request.GET['q'].upper()
        qq = t.split()
        if len(qq[0]) < 3:
            errors.append('Enter a search term more than two characters')
        else:    
            for model in wine.views.getAllModels():
                for q in qq:
                    if (q=="PORT"):
                        result = model.objects.filter(Q(name__contains=q) | \
                                                    Q(description__contains=q))                                                    
                    else:
                        result = model.objects.filter(Q(name__contains=q) | \
                                                      Q(region__contains=q) | \
                                                    Q(description__contains=q))
                    if (result):
                        objects.append(result)
            for model in objects:
                for object in model:
                    num += 1
                    wines.append(object)
            return render(request, 'search_results.html',
                          {'wines': wines, 'query': t, 'wine_num': num}
                          )
    return render(request, 'search_results.html', {'errors': errors})
