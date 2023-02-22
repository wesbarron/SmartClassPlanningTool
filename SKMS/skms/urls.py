from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('sign-up', views.createAccount),
    path('user-profile/', views.userProfile),
    path('forum/', views.forum, name='forum'),
    path('edit-profile/', views.editProfile),
    path('create-post/', views.renderCreatePost),
    path('create/', views.createPost, name='create'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('submit-comment/<int:post_id>', views.createComment, name='create-comment'),
    path('login', auth_views.LoginView.as_view(template_name='skms/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='skms/logout.html'), name='logout'),
]
