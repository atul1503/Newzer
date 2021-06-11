from django.urls import path,re_path
from .views import *


urlpatterns=[
    path('',general),# '' is /top_headlines/
    re_path('general/prev?.*',gen_prev),
    re_path('general/next?.*',gen_next)
    
]
