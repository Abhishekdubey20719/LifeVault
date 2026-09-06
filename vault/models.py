from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# -----------------------
# Documents
# -----------------------

CATEGORY_CHOICES = [

    ('Personal', 'Personal'),

    ('Education', 'Education'),

    ('Career', 'Career'),

    ('Finance', 'Finance'),

    ('Medical', 'Medical'),

    ('Others', 'Others'),

]

class Document(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    file = models.FileField(
        upload_to='documents/'
    )

    description = models.TextField(
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title    
    
# ==========================
# PASSWORD VAULT
# ==========================

class Password(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='vault_passwords'
)

    title = models.CharField(
        max_length=100
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    username = models.CharField(
        max_length=150
    )

    password = models.CharField(
        max_length=255
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    favorite = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title
    
# ==========================================
# CALENDAR EVENT
# ==========================================

class Event(models.Model):

    COLOR_CHOICES = [

    ('primary', 'Blue'),

    ('success', 'Green'),

    ('danger', 'Red'),

    ('warning', 'Yellow'),

    ('purple', 'Purple'),

]

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name='calendar_events'

    )

    title = models.CharField(

        max_length=200

    )

    description = models.TextField(

        blank=True,

        null=True

    )

    date = models.DateField()


    location = models.CharField(

        max_length=255,

        blank=True,

        null=True

    )

    color = models.CharField(

        max_length=20,

        choices=COLOR_CHOICES,

        default='blue'

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    def __str__(self):

        return self.title    
    

# ==========================================
# TASKS
# ==========================================

class Task(models.Model):

    PRIORITY_CHOICES = [

        ('Low', 'Low'),

        ('Medium', 'Medium'),

        ('High', 'High'),

    ]

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Completed', 'Completed'),

    ]

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name='tasks'

    )

    title = models.CharField(

        max_length=200

    )

    description = models.TextField(

        blank=True,

        null=True

    )

    due_date = models.DateField()

    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES,

        default='Medium'

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='Pending'

    )

    favorite = models.BooleanField(

        default=False

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    def __str__(self):

        return self.title
    
# ==========================================
# EXPENSE TRACKER
# ==========================================

class Transaction(models.Model):

    TYPE_CHOICES = [

        ('Income', 'Income'),

        ('Expense', 'Expense'),

    ]

    CATEGORY_CHOICES = [

        # Income

        ('Salary', 'Salary'),

        ('Business', 'Business'),

        ('Freelancing', 'Freelancing'),

        ('Investment', 'Investment'),

        ('Other Income', 'Other Income'),

        # Expense

        ('Food', 'Food'),

        ('Shopping', 'Shopping'),

        ('Bills', 'Bills'),

        ('Transport', 'Transport'),

        ('Medical', 'Medical'),

        ('Education', 'Education'),

        ('Entertainment', 'Entertainment'),

        ('Travel', 'Travel'),

        ('Other Expense', 'Other Expense'),

    ]

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name='transactions'

    )

    transaction_type = models.CharField(

        max_length=20,

        choices=TYPE_CHOICES

    )

    title = models.CharField(

        max_length=200

    )

    category = models.CharField(

        max_length=50,

        choices=CATEGORY_CHOICES

    )

    amount = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )

    date = models.DateField()

    description = models.TextField(

        blank=True,

        null=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    def __str__(self):

        return f"{self.title} - ₹{self.amount}"    