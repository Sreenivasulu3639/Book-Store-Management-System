from django.urls import path

from BookStore import views

urlpatterns = [
    path('',views.home),
    path('addauthor',views.add_author),
    path('displayauthor',views.display_author,name='displayauthor'),
    path('deleteauthor/<int:id>',views.delete_author,name='deleteauthor'),
    path('editauthor/<int:id>',views.edit_author,name='editauthor'),
    ]