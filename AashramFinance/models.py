from django.db import models
from django.utils import timezone


class DandiSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Dandi Samarpan Aashram'
        verbose_name_plural = 'Dandi Samarpan Aashram'

    description = models.TextField()
    manager = models.BooleanField()
    manager_updated_at = models.DateTimeField()
    vyavasthapak = models.BooleanField()
    vyavasthapak_updated_at = models.DateTimeField()
    trustee = models.BooleanField()
    trustee_updated_at = models.DateTimeField()
    finance_house_head = models.BooleanField()
    finance_house_head_updated_at = models.DateTimeField()
    Ambareeshbhai = models.BooleanField()
    Ambareeshbhai_updated_at = models.DateTimeField()
    Cashier = models.BooleanField()
    Cashier_updated_at = models.DateTimeField()
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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


class SaurashtraSamarpanAashram(models.Model):
    class Meta:
        verbose_name = 'Saurashtra Samarpan Aashram'
        verbose_name_plural = 'Saurashtra Samarpan Aashram'

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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = DandiSamarpanAashram.objects.get(pk=self.pk)

            # Update manager_updated_at
            if self.manager != old_instance.manager:
                self.manager_updated_at = timezone.now()

            # Update vyavasthapak_updated_at
            if self.vyavasthapak != old_instance.vyavasthapak:
                self.vyavasthapak_updated_at = timezone.now()

            # Update trustee_updated_at
            if self.trustee != old_instance.trustee:
                self.trustee_updated_at = timezone.now()

            # Update finance_house_head_updated_at
            if self.finance_house_head != old_instance.finance_house_head:
                self.finance_house_head_updated_at = timezone.now()

            # Update Ambareeshbhai_updated_at
            if self.Ambareeshbhai != old_instance.Ambareeshbhai:
                self.Ambareeshbhai_updated_at = timezone.now()

            # Update Cashier_updated_at
            if self.Cashier != old_instance.Cashier:
                self.Cashier_updated_at = timezone.now()

        super().save(*args, **kwargs)
