# from http.client import HTTPResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Стартовая страница')


def group_posts(request, slug):
    return HttpResponse(f'Любая {slug} строка')
