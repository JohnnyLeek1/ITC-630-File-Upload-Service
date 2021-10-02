from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('upload/index.html')
    context = { 'test': 'johnny' }
    return HttpResponse(template.render(context, request))
