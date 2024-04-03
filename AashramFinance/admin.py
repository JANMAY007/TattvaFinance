from django.contrib import admin
from .models import (DandiSamarpanAashram, KutchSamarpanAashram, SaurastraSamarpanAashram,
                     GujaratSamarpanAashram, GoaSamarpanAashram, MadhyaBharatSamarpanAashram,
                     RajasthanSamarpanAashram, DakshinBharatShreeShivkrupanandSwamiMath)


class DandiSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class KutchSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class SaurastraSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class GujaratSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class GoaSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class MadhyaBharatSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class RajasthanSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


class DakshinBharatSettings(admin.ModelAdmin):
    list_display = ['description', 'manager', 'vyavasthapak', 'trustee', 'finance_house_head', 'Ambareeshbhai',
                    'Cashier', 'quotation_file_1', 'quotation_file_2', 'quotation_file_3', 'bill_file',
                    'payment_1', 'payment_1_datetime',
                    'payment_2', 'payment_2_datetime',
                    'payment_3', 'payment_3_datetime']
    readonly_fields = ['manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
                       'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'Cashier_updated_at',
                       'payment_1_datetime', 'payment_2_datetime', 'payment_3_datetime', 'created_at']


admin.site.register(DandiSamarpanAashram, DandiSettings)
admin.site.register(KutchSamarpanAashram, KutchSettings)
admin.site.register(SaurastraSamarpanAashram, SaurastraSettings)
admin.site.register(GujaratSamarpanAashram, GujaratSettings)
admin.site.register(GoaSamarpanAashram, GoaSettings)
admin.site.register(MadhyaBharatSamarpanAashram, MadhyaBharatSettings)
admin.site.register(RajasthanSamarpanAashram, RajasthanSettings)
admin.site.register(DakshinBharatShreeShivkrupanandSwamiMath, DakshinBharatSettings)
