from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.tasklist_view.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdate.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.taskdelete.as_view(),name='cbvdelete'),
]