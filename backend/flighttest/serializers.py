from rest_framework import serializers 
from .models import Requirement, TestEvent, TestPlan, TestPoint

#represents Requirement as JSON, validates incoming requirement payloads
class RequirementSerializer(serializers.ModelSerializer):
    
    #Adds status_display so the frontend doesn't need to map codes -> labels
    status_display = serializers.CharField(source = "get_status_display", read_only = True)
   
    class Meta:
        model = Requirement
        fields = "__all__"
    
#represents TestPlan as JSON for list/create endpoints
class TestPlanSerializer(serializers.ModelSerializer):
    
    #Adds status_display for UI usage
    status_display = serializers.CharField(source = "get_status_display", read_only = True)

    class Meta:
        model = TestPlan
        fields = "__all__"

#represents TestPoint as JSON, validates references to TestPlan/Requirement via FK IDs
class TestPointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestPoint
        fields = "__all__"

#represents TestEvent as JSON, validates scheduled_for & status choices         
class TestEventSerializer(serializers.ModelSerializer):
    
    #Adds status_display for UI usage
    status_display = serializers.CharField(source = "get_status_display", read_only = True)
    
    class Meta:
        model = TestEvent
        fields = "__all__"

#provides single payload for frontend by nesting test_points and events
class TestPlanDetailSerializer(serializers.ModelSerializer):
    test_points = TestPointSerializer(many = True, read_only = True)
    events = TestEventSerializer(many = True, read_only = True)
    
    class Meta:
        model = TestPlan
        fields = "__all__"