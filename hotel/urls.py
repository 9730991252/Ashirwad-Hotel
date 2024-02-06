from django.urls import path
from hotel import views


urlpatterns = [
    path('', views.index,name='index'),
    path('sunil_login', views.sunil_login,name='sunil_login'),
    path('add_admin', views.add_admin,name='add_admin'),
    path('admin_login', views.admin_login,name='admin_login'),
    path('admin_dashboard', views.admin_dashboard,name='admin_dashboard'),
    path('dish_category',views.dish_category , name='dish_category'),
    path('dish',views.dish , name='dish'),
    path('book_order',views.book_order , name='book_order'),
    path('filter_by_category',views.filter_by_category , name='filter_by_category'),
    path('place_order',views.place_order , name='place_order'),
    path('complate_order',views.complate_order , name='complate_order'),
    path('daily_report',views.daily_report , name='daily_report'),
    path('test',views.test , name='test'),
   
]
