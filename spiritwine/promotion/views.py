from django.shortcuts import render, render_to_response
from django.db.models import get_app, get_model
# Create your views here.
def special(request, special_id):
    model = get_model('promotion', 'PromotionSpecial')
    object = model.objects.get(id=special_id)
    return render_to_response('special.html',
                              {'model_name': object.region,
                              'object': object
                              })
