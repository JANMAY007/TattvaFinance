from django.db import models


class DandiSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Dandi Samarpan Aashram'
        verbose_name_plural = 'Dandi Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class KutchSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Kutch Samarpan Aashram'
        verbose_name_plural = 'Kutch Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class SaurastraSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Saurastra Samarpan Aashram'
        verbose_name_plural = 'Saurastra Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class GujaratSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Gujarat Samarpan Aashram'
        verbose_name_plural = 'Gujarat Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class RajasthanSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Rajasthan Samarpan Aashram'
        verbose_name_plural = 'Rajasthan Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class GoaSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Goa Samarpan Aashram'
        verbose_name_plural = 'Goa Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class MadhyaBharatSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Madhya Bharat Samarpan Aashram'
        verbose_name_plural = 'Madhya Bharat Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager


class DakshinBharatShreeShivkrupanandSwamiMath(models.Model):
    class Meta:
        verbose_name = 'Dakshin Bharat Shree Shivkrupanand Swami Math'
        verbose_name_plural = 'Dakshin Bharat Shree Shivkrupanand Swami Math'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField(auto_now=True)
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField(auto_now=True)
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField(auto_now=True)
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField(auto_now=True)
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField(auto_now=True)
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField(auto_now=True)
    quotation_file_1 = models.FileField(upload_to='quotation_files_1/')
    quotation_file_2 = models.FileField(upload_to='quotation_files_2/')
    quotation_file_3 = models.FileField(upload_to='quotation_files_3/')
    bill_file = models.FileField(upload_to='bill_files/')
    payment_1 = models.FloatField()
    payment_1_datetime = models.DateTimeField(auto_now=True)
    payment_2 = models.FloatField()
    payment_2_datetime = models.DateTimeField(auto_now=True)
    payment_3 = models.FloatField()
    payment_3_datetime = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.manager
