from rest_framework import serializers
from .models import Goods, GoodsDetail, GoodsPictures


class GoodsPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsPictures
        fields = 'goods_img_path'


class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDetail
        fields = ('volume', 'calories', 'fat', 'carbohydrates', 'protein', 'sugar', 'fiber', 'allergies')


class GoodsListSerializer(serializers.ModelSerializer):
    goods_img_path = GoodsPicturesSerializer(source='goods_pictures', read_only=True)

    class Meta:
        model = Goods
        fields = ('goods_code', 'goods_name', 'goods_price', 'goods_img_path')


class GoodsOneSerializer(serializers.ModelSerializer):
    goods_img_path = GoodsPicturesSerializer(source='goods_pictures', read_only=True)
    goods_detail = GoodsDetailSerializer(source='goodsdetail', read_only=True)

    class Meta:
        model = Goods
        fields = ('goods_code', 'goods_name', 'goods_price', 'goods_img_path', 'goods_detail')