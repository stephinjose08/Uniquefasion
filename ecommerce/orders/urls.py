from django.urls import  path
from  .import views

urlpatterns = [

#   path("",views.grid_view,name="grid-view"),  
path('check_out/',views.check_out,name="check-out"),
path('place_order/',views.placeorder,name="place-order"),
path('check_out/proced-to-pay/',views.proced_to_pay,name="procedtopay"),
path('check_out/online/',views.online,name="online"),
path('my_orders/<int:id>/',views.my_orders,name="my-order"),

] 