from django.db import models


class Goods(models.Model):
    goods_code = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50)
    goods_price = models.IntegerField(blank=True, null=True)
    goods_description = models.CharField(max_length=255)
    goods_category = models.IntegerField()
    goods_img_path = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'goods'


class GoodsDetail(models.Model):
    detail_code = models.AutoField(primary_key=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goodsdetail')
    volume = models.IntegerField()
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    sugar = models.IntegerField()
    fiber = models.IntegerField()
    allergies = models.CharField(max_length=19)

    class Meta:
        managed = True
        db_table = 'goods_detail'
