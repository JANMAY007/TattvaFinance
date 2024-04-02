from django.db import models


class DandiSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class KutchSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class SaurastraSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class GujaratSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class RajasthanSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class GoaSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class MadhyaBharatSamarpanAashram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title


class DakshinBharatShreeShivkrupanandSwamiMath(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.BooleanField(max_length=100)
    vyavasthapak = models.BooleanField(max_length=100)
    trustee = models.BooleanField(max_length=100)
    Amareeshbhai = models.BooleanField(max_length=100)
    Cashier = models.BooleanField(max_length=100)
    bill_file = models.FileField(upload_to='bill_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.title
