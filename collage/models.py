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

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Category.objects.get(id = self.id).update(field = val)

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

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Location.objects.get(id = self.id).update(field = val)

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

    def delete_image(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_image(self,val):
        """
        This is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__contains = search_term)
        return images

    def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

    @classmethod
    def filter_by_location(cls,location):
        """
        This is the method to get images taken in a certain location
        """
        the_location = Location.objects.get(name = location)
        return cls.objects.filter(location_id = the_location.id)

