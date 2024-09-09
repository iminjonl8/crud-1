from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create_news', views.create_news, name='create_news'),
    path('delete_news/<int:id>', views.delete_news, name='delete_news'),
    path('update_news_page/<int:id>', views.update_news_page, name='update_news_page'),
    path('update_news/<int:id>', views.update_news, name='update_news'),
    path('add_comment/<int:id>', views.comment_page, name='add_comment'),
    path('save_comment/', views.create_comment, name='save_comment'),

] + debug_toolbar_urls()