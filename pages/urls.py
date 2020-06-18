from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name= "home"),
    path('contact/',views.contact, name="contact" ),
    path('about/', views.about, name='about'),
    path('index/', views.index, name = 'index'),
    # path('team/',views.team, name="team"),
    # path('teams/<int:mem_id>/<int:team_id>',views.teams,name='teams')
    
]