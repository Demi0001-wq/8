from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    preview = models.ImageField(upload_to='materials/', verbose_name='Preview', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    preview = models.ImageField(upload_to='materials/', verbose_name='Preview', null=True, blank=True)
    video_url = models.URLField(verbose_name='Video URL', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', related_name='lessons')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
