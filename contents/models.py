from django.db import models


class Paint(models.Model):
    kid = models.ForeignKey("accounts.Kid", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_source = models.ImageField()


class Picture(models.Model):
    kid = models.ForeignKey("accounts.Kid", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_source = models.ImageField()


class Music(models.Model):
    title = models.CharField(max_length=50)
    file_source = models.FileField()


class Script(models.Model):
    kid = models.ForeignKey(
        "accounts.Kid", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    file_source = models.FileField(null=True, blank=True)
    state = models.IntegerField(null=True)


class Video(models.Model):
    kid = models.ForeignKey("accounts.Kid", on_delete=models.CASCADE)
    script = models.OneToOneField(Script, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_source = models.FileField()


class Character(models.Model):
    kid = models.ForeignKey("accounts.Kid", on_delete=models.CASCADE)
    eat_time = models.DateTimeField(default="2020-01-01 00:00:00")
    wash_time = models.DateTimeField(default="2020-01-01 00:00:00")
