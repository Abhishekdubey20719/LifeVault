from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Notes
    path('notes/', views.notes, name='notes'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/edit/<int:id>/', views.edit_note, name='edit_note'),
    path('notes/delete/<int:id>/', views.delete_note, name='delete_note'),
    path(
    'notes/view/<int:id>/',
    views.view_note,
    name='view_note'
),

    # Documents
    path('documents/', views.documents, name='documents'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    path('documents/edit/<int:id>/', views.edit_document, name='edit_document'),
    path('documents/delete/<int:id>/', views.delete_document, name='delete_document'),
    path('documents/view/<int:id>/', views.view_document, name='view_document'),
    path('documents/category/<str:category>/', views.category_documents, name='category_documents'),
    path(
    'documents/upload/<str:category>/',
    views.upload_document_category,
    name='upload_document_category'
),

path(
    'documents/open/<int:id>/',
    views.open_document,
    name='open_document'
),
path(
    'documents/download/<int:id>/',
    views.download_document,
    name='download_document'
),

# ==========================
# PASSWORD VAULT
# ==========================

path(
    'password-vault/',
    views.password_vault,
    name='password_vault'
),

path(
    'password-vault/add/',
    views.add_password,
    name='add_password'
),

path(
    'password-vault/view/<int:id>/',
    views.view_password,
    name='view_password'
),

path(
    'password-vault/edit/<int:id>/',
    views.edit_password,
    name='edit_password'
),

path(
    'password-vault/delete/<int:id>/',
    views.delete_password,
    name='delete_password'
),

path(
    'password-vault/favorite/<int:id>/',
    views.toggle_favorite,
    name='toggle_favorite'
),
# ==========================================
# CALENDAR
# ==========================================

path(
    'calendar/',
    views.calendar,
    name='calendar'
),

path(
    'calendar/add/',
    views.add_event,
    name='add_event'
),

path(
    'calendar/view/<int:id>/',
    views.view_event,
    name='view_event'
),

path(
    'calendar/edit/<int:id>/',
    views.edit_event,
    name='edit_event'
),

path(
    'calendar/delete/<int:id>/',
    views.delete_event,
    name='delete_event'
),

# ==========================================
# TASKS
# ==========================================

path(
    'tasks/',
    views.tasks,
    name='tasks'
),

path(
    'tasks/add/',
    views.add_task,
    name='add_task'
),

path(
    'tasks/view/<int:id>/',
    views.view_task,
    name='view_task'
),

path(
    'tasks/edit/<int:id>/',
    views.edit_task,
    name='edit_task'
),

path(
    'tasks/delete/<int:id>/',
    views.delete_task,
    name='delete_task'
),

path(
    'tasks/favorite/<int:id>/',
    views.toggle_task_favorite,
    name='toggle_task_favorite'
),

path(
    'tasks/toggle/<int:id>/',
    views.toggle_task_status,
    name='toggle_task_status'
),

# ==========================================
# EXPENSE TRACKER
# ==========================================

path(
    'expenses/',
    views.expenses,
    name='expenses'
),

path(
    'expenses/add/',
    views.add_transaction,
    name='add_transaction'
),

path(
    'expenses/view/<int:id>/',
    views.view_transaction,
    name='view_transaction'
),

path(
    'expenses/edit/<int:id>/',
    views.edit_transaction,
    name='edit_transaction'
),

path(
    'expenses/delete/<int:id>/',
    views.delete_transaction,
    name='delete_transaction'
),

# ==========================================
# PROFILE
# ==========================================

path(
    'profile/',
    views.profile,
    name='profile'
),

path(
    'profile/edit/',
    views.edit_profile,
    name='edit_profile'
),

path(
    'profile/change-password/',
    views.change_password,
    name='change_password'
),

path(
    "search/",
    views.global_search,
    name="global_search",
),
]