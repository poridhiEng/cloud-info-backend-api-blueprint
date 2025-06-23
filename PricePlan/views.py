from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricePlan
from .serializers import PricePlanSerializer


"""
    @param request: The HTTP request containing the price plan data.
    @return: A response containing the created price plan data or an error message.
    @raises: HTTP 201 Created if successful, HTTP 400 Bad Request if validation fails.
    
    @param: id UUIDField, primary key, auto-generated.
    @param: name CharField, max_length=100, required.
    @param: price CharField, max_length=6, required.
    @param: credit PositiveSmallIntegerField, required.
    @param: gpu_hours CharField, max_length=6, required.
    @model: PricePlan
"""

class PricePlanList(APIView):
    """
    List all price plans.
    """
    def get(self, request):
        price_plans = PricePlan.objects.all()
        serializer = PricePlanSerializer(price_plans, many=True)
        return Response(serializer.data)


    """
    Create a new price plan.
    """
    def post(self, request):
        serializer = PricePlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PricePlanDetail(APIView):
    """
    Retrieve, update or delete a price plan instance.
    """
   
    def get_object(self, pk):
        try:
            return PricePlan.objects.get(pk=pk)
        except PricePlan.DoesNotExist:
            return None

    def get(self, request, pk):
        price_plan = self.get_object(pk)
        if price_plan is not None:
            serializer = PricePlanSerializer(price_plan)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        price_plan = self.get_object(pk)
        if price_plan is not None:
            serializer = PricePlanSerializer(price_plan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        price_plan = self.get_object(pk)
        if price_plan is not None:
            price_plan.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
