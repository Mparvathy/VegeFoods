from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    path("shop/", views.shop, name="shop"),
    path("vegetable_list/", views.vegetable_list, name="vegetable_list"),
    path("fruit_list/", views.fruit_list, name="fruit_list"),
    path("juice_list/", views.juice_list, name="juice_list"),

    path('add/', views.add_product, name='add_product'),
    
    path('view/<int:p>/', views.view, name='view'),
    path('view1/<int:p>/', views.view1, name='view1'),
    path('view2/<int:p>/', views.view2, name='view2'),
    path('view3/<int:p>/', views.view3, name='view3'),
  
    path('add-to-cart/<int:b>/<str:item_type>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cartview, name='cart'),
    path('delete/<int:item_id>/<str:item_type>/', views.cart_delete, name='delete'),

   
    path('product/update/<int:p_id>/', views.update_product, name='update_product'),
    path('veg/update/<int:v_id>/', views.update_veg, name='update_veg'),
    path('fruit/update/<int:f_id>/', views.update_fruit, name='update_fruit'),
    path('juice/update/<int:j_id>/', views.update_juice, name='update_juice'),

    path('delete/product/<int:id>/', views.delete_product, name='delete_product'),
    path('delete/veg/<int:id>/', views.delete_veg, name='delete_veg'),
    path('delete/fruit/<int:id>/', views.delete_fruit, name='delete_fruit'),
    path('delete/juice/<int:id>/', views.delete_juice, name='delete_juice'),

    path('checkout/', views.checkout, name='checkout'),
    path('final/', views.final, name='final'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('wishlist/add/<int:item_id>/<str:item_type>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/<str:item_type>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    path('order-history/', views.order_history, name='order_history'),
    path('login/', views.user_login, name="login"),
    path('adminsignup/', views.adminsignup, name='adminsignup'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('logout/', views.user_logout, name='logout'), 
  
    path('contact/contact-messages/', views.contact_messages, name='contact_messages'),
    path('delete_contact_message/<int:id>/', views.delete_contact_message, name='delete_contact_message'),
    path('profile/', views.user_profile_details, name='user_profile_details'),
    path('profile/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('user-list/', views.user_list, name='user_list'),
    path('user-orders/', views.admin_user_orders, name='admin_user_orders'),
    path('user-orders/<int:order_id>/', views.admin_user_order_detail, name='admin_user_order_detail'),
path('user/<int:user_id>/order-history/', views.user_order_history, name='admin_user_order_history'),

   
]


