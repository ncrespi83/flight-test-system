from django.db import models
    
class Requirement(models.Model):
    text = models.TextField()

    REQ_CHOICES = [
        ("DR", "Draft"),
        ("AP", "Approved"),
    ]
    
    status = models.CharField(max_length=2, choices=REQ_CHOICES,default="DR")
    
    def __str__(self):
        return self.text
    
class TestPlan(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #timestamp for creation of test plan
    
    PLAN_CHOICES = [
        ("DR", "Draft"),
        ("IR", "In Review"),
        ("AP", "Approved"),
    ]
    
    status = models.CharField(max_length=2, choices=PLAN_CHOICES, default="DR")
    
    def __str__(self):
        return self.name

#belongs to a TestPlan
class TestEvent(models.Model):
    scheduled_for = models.DateTimeField(
        null=True, 
        blank=True, 
        help_text="Date & time this event should be executed."
    ) #timestamp for scheduled date and time
    
    EVENT_CHOICES = [
        ("SC", "Scheduled"),
        ("EX", "Executed"),
        ("CX", "Cancelled"),
    ]
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE, related_name="events")
    status = models.CharField(max_length=2, choices=EVENT_CHOICES, default="SC")
    
    def __str__(self):
        return f"{self.test_plan.name} -> {self.scheduled_for}"

#belongs to a TestPlan, links to a Requirement 
class TestPoint(models.Model):
    title = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)     #optional field
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)    #optional field
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE, related_name="test_points")
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name="test_points")
    
    def coordinates(self):
        return (self.latitude, self.longitude)
    
    def __str__(self):
        return self.title
    
     
