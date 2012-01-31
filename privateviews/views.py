from django.http import Http404


def private_404(request):
    """
    A catch-all 404 page.

    Using LoginRequiredMiddleware together with this view will ensure that
    users need to be logged in to see 404 responses.
    """
    raise Http404()
