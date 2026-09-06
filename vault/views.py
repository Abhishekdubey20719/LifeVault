from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import calendar as pycalendar
from datetime import datetime
from django.http import FileResponse, Http404
import os
from .models import Note, Document, Password, Event,Task,Transaction
from .forms import (
    NoteForm,
    DocumentForm,
    CategoryDocumentForm,
    PasswordForm,
    EventForm,
    TaskForm,
    TransactionForm,
    EditProfileForm
)

# ===========================
# HOME
# ===========================

def home(request):
    return render(request, 'home/index.html')


# ===========================
# LOGIN
# ===========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            return redirect('dashboard')

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, 'accounts/login.html')


# ===========================
# REGISTER
# ===========================

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists.")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful!")
        return redirect('login')

    return render(request, 'accounts/register.html')


# ===========================
# LOGOUT
# ===========================

@login_required(login_url='login')
def logout_view(request):

    logout(request)

    return redirect('home')


# ===========================
# DASHBOARD
# ===========================

@login_required(login_url='login')
def dashboard(request):

    notes_count = Note.objects.filter(user=request.user).count()

    documents_count = Document.objects.filter(user=request.user).count()

    tasks_count = Task.objects.filter(user=request.user).count()

    transactions_count = Transaction.objects.filter(
    user=request.user
).count()

    total_passwords = Password.objects.filter(
    user=request.user
).count()
    total_events = Event.objects.filter(
    user=request.user
).count()

    context = {

    'notes_count': notes_count,

    'documents_count': documents_count,

    'tasks_count': tasks_count,

    'transactions_count': transactions_count,

    'total_passwords': total_passwords,

    'total_events': total_events,

}

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )


# ===========================
# NOTES
# ===========================

@login_required(login_url='login')
def notes(request):

    all_notes = Note.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'notes/notes.html',
        {
            'notes': all_notes
        }
    )


@login_required(login_url='login')
def add_note(request):

    if request.method == "POST":

        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)

            note.user = request.user

            note.save()

            return redirect('notes')

    else:

        form = NoteForm()

    return render(
        request,
        'notes/add_note.html',
        {
            'form': form
        }
    )


@login_required(login_url='login')
def edit_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = NoteForm(
            request.POST,
            instance=note
        )

        if form.is_valid():

            form.save()

            return redirect('notes')

    else:

        form = NoteForm(instance=note)

    return render(
        request,
        'notes/edit_note.html',
        {
            'form': form
        }
    )

@login_required(login_url='login')
def view_note(request, id):

    note = Note.objects.get(
        id=id,
        user=request.user
    )

    return render(
        request,
        'notes/view_note.html',
        {
            'note': note
        }
    )

@login_required(login_url='login')
def delete_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        user=request.user
    )

    note.delete()

    return redirect('notes')


# ===========================
# DOCUMENTS
# ===========================

@login_required(login_url='login')
def documents(request):

    documents = Document.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')

    return render(
        request,
        'documents/documents.html',
        {
            'documents': documents
        }
    )


@login_required(login_url='login')
def upload_document(request):

    if request.method == "POST":

        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document = form.save(commit=False)

            document.user = request.user

            document.save()

            return redirect('documents')

    else:

        form = DocumentForm()

    return render(
        request,
        'documents/upload_document.html',
        {
            'form': form
        }
    )
@login_required(login_url='login')
def upload_document_category(request, category):

    if request.method == "POST":

        form = CategoryDocumentForm(

            request.POST,

            request.FILES

        )

        if form.is_valid():

            document = form.save(commit=False)

            document.user = request.user

            document.category = category

            document.save()

            return redirect(

                'category_documents',

                category=category

            )

    else:

        form = CategoryDocumentForm()

    return render(

        request,

        'documents/upload_document_category.html',

        {

            'form': form,

            'category': category

        }

    )


