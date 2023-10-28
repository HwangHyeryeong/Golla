from django.shortcuts import render
from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from .models import Goods
from rest_framework.decorators import api_view
from .serializer import GoodsListSerializer, GoodsOneSerializer

# Create your views here.

"""
상품 목록을 조회하는 API(goods 객체 목록 표시)
: path parameter: category(전체 0 / 파인트 1 / 빵샌드 2/ 패키지 3) 
"""
@api_view(['GET'])
def selectGoodsList(request, category):
    query = 'SELECT goods_code, goods_name, goods_price, gp.img as goods_img_path from goods g join goods_picture gp on g.Goods_Img_Path = Goods_Code'
    if category == 'all':
        return executeQueryforGoodsList(query + ' where Goods_Category = 0')
    elif category == 'pint':
        return executeQueryforGoodsList(query + ' where Goods_Category = 1')
    elif category == 'bread':
        return executeQueryforGoodsList(query + ' where Goods_Category = 2')
    elif category == 'package':
        return executeQueryforGoodsList(query + ' where Goods_Category = 3')


#TODO: 상품 상세 조회 API 완성하기
@api_view(['GET'])
def selectGoodsInfo(request, goodsCode):
    query = '''SELECT g.Goods_Code, g.Goods_Name, g.Goods_Price, 
                gp.img as Goods_Img_Path, 
                gd.volume, gd.Calories, gd.Fat, gd.Carbohydrates, gd.Protein, gd.Protein, gd.Sugar, gd.Fiber, gd.Allergies 
                from goods g 
                join goodsDetail gd on g.Goods_Code = gd.Goods_Code 
                join goods_picture gp on g.Goods_Img_Path = gp.id 
                where g.Goods_Code = %s'''

    return executeQueryforGoodsInfo(query, [goodsCode])


def executeQueryforGoodsList(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        serializer = GoodsListSerializer(results, many=True)
        return Response(serializer.data)


def executeQueryforGoodsInfo(query, params):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchone()
        serializer = GoodsOneSerializer(results, many=False)
        return Response(serializer.data)
