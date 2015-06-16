from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.utils.timezone import now

# Create your views here.
class BusinessHomepage(View):
    """
    Homepage for Business Users
    """
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        #if request.user.is_authenticated():
            # go to business view
        return render(request, 'business.html')
    