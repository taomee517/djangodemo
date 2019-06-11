from django.db import models

# Create your models here.
# 用于创建模型
# 模型类必须继承models.Model类


class Brand(models.Model):
    # 说明：不需要定义主键，在生成时自动添加，并且值为自动增加
    brand_name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    logo_url = models.CharField(max_length=255)
    is_deleted = models.BooleanField()


class Series(models.Model):
    # 关联外键
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    series_name = models.CharField(max_length=48)
    publish_year = models.IntegerField()
    lower_price = models.IntegerField()
