from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.base, name='base'),
    path('about-me/', views.About, name = 'about-me'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('project/', views.project, name='project'),
]
