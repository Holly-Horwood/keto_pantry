"""keto_pantry URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login, registration, user_profile
from accounts import urls as accounts_urls
from accounts import url_reset
from products import urls as urls_products
from products.views import all_products
from cart import urls as urls_cart
from search import urls as urls_search
from django.views import static
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^posts/', include('blog.urls')),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]  



