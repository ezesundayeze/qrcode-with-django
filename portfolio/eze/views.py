from django.shortcuts import render
import os
# rest_frameowrk required modules
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, Department
from .serializers import EmployeeSerializers, DepartmentSerializers

# Create your views here.

# Qrcode modules
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# file system module
from django.core.files.storage import FileSystemStorage


def home(request):

    return render(request, 'eze/index.html')


def upload(request):

    if request.method == "POST":
         # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        # The data that you want to store
        data = request.POST['data']

        # Add data
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        img.save("media/barcode.jpg")

        context = {
            "Result": "media/barcode.jpg",
            "Success": "Barcode was generated successfully",

        }

        return render(request, "eze/upload.html", context)
    else:
        return render(request, "eze/upload.html")


def readBarcode(request):

    if request.method == "POST" and request.FILES['bcode']:
        
        myFile = request.FILES['bcode']
        #create file system storage location
        fs = FileSystemStorage(location="media")
        #get the file name of the uploaded file and save the file in the location specified in the fs variable

        filename = fs.save(myFile.name, myFile)
        #name = request.POST['bcode']
        # reading qrcode
        dcode = decode(Image.open("media/"+filename))
        d = str(dcode[0][0])
        lent = len(d)
        solution = (d)[2:lent-1]
        context = {
            "code": solution,

        }
        return render(request, "eze/upload.html", context)


class employeeList(APIView):

    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializers(employee, many=True)

        return Response(serializer.data)


class DepartmentList(APIView):

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializers(department, many=True)

        return Response(serializer.data)
