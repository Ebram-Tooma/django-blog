from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    
    path('add_category/', AddCategoryView.as_view(), name="add_category"), 
    path('category/<str:cats>/', CategoryView, name="category"), 
    path('category_list/', CategoryListView, name="category_list"), 
    path('like/<int:pk>', LikeView, name="like_post"), 



]
