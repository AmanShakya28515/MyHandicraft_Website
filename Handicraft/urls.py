from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.user_login, name='login'),

    path('landingPage/', views.LandingPage, name='LandingPage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('HomeDashboard/', views.HomeDashboard, name='HomeDashboard'),

    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_user, name='create_user'),
    path('user_list', views.user_list, name="user_list"),
    path('update_user/<int:user_id>/', views.update_user, name="update_user"),
    path('user_delete/<int:user_id>', views.user_delete, name="user_delete"),
    
    path('Buddha_products/', views.Buddha_list, name='Buddha_product_list'),
    path('Buddha_products/add/',views.addProduct_Buddha, name='Buddha_add_product'),
    path('Buddha_products/update/<int:pk>/', views.Buddha_update_product, name='Buddha_update_product'),
    path('Buddha_products/delete/<int:pk>/', views.Buddha_deleteProduct, name='Buddha_delete_product'),

    path('Tara_products/', views.Tara_list, name='Tara_product_list'),
    path('Tara_products/add/', views.addProduct_Tara, name='Tara_add_product'),
    path('Tara_products/update/<int:pk>/', views.Tara_update_product, name='Tara_update_product'),
    path('Tara_products/delete/<int:pk>/', views.Tara_deleteProduct, name='Tara_delete_product'),

    path('Ganesh_products/', views.Ganesh_list, name='Ganesh_product_list'),
    path('Ganesh_products/add/', views.addProduct_Ganesh, name='Ganesh_add_product'),
    path('Ganesh_products/update/<int:pk>/', views.Ganesh_update_product, name='Ganesh_update_product'),
    path('Ganesh_products/delete/<int:pk>/', views.Ganesh_deleteProduct, name='Ganesh_delete_product'),

    path('Sarsoti_Laxmi_products/', views.Sarsoti_Laxmi_list, name='Sarsoti_Laxmi_product_list'),
    path('Sarsoti_Laxmi_products/add/', views.addProduct_Sarsoti_Laxmi, name='Sarsoti_Laxmi_add_product'),
    path('Sarsoti_Laxmi_products/update/<int:pk>/', views.Sarsoti_Laxmi_update_product, name='Sarsoti_Laxmi_update_product'),
    path('Sarsoti_Laxmi_products/delete/<int:pk>/', views.Sarsoti_Laxmi_deleteProduct, name='Sarsoti_Laxmi_delete_product'),

    path('Utencils_products/', views.Utencils_list, name='Utencils_product_list'),
    path('Utencils_products/add/', views.addProduct_Utencils, name='Utencils_add_product'),
    path('Utencils_products/update/<int:pk>/', views.Utencils_update_product, name='Utencils_update_product'),
    path('Utencils_products/delete/<int:pk>/', views.Utencils_deleteProduct, name='Utencils_delete_product'),

    path(' ProductCategory/', views.ProductsCategory, name='ProductCategory'),
    path('updateCategoryProduct/update/<int:pk>',views.UpdateProductCategory,name="updateCategoryProduct"),
    path('CategoryList/',views.CategoryList, name="CategoryList"),
    path('CategoryDelete/delete/<int:pk>',views.CategoryDelete, name="CategoryDelete"),

    path('buddha_product_detail/<int:pk>/', views.Buddha_product_details, name='buddha_product_detail'),
    path('tara_product_detail/<int:pk>/', views.Tara_product_details, name='tara_product_detail'),
    path('ganesh_product_detail/<int:pk>/', views.Ganesh_product_details, name='ganesh_product_detail'),

    path('edit_p',views.edit_profile,name='edit_p'),
    path('profile_edit/<int:pk>/', views.edit_profile, name="profile_edit"),
    path('profile_view/<int:pk>/', views.profile, name="profile_view"),
    path('GodInfo/<int:pk>/', views.godinfo, name="GodInfo"),

    path('cart/', views.cart_view, name='cart_view'),
    path('cart/update/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/<str:product_type>/', views.add_to_cart, name='add_to_cart'),
    path('',views.backfunction,name='back'),

    path('buy_now/<int:product_id>/<str:category>/', views.buy_now, name='buy_now'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('process-payment/<int:order_id>/', views.process_payment, name='process_payment'),



    
]