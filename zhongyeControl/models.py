# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=54)
    pwd = models.CharField(max_length=54)
    addtime = models.DateTimeField()
    cx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'allusers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chemical(models.Model):
    sample_id = models.IntegerField(primary_key=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    machine_name = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    get_people = models.CharField(max_length=255, blank=True, null=True)
    measuring_name = models.CharField(max_length=255, blank=True, null=True)
    measuring_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical'


class CommissionCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
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
    report_id = models.CharField(max_length=255)
    test_basis = models.CharField(max_length=255)
    company_id = models.IntegerField(blank=True, null=True)
    invoice = models.CharField(max_length=30)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_sheet'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    sample_id = models.IntegerField(primary_key=True)
    sample_actual_id = models.CharField(max_length=255, blank=True, null=True)
    sheet_id = models.IntegerField(blank=True, null=True)
    brand_grade = models.CharField(max_length=255, blank=True, null=True)
    d = models.CharField(max_length=255, blank=True, null=True)
    sample_number = models.IntegerField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    laiyang_id = models.CharField(max_length=255, blank=True, null=True)
    lashen = models.IntegerField(blank=True, null=True)
    wanqu = models.IntegerField(blank=True, null=True)
    fanwan = models.IntegerField(blank=True, null=True)
    huaxue = models.IntegerField(blank=True, null=True)
    jinxiang = models.IntegerField(blank=True, null=True)
    chicun = models.IntegerField(blank=True, null=True)
    biaomianbiaozhi = models.IntegerField(blank=True, null=True)
    zhonglaingpiancha = models.IntegerField(blank=True, null=True)
    biaomianzhiliang = models.IntegerField(blank=True, null=True)
    ceq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'


class Share(models.Model):
    sample_actual_id = models.CharField(max_length=255)
    d = models.CharField(max_length=255, blank=True, null=True)
    brand_grade = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField()
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

    class Meta:
        managed = False
        db_table = 'share'
