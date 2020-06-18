"""djangos_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
'''this is for function based 
from pages import views'''


'''for class based views
from pages.views import index, About'''

# for the theird to declare views by the include fucntions
from django.urls import include
urlpatterns = [
    path('',include('pages.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]
    # '''these are procedural process 
    # path('home/',views.home, name='home'),
    # path('contact/',views.contact, name='contact'),'''
    # '''for class based views
    # path('',index.as_view()),
    # path('about/',About.as_view()),'''
   



