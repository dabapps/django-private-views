from django.http import HttpResponse


def undecorated(request):
    return HttpResponse('ok')

def test_public_views(request):
    return HttpResponse('ok')
