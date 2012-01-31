import re
from django.conf import settings
from django.contrib.auth.decorators import login_required
from privateviews.decorators import PublicView


class LoginRequiredMiddleware(object):

    def __init__(self):
        self.public_patterns = []
        self.public_views = []

        if hasattr(settings, 'PUBLIC_VIEWS'):
            for view_path in settings.PUBLIC_VIEWS:
                view = self.get_view(view_path)
                self.public_views.append(view)
        if hasattr(settings, 'PUBLIC_PATHS'):
            for public_path in settings.PUBLIC_PATHS:
                self.public_patterns.append(re.compile(public_path))
        if hasattr(settings, 'LOGIN_URL'):
            pattern = re.compile(re.escape(settings.LOGIN_URL))
            self.public_patterns.append(pattern)

    def get_view(self, view_path):
        i = view_path.rfind('.')
        module_path, view_name = view_path[:i], view_path[i + 1:]
        module = __import__(module_path, globals(), locals(), [view_name])
        return getattr(module, view_name)

    def matches_public_view(self, view):
        if self.public_views:
            for public_view in self.public_views:
                if view == public_view:
                    return True
        return False

    def matches_public_path(self, path):
        if self.public_patterns:
            for pattern in self.public_patterns:
                if pattern.match(path) is not None:
                    return True
        return False

    def process_view(self, request, view_func, view_args, view_kwargs):
        if (request.user.is_authenticated()
            or isinstance(view_func, PublicView)
            or self.matches_public_path(request.path)
            or self.matches_public_view(view_func)):
            return None
        else:
            return login_required(view_func)(request, *view_args, **view_kwargs)
