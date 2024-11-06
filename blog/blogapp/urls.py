# create your urls here

from django.urls import path
from . import views as vi


app_name = 'blogapp'

urlpatterns = [
    path('base/', vi.basedir, name='base page'),
    path('', vi.homepage, name='homepage') ,
]