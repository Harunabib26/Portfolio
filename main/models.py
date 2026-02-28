from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    impact = models.CharField(max_length=200)
    description = models.TextField()
    stack = models.CharField(max_length=200, help_text="Comma separated skills")
    demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_stack_list(self):
        return [s.strip() for s in self.stack.split(',')]

class SkillCategory(models.Model):
    name = models.CharField(max_length=100) # e.g. Backend, Frontend

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name}: {self.name}"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    impact = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
