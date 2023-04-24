from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('lists/', views.lists_index, name='index'),
    path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
    path('lists/<int:list_id>/', views.lists_detail, name='detail'),
    path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete'),
]