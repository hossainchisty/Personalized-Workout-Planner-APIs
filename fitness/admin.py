from django.contrib import admin
from fitness.models import Exercise, WorkoutPlan, WorkoutPlanExercise, Tracking

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanExercise)
admin.site.register(Tracking)
