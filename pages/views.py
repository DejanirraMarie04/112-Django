from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

# Function based view
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    return render(request, "pages/contact.html")
