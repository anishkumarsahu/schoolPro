from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User


class SchoolOwner(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    userGroup = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'a) School Owner.'


class SchoolDetail(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    logo = StdImageField(upload_to="SchoolLogo", blank=True, null=True,
                         variations={'thumbnail': {'width': 250, 'height': 250}})
    address = models.TextField()
    city = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    pinCode = models.CharField(max_length=15, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    ownerID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'b) School Detail.'


class SchoolSocialLink(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    ownerID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=500, blank=True, null=True, default='NaN')
    twitter = models.CharField(max_length=500, blank=True, null=True, default='NaN')
    googlePlus = models.CharField(max_length=500, blank=True, null=True, default='NaN')
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.schoolID.name)

    class Meta:
        verbose_name_plural = 'c) School Social Links.'


class SchoolSession(models.Model):
    sessionYear = models.CharField(max_length=500, blank=True, null=True)
    isCurrent = models.BooleanField(default=False)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.sessionYear

    class Meta:
        verbose_name_plural = 'd) School Session.'


class ComputerOperator(models.Model):
    firstName = models.CharField(max_length=500, blank=True, null=True)
    middleName = models.CharField(max_length=500, blank=True, null=True)
    lastName = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    pinCode = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    aadhar = models.CharField(max_length=500, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=500, blank=True, null=True)
    joinDate = models.DateField(blank=True, null=True)
    releaveDate = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    photo = StdImageField(upload_to="OperatorImage", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = 'e) Computer Operator.'


class NonTeachingStaff(models.Model):
    firstName = models.CharField(max_length=500, blank=True, null=True)
    middleName = models.CharField(max_length=500, blank=True, null=True)
    lastName = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    pinCode = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    aadhar = models.CharField(max_length=500, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=500, blank=True, null=True)
    bloodGroup = models.CharField(max_length=500, blank=True, null=True)
    EmployeeCode = models.CharField(max_length=500, blank=True, null=True)
    currentPosition = models.CharField(max_length=500, blank=True, null=True)
    qualification = models.CharField(max_length=500, blank=True, null=True)
    joinDate = models.DateField(blank=True, null=True)
    releaveDate = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    photo = StdImageField(upload_to="NonTeachingStaff", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = 'f) Non- Teaching Staff.'


class TeacherDetail(models.Model):
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=500, blank=True, null=True)
    middleName = models.CharField(max_length=500, blank=True, null=True)
    lastName = models.CharField(max_length=500, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    aadhar = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=500, blank=True, null=True)
    bloodGroup = models.CharField(max_length=500, blank=True, null=True)
    presentAddress = models.TextField(blank=True, null=True)
    presentPinCode = models.CharField(max_length=500, blank=True, null=True)
    presentCity = models.CharField(max_length=500, blank=True, null=True)
    presentState = models.CharField(max_length=500, blank=True, null=True)
    presentCountry = models.CharField(max_length=500, blank=True, null=True)
    permanentAddress = models.TextField(blank=True, null=True)
    permanentPinCode = models.CharField(max_length=500, blank=True, null=True)
    permanentCity = models.CharField(max_length=500, blank=True, null=True)
    permanentState = models.CharField(max_length=500, blank=True, null=True)
    permanentCountry = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    photo = StdImageField(upload_to="TeacherImage", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    username = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    dateOfJoining = models.DateField(blank=True, null=True)
    dateOfLeaving = models.DateField(blank=True, null=True)
    currentPosition = models.CharField(max_length=500, blank=True, null=True)
    EmployeeCode = models.CharField(max_length=500, blank=True, null=True)
    qualification = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = 'g) Teachers Details'


class Standard(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    classLocation = models.CharField(max_length=500, blank=True, null=True, default='No Data')
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    hasSection = models.CharField(max_length=500, blank=True, null=True)
    startingRoll = models.CharField(max_length=500, blank=True, null=True)
    endingRoll = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + self.sessionID.sessionYear

    class Meta:
        verbose_name_plural = 'h) Standard Details'


class Section(models.Model):
    standardID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True, null=True)
    startingRoll = models.CharField(max_length=500, blank=True, null=True)
    endingRoll = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'i) Section Details'


class AssignTeacherToClassOrSection(models.Model):
    standardID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    classTeacher = models.ForeignKey(TeacherDetail, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isAssign = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'j)Assign Teacher To Class Or Section'


class ParentDetail(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    fatherFirstName = models.CharField(max_length=500, blank=True, null=True)
    fatherMiddleName = models.CharField(max_length=500, blank=True, null=True)
    fatherLastName = models.CharField(max_length=500, blank=True, null=True)
    motherFirstName = models.CharField(max_length=500, blank=True, null=True)
    motherMiddleName = models.CharField(max_length=500, blank=True, null=True)
    motherLastName = models.CharField(max_length=500, blank=True, null=True)
    occupation = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.fatherFirstName

    class Meta:
        verbose_name_plural = 'k) Parent Details'


class StudentDetail(models.Model):
    firstName = models.CharField(max_length=500, blank=True, null=True)
    middleName = models.CharField(max_length=500, blank=True, null=True)
    lastName = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    aadhar = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=500, blank=True, null=True)
    bloodGroup = models.CharField(max_length=500, blank=True, null=True)
    presentAddress = models.TextField(blank=True, null=True)
    presentPinCode = models.CharField(max_length=500, blank=True, null=True)
    presentCity = models.CharField(max_length=500, blank=True, null=True)
    presentState = models.CharField(max_length=500, blank=True, null=True)
    presentCountry = models.CharField(max_length=500, blank=True, null=True)
    permanentAddress = models.TextField(blank=True, null=True)
    permanentPinCode = models.CharField(max_length=500, blank=True, null=True)
    permanentCity = models.CharField(max_length=500, blank=True, null=True)
    permanentState = models.CharField(max_length=500, blank=True, null=True)
    permanentCountry = models.CharField(max_length=500, blank=True, null=True)
    parentID = models.ForeignKey(ParentDetail, blank=True, null=True, on_delete=models.CASCADE)
    standardID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    rollNumber = models.CharField(max_length=500, blank=True, null=True)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    photo = StdImageField(upload_to="StudentImage", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    username = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    dateOfJoining = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    uniqueKey = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = 'l) Student Details'


class TeacherAttendance(models.Model):
    isAbsent = models.BooleanField(default=False)
    teacherID = models.ForeignKey(TeacherDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    attendanceDate = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'm) Teacher Attendance.'


class Subject(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    subjectName = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.subjectName

    class Meta:
        verbose_name_plural = 'n) Subject'


class AssignClassSubject(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    subjectID = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    classID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.subjectID.subjectName

    class Meta:
        verbose_name_plural = 'o) Assign Class Subject'


class StudentAttendance(models.Model):
    isAbsent = models.BooleanField(default=False)
    studentID = models.ForeignKey(StudentDetail, blank=True, null=True, on_delete=models.CASCADE)
    standardID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    subjectID = models.ForeignKey(AssignClassSubject, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    attendanceDate = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'p) Student Attendance'


class AssignSubjectToTeacher(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    subjectID = models.ForeignKey(AssignClassSubject, blank=True, null=True, on_delete=models.CASCADE)
    classID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    teacherID = models.ForeignKey(TeacherDetail, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'q) Assign Subject To Teacher'


class ExamList(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    examName = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.examName

    class Meta:
        verbose_name_plural = 'r) Exam List'


class Exam(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    classID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    examID = models.ForeignKey(ExamList, blank=True, null=True, on_delete=models.CASCADE)
    startExamDate = models.DateField(blank=True, null=True)
    endExamDate = models.DateField(blank=True, null=True)
    fullMark = models.CharField(max_length=500, blank=True, null=True)
    passMark = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.examID.examName

    class Meta:
        verbose_name_plural = 's) Exam'


class AssignExamSubject(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    examID = models.ForeignKey(Exam, blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    fullMark = models.CharField(max_length=500, blank=True, null=True)
    passMark = models.CharField(max_length=500, blank=True, null=True)
    examDate = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 't) AssignExamSubject'


class MarkOfStudentsByExam(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    examID = models.ForeignKey(Exam, blank=True, null=True, on_delete=models.CASCADE)
    studentID = models.ForeignKey(StudentDetail, blank=True, null=True, on_delete=models.CASCADE)
    standardID = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.CASCADE)
    sectionID = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    subjectID = models.ForeignKey(AssignClassSubject, blank=True, null=True, on_delete=models.CASCADE)
    mark = models.CharField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'u) Mark Of Students By Exam'


class Event(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'v) Event'


class StudentFee(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    studentID = models.ForeignKey(StudentDetail, blank=True, null=True, on_delete=models.CASCADE)
    month = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    payDate = models.DateField(blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'w) Student Fee'


class SendSms(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    to = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)
