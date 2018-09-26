from django.views.generic import TemplateView

# Create your views here.
#Pagina Incial
class Index(TemplateView):
    template_name = "pagina_inicial.html"


#Página de Ajuda
class Ajuda(TemplateView):
    template_name = "ajuda.html"
