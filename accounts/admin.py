from django.contrib import admin
from .models import User, Faculty, Group, Student

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    search_fields = ('name', 'faculty__name')
    list_filter = ('faculty',)
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'group', 'student_type', 'student_enrollment')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone', 'group__name')
    list_filter = ('student_type', 'student_enrollment', 'group__faculty')
    ordering = ('user__username',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'group')