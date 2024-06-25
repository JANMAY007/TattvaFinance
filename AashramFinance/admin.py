from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from .models import (
    DandiSamarpanAashram, KutchSamarpanAashram, SaurashtraSamarpanAashram,
    GujaratSamarpanAashram, SamarpanAashramGoa, MadhyaBharatSamarpanAashram,
    RajasthanSamarpanAashram, DakshinBharatShreeShivkrupanandSwamiMath,
    Quotation, Payment, Vendors, Orders
)


class QuotationInline(GenericTabularInline):
    model = Quotation
    extra = 1


class PaymentInline(GenericTabularInline):
    model = Payment
    extra = 1
    readonly_fields = ('payment_datetime',)


class BaseAashramAdmin(admin.ModelAdmin):
    list_display = (
        'procurement_name', 'comments', 'get_boolean_fields', 'get_bill_file',
        'get_quotations', 'get_payments'
    )
    readonly_fields = (
        'manager_updated_at', 'vyavasthapak_updated_at', 'trustee_updated_at',
        'finance_house_head_updated_at', 'Ambareeshbhai_updated_at', 'accountant_updated_at',
        'created_at'
    )
    inlines = [QuotationInline, PaymentInline]

    def get_bill_file(self, obj):
        if obj.bill_file:
            return format_html('<a href="{}">View Bill</a>', obj.bill_file.url)
        return "No Bill File"
    get_bill_file.short_description = 'Bill File'

    def get_quotations(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        quotations = Quotation.objects.filter(content_type=content_type, object_id=obj.id)
        if quotations:
            links = [format_html('<a href="{}">View Quotation {}</a>', q.quotation_file.url, i + 1) for i, q in enumerate(quotations)]
            return format_html('<br>'.join(links))
        return "No Quotations"
    get_quotations.short_description = 'Quotations'

    def get_payments(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        payments = Payment.objects.filter(content_type=content_type, object_id=obj.id)
        if payments:
            links = [format_html('{1}. Amount Paid {0}', p.amount, i + 1) for i, p in enumerate(payments)]
            return format_html('<br>'.join(links))
        return "No Payments"
    get_payments.short_description = 'Payments'

    def get_boolean_fields(self, obj):
        fields = [
            ('Manager', obj.manager),
            ('Vyavasthapak', obj.vyavasthapak),
            ('Trustee', obj.trustee),
            ('Finance House Head', obj.finance_house_head),
            ('Ambareeshbhai', obj.Ambareeshbhai),
            ('Accountant', obj.accountant),
        ]
        formatted_fields = [f"{label}: {'✔' if value else '✘'}" for label, value in fields]
        return format_html('<br>'.join(formatted_fields))
    get_boolean_fields.short_description = 'Roles'


admin.site.register(DandiSamarpanAashram, BaseAashramAdmin)
admin.site.register(KutchSamarpanAashram, BaseAashramAdmin)
admin.site.register(SaurashtraSamarpanAashram, BaseAashramAdmin)
admin.site.register(GujaratSamarpanAashram, BaseAashramAdmin)
admin.site.register(SamarpanAashramGoa, BaseAashramAdmin)
admin.site.register(MadhyaBharatSamarpanAashram, BaseAashramAdmin)
admin.site.register(RajasthanSamarpanAashram, BaseAashramAdmin)
admin.site.register(DakshinBharatShreeShivkrupanandSwamiMath, BaseAashramAdmin)


class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 1


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'contact', 'email', 'city',
                    'state', 'country', 'get_boolean_fields')
    inlines = [OrdersInline]

    def get_boolean_fields(self, obj):
        fields = [
            ('Dandi Samarpan Aashram', obj.dandi_samarpan_aashram),
            ('Kutch Samarpan Aashram', obj.kutch_samarpan_aashram),
            ('Saurashtra Samarpan Aashram', obj.saurashtra_samarpan_aashram),
            ('Gujarat Samarpan Aashram', obj.gujarat_samarpan_aashram),
            ('Goa Samarpan Aashram', obj.goa_samarpan_aashram),
            ('Madhya Bharat Samarpan Aashram', obj.madhya_bharat_samarpan_aashram),
            ('Rajasthan Samarpan Aashram', obj.rajasthan_samarpan_aashram),
            ('Dakshin Bharat Shree Shivkrupanand Swami Math', obj.dakshin_bharat_shree_shivkrupanand_swami_math),
        ]
        formatted_fields = [f"{label}✔" for label, value in fields if value]
        return format_html('<br>'.join(formatted_fields))
    get_boolean_fields.short_description = 'Roles'


admin.site.register(Vendors, VendorsAdmin)
