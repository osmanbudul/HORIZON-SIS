from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student, StaffMember, SchoolClass, Subject, Attendance, Exam, Result, Fee, Payment, TimetableEntry
from .forms import StudentForm, StaffForm, ClassForm, SubjectForm, AttendanceForm, ExamForm, ResultForm, FeeForm, TimetableForm

@login_required
def dashboard(request):
    today=__import__('datetime').date.today()
    return render(request,'core/dashboard.html',{
      'student_count':Student.objects.filter(status='active').count(), 'staff_count':StaffMember.objects.filter(active=True).count(),
      'class_count':SchoolClass.objects.count(), 'subject_count':Subject.objects.count(),
      'present_today':Attendance.objects.filter(date=today,status='present').count(),
      'absent_today':Attendance.objects.filter(date=today,status='absent').count(),
      'fees_due':sum([f.balance for f in Fee.objects.all()]),
      'recent_students':Student.objects.select_related('school_class').order_by('-created')[:6],
      'attendance_today':Attendance.objects.filter(date=today).select_related('student')[:6], 'today':today,
    })

class SecureList(LoginRequiredMixin,ListView):
    paginate_by=12
    def get_queryset(self):
        qs=super().get_queryset()
        q=self.request.GET.get('q','').strip()
        if q:
            fields=getattr(self,'search_fields',[])
            cond=Q()
            for f in fields: cond |= Q(**{f+'__icontains':q})
            if fields: qs=qs.filter(cond)
        return qs
class SecureCreate(LoginRequiredMixin,CreateView):
    template_name='core/form.html'
    def get_context_data(self,**kwargs):
        c=super().get_context_data(**kwargs); c['page_title']=self.page_title; c['cancel_url']=self.success_url; return c
    def form_valid(self,form): messages.success(self.request,self.success_message); return super().form_valid(form)
class SecureUpdate(LoginRequiredMixin,UpdateView):
    template_name='core/form.html'
    def get_context_data(self,**kwargs):
        c=super().get_context_data(**kwargs); c['page_title']='Edit '+self.page_title; c['cancel_url']=self.success_url; return c
    def form_valid(self,form): messages.success(self.request,'Record updated successfully.'); return super().form_valid(form)
class StudentList(SecureList): model=Student; template_name='core/list.html'; search_fields=['full_name','admission_no','phone']; ordering=['full_name']; extra_context={'page_title':'Students','section':'students','columns':['Admission No.','Student name','Class','Gender','Status']}
class StudentCreate(SecureCreate): model=Student; form_class=StudentForm; success_url=reverse_lazy('students'); page_title='New student'; success_message='Student registered successfully.'
class StudentUpdate(SecureUpdate): model=Student; form_class=StudentForm; success_url=reverse_lazy('students'); page_title='student'
class StaffList(SecureList): model=StaffMember; template_name='core/list.html'; search_fields=['full_name','email','phone']; ordering=['full_name']; extra_context={'page_title':'Staff & Teachers','section':'staff','columns':['Name','Role','Subject','Phone','Status']}
class StaffCreate(SecureCreate): model=StaffMember; form_class=StaffForm; success_url=reverse_lazy('staff'); page_title='Staff member'; success_message='Staff member added.'
class StaffUpdate(SecureUpdate): model=StaffMember; form_class=StaffForm; success_url=reverse_lazy('staff'); page_title='staff member'
class ClassList(SecureList): model=SchoolClass; template_name='core/list.html'; search_fields=['name','room']; ordering=['grade']; extra_context={'page_title':'Classes','section':'classes','columns':['Class','Grade','Room','Students']}
class ClassCreate(SecureCreate): model=SchoolClass; form_class=ClassForm; success_url=reverse_lazy('classes'); page_title='Class'; success_message='Class added.'
class SubjectList(SecureList): model=Subject; template_name='core/list.html'; search_fields=['name','code']; ordering=['name']; extra_context={'page_title':'Subjects','section':'subjects','columns':['Subject','Code']}
class SubjectCreate(SecureCreate): model=Subject; form_class=SubjectForm; success_url=reverse_lazy('subjects'); page_title='Subject'; success_message='Subject added.'
class AttendanceList(SecureList): model=Attendance; template_name='core/list.html'; search_fields=['student__full_name','student__admission_no']; ordering=['-date']; extra_context={'page_title':'Attendance','section':'attendance','columns':['Date','Student','Class','Status']}
class AttendanceCreate(SecureCreate): model=Attendance; form_class=AttendanceForm; success_url=reverse_lazy('attendance'); page_title='Attendance record'; success_message='Attendance saved.'
class ExamList(SecureList): model=Exam; template_name='core/list.html'; search_fields=['name','term']; ordering=['-date']; extra_context={'page_title':'Exams','section':'exams','columns':['Exam','Class','Term','Date']}
class ExamCreate(SecureCreate): model=Exam; form_class=ExamForm; success_url=reverse_lazy('exams'); page_title='Exam'; success_message='Exam created.'
class ResultList(SecureList): model=Result; template_name='core/list.html'; search_fields=['student__full_name','subject__name','exam__name']; ordering=['student__full_name']; extra_context={'page_title':'Exam results','section':'results','columns':['Student','Exam','Subject','Score','Percentage']}
class ResultCreate(SecureCreate): model=Result; form_class=ResultForm; success_url=reverse_lazy('results'); page_title='Exam result'; success_message='Result saved.'
class FeeList(SecureList): model=Fee; template_name='core/list.html'; search_fields=['student__full_name','title','student__admission_no']; ordering=['-created']; extra_context={'page_title':'Fees & Payments','section':'fees','columns':['Student','Fee','Due','Paid','Balance','Status']}
class FeeCreate(SecureCreate): model=Fee; form_class=FeeForm; success_url=reverse_lazy('fees'); page_title='Student fee'; success_message='Fee record created.'
class TimetableList(SecureList): model=TimetableEntry; template_name='core/list.html'; search_fields=['school_class__name','subject__name']; ordering=['day','start_time']; extra_context={'page_title':'Timetable','section':'timetable','columns':['Day','Class','Subject','Teacher','Start','End']}
class TimetableCreate(SecureCreate): model=TimetableEntry; form_class=TimetableForm; success_url=reverse_lazy('timetable'); page_title='Timetable entry'; success_message='Timetable entry saved.'

@login_required
def reports(request):
    return render(request,'core/reports.html',{'students':Student.objects.count(),'staff':StaffMember.objects.count(),'fees':Fee.objects.all(),'attendance':Attendance.objects.count()})

@login_required
def parent_accounts(request):
    if not request.user.is_staff: return redirect('dashboard')
    parents=__import__('django.contrib.auth.models',fromlist=['User']).User.objects.filter(parent_profile__isnull=False).prefetch_related('parent_profile__students')
    return render(request,'core/parents.html',{'parents':parents})

@login_required
def parent_portal(request):
    profile=getattr(request.user,'parent_profile',None)
    if profile is None: return redirect('dashboard')
    children=profile.students.all().select_related('school_class')
    return render(request,'core/parent_portal.html',{'children':children,'attendance':Attendance.objects.filter(student__in=children).order_by('-date')[:30], 'results':Result.objects.filter(student__in=children).select_related('student','exam','subject').order_by('-exam__date')[:50], 'fees':Fee.objects.filter(student__in=children).select_related('student')})
