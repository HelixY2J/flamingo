from django.urls import path
# This line imports the path function from 
#the django.urls module. The path function is used to 
# define URL patterns in your Django application


from . import views


app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('price/',views.price, name='price'),
]

'''
This line defines a URL pattern. It specifies that when the 
base URL (empty string) is accessed, the index view from the 
views module should be called. The name parameter is set to 
'index', allowing you to reference this URL pattern by name 
in your code or templates
'''