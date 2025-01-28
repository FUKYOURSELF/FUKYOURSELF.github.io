from django.urls import path
from .views import function_view_test,ClassViewTest,book_query,book_query1
urlpatterns=[
    path('test-function/',function_view_test),
    path('test-class/',ClassViewTest.as_view()),
    path('book',book_query),
    path('book/<str:book_id>',book_query1)
]
