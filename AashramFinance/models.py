from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class BaseAashram(models.Model):
    procurement_name = models.CharField(max_length=100, unique=True)
    comments = models.TextField()
    tds_choices = (
        ('94C Any contract payments',
         (
             ('Individual/HUF - 1%', 'Individual/HUF - 1%'),
             ('Others - 2%', 'Others - 2%'),
         )),
        ('94J - Professional fees',
         (
             ('Professional fees - 10%', 'Professional fees - 10%'),
         )),
        ('94Q - TDS on all purchases',
         (
             (' 0.10% on bill amount', ' 0.10% on bill amount'),
         ))
    )
    tds = models.CharField(max_length=100, choices=tds_choices, default='94C Any contract payments',
                           help_text='94C -> Applicable when Single bill more than 30k & yearly payment more than 1 '
                                     'lakh<br>'
                                     '94J -> Applicable when Single bill more than 30k<br>'
                                     '94Q -> Applicable when purchases from single party exceeds Rs.50 lakh.')
    manager = models.BooleanField(default=False)
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField(default=False)
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField(default=False)
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField(default=False)
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField(default=False)
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    accountant = models.BooleanField(default=False)
    accountant_updated_at = models.DateTimeField(auto_now=True)
    bill_file = models.FileField(upload_to='bill_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.manager

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = self.__class__.objects.get(pk=self.pk)
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()
            if self.accountant != old_instance.accountant:
                self.accountant_updated_at = timezone.now()
        super().save(*args, **kwargs)


class Quotation(models.Model):
    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    aashram = GenericForeignKey('content_type', 'object_id')
    quotation_file = models.FileField(upload_to='quotation_files/')
    objects = models.Manager()


class Payment(models.Model):
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    aashram = GenericForeignKey('content_type', 'object_id')
    amount = models.FloatField()
    payment_datetime = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class DandiSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Dandi Samarpan Aashram'
        verbose_name_plural = 'Dandi Samarpan Aashram'


class KutchSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Kutch Samarpan Aashram'
        verbose_name_plural = 'Kutch Samarpan Aashram'


class SaurashtraSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Saurashtra Samarpan Aashram'
        verbose_name_plural = 'Saurashtra Samarpan Aashram'


class GujaratSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Gujarat Samarpan Aashram'
        verbose_name_plural = 'Gujarat Samarpan Aashram'


class GoaSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Goa Samarpan Aashram'
        verbose_name_plural = 'Goa Samarpan Aashram'


class MadhyaBharatSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Madhya Bharat Samarpan Aashram'
        verbose_name_plural = 'Madhya Bharat Samarpan Aashram'


class RajasthanSamarpanAashram(BaseAashram):
    class Meta:
        verbose_name = 'Rajasthan Samarpan Aashram'
        verbose_name_plural = 'Rajasthan Samarpan Aashram'


class DakshinBharatShreeShivkrupanandSwamiMath(BaseAashram):
    class Meta:
        verbose_name = 'Dakshin Bharat Shree Shivkrupanand Swami Math'
        verbose_name_plural = 'Dakshin Bharat Shree Shivkrupanand Swami Math'


class Vendors(models.Model):
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    dandi_samarpan_aashram = models.BooleanField(default=False)
    kutch_samarpan_aashram = models.BooleanField(default=False)
    saurashtra_samarpan_aashram = models.BooleanField(default=False)
    gujarat_samarpan_aashram = models.BooleanField(default=False)
    goa_samarpan_aashram = models.BooleanField(default=False)
    madhya_bharat_samarpan_aashram = models.BooleanField(default=False)
    rajasthan_samarpan_aashram = models.BooleanField(default=False)
    dakshin_bharat_shree_shivkrupanand_swami_math = models.BooleanField(default=False)
    name = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    contact = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Orders(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    order_date = models.DateField()
    order_amount = models.FloatField()
    order_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
