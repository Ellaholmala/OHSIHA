from django.urls import path

from . import views

urlpatterns = [
    path('', views.DataList.as_view(), name='data_list'),
    path('view/<int:pk>', views.DataView.as_view(), name='data_view'),
    path('new', views.DataCreate.as_view(), name='data_new'),
    path('view/<int:pk>', views.DataView.as_view(), name='data_view'),
    path('edit/<int:pk>', views.DataUpdate.as_view(), name='data_edit'),
    path('delete/<int:pk>', views.DataDelete.as_view(), name='data_delete'),

    path('', views.data_list, name='data_list'),
    path('view/<int:pk>', views.data_view, name='data_view'),
    path('new', views.data_create, name='data_new'),
    path('edit/<int:pk>', views.data_update, name='data_edit'),
    path('delete/<int:pk>', views.data_delete, name='data_delete'),
]