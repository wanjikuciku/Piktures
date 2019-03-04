from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def save_category(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Category.objects.get(id = self.id).delete()

    

    def __str__(self):
        return self.name


    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

class Location(models.Model):
    name = models.CharField(max_length = 30)


    def save_location(self):
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        self.delete()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

   

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image_location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__contains = search_term)
        return images

