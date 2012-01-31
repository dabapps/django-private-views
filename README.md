Django Private Views
====================

**Site-wide login protection.**

**Author:** Julien Phalip, [@julienphalip][1]. Originally released in this [blog post][3].

**Packaged and released by:** Tom Christie, [@_tomchristie][2].

Overview
========

A common pattern in websites is when a few pages are protected and require a
login to be accessed. The `@login_required` decorator often comes in handy for
these situations. But, another pattern which is quite common is when most of
the site is protected, with just a few exceptions of pages that remain public
(e.g. frontpage, registration page, etc.). In that case, it can be quite
tedious to decorate all of the views with `@login_required`, and it can be easy
to forget to decorate some of them.

`django-private-views` protects every view and then lets you explicitly tell which
views should be public. This makes things both easier and less error-prone.


Installation
============

Install `django-private-views` from PyPI.

    pip install django-private-views

Add the `privateviews` middleware to your settings:

    MIDDLEWARE_CLASSES = (
        ...
        privateviews.middleware.LoginRequiredMiddleware
    )


Declaring public views
======================

At this point, all of your views will require you to log in, including the
login page itself. So, we now need to specify the few views that should be
public. There are three different ways at your disposal: using a special
decorator, listing the public views, or listing the public URL paths.

Using a Decorator
-----------------

Using `@login_not_required` you can explicitly force a view to be public.
For example:

    from privateviews.decorators import login_not_required

    @login_not_required
    def frontpage(request):
        ...

In this case, the frontpage view will be properly displayed even if you’re not
logged in.

Listing public views
--------------------

If you don’t have direct access to modify a view’s code (e.g., it’s in a
third-party application), you still can force that view to be public by adding
it to the `PUBLIC_VIEWS` setting in your settings file. Here’s an example if
you’re using the `django.contrib.auth` system and the `django-registration`
application:

    PUBLIC_VIEWS = [
        'django.contrib.auth.views.login',
        'django.contrib.auth.views.password_reset_done',
        'django.contrib.auth.views.password_reset',
        'django.contrib.auth.views.password_reset_confirm',
        'django.contrib.auth.views.password_reset_complete',
        'registration.views.register',
        'registration.views.activate',
    ]

Listing URL public paths
------------------------

The third and last way is to directly specify the URL paths (as regular
expressions) for the pages you want to be public. This can be useful, for
example, if a page is rendered by a generic view. It is also useful if you are
serving your media files statically via Django (only recommended in development
mode). For that, you need to add the `PUBLIC_PATHS` setting in your settings
file. Here’s an example:

    PUBLIC_PATHS = [
        '^%s' % MEDIA_URL,
        '^/accounts/register/complete/$', # Uses the 'direct_to_template' generic view
    ]

Private 404 views
=================

With the current setup you'll still serve 404 views to unauthenticated users
if they request a URL that isn't in the site's `urlconf`.  This isn't ideal,
as the site layout shouldn't be visible to unauthenticated users.

To make sure that even 404 views remain private, add the following as the last
line in your project's top level urlconf:

    urlpatterns = patterns(''
        ...
        url(r'^', 'privateviews.views.private_404')
    )


(Un)License
===========

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to [unlicense.org][4].

[1]: http://twitter.com/julienphalip
[2]: http://twitter.com/_tomchristie
[3]: http://julienphalip.com/post/2824985334/site-wide-login-protection-and-public-views
[4]: http://unlicense.org/
