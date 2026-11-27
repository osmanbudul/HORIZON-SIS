from django.db import models
from django.contrib.auth.models import User

class SchoolClass(models.Model):
    name=models.CharField(max_length=60,unique=True)
    grade=models.PositiveSmallIntegerField(default=1)
    room=models.CharField(max_length=30,blank=True)
    class Meta: ordering=['grade','name']
    def __str__(self): return self.name

class Subject(models.Model):
    name=models.CharField(max_length=80,unique=True)
    code=models.CharField(max_length=12,blank=True)
    def __str__(self): return self.name

class Student(models.Model):
    GENDER=[('M','Male'),('F','Female')]
    STATUS=[('active','Active'),('inactive','Inactive'),('graduated','Graduated')]
    admission_no=models.CharField(max_length=24,unique=True)
    full_name=models.CharField(max_length=140)
    gender=models.CharField(max_length=1,choices=GENDER)
    date_of_birth=models.DateField(null=True,blank=True)
    email=models.EmailField(blank=True)
    phone=models.CharField(max_length=30,blank=True)
    school_class=models.ForeignKey(SchoolClass,on_delete=models.SET_NULL,null=True,related_name='students')
    status=models.CharField(max_length=12,choices=STATUS,default='active')
    address=models.CharField(max_length=220,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['full_name']
    def __str__(self): return f'{self.admission_no} - {self.full_name}'

class StaffMember(models.Model):
    ROLE=[('teacher','Teacher'),('admin','Administrator'),('support','Support Staff'),('other','Other')]
    full_name=models.CharField(max_length=140)
    role=models.CharField(max_length=12,choices=ROLE,default='teacher')
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True)
    phone=models.CharField(max_length=30,blank=True)
    email=models.EmailField(blank=True)
    joined=models.DateField(null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self): return self.full_name

class ParentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='parent_profile')
    phone=models.CharField(max_length=30,blank=True)
    students=models.ManyToManyField(Student,related_name='parents',blank=True)
    def __str__(self): return self.user.get_username()

class Attendance(models.Model):
    STATUS=[('present','Present'),('absent','Absent'),('late','Late'),('excused','Excused')]
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendance_records')
    date=models.DateField()
    status=models.CharField(max_length=10,choices=STATUS,default='present')
    note=models.CharField(max_length=220,blank=True)
    class Meta:
        ordering=['-date','student__full_name']
        constraints=[models.UniqueConstraint(fields=['student','date'],name='unique_student_attendance_per_day')]
    def __str__(self): return f'{self.student} - {self.date} - {self.status}'

class Exam(models.Model):
    name=models.CharField(max_length=100)
    school_class=models.ForeignKey(SchoolClass,on_delete=models.CASCADE)
    date=models.DateField(null=True,blank=True)
    term=models.CharField(max_length=40,blank=True)
    def __str__(self): return f'{self.name} - {self.school_class}'

class Result(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='results')
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='results')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    score=models.DecimalField(max_digits=5,decimal_places=2)
    max_score=models.DecimalField(max_digits=5,decimal_places=2,default=100)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['exam','student','subject'],name='unique_exam_student_subject')]
    @property
    def percentage(self): return round(float(self.score)/float(self.max_score)*100,1) if self.max_score else 0
    def __str__(self): return f'{self.student} - {self.subject}: {self.score}'

class Fee(models.Model):
    STATUS=[('paid','Paid'),('partial','Partially Paid'),('pending','Pending')]
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='fees')
    title=models.CharField(max_length=100,default='School Fee')
    amount_due=models.DecimalField(max_digits=10,decimal_places=2)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    due_date=models.DateField(null=True,blank=True)
    created=models.DateField(auto_now_add=True)
    @property
    def balance(self): return self.amount_due-self.amount_paid
    @property
    def status(self):
        if self.amount_paid>=self.amount_due: return 'paid'
        if self.amount_paid>0: return 'partial'
        return 'pending'
    def __str__(self): return f'{self.student} - {self.title}'

class Payment(models.Model):
    fee=models.ForeignKey(Fee,on_delete=models.CASCADE,related_name='payments')
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField(auto_now_add=True)
    reference=models.CharField(max_length=60,blank=True)
    received_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    def save(self,*args,**kwargs):
        is_new=self.pk is None
        super().save(*args,**kwargs)
        if is_new:
            total=self.fee.payments.aggregate(total=models.Sum('amount'))['total'] or 0
            self.fee.amount_paid=total
            self.fee.save(update_fields=['amount_paid'])
    def __str__(self): return f'{self.fee} - {self.amount}'

class TimetableEntry(models.Model):
    DAYS=[('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Saturday','Saturday'),('Sunday','Sunday')]
    school_class=models.ForeignKey(SchoolClass,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    staff=models.ForeignKey(StaffMember,on_delete=models.SET_NULL,null=True,blank=True)
    day=models.CharField(max_length=12,choices=DAYS)
    start_time=models.TimeField()
    end_time=models.TimeField()
    def __str__(self): return f'{self.school_class} {self.day} {self.subject}'
