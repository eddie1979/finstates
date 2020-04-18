from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.veiws.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'finchart/index'