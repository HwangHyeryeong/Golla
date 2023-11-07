from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from .models import Goods, GoodsDetail
from rest_framework.decorators import api_view
from .serializer import GoodsListSerializer, GoodsOneSerializer, GoodsDetailSerializer
from .messages import *


# Create your views here.
"""
상품 목록을 조회하는 API(goods 객체 목록 표시)
: path parameter: category(파인트 1 / 빵샌드 2/ 패키지 3) 
"""
@api_view(['GET'])
def selectGoodsList(request, category):
    if category == 'all':
        goods_list = Goods.objects.values(
            'goods_code', 'goods_name', 'goods_price', 'goods_img_path'
        )

    elif category == 'pint':
        goods_list = Goods.objects.filter(goods_category=1).values(
            'goods_code', 'goods_name', 'goods_price', 'goods_img_path'
        )
    elif category == 'bread':
        goods_list = Goods.objects.filter(goods_category=2).values(
            'goods_code', 'goods_name', 'goods_price', 'goods_img_path'
        )
    elif category == 'package':
        goods_list = Goods.objects.filter(goods_category=3).values(
            'goods_code', 'goods_name', 'goods_price', 'goods_img_path'
        )

    serializer = GoodsListSerializer(goods_list, many=True)
    return Response(serializer.data)



#TODO: 상품 상세 조회 API 완성하기
@api_view(['GET'])
def selectGoodsInfo(request, goodsCode):
    goods = Goods.objects.filter(goods_code=goodsCode).values(
        'goods_code', 'goods_name', 'goods_price', 'goods_description', 'goods_category', 'goods_img_path'
    ).first()
    goods_detail = GoodsDetail.objects.filter(goods=goodsCode).values(
        'volume', 'calories', 'fat', 'carbohydrates', 'protein', 'sugar', 'fiber', 'allergies'
    ).first()

    if goods and goods_detail:
        goods_serializer = GoodsOneSerializer(goods, many=False)
        detail_serializer = GoodsDetailSerializer(goods_detail, many=False)
        data = {
            "status": status.HTTP_200_OK,
            "success": True,
            "message": SUCCESS_FOUND_ITEM,
            "data": {
                **goods_serializer.data,
                **detail_serializer.data
            }
        }
        return Response(data, status=status.HTTP_200_OK)

    else:
        data = {
            "status": status.HTTP_404_NOT_FOUND,
            "success": False,
            "message": NOT_FOUND_ITEM
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
