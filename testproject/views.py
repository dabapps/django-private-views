from django.http import HttpResponse
from django.views.generic import View


def undecorated(request):
    return HttpResponse('ok')


def test_public_views(request):
    return HttpResponse('ok')


def test_public_paths(request):
    return HttpResponse('ok')


class TestClassBasedView(View):

    def get(self, request):
        return HttpResponse('ok')
