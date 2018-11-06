# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib import admin
from django.db import models



class TBlog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=32, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_blog'
        ordering = ('-create_time',)


class TUser(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    birthday = models.CharField(max_length=8, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=32, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


admin.site.register(TBlog)


admin.site.register(TUser)