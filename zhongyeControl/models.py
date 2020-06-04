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
    pwd = models.CharField(max_length=54)
    addtime = models.DateTimeField()
    cx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'allusers'


class CommissionCompany(models.Model):
    company_name = models.CharField(max_length=255)
    contactor = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    company_tel = models.CharField(max_length=255, blank=True, null=True)
    taxpayer_identity_number = models.CharField(max_length=255, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_company'


class CommissionSheet(models.Model):
    period = models.CharField(max_length=2, blank=True, null=True)
    laiyang_id = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=2, blank=True, null=True)
    sample_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    sample_state = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    presentation = models.CharField(max_length=4, blank=True, null=True)
    processing_method = models.CharField(max_length=5, blank=True, null=True)
    manufactory = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    sample_disposal = models.CharField(max_length=5, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    deposit = models.FloatField(blank=True, null=True)
    yangpin_name = models.CharField(max_length=255, blank=True, null=True)
    test_basis = models.CharField(max_length=255)
    items = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    assign_people = models.IntegerField(blank=True, null=True)
    assign_time = models.DateTimeField(blank=True, null=True)
    report_id = models.CharField(max_length=255)
    command_date = models.DateField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    invoice = models.CharField(max_length=30)
    sample_number = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_sheet'


class Experiment(models.Model):
    sample_id = models.IntegerField()
    sample_number = models.CharField(max_length=50)
    lashen = models.IntegerField(blank=True, null=True)
    wanqu = models.IntegerField(blank=True, null=True)
    fanwan = models.IntegerField(blank=True, null=True)
    huaxue = models.IntegerField(blank=True, null=True)
    jinxiang = models.IntegerField(blank=True, null=True)
    chicun = models.IntegerField(blank=True, null=True)
    biaomianbiaozhi = models.IntegerField(blank=True, null=True)
    zhongliangpiancha = models.IntegerField(blank=True, null=True)
    biaomianzhiliang = models.IntegerField(blank=True, null=True)
    ceq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment'


class OriginalSample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    d = models.CharField(max_length=255)
    brand_grade = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=255, blank=True, null=True)
    sample_actual_id = models.CharField(max_length=255, blank=True, null=True)
    reportid = models.IntegerField(db_column='reportID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'original_sample'


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


class Sample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    max_n_after_bre = models.FloatField(db_column='max_N_after_bre', blank=True, null=True)  # Field name made lowercase.
    max_n_origin = models.FloatField(db_column='max_N_origin', blank=True, null=True)  # Field name made lowercase.
    post_break_gauge = models.FloatField(db_column='post_break_ gauge', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    origin_gauge = models.FloatField(blank=True, null=True)
    peak_load = models.FloatField(blank=True, null=True)
    yeild_load = models.FloatField(blank=True, null=True)
    rel = models.FloatField(db_column='ReL', blank=True, null=True)  # Field name made lowercase.
    rm = models.FloatField(db_column='Rm', blank=True, null=True)  # Field name made lowercase.
    a = models.FloatField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    rm0_rel0 = models.FloatField(db_column='Rm0/ReL0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rel0_rel = models.FloatField(db_column='ReL0/ReL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    agt = models.FloatField(db_column='Agt', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    machine_name = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    get_people = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    measuring_name = models.CharField(max_length=255, blank=True, null=True)
    measuring_id = models.IntegerField(blank=True, null=True)
    d = models.CharField(max_length=255, blank=True, null=True)
    brand_grade = models.CharField(max_length=255, blank=True, null=True)
    sample_actual_id = models.CharField(max_length=255, blank=True, null=True)
    reportid = models.IntegerField(db_column='reportID', blank=True, null=True)  # Field name made lowercase.
    backup = models.CharField(max_length=255, blank=True, null=True)
    laiyang_id = models.CharField(max_length=20, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    product_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'


class Standard(models.Model):
    brand_grade = models.CharField(primary_key=True, max_length=255)
    d = models.CharField(max_length=255)
    csa = models.CharField(max_length=255)
    theoretical_weight = models.CharField(max_length=255, blank=True, null=True)
    lengwanshiyan = models.CharField(max_length=255, blank=True, null=True)
    rel = models.CharField(db_column='ReL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rm = models.CharField(db_column='Rm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a = models.CharField(db_column='A', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rm0_rel0 = models.CharField(db_column='Rm0/ReL0', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rel0_rel = models.CharField(db_column='ReL0/ReL', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    agt = models.CharField(db_column='Agt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mn = models.CharField(db_column='Mn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    si = models.CharField(db_column='Si', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p = models.CharField(db_column='P', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s = models.CharField(db_column='S', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neijing = models.CharField(max_length=255, blank=True, null=True)
    hengleigao = models.CharField(max_length=255, blank=True, null=True)
    zhongleigao = models.CharField(max_length=255, blank=True, null=True)
    hengleikuan = models.CharField(max_length=255, blank=True, null=True)
    zongleikuan = models.CharField(max_length=255, blank=True, null=True)
    jianjugongcheng = models.CharField(max_length=255, blank=True, null=True)
    heileimoduan = models.CharField(max_length=255, blank=True, null=True)
    ceq = models.CharField(db_column='Ceq', max_length=255, blank=True, null=True)  # Field name made lowercase.
    waquyatou = models.CharField(max_length=255, blank=True, null=True)
    fanxiangwanqu = models.CharField(max_length=255, blank=True, null=True)
    jinglidu = models.CharField(max_length=255, blank=True, null=True)
    jinxiangzuzhi = models.CharField(max_length=255, blank=True, null=True)
    biaomianzhiliang = models.CharField(max_length=255, blank=True, null=True)
    zhongliangpiancha = models.CharField(max_length=255, blank=True, null=True)
    biaomianbiaozhi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard'
        unique_together = (('brand_grade', 'd'),)
