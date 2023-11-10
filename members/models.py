from django.db import models

class Store(models.Model):
    store_code = models.AutoField(db_column='store_code', primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='store_name', max_length=20)  # Field name made lowercase.
    store_address = models.CharField(db_column='store_address', max_length=255)  # Field name made lowercase.
    store_phone = models.CharField(db_column='store_phone', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'store'


class Grade(models.Model):
    gradeCode = models.AutoField(db_column='grade_code', primary_key=True)  # Field name made lowercase.
    gradeName = models.CharField(db_column='grade_name', max_length=20)  # Field name made lowercase.
    pointRate = models.IntegerField(db_column='point_rate')  # Field name made lowercase.
    baseAmount = models.IntegerField(db_column='base_amount')  # Field name made lowercase.
    gradeImg = models.CharField(db_column='grade_img', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'grade'


class Member(models.Model):
    memberCode = models.AutoField(db_column='member_Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='member_Name', max_length=20)  # Field name made lowercase.
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    grade = models.IntegerField()
    point = models.IntegerField()
    joindate = models.DateTimeField(db_column='joinDate')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'member'


class Payment(models.Model):
    paymentCode = models.AutoField(db_column='paymentCode', primary_key=True)  # Field name made lowercase.
    memberCode = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberCode')  # Field name made lowercase.
    storeCode = models.IntegerField(db_column='storeCode')  # Field name made lowercase.
    paymentPrice = models.IntegerField(db_column='paymentPrice')  # Field name made lowercase.
    paymentDate = models.DateTimeField(db_column='paymentDate')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment'