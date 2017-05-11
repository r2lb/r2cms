from django.conf.urls import url


from adm import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'index2', views.dashboard2),
    url(r'index',views.dashboard),
]
