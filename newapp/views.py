from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import ContactSubmissionSerializer
from . models import UsersModel
from . utils import send_contact_email

class ContactSubmissionAPIView(APIView):
    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            send_contact_email(contact.name, contact.phone, contact.email)
            return Response({"message": "Submission successful and email sent."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
