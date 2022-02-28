from django.db import models

# Create your models here.
# class employee(models.Model):
#     firstname=models.CharField(max_length=10)
#     lastname = models.CharField(max_length=10)
#     emp_id = models.CharField(max_length=10)
#
#
#     def __str__(self):
#         return self.firstname

class documents(models.Model):
    doc_name = models.CharField(max_length=50)
    fol_name = models.CharField(max_length=50)
    top_name = models.CharField(max_length=50)
    doc_id = models.IntegerField()

    def __str__(self):
        return self.doc_name


# class folders(models.Model):
#     fol_name = models.CharField(max_length=10)
#     fol_id = models.IntegerField(max_length=10)
#
#     def __str__(self):
#         return self.fol_name
#
#
# class topics(models.Model):
#     top_name = models.CharField(max_length=10)
#     top_id = models.IntegerField(max_length=10)
#
#     def __str__(self):
#         return self.top_name