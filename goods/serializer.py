from rest_framework import serializers
from .models import Goods, GoodsDetail


class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('goods_code', 'goods_name', 'goods_price', 'goods_img_path')


class GoodsOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('goods_code', 'goods_name', 'goods_price', 'goods_description', 'goods_category', 'goods_img_path')



class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDetail
        fields = ('volume', 'calories', 'fat', 'carbohydrates', 'protein', 'sugar', 'fiber', 'allergies')
