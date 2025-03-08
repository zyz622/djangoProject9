from django.db import models

# Create your models here.
# python manage.py inspectdb
# python manage.py inspectdb >> app01/models.py# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App01Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'app01_admin'


class App01BloodPressure(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    morning_evening = models.SmallIntegerField()
    times = models.SmallIntegerField()
    high_pressure = models.IntegerField()
    low_pressure = models.IntegerField()
    pulse = models.IntegerField()
    remarks = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'app01_blood_pressure'


class App01City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    count = models.IntegerField()
    img = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'app01_city'


class App01Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'app01_department'


class App01EmployeeInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    department = models.CharField(max_length=75)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'app01_employee_information'


class App01Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_number = models.CharField(max_length=64)
    goods_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stadus = models.SmallIntegerField()
    admin = models.ForeignKey(App01Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_order'


class App01Pn(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=11)
    price = models.IntegerField()
    level = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'app01_pn'


class App01Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.SmallIntegerField()
    title = models.CharField(max_length=64)
    detail = models.TextField()
    user = models.ForeignKey(App01Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_task'


class App01Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=8)
    age = models.IntegerField()
    account = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateField()
    gender = models.SmallIntegerField()
    depart = models.ForeignKey(App01Department, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_userinfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DateTest(models.Model):
    iddate_test = models.IntegerField(primary_key=True)
    date_t = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_test'


# class Denpyou(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     ��ע��Ʊ���� = models.CharField(max_length=10, blank=True, null=True)
#     ���Ϸ��� = models.CharField(max_length=10, blank=True, null=True)
#     ��ע�� = models.DateField(blank=True, null=True)
#     ��ע���� = models.CharField(max_length=10, blank=True, null=True)
#     ������ = models.DateField(blank=True, null=True)
#     �؅��趨�� = models.DateField(blank=True, null=True)
#     �M������ = models.CharField(max_length=15, blank=True, null=True)
#     ��ע���T���`�� = models.CharField(max_length=15, blank=True, null=True)
#     ��ע���T���� = models.CharField(max_length=45, blank=True, null=True)
#     ���� = models.CharField(max_length=15, blank=True, null=True)
#     ��ע���� = models.CharField(max_length=45, blank=True, null=True)
#     ͷN�e = models.CharField(max_length=45, blank=True, null=True)
#     ���åȥ��`�� = models.CharField(max_length=45, blank=True, null=True)
#     ���å���Ʒ = models.CharField(max_length=45, blank=True, null=True)
#     ��ע���å��� = models.IntegerField(blank=True, null=True)
#     �����ȥ��`�� = models.CharField(max_length=45, blank=True, null=True)
#     ���������� = models.CharField(max_length=45, blank=True, null=True)
#     ؜�ӷN�e = models.CharField(max_length=45, blank=True, null=True)
#     �ե������`no = models.IntegerField(db_column='�ե������`No', blank=True, null=True)  # Field name made lowercase.
#     ����Ӌ = models.IntegerField(blank=True, null=True)
#     ���M˰ = models.IntegerField(blank=True, null=True)
#     Ո���ȥ��`�� = models.CharField(max_length=45, blank=True, null=True)
#     Ո���� = models.CharField(max_length=45, blank=True, null=True)
#     �Ӓ�� = models.IntegerField(blank=True, null=True)
#     ��s�� = models.IntegerField(blank=True, null=True)
#     ���}�� = models.IntegerField(blank=True, null=True)
#     ���ډ��� = models.IntegerField(blank=True, null=True)
#     ԭ�� = models.IntegerField(blank=True, null=True)
#     ���� = models.IntegerField(blank=True, null=True)
#     �����ƥ��` = models.IntegerField(blank=True, null=True)
#     ��٩`�� = models.IntegerField(blank=True, null=True)
#     ��s���俼 = models.CharField(max_length=145, blank=True, null=True)
#     �俼1 = models.CharField(max_length=45, blank=True, null=True)
#     �俼2 = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'denpyou'


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
    id = models.BigAutoField(primary_key=True)
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

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title