from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'signup',views.signup,name='signup'),
    url(r'login',views.login_user,name='login'),
    url(r'logout',views.logout_view,name='logout')
]
