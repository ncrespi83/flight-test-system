from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Requirement, TestPlan, TestEvent, TestPoint
from .serializers import (
    RequirementSerializer,
    TestPlanSerializer,
    TestEventSerializer,
    TestPointSerializer,
    TestPlanDetailSerializer,
)

#provides CRUD endpoints for Requirements
class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all().order_by("id")
    serializer_class = RequirementSerializer
    
#provides CRUD endpoints for TestPoints
class TestPointViewSet(viewsets.ModelViewSet):
    #allows user to create points that link to a plan + requirements using FK ids
    queryset = TestPoint.objects.all().order_by("id")
    serializer_class = TestPointSerializer
    
#provides CRUD endpoints for TestEvents
class TestEventViewSet(viewsets.ModelViewSet):
    #allows user to schedule/execute/cancel events and associate them w/ a TestPlan
    queryset = TestEvent.objects.all().order_by("-scheduled_for", "-id")
    serializer_class = TestEventSerializer
    
#provides CRUD endpoints for TestPlans
class TestPlanViewSet(viewsets.ModelViewSet):
    """
    nested serializer utilized for "retrieve" (aka detail view) so frontend
    can load a plan and its related test points/events in one request
    """
    queryset = TestPlan.objects.all().order_by("-created_at")
    
    #list/create uses a lighter serializer; detail uses nested data
    def get_serializer_class(self):
        if self.action == "retrieve":
            return TestPlanDetailSerializer
        return TestPlanSerializer
    
    """
    POST /api/testplans/<id>/approve/
    
    used to simulate a workflow operation beyond basic CRUD for a real system
    by adding a method based behaivor for associated domain action
    """
    @action(detail = True, methods = ["post"])
    def approve(self, request, pk = None):
        plan = self.get_object()
       
        #require at least one test point before approval
        if plan.test_points.count() == 0:
            return Response(
                {"detail": "Cannot approve a TestPlan with zero test points."},
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        plan.status = "AP"
        plan.save(update_fields = ["status"])
        
        serializer = TestPlanSerializer(plan)
        return Response(serializer.data, status = status.HTTP_200_OK)