from django.db import models


class Goods(models.Model):
    goods_code = models.AutoField(db_column='Goods_Code', primary_key=True)
    goods_name = models.CharField(db_column='Goods_Name', max_length=50)
    goods_price = models.IntegerField(db_column='Goods_Price', blank=True, null=True)
    goods_description = models.CharField(db_column='Goods_Description', max_length=255)
    goods_category = models.IntegerField(db_column='Goods_Category')

    # 이미지 모델과의 관계 설정 (외래 키)
    goods_picture = models.ForeignKey('GoodsPictures', on_delete=models.SET_NULL, null=True, related_name='goods')

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsDetail(models.Model):
    detail_code = models.AutoField(db_column='Detail_Code', primary_key=True)
    goods_code = models.ForeignKey(Goods, models.DO_NOTHING, db_column='Goods_Code')
    volume = models.IntegerField()
    calories = models.IntegerField(db_column='Calories')
    fat = models.IntegerField(db_column='Fat')
    carbohydrates = models.IntegerField(db_column='Carbohydrates')
    protein = models.IntegerField(db_column='Protein')
    sugar = models.IntegerField(db_column='Sugar')
    fiber = models.IntegerField(db_column='Fiber')
    allergies = models.CharField(db_column='Allergies', max_length=19)

    class Meta:
        managed = False
        db_table = 'goodsDetail'


class GoodsPictures(models.Model):
    id = models.BigAutoField(primary_key=True)
    img = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'goods_picture'
