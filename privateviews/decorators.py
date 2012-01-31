from functools import update_wrapper
#from django.contrib.auth.decorators import _CheckLogin


def login_not_required(view_func):
    """
    Decorator which marks the given view as public (no login required).
    """
    return PublicView(view_func)


class PublicView(object):
    """
    Forces a view to be public (no login required).
    """
    def __init__(self, view_func):
        #if isinstance(view_func, _CheckLogin):
        #    self.view_func = view_func.view_func
        #else:
        #    self.view_func = view_func
        update_wrapper(self, view_func)

    def __get__(self, obj, cls=None):
        view_func = self.view_func.__get__(obj, cls)
        return PublicView(view_func)

    def __call__(self, request, *args, **kwargs):
        return self.view_func(request, *args, **kwargs)
