from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('contests/',contests, name='contests'),
    path('categories/',categories, name='categories'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('allposts/',allposts, name='allposts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)