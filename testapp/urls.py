from django.urls import path
from django.conf.urls import url
from . import views


# どのアプリのurlsなのか分かるようにapp_nameを使用する。
app_name = 'testapp'

urlpatterns = [
    path('test1/',views.test1_View.as_view(),name='test1'),
    path('test2/',views.test2_View.as_view(), name="test2"),
]
