from rest_framework import serializers

# Define a serializer for file metadata (optional)
class FileUploadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    file_url = serializers.CharField(max_length=255)
    uploaded_at = serializers.DateTimeField()

# Define a serializer to handle processed data (optional)
class DataSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.DictField())

    # Example for serializing a specific structure:
    # column_1 = serializers.CharField(max_length=100)
    # column_2 = serializers.IntegerField()

    # Add more fields as necessary for your dataset
