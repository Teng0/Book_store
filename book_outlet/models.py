from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural="Countries"

    def __str__(self):
        return self.name + "-" + self.code
    


class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street} , {self.city} , {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"
    


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address =  models.OneToOneField(Address,on_delete=models.CASCADE,related_name="author",null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
        



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(6)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)
    published_cuntries = models.ManyToManyField(Country)
    
    
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args,**kwargs)



    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    

    def __str__(self):
        return f" {self.title}  ({self.rating})"