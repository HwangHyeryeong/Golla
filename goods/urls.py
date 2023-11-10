from django.urls import path

from . import views

urlpatterns = [
    path('<category>', views.selectGoodsList, name="selectGoodsList"),
    path('detail/<goodsCode>', views.selectGoodsInfo, name="selectGoodsInfo"),
]