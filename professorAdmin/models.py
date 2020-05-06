# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allusers(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=54)
    adduserid = models.IntegerField()
    addusername = models.CharField(max_length=54)
    pwd = models.CharField(max_length=54)
    addtime = models.DateTimeField()
    cx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'allusers'


class Professors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    danwei = models.CharField(max_length=50)
    zhengzhimianmao = models.CharField(max_length=50)
    zhiwu = models.CharField(max_length=30)
    zhicheng = models.CharField(max_length=15)
    shenfenzhenghao = models.CharField(max_length=54)
    lianxidianhua = models.CharField(max_length=45)
    kechengmingcheng = models.CharField(max_length=150)
    kaihuhang = models.CharField(max_length=60)
    kahao = models.CharField(max_length=60)
    shehuijianzhi = models.CharField(max_length=150)
    jianjie = models.CharField(max_length=600)
    hezuoqingkuang = models.CharField(max_length=60)
    zhengzhibiaoxian = models.CharField(max_length=30)
    shoukejilu = models.CharField(max_length=150)
    labels = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'professors'
