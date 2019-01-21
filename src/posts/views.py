from django.shortcuts import render
from django.views import View
from .models import Post


class Home(View):
    template_name = 'posts/home.html'

    def get(self, request):

        context = {
            'posts': Post.objects.all()
        }
        return render(request, self.template_name, context)
