from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/books/',get_books, name='get_books'),
    path('api/books/<int:pk>/',get_books, name='get_books'),
    path('api/books/add/', add_book, name='add-book'),
    path('api/books/manage/<int:pk>/', manage_book, name='manage-book'),


    path('api/register/', register_user, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/change-password/', change_password, name='change-password'),

    path('api/books/<int:book_id>/reviews/', book_reviews, name='book-reviews'),
    path('api/reviews/<int:review_id>/', review_detail, name='review-detail'),

]
