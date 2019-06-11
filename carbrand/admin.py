from django.contrib import admin
from .models import Brand, Series

# Register your models here.
# 进行站点配置


class BrandAdmin(admin.ModelAdmin):
    # list_display = ['brand_name', 'state', 'logo_url', 'is_deleted']

    def name_cn(self):
        return self.brand_name

    def state_cn(self):
        return self.state

    def logo_cn(self):
        return self.logo_url

    def delete_cn(self):
        if self.is_deleted:
            return 'Y'
        else:
            return 'N'

    name_cn.short_description = '品牌名称'
    state_cn.short_description = '国家'
    logo_cn.short_description = 'logo地址'
    delete_cn.short_description = '删除'
    list_display = [name_cn, state_cn, logo_cn, delete_cn]


class SeriesAdmin(admin.ModelAdmin):
    def brand(self):
        return self.brand.brand_name

    list_display = [brand, 'series_name', 'publish_year', 'lower_price']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Series, SeriesAdmin)
# admin.site.register(Brand)
# admin.site.register(Series)

