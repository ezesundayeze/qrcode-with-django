from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Employees(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    thumb = models.ImageField(default="default.png", blank=True, null=True)

    class Meta:
        verbose_name = "Employee"

    def __str__(self):
        return self.fName
