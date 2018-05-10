from django.urls import path
from .views import post_list

app_name = 'ep01'

urlpatterns = [
   path('post/', post_list, name='post-list'),
    # path('', include(router.urls)),
]
