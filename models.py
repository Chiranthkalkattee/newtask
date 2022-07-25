from django.db import models

# Create your models here.

class Candidate_details(models.Model):
    gender_choice = (
        ('male', 'male'),
        ('Female', 'Female')
    )
    skill_choice = (
        ('python','python'),
        ('java','java'),
        ('c','c')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=25, choices=gender_choice, default='fill')
    skills = models.CharField(max_length=25, choices=skill_choice, default='fill the skills')

    def self(self):
        return self.name

class skill_details(models.Model):
    u_skill_choice = (
        ('django','django'),
        ('nodejs','nodejs'),
        ('express','express')
    )
    skill_name = models.ForeignKey(Candidate_details,related_name='skill',on_delete=models.CASCADE)
    updated_skills = models.CharField(max_length=200,choices=u_skill_choice,default='fill')
    level = models.IntegerField(default=0)

    def __str__(self):
       return self.updated_skills
