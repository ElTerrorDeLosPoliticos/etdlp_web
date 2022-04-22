from etdlp_app import views
from django.urls import path, include

urlpatterns = [
    path('', views.main_page, name='main_page'),
    # path('logout/', views.logout,name="logout"),
    # path('create_email/', views.create_email, name="create_email"),
    # path('register', views.RegisterOrgView.as_view(), name="organization_register"),
    # path('perfil/', views.perfil, name='perfil'),
    # #PARTE DEL ADMIN
    # path('admin_list', views.admin_cliente_list, name="admin_list_client"),
    # path('admin_list_update/<int:id>/', views.admin_cliente_list_validate, name="admin_list_client_update"),
    # path('admin_list_invalid/<int:id>/', views.admin_cliente_list_invalid, name="admin_list_client_invalid"),
    # path('perfil/<int:pk>/', views.perfil, name='perfil'),
]
