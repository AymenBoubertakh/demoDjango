from django.test import TestCase
from students.models import Student, University

class StudentTestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.university = University.objects.create(name="Test University")
        self.student = Student.objects.create(
            name="Test Student",
            address="Test Address",
            university=self.university
        )
    
    def test_student_creation(self):
        """Test that a student can be created"""
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.address, "Test Address")
        self.assertEqual(self.student.university.name, "Test University")
    
    def test_student_count(self):
        """Test that we can count students"""
        count = Student.objects.count()
        self.assertEqual(count, 1)
    
    def test_university_students(self):
        """Test university-student relationship"""
        students = self.university.students.all()
        self.assertEqual(students.count(), 1)
        self.assertEqual(students.first().name, "Test Student")

class UniversityTestCase(TestCase):
    def test_university_creation(self):
        """Test that a university can be created"""
        university = University.objects.create(name="Harvard")
        self.assertEqual(university.name, "Harvard")
        self.assertEqual(University.objects.count(), 1)
