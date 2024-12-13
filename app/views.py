from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Student
from app.serializers import StudentSerializer

# Create your views here.

class Home(APIView):
    def get(self, request):
        return Response({'msg': 'This is my Home page'})


class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'msg': 'List of students', 'data': serializer.data})
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record created successfully', 'data': serializer.data})


class StudentDetailView(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'})
        
        serializer = StudentSerializer(student)
        return Response({'msg': 'Student record', 'data': serializer.data})
    
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'})
        
        data = request.data
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record updated successsfully', 'data': serializer.data})
        return Response({'msg': 'Validation Error', 'error': serializer.errors})
    
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Invalid id'})
        
        student.delete()
        return Response({'msg': 'Record deleted successfully'})


