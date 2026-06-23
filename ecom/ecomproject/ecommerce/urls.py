from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
   
    path('about',views.about,name='abouts'),
    
    path('products/', views.category, name='category'),   
    path('products/<str:code>/', views.category, name='hello'),
    
    path('category_page2/', views.category_page2, name='category_page2'),
    path('category_page3/', views.category_page3, name='category_page3'),
    path('category_page4/', views.category_page4, name='category_page4'),
    path('category_page5/', views.category_page5, name='category_page5'),
    
    path('single_product/<int:single_id>/', views.single_product, name='single_product'),
    
    path('cart',views.cart,name='cart'),
    path('add_cart/<int:product_id>',views.add_cart,name='hi'),
    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:remove_id>/', views.remove_cart, name='remove'),

   path('signup_page',views.signup,name='signup'),
   path('login_page',views.loginpage,name='login'),
   path('logout/',views.logout_view, name='logout'),
   
   path('userprofile',views.userprofile,name='profile'),
   path('profile/edit/', views.profile_form, name='userprofile_edit'),
   
   path('buy',views.buy,name='buy')

]
