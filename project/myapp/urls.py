from django.urls import path  # type: ignore
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

app_name = 'myapp'  # Esto permite referenciar las URLs de esta app

def debug_view(request):
    return HttpResponse("<pre>" + "\n".join([str(url) for url in urlpatterns]) + "</pre>")

urlpatterns = [
        path('', views.index, name='index'),  # Vista del índice
        path('client/list/', views.client_list, name='client_list'),
        path('product/list/', views.product_list, name='product_list'),
        path('order/list/', views.order_list, name='order_list'),
        path('client/create/', views.client_create, name='client_create'),
        path('product/create/', views.product_create, name='product_create'),
        path('order/create/', views.order_create, name='order_create'),
        path('signup/', views.signup, name='signup'),  # Vista para registro de usuarios
        path('login/', auth_views.LoginView.as_view(), name='login'),  # Vista ingreso cuenta
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('accounts/profile/', views.user_profile, name='user_profile'),
        path('about/', views.about, name='about'),
    ]
