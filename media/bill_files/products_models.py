from django.db import models
from django.contrib.auth.models import User
from Profile.models import ClientProfile, DeveloperProfile, HosterProfile, ReviewerProfile


class HostingPlan(models.Model):
    hoster = models.ForeignKey(HosterProfile, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    plan_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.plan_name + ' -> ' + self.hoster.hoster.user.username


class ReviewPlan(models.Model):
    reviewer = models.ForeignKey(ReviewerProfile, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    plan_description = models.TextField()
    plan_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.plan_name + ' -> ' + self.reviewer.reviewer.user.username


class DeveloperProject(models.Model):
    developer = models.ForeignKey(DeveloperProfile, on_delete=models.CASCADE)
    hosting_plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE, null=True, blank=True)
    review_plan = models.ForeignKey(ReviewPlan, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_tech_used = models.JSONField()
    project_category = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    project_url = models.URLField(null=True, blank=True)
    project_demo_video = models.URLField(null=True, blank=True)
    project_banner = models.ImageField(upload_to='project_banners', blank=True)
    project_card_image = models.ImageField(upload_to='project_card_images', blank=True)
    project_gallery_images_1 = models.ImageField(upload_to='project_gallery_images', blank=True)
    project_gallery_images_2 = models.ImageField(upload_to='project_gallery_images', blank=True)
    project_gallery_images_3 = models.ImageField(upload_to='project_gallery_images', blank=True)
    project_gallery_images_4 = models.ImageField(upload_to='project_gallery_images', blank=True)
    estimated_price = models.FloatField()
    is_hosted = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
    average_rating = models.FloatField()
    total_sales = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.project_name + ' -> ' + self.developer.developer.user.username


class ProjectRatings(models.Model):
    project = models.ForeignKey(DeveloperProject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.user.username + ' -> ' + str(self.rating)


class ClientDeveloperProject(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(DeveloperProject, on_delete=models.CASCADE)
    hosting_plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE, null=True, blank=True)
    hoster = models.ForeignKey(HosterProfile, on_delete=models.CASCADE, null=True, blank=True)
    review_plan = models.ForeignKey(ReviewPlan, on_delete=models.CASCADE, null=True, blank=True)
    review = models.ForeignKey(ReviewerProfile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.client.client.user.username + ' -> ' + self.project.project_name


class ClientProject(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    hosting_plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE, null=True, blank=True)
    review_plan = models.ForeignKey(ReviewPlan, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_details_file = models.FileField(upload_to='project_details_files', blank=True)
    project_tech_used = models.JSONField()
    project_category = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    project_amount = models.FloatField()
    project_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.client.client.user.username + ' -> ' + self.project_name


class DeveloperBiding(models.Model):
    developer = models.ForeignKey(DeveloperProfile, on_delete=models.CASCADE)
    developer_client_project = models.ForeignKey(ClientProject, on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    bid_description = models.TextField()
    bid_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.developer_client_project.project_name + ' -> ' + str(self.bid_amount)


class HostBiding(models.Model):
    hoster = models.ForeignKey(HosterProfile, on_delete=models.CASCADE)
    client_developer_project = models.ForeignKey(ClientDeveloperProject, on_delete=models.CASCADE, null=True, blank=True)
    developer_client_project = models.ForeignKey(ClientProject, on_delete=models.CASCADE, null=True, blank=True)
    bid_amount = models.FloatField()
    bid_description = models.TextField()
    bid_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.client_developer_project.project.project_name + ' -> ' + str(self.bid_amount)


class ReviewBiding(models.Model):
    reviewer = models.ForeignKey(ReviewerProfile, on_delete=models.CASCADE)
    client_developer_project = models.ForeignKey(ClientDeveloperProject, on_delete=models.CASCADE, null=True, blank=True)
    developer_client_project = models.ForeignKey(ClientProject, on_delete=models.CASCADE, null=True, blank=True)
    bid_amount = models.FloatField()
    bid_description = models.TextField()
    bid_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return self.client_developer_project.project.project_name + ' -> ' + str(self.bid_amount)
