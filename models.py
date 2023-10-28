# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GollaPicture(models.Model):
    id = models.BigAutoField(primary_key=True)
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'golla_picture'


class Grade(models.Model):
    grade_code = models.AutoField(db_column='Grade_Code', primary_key=True)  # Field name made lowercase.
    grade_name = models.CharField(db_column='Grade_Name', max_length=20)  # Field name made lowercase.
    point_rate = models.IntegerField(db_column='point_Rate')  # Field name made lowercase.
    base_amount = models.IntegerField(db_column='Base_Amount')  # Field name made lowercase.
    grade_img_path = models.CharField(db_column='Grade_Img_Path', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grade'


class Store(models.Model):
    storecode = models.AutoField(db_column='storeCode', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=20)  # Field name made lowercase.
    store_address = models.CharField(db_column='Store_Address', max_length=255)  # Field name made lowercase.
    stroe_phone = models.CharField(db_column='Stroe_Phone', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'
