from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from buyer.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from buyer.models import Buyer
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

def BuyerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.save()
            buyer = Buyer(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
            buyer.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            buyer = authenticate(username=username, password=password)
            if buyer is not None:
                login(request, buyer)
                #return HttpResponseRedirect('/profile/')
                return render_to_response('base.html', context_instance=RequestContext(request))
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')