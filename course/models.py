from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Catagories"
        
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="courses", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="course_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    