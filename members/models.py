from django.db import models

# Create your models here.
class Member(models.Model):
    member_code = models.AutoField(db_column='member_Code', primary_key=True)  # Field name made lowercase.
    member_name = models.CharField(db_column='member_Name', max_length=20)  # Field name made lowercase.
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    grade = models.IntegerField()
    member_point = models.IntegerField()
    joindate = models.DateTimeField(db_column='joinDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Payment(models.Model):
    paymentcode = models.AutoField(db_column='paymentCode', primary_key=True)  # Field name made lowercase.
    membercode = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberCode')  # Field name made lowercase.
    storecode = models.IntegerField(db_column='storeCode')  # Field name made lowercase.
    paymentprice = models.IntegerField(db_column='paymentPrice')  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='paymentDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'