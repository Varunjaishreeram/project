from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vendor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import VendorSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
import json

@csrf_exempt
@api_view(['GET', 'POST'])
def home(request):
    if request.method == "POST":
        try:
            # Decode JSON data from the request body
            json_data = json.loads(request.body.decode('utf-8'))

            # Extract vendor details from JSON data
            name = json_data.get('name')
            contact_details = json_data.get('contact_details')
            address = json_data.get('address')

            # Create a new Vendor instance
            new_vendor = Vendor(
                name=name,
                contact_details=contact_details,
                address=address,
            )

            # Save the new vendor to the database
            new_vendor.save()

            return HttpResponse("Vendor created successfully", status=201)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
    
    
    
    elif request.method=="GET":
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        response_data = serializer.data
        print(response_data)
        return Response(response_data)
        
    else:
        return HttpResponse("This is the home page")

@api_view(['GET', 'POST','PUT','DELETE'])
def retrieve_vendor(request,vendor_id):
    vendor = get_object_or_404(Vendor, vendor_code=vendor_id)

    print(vendor)
    
    if request.method=="GET":
        
        serializer = VendorSerializer(vendor)
        if serializer:
            
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
    
    elif request.method=="PUT":
        
        serializer = VendorSerializer(instance=vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=="DELETE":
        
        if vendor:
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




    



