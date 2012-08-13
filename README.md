Django Private Views
====================

**Site-wide login protection.**

**Author:** Julien Phalip, [@julienphalip][1]. Originally released in this [blog post][3].

**Packaged and released by:** Tom Christie, [@_tomchristie][2].

[![Build Status](https://secure.travis-ci.org/dabapps/django-private-views.png)](http://travis-ci.org/dabapps/django-private-views)

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

At this point, all of your views except `settings.LOGIN_URL` will require
you to log in.  So, we now need to specify the few views that should be
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
example, if a page is rendered by a generic view. For that, you need to add
the `PUBLIC_PATHS` setting in your settings file. Here’s an example:

    PUBLIC_PATHS = [
        '^/accounts/register/complete/$', # Uses the 'direct_to_template' generic view
    ]

Making 404 views private
========================

At this point non-logged in users will still be able to see 404 responses if
they visit a url that doesn't map to a view.  That's not ideal as it shouldn't
be possible to determine the site structure without being logged in.

To make 404 views private to everyone except logged in users, add the following
as the final line in your top level urlconf:

    urlpatterns = patterns('',
        ...
        url(r'^', 'privateviews.views.private_404')
    )

License
=======

Copyright © 2012, Julien Phalip & DabApps.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://twitter.com/julienphalip
[2]: http://twitter.com/_tomchristie
[3]: http://julienphalip.com/post/2824985334/site-wide-login-protection-and-public-views
