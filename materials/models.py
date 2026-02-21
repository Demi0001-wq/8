from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    preview = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name='Preview')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    preview = models.ImageField(upload_to='lessons/', blank=True, null=True, verbose_name='Preview')
    video_link = models.URLField(verbose_name='Video link', blank=True, null=True)
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Course')

    def __str__(self):
        return self.name
