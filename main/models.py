from django.db import models

# Create models here


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.name


class review(models.Model):

    POST_TYPES = [("c", "copyright"), ("p", "public")]
    TITLE_MAX_LENGTH = 250

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to="uploads")

    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class iPhoneCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class iPhoneModel(models.Model):
    name = models.CharField(max_length=100)
    memory = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(iPhoneCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.memory} - ${self.price}"
