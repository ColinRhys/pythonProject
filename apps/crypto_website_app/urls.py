from django.conf.urls import url
from . import views           
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^books$', views.books,name='books'),
    url(r'^mining$', views.mining, name='mining'),
    url(r'^charting$', views.charting, name='charting'),
    url(r'^lending$', views.lending, name='lending'),
    ]

urlpatterns += staticfiles_urlpatterns()