from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Machine
from .serializers import MachineSerializer

"""
    @param request: The HTTP request containing the machine data.
    @return: A response containing the created machine data or an error message.
    @raises: HTTP 201 Created if successful, HTTP 400 Bad Request if validation fails.
    @param: id UUIDField, primary key, auto-generated.
    @param: cpu PositiveIntegerField, required. 
    @param: memory PositiveIntegerField, required.
    @param: gpu_count PositiveIntegerField, required.
    @param: gpu_model CharField, max_length=20, required.
    @param: credit PositiveSmallIntegerField, required.
    @model: Machine
"""

# Create your views here.
class MachineList(APIView):
    """
    List all machines.
    """
    def get(self, request):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    """
    Create a new machine.
    """
    def post(self, request):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MachineDetail(APIView):
    """
    Retrieve, update or delete a machine instance.
    """

    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            return None

    def get(self, request, pk):
        machine = self.get_object(pk)
        if machine is not None:
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        machine = self.get_object(pk)
        if machine is not None:
            serializer = MachineSerializer(machine, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        machine = self.get_object(pk)
        if machine is not None:
            machine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
