from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestCases(TestCase):
    """
    This is the class we will use to test the images
    """
    
    def setUp(self):
        """
        This will create a new image before each test case
        """
        food = Category(name = "food")
        food.save()
        africa = Location(name = "Africa")
        africa.save()
        self.new_image = Image(name = "image",description = "h",location = africa,category = funny)
    
    def tearDown(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """
        self.assertTrue(self.new_image.image_name == "image")

    def test_save_image(self):
        """
        This will test whether the new image is added to the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_delete_image(self):
        """
        This will test whether the new image is deleted from the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        

    def test_get_images(self):
        """
        This will test whether the get_image will return all the images
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.get_images()) == 1)

    def test_search_image(self):
        """
        This will test whether the image is queried based on category
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.search_image("funny")) > 0)

    def test_filter_by_location(self):
        """
        This will test whether the filter_by_loc will return photos in a certain category
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.filter_by_location("Africa")) == 1)

class LocationTestCases(TestCase):
    """
    This is the class we will use to test the Locations
    """
    def setUp(self):
        self.new_location = Location(name = "Moringa")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Location.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the location created is an instance of the Location class
        """
        self.assertTrue(isinstance(self.new_location,Location))
    def test_init(self):
        """
        This will test whether the new location is instantiated correctly
        """
        self.assertTrue(self.new_location.name == "Moringa")

    def test_save_location(self):
        """
        This will test whether the new location is added to the db
        """
        self.new_location.save_location()
        self.assertTrue(len(Location.objects.all()) == 1)

class CategoryTestCases(TestCase):
    """
    This is the class we will use to test the Locations
    """
    def setUp(self):
        self.new_category = Category(name = "Moringa")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Category.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the category created is an instance of the Category class
        """
        self.assertTrue(isinstance(self.new_category,Category))

    def test_init(self):
        """
        This will test whether the new category is instantiated correctly
        """
        self.assertTrue(self.new_category.name == "Moringa")

    def test_save_category(self):
        """
        This will test whether the new category is added to the db
        """
        self.new_category.save_category()
        self.assertTrue(len(Category.objects.all()) == 1)
