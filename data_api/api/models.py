from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_session'


class LegoColors(models.Model):
    name = models.CharField(max_length=255)
    rgb = models.CharField(max_length=6)
    is_trans = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'lego_colors'


class LegoInventories(models.Model):
    version = models.IntegerField()
    set_num = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'lego_inventories'


class LegoInventoryParts(models.Model):
    inventory_id = models.IntegerField()
    part_num = models.CharField(max_length=255)
    color_id = models.IntegerField()
    quantity = models.IntegerField()
    is_spare = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lego_inventory_parts'


class LegoInventorySets(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    set_num = models.CharField(max_length=255)
    quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'lego_inventory_sets'


class LegoPartCategories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'lego_part_categories'


class LegoParts(models.Model):
    part_num = models.CharField(primary_key=True, max_length=255)
    name = models.TextField()
    part_cat_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'lego_parts'


class LegoPartsPerYear(models.Model):
    year: int
    total_parts: int


class LegoSets(models.Model):
    set_num = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    theme_id = models.IntegerField(blank=True, null=True)
    num_parts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lego_sets'


class LegoThemes(models.Model):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lego_themes'
