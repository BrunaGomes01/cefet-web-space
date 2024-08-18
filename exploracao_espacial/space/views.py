from django.shortcuts import render
from django.views import View

class Home(View):
    template_path = 'home/home.html'
    def get(self, request):
        return render(request, self.template_path)

class Philae(View):
    template_path = 'philae/philae.html'
    def get(self, request):
        return render(request, self.template_path)