from django.conf.urls import url,include

urlpatterns = [
    url(r'^$', 'huhu.views.index'),
    url(r'^insert$', 'huhu.views.insert'),
    url(r'^passnext$', 'huhu.views.passnext'),
    url(r'^deleteaction$', 'huhu.views.deleteaction'),
]
