from django.urls import path
from . import views as v
urlpatterns=[
 path('',v.dashboard,name='dashboard'),
 path('students/',v.StudentList.as_view(),name='students'),path('students/add/',v.StudentCreate.as_view(),name='student_add'),path('students/<int:pk>/edit/',v.StudentUpdate.as_view(),name='student_edit'),
 path('staff/',v.StaffList.as_view(),name='staff'),path('staff/add/',v.StaffCreate.as_view(),name='staff_add'),path('staff/<int:pk>/edit/',v.StaffUpdate.as_view(),name='staff_edit'),
 path('classes/',v.ClassList.as_view(),name='classes'),path('classes/add/',v.ClassCreate.as_view(),name='class_add'),path('subjects/',v.SubjectList.as_view(),name='subjects'),path('subjects/add/',v.SubjectCreate.as_view(),name='subject_add'),
 path('attendance/',v.AttendanceList.as_view(),name='attendance'),path('attendance/add/',v.AttendanceCreate.as_view(),name='attendance_add'),
 path('exams/',v.ExamList.as_view(),name='exams'),path('exams/add/',v.ExamCreate.as_view(),name='exam_add'),path('results/',v.ResultList.as_view(),name='results'),path('results/add/',v.ResultCreate.as_view(),name='result_add'),
 path('fees/',v.FeeList.as_view(),name='fees'),path('fees/add/',v.FeeCreate.as_view(),name='fee_add'),path('timetable/',v.TimetableList.as_view(),name='timetable'),path('timetable/add/',v.TimetableCreate.as_view(),name='timetable_add'),
 path('reports/',v.reports,name='reports'),path('parents/',v.parent_accounts,name='parent_accounts'),path('parent-portal/',v.parent_portal,name='parent_portal'),
]
