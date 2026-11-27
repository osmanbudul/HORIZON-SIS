from django import forms
from .models import Student, StaffMember, SchoolClass, Subject, Attendance, Exam, Result, Fee, TimetableEntry
class StyledModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-select' if isinstance(field.widget,forms.Select) else 'form-control'
class StudentForm(StyledModelForm):
    class Meta:
        model=Student; fields=['admission_no','full_name','gender','date_of_birth','email','phone','school_class','status','address']
        widgets={'date_of_birth':forms.DateInput(attrs={'type':'date'})}
class StaffForm(StyledModelForm):
    class Meta: model=StaffMember; fields=['full_name','role','subject','phone','email','joined','active']; widgets={'joined':forms.DateInput(attrs={'type':'date'})}
class ClassForm(StyledModelForm):
    class Meta: model=SchoolClass; fields=['name','grade','room']
class SubjectForm(StyledModelForm):
    class Meta: model=Subject; fields=['name','code']
class AttendanceForm(StyledModelForm):
    class Meta: model=Attendance; fields=['student','date','status','note']; widgets={'date':forms.DateInput(attrs={'type':'date'})}
class ExamForm(StyledModelForm):
    class Meta: model=Exam; fields=['name','school_class','date','term']; widgets={'date':forms.DateInput(attrs={'type':'date'})}
class ResultForm(StyledModelForm):
    class Meta: model=Result; fields=['exam','student','subject','score','max_score']
class FeeForm(StyledModelForm):
    class Meta: model=Fee; fields=['student','title','amount_due','amount_paid','due_date']; widgets={'due_date':forms.DateInput(attrs={'type':'date'})}
class TimetableForm(StyledModelForm):
    class Meta: model=TimetableEntry; fields=['school_class','subject','staff','day','start_time','end_time']; widgets={'start_time':forms.TimeInput(attrs={'type':'time'}),'end_time':forms.TimeInput(attrs={'type':'time'})}
