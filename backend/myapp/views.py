from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .data_processor import process_csv, process_json
from rest_framework.response import Response
from .models import FileUpload
import os

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        file_format = file.name.split('.')[-1].lower()

        # Save the uploaded file to the media directory
        file_path = os.path.join('media/uploads/', file.name)
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        if file_format == 'csv':
            data = process_csv(file_path)
        elif file_format == 'json':
            data = process_json(file_path)
        else:
            return Response({"error": "Invalid file format"}, status=400)

        # Optionally save metadata about the file in the database
        FileUpload.objects.create(name=file.name, file=file_path)

        return JsonResponse({"message": "File uploaded successfully", "data": data})
