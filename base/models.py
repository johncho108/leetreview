from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import tree

# Create your models here.

class Entry(models.Model):
    
    SOURCE_CHOICES= (
        ('LeetCode', 'LeetCode'),
        ('HackerRank', 'HackerRank'),
        ('Codewars', 'Codewars'),
        ('Other', 'Other'),
    )

    TOPIC_CHOICES= (
        ('Arrays', 'Arrays'),
        ('Hashmaps', 'Hashmaps'),
        ('Strings', 'Strings'),
        ('Linked Lists', 'Linked Lists'),
        ('Stacks/Queues', 'Stacks/Queues'),
        ('Trees', 'Trees'),
        ('Graphs', 'Graphs'),
        ('Sorting', 'Sorting'),
        ('Searching', 'Searching'),
        ('Greedy', 'Greedy'),
        ('Recursion/Backtracking', 'Recursion/Backtracking'),
        ('Dynamic Programming', 'Dynamic Programming'),
        ('Bit Manipulation', 'Bit Manipulation'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True, choices=SOURCE_CHOICES)
    link = models.URLField(max_length=200, null=True)
    topic = models.CharField(max_length=200, null=True, choices=TOPIC_CHOICES)
    user_code = models.TextField(null=True)
    optimized_code = models.TextField(null=True)
    user_notes = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[0:50]

