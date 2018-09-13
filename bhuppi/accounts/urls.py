from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'signup',views.signup,name='signup'),
    url(r'login',views.login_user,name='login'),
    url(r'logout',views.logout_view,name='logout'),
    #url(r'update/(?P<id>[0-9]+)/',views.update,name='update'),
]
# url(r'register/(?P<id>[0-9]+)/',views.home,name='home'),
