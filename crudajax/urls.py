from django.urls import path
from . import views

urlpatterns = [
    path('crud/',views.CrudView,name='crud_ajax'),
    path('ajax/crud/create/',views.CreateUser,name='create'),
    path('ajax/crud/update/',views.UpdateUser,name='update'),
    path('ajax/crud/delete',views.DeleteUser,name='delete'),
]