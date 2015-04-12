from django.shortcuts import redirect, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Template, Context
from django.core.exceptions import PermissionDenied
from ATS.models import Keyword
from ATS.forms import AddMultipleKeywords, AddKeyword
from django.views.generic import View

class BulkKeywords(View):
    """
    Bulk Keyword input
    """   
    template_name = 'BulkKeywords.html'
    def post(self, request, *args, **kwargs):
        form = AddMultipleKeywords(data=request.POST)
        #return HttpResponse(form.data['text_area'])
        words_list = form.data['text_area'].split(',')
        for word in words_list:
            try:
                obj = Keyword.objects.get(word=word)
                obj.popularity = obj.popularity + 1
            except Keyword.DoesNotExist:
                obj = Keyword(word=word)
            obj.save()
                
        if self.request.user.is_admin:
            form = AddMultipleKeywords()
            return render_to_response(self.template_name, {'form': form,}, context_instance=RequestContext(request))
        raise PermissionDenied()
        
    def get(self, request, *args, **kwargs):
        if self.request.user.is_admin:
            form = AddMultipleKeywords()
            return render_to_response(self.template_name, {'form': form,}, context_instance=RequestContext(request))
        raise PermissionDenied()
      
        
# def findSynonyms(request):
#     if request.user.is_admin:
#         keyword_list = Keyword.objects.all()
#         for keyword in keyword_list:
#             try:
#                 print keyword.synonyms
#             except:
#                 print "GET SYN"
#                 try:
#                     syn_list = pyhugeconnector.thesaurus_entry(
#                             word=keyword.word,
#                             api_key='524aec7b34958b8d6f6ca45134d7592f',
#                             pos_tag='v',
#                             ngram=0,
#                             relationship_type='syn'
#                             )
#                     for syn in syn_list:
#                         #create synonym objects
#                         try:
#                             obj = Keyword(word=syn, word_type="verb")
#                             obj.save()
#                             obj.synonyms.add(keyword)
#                             obj.save()
#                             print "saving!!!"
#                         except:
#                             print "unique value limit."
#                 except:
#                     pass
#         return HttpResponse("Done!")
#     raise PermissionDenied()