@login_required(login_url='login')
def edit_document(request, id):

    document = get_object_or_404(
        Document,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = DocumentForm(
            request.POST,
            request.FILES,
            instance=document
        )

        if form.is_valid():

            form.save()

            return redirect(
    'view_document',
    id=document.id
)

    else:

        form = DocumentForm(instance=document)

    return render(
        request,
        'documents/edit_document.html',
        {
            'form': form
        }
    )


@login_required(login_url='login')
def delete_document(request, id):

    document = get_object_or_404(
        Document,
        id=id,
        user=request.user
    )

    document.delete()

    return redirect('documents')


@login_required(login_url='login')
def view_document(request, id):

    document = get_object_or_404(
        Document,
        id=id,
        user=request.user
    )

    return render(
        request,
        'documents/view_document.html',
        {
            'document': document
        }
    )
@login_required(login_url='login')
def open_document(request, id):

    document = get_object_or_404(
        Document,
        id=id,
        user=request.user
    )

    if not document.file:
        raise Http404("File not found.")

    file_path = document.file.path

    if not os.path.exists(file_path):
        raise Http404("File does not exist.")

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=False
    )
@login_required(login_url='login')
def download_document(request, id):

    document = get_object_or_404(
        Document,
        id=id,
        user=request.user
    )

    if not document.file:
        raise Http404("File not found.")

    file_path = document.file.path

    if not os.path.exists(file_path):
        raise Http404("File does not exist.")

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=os.path.basename(file_path)
    )
@login_required(login_url='login')
def category_documents(request, category):

    documents = Document.objects.filter(
        user=request.user,
        category=category
    ).order_by('-uploaded_at')

    context = {

        'documents': documents,
        'category': category,

    }

    return render(
        request,
        'documents/category_documents.html',
        context
    )
# =====================================
# PASSWORD VAULT
# =====================================

@login_required(login_url='login')
def password_vault(request):

    passwords = Password.objects.filter(
        user=request.user
    ).order_by('-created_at')

    total_passwords = passwords.count()

    favorite_passwords = passwords.filter(
        favorite=True
    ).count()

    context = {

        'passwords': passwords,

        'total_passwords': total_passwords,

        'favorite_passwords': favorite_passwords,

    }

    return render(
        request,
        'passwords/password_vault.html',
        context
    )

# ==========================================
# ADD PASSWORD
# ==========================================

@login_required(login_url='login')
def add_password(request):

    if request.method == "POST":

        form = PasswordForm(request.POST)

        if form.is_valid():

            password = form.save(commit=False)

            password.user = request.user

            password.save()

            return redirect('password_vault')

    else:

        form = PasswordForm()

    return render(
        request,
        'passwords/add_password.html',
        {
            'form': form
        }
    )

# ==========================================
# VIEW PASSWORD
# ==========================================

@login_required(login_url='login')
def view_password(request, id):

    password = get_object_or_404(

        Password,

        id=id,

        user=request.user

    )

    return render(

        request,

        'passwords/view_password.html',

        {

            'password': password

        }

    )

# ==========================================
# EDIT PASSWORD
# ==========================================

