from django.urls import path
from .import views
app_name = 'userauth'


urlpatterns = [
    path('',views.index, name='index'),
    path('kozhikkod',views.kozhikkod , name='kozhikkod'),
    path('malapuram',views.malapuram , name='malapuram'),
    path('kannur',views.kannur , name='kannur'),
    path('palakkad',views.palakkad , name='palakkad'),
    path('kochi',views.kochi , name='kochi'),
    path('user_login',views.user_login , name='user_login'),
    path('user_register',views.user_register,name='user_register')
]
    