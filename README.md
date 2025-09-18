# 🌍 GoVisa

GoVisa is a **Visa Application Management System** built with Django.  
It allows users to apply for visas online, while administrators manage and approve applications through an easy-to-use dashboard.

---

## ✨ Features

- **User Registration & Authentication:** Secure signup, login, and password management.
- **Visa Application Submission:** Users can fill out and submit visa applications online.
- **Document Upload:** Upload required documents (passport, photos, etc.) with each application.
- **Application Status Tracking:** Users can view the status of their applications (Pending, Approved, Rejected).
- **Admin Dashboard:** Admins can review, approve, or reject visa applications.
- **Messaging System:** Users and admins can communicate regarding applications.
- **Notifications:** in-app notifications for status updates and messages.
- **Role-Based Access:** Separate permissions for users and admins.

---

### 👤 User
- 📝 Register and login securely.
- 🛂 Apply for a visa with personal information and required documents.
- 📊 Track the status of submitted applications.
- 📄 Download visa documents once approved.

### 🛡️ Admin
- 👥 Manage users (approve/reject admin requests).
- ✅ Review and approve/reject visa applications.
- 🔄 Update the status of applications (Pending, Approved, Completed).
- ✉️ Send and receive messages with users.
- 📈 Generate basic reports.

---

## 📁 Project Structure

```
GoVisa/
├── Go_Visa/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── main_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── visas/
│   └── templates/
│       ├── about.html
│       ├── base.html
│       ├── home.html
│       ├── signup.html
│       ├── admin/
│       ├── main_app/
│       ├── messages/
│       └── visas/
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── media/
│   └── uploads/
```

---

## ⚙️ Tech Stack
- **Backend:** Django 5+
- **Frontend:** HTML, CSS (Tailwind / Bootstrap)
- **Database:** SQLite (default), can be replaced with PostgreSQL
- **Authentication:** Django built-in auth system

---
## Additions
- [My Trello]()
- [My ERD](https://drive.google.com/file/d/1yQVfUsEfGE2pCRMDGIYnZh5NjfqZUzkH/view?usp=sharing)