@login_required(login_url='login')
def edit_password(request, id):

    password = get_object_or_404(
        Password,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = PasswordForm(
            request.POST,
            instance=password
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_password',
                id=password.id
            )

    else:

        form = PasswordForm(
            instance=password
        )

    return render(
        request,
        'passwords/edit_password.html',
        {
            'form': form,
            'password': password
        }
    )

# ==========================================
# DELETE PASSWORD
# ==========================================

@login_required(login_url='login')
def delete_password(request, id):

    password = get_object_or_404(
        Password,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        password.delete()

        return redirect('password_vault')

    return render(
        request,
        'passwords/delete_password.html',
        {
            'password': password
        }
    )


# ==========================================
# TOGGLE FAVORITE
# ==========================================

@login_required(login_url='login')
def toggle_favorite(request, id):

    password = get_object_or_404(

        Password,

        id=id,

        user=request.user

    )

    password.favorite = not password.favorite

    password.save()

    return redirect('password_vault')
# ==========================================
# CALENDAR HOME
# ==========================================

@login_required(login_url='login')
def calendar(request):

    today = datetime.today()

    month = request.GET.get("month")
    year = request.GET.get("year")

    if month:
        month = int(month)
    else:
        month = today.month

    if year:
        year = int(year)
    else:
        year = today.year

    # Previous month
    prev_month = month - 1
    prev_year = year

    if prev_month == 0:
        prev_month = 12
        prev_year -= 1

    # Next month
    next_month = month + 1
    next_year = year

    if next_month == 13:
        next_month = 1
        next_year += 1

    cal = pycalendar.monthcalendar(year, month)

    month_name = pycalendar.month_name[month]

    events = Event.objects.filter(
        user=request.user,
        date__year=year,
        date__month=month
    )

    upcoming_events = Event.objects.filter(
        user=request.user
    ).order_by("date")[:5]

    context = {

        "calendar_days": cal,

        "month": month,

        "year": year,

        "month_name": month_name,

        "today": today.day,

        "events": events,

        "upcoming_events": upcoming_events,

        "prev_month": prev_month,
        "prev_year": prev_year,

        "next_month": next_month,
        "next_year": next_year,

        "current_month": today.month,
        "current_year": today.year,

    }

    return render(
        request,
        "calendar/calendar.html",
        context
    )


@login_required(login_url='login')
def add_event(request):

    if request.method == "POST":

        form = EventForm(request.POST)

        if form.is_valid():

            event = form.save(commit=False)

            event.user = request.user

            event.save()

            return redirect('calendar')

    else:

        form = EventForm()

    return render(
        request,
        'calendar/add_event.html',
        {
            'form': form
        }
    )


@login_required(login_url='login')
def view_event(request, id):

    event = get_object_or_404(
        Event,
        id=id,
        user=request.user
    )

    return render(
        request,
        'calendar/view_event.html',
        {
            'event': event
        }
    )


@login_required(login_url='login')
def edit_event(request, id):

    event = get_object_or_404(
        Event,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = EventForm(
            request.POST,
            instance=event
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_event',
                id=event.id
            )

    else:

        form = EventForm(
            instance=event
        )

    return render(
        request,
        'calendar/edit_event.html',
        {
            'form': form,
            'event': event
        }
    )


@login_required(login_url='login')
def delete_event(request, id):

    event = get_object_or_404(
        Event,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        event.delete()

        return redirect('calendar')

    return render(
        request,
        'calendar/delete_event.html',
        {
            'event': event
        }
    )

# ==========================================
# TASKS HOME
# ==========================================

@login_required(login_url='login')
def tasks(request):

    tasks = Task.objects.filter(
        user=request.user
    ).order_by('-created_at')

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        status='Completed'
    ).count()

    pending_tasks = tasks.filter(
        status='Pending'
    ).count()

    favorite_tasks = tasks.filter(
        favorite=True
    ).count()

    context = {

        'tasks': tasks,

        'total_tasks': total_tasks,

        'completed_tasks': completed_tasks,

        'pending_tasks': pending_tasks,

        'favorite_tasks': favorite_tasks,

    }

    return render(
        request,
        'tasks/tasks.html',
        context
    )

# ==========================================
# ADD TASK
# ==========================================

@login_required(login_url='login')
def add_task(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('tasks')

    else:

        form = TaskForm()

    return render(
        request,
        'tasks/add_task.html',
        {
            'form': form
        }
    )

# ==========================================
# VIEW TASK
# ==========================================

@login_required(login_url='login')
def view_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    return render(
        request,
        'tasks/view_task.html',
        {
            'task': task
        }
    )

# ==========================================
# EDIT TASK
# ==========================================

@login_required(login_url='login')
def edit_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_task',
                id=task.id
            )

    else:

        form = TaskForm(
            instance=task
        )

    return render(
        request,
        'tasks/edit_task.html',
        {
            'form': form,
            'task': task
        }
    )

# ==========================================
# DELETE TASK
# ==========================================

@login_required(login_url='login')
def delete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        task.delete()

        return redirect('tasks')

    return render(
        request,
        'tasks/delete_task.html',
        {
            'task': task
        }
    )

# ==========================================
# FAVORITE TASK
# ==========================================

@login_required(login_url='login')
def toggle_task_favorite(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.favorite = not task.favorite

    task.save()

    return redirect('tasks')

@login_required(login_url='login')
def toggle_task_status(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    if task.status == "Pending":
        task.status = "Completed"
    else:
        task.status = "Pending"

    task.save()

    return redirect('tasks')

# ==========================================
# EXPENSE TRACKER
# ==========================================

# ==========================================
# EXPENSE TRACKER HOME
# ==========================================

@login_required(login_url='login')
def expenses(request):

    transactions = Transaction.objects.filter(
        user=request.user
    ).order_by('-date', '-created_at')

    income = sum(
        t.amount
        for t in transactions
        if t.transaction_type == "Income"
    )

    expense = sum(
        t.amount
        for t in transactions
        if t.transaction_type == "Expense"
    )

    balance = income - expense

    context = {

        "transactions": transactions,

        "total_income": income,

        "total_expense": expense,

        "balance": balance,

    }

    return render(
        request,
        "expenses/expenses.html",
        context
    )

# ==========================================
# ADD TRANSACTION
# ==========================================

@login_required(login_url='login')
def add_transaction(request):

    if request.method == "POST":

        form = TransactionForm(request.POST)

        if form.is_valid():

            transaction = form.save(commit=False)

            transaction.user = request.user

            transaction.save()

            return redirect('expenses')

    else:

        form = TransactionForm()

    return render(
        request,
        'expenses/add_transaction.html',
        {
            'form': form
        }
    )

# ==========================================
# VIEW TRANSACTION
# ==========================================

@login_required(login_url='login')
def view_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id,
        user=request.user
    )

    return render(
        request,
        'expenses/view_transaction.html',
        {
            'transaction': transaction
        }
    )

# ==========================================
# EDIT TRANSACTION
# ==========================================

@login_required(login_url='login')
def edit_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = TransactionForm(
            request.POST,
            instance=transaction
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_transaction',
                id=transaction.id
            )

    else:

        form = TransactionForm(
            instance=transaction
        )

    return render(
        request,
        'expenses/edit_transaction.html',
        {
            'form': form,
            'transaction': transaction
        }
    )


# ==========================================
# DELETE TRANSACTION
# ==========================================

@login_required(login_url='login')
def delete_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        transaction.delete()

        return redirect('expenses')

    return render(
        request,
        'expenses/delete_transaction.html',
        {
            'transaction': transaction
        }
    )

# ==========================================
# PROFILE
# ==========================================

@login_required(login_url='login')
def profile(request):

    return render(
        request,
        'profile/profile.html',
        {
            'user': request.user
        }
    )

@login_required(login_url='login')
def edit_profile(request):

    if request.method == "POST":

        form = EditProfileForm(

            request.POST,

            instance=request.user

        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = EditProfileForm(

            instance=request.user

        )

    return render(

        request,

        'profile/edit_profile.html',

        {

            'form': form

        }

    )

@login_required(login_url='login')
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        for field in form.fields.values():

            field.widget.attrs.update({

                "class": "form-control"

            })

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(
            user=request.user
        )

        for field in form.fields.values():

            field.widget.attrs.update({

                "class": "form-control"

            })

    return render(
        request,
        "profile/change_password.html",
        {
            "form": form
        }
    )

# ==========================================
# GLOBAL SEARCH
# ==========================================

@login_required(login_url='login')
def global_search(request):

    query = request.GET.get("q", "").strip()

    notes = []
    documents = []
    passwords = []
    events = []
    tasks = []
    expenses = []

    if query:

        notes = Note.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

        documents = Document.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) |
            Q(category__icontains=query)
        )

        passwords = Password.objects.filter(
            user=request.user
        ).filter(
            Q(website__icontains=query) |
            Q(username__icontains=query)
        )

        events = Event.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) |
            Q(location__icontains=query)
        )

        tasks = Task.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

        expenses = Transaction.objects.filter(
    user=request.user
).filter(
    Q(category__icontains=query)
)
    context = {

        "query": query,

        "notes": notes,
        "documents": documents,
        "passwords": passwords,
        "events": events,
        "tasks": tasks,
        "expenses": expenses,

    }

    return render(
        request,
        "search/search.html",
        context
    )