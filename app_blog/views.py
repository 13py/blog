from django.http import HttpResponse


# Create your views here.
def posts_list(request):
    return HttpResponse('hi')
