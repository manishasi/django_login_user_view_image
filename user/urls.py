from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    # path('update/<str:id>',views.update_image,name='update_image'),
    # path('delete/<int:id>/',views.delete_image, name='delete_image'),
#     path('like/<int:id>', like_image, name='like_image'),
#     path('dislike/<int:id>', dislike_image, name='dislike_image'),
]