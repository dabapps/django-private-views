from django.http import HttpResponse


def undecorated(request):
    return HttpResponse('ok')
