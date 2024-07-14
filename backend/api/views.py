from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from .models import Company

# Create your views here.

class IndexApi(View):
    def get(self, request):
        return JsonResponse({"pesan": "Sukses cok"})
    
class SendData(View):
    def post(self, request):
        return JsonResponse({"pesan": "Data Berhasil di Post"})
    
    @csrf_exempt
    def receive_data(request):
        data = json.loads(request)
        print("Data diterima:", data)
        return JsonResponse({'status': 'success', 'data': data})
    

class CompanyRegestration(APIView):
    def post(self, request):
        print(f"Request Data: {request.data}")  # Debugging input data
        serializer = CompanySerializers(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                print(f"Validated Data: {validated_data}")  # Debugging validated data
                company = serializer.save()  # Simpan data ke model Company
                print(f"Saved Company: {company}")  # Debugging saved company
                return Response({'status': 'Data Received', 'company': CompanySerializers(company).data}, status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Error during save: {e}")  # Debugging error
                return Response({'status': 'Save Failed', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print(serializer.errors)  # Cetak kesalahan untuk debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializers(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

