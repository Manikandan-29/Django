#from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from .serializers import SubjectDetailsSerializer
from .models import StudentDetails
from .serializers import StudentDetailsSerializer


# APIView for Users Table
class usersViewset(APIView):
    def get(self, request):
        # Extract reg_emp_id and password from query parameters
        reg_emp_id = request.query_params.get('reg_emp_id')
        password = request.query_params.get('password')

        # Debugging logs
        print(f"Query Params - reg_emp_id: {reg_emp_id}, password: {password}")

        # If both reg_emp_id and password are provided
        if reg_emp_id and password:
            try:
                # Check for user with matching reg_emp_id and password
                user = models.users.objects.get(reg_emp_id=reg_emp_id, password=password)
                print(f"Debug: User Found - {user}")

                # Fetch additional student details
                student_details = StudentDetails.objects.get(reg_emp_id=reg_emp_id)

                # Serialize the user and student details
                user_serializer = serializers.usersSerializer(user)
                student_serializer = serializers.StudentDetailsSerializer(student_details)

                # Combine the results into one response
                return Response({
                    "status": "success",
                    "data": {
                        "user": user_serializer.data,
                        "student_details": student_serializer.data
                    }
                }, status=status.HTTP_200_OK)

            except models.users.DoesNotExist:
                return Response({"status": "error", "data": "User not found or incorrect password"}, status=status.HTTP_404_NOT_FOUND)
            except StudentDetails.DoesNotExist:
                return Response({"status": "error", "data": "Student details not found"}, status=status.HTTP_404_NOT_FOUND)

        # If no filters, return all users
        queryset = models.users.objects.all()
        serializer = serializers.usersSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
   # def patch(self, request, id=None):
    #    user = models.users.objects.get(id=id)
     #   serializer = serializers.usersSerializer(user, data=request.data, partial=True)
     #   if serializer.is_valid():
      ##      serializer.save()
      #      return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     #   return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        try:
            user = models.users.objects.get(id=id)
            serializer = serializers.usersSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except models.users.DoesNotExist:
            return Response({"status": "error", "data": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id=None):
        user = models.users.objects.filter(id=id)
        user.delete()
        return Response({"status": "success", "data": "User Deleted"}, status=status.HTTP_200_OK)
# APIView for Student Details Table
class StudentDetailsViewset(APIView):
    def get(self, request, reg_emp_id=None):
        if reg_emp_id:
            try:
                student = models.StudentDetails.objects.get(reg_emp_id=reg_emp_id)
                serializer = serializers.StudentDetailsSerializer(student)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except models.StudentDetails.DoesNotExist:
                return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        # If reg_emp_id is not provided, return all students
        students = models.StudentDetails.objects.all()
        serializer = serializers.StudentDetailsSerializer(students, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = serializers.StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        student = models.StudentDetails.objects.get(id=id)
        serializer = serializers.StudentDetailsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, reg_emp_id=None):
        """
        Update a student's details based on their reg_emp_id.
        """
        if reg_emp_id:
            try:
                # Find the student using reg_emp_id
                student = models.StudentDetails.objects.get(reg_emp_id=reg_emp_id)
            except models.StudentDetails.DoesNotExist:
                return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Create or update the student data using the serializer
            serializer = serializers.StudentDetailsSerializer(student, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  # Save the updated student details
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"status": "error", "data": "reg_emp_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        student = models.StudentDetails.objects.filter(id=id)
        student.delete()
        return Response({"status": "success", "data": "Student Deleted"}, status=status.HTTP_200_OK)
class SubjectDetailsViewset(APIView):
    def get(self, request, reg_emp_id=None):
        try:
            # Get subject details for the provided reg_emp_id
            subject_details = models.SubjectDetails.objects.get(reg_emp_id=reg_emp_id)
            serializer = serializers.SubjectDetailsSerializer(subject_details)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except models.SubjectDetails.DoesNotExist:
            return Response({"status": "error", "data": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the error to the console or logs for debugging
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        # Deserialize the incoming data
        serializer = SubjectDetailsSerializer(data=request.data)
        
        # Check if the data is valid
        if serializer.is_valid():
            # Save the new subject details
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return error response
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
