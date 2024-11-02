from django.contrib import admin

from .models import Choice, Question

list_filter = ["pub_date"]
search_fields = ["question_text"]
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)

# Register your models here.
