from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework import status

# Create your views here.

class Home(APIView):
    def get(self, request):
        return Response({'msg': 'This is my Home page'})


class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'msg': 'List of students', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        
        # if data.get('age') < 18:
        #     return Response({'msg': 'Failed: Age should be greater than 18'})
        
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'Validation Error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = StudentSerializer(student)
        return Response({'msg': 'Student record', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record updated successsfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Validation Error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'}, status=status.HTTP_400_BAD_REQUEST)
        
        student.delete()
        return Response({'msg': 'Record deleted successfully'}, status=status.HTTP_200_OK)


