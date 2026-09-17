# CampusHub 🎓📚

> **A Decoupled Academic Resource Sharing Platform for Higher Education**  
> *CSE 8th Semester Capstone Project / Thesis*

[![Backend](https://img.shields.io/badge/Backend-Django%20REST%20Framework-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React%2018-61DAFB?style=for-the-badge&logo=react)](https://react.dev/)
[![Build Tool](https://img.shields.io/badge/Build%20Tool-Vite-646CFF?style=for-the-badge&logo=vite)](https://vitejs.dev/)
[![Styling](https://img.shields.io/badge/Styling-Tailwind%20CSS-38BDF8?style=for-the-badge&logo=tailwindcss)](https://tailwindcss.com/)
[![API](https://img.shields.io/badge/API-OpenAPI%203.0-6BA539?style=for-the-badge&logo=openapi-initiative)](https://www.openapis.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)

---

## 📌 Project Overview

**CampusHub** is a full-stack academic resource-sharing platform designed to centralize course materials for university students.

The platform provides a REST API backend built with Django REST Framework and a decoupled React + Vite frontend. Students can work with academic resources organized around **Departments, Semesters, Subjects, and Resource Types**.

Supported resource types include:

- 📘 **Lecture Notes**
- 📝 **Question Papers**
- 📚 **Books / PDFs**

The backend also provides JWT authentication, OpenAPI 3.0 schema generation, and file upload support.

---

## ✨ Key Features

- 📁 **Academic Resource Management**
  - Create, list, retrieve, and delete academic resources.
  - Associate resources with subjects.
  - Track download counts.
  - Store uploaded resource files.

- 🏫 **Department Management**
  - List academic departments.
  - Each department has a name and unique code.

- 📚 **Subject Management**
  - Subjects are associated with departments.
  - Subjects contain name, code, and semester information.

- 🔒 **JWT Authentication**
  - User registration.
  - Username/password login.
  - Access and refresh JWT tokens.
  - Authenticated profile endpoint.
  - Bearer-token authentication for protected API operations.

- 📑 **OpenAPI 3.0 Documentation**
  - Auto-generated API schema.
  - YAML and JSON schema formats.
  - Language selection support through the schema endpoint.

- 📂 **File Uploads**
  - Resources support uploaded files.
  - The API accepts JSON, form-urlencoded, and multipart form-data requests for resource creation.

- ⚡ **Decoupled Architecture**
  - Django REST Framework serves the API.
  - React + Vite provides the client-side application.
  - Frontend and backend can be developed and deployed independently.

---

## 🛠️ Tech Stack

### Backend

| Technology | Purpose |
|---|---|
| Django 6.1.1 | Web framework |
| Django REST Framework 3.18.1 | REST API |
| Simple JWT 5.5.1 | JWT authentication |
| drf-spectacular 0.30.0 | OpenAPI 3.0 schema |
| django-cors-headers 4.9.0 | CORS handling |
| SQLite3 | Database |
| Pillow 12.3.0 | Image/file processing support |
| PyYAML 6.0.3 | YAML support |

### Frontend

| Technology | Purpose |
|---|---|
| React 18 | UI library |
| Vite | Frontend build tool |
| Tailwind CSS | Styling |
| Axios | HTTP client |
| React Router v6 | Client-side routing |

> The frontend stack above follows the project specification. The supplied OpenAPI schema describes the backend API independently of the frontend implementation.

---

## 📂 Repository Structure

```text
campushub/
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── resources/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── users/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── media/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── index.html
│   └── package.json
│
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd campushub
```

---

## 2️⃣ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\.venv\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create an Admin User

```bash
python manage.py createsuperuser
```

### Start the Development Server

```bash
python manage.py runserver
```

Backend:

```text
http://127.0.0.1:8000/
```

---

## 3️⃣ Frontend Setup

Open a new terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173/
```

---

# 📡 API Documentation

The supplied OpenAPI schema defines the following API resources and authentication behavior. fileciteturn0file0L5-L23

## 🔐 Authentication

CampusHub uses JWT Bearer authentication. The OpenAPI schema defines a `jwtAuth` HTTP security scheme using the Bearer scheme with JWT as the bearer format. fileciteturn0file0L516-L520

### Register

```http
POST /api/users/register/
```

Registration accepts:

- `username`
- `email`
- `password`

The generated schema identifies `username` and `password` as required registration fields, along with the returned `id`. fileciteturn0file0L373-L399

### Login

```http
POST /api/users/login/
```

Login accepts:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

A successful login returns an access and refresh token pair. fileciteturn0file0L264-L290

### Refresh Access Token

```http
POST /api/users/token/refresh/
```

The refresh endpoint accepts a refresh token and returns a new access token. fileciteturn0file0L328-L353

### Profile

```http
GET /api/users/profile/
```

This endpoint requires JWT authentication. fileciteturn0file0L291-L300

---

# 📚 Resource API

## List Resources

```http
GET /api/resources/
```

Returns an array of academic resources. The endpoint can be accessed with or without JWT authentication according to the supplied schema. fileciteturn0file0L5-L23

## Create Resource

```http
POST /api/resources/
```

Creating a resource requires JWT authentication.

The endpoint supports:

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

fileciteturn0file0L24-L46

Example multipart request fields:

```text
title
description
file
resource_type
subject
```

## Retrieve Resource

```http
GET /api/resources/{id}/
```

Returns a specific resource by integer ID. fileciteturn0file0L48-L67

## Delete Resource

```http
DELETE /api/resources/{id}/
```

Requires JWT authentication and returns HTTP `204 No Content` on success. fileciteturn0file0L69-L83

---

# 🏫 Department API

```http
GET /api/resources/departments/
```

Returns the available departments. fileciteturn0file0L84-L100

A department contains:

```json
{
  "id": 1,
  "name": "Computer Science and Engineering",
  "code": "CSE"
}
```

The OpenAPI schema defines `id`, `name`, and `code`, with `name` allowing up to 100 characters and `code` up to 10 characters. fileciteturn0file0L357-L372

---

# 📖 Subject API

```http
GET /api/resources/subjects/
```

Returns available subjects. fileciteturn0file0L102-L117

A subject contains:

```json
{
  "id": 1,
  "department_name": "Computer Science and Engineering",
  "name": "Data Structures",
  "code": "CSE-201",
  "semester": 2,
  "department": 1
}
```

The schema defines subject fields for department name, subject name, subject code, semester, and department ID. fileciteturn0file0L456-L484

---

# 📄 Resource Types

CampusHub supports three resource types:

| Value | Description |
|---|---|
| `NOTE` | Lecture Note |
| `QUESTION` | Question Paper |
| `BOOK` | Book / PDF |

These values are defined by the generated OpenAPI schema. fileciteturn0file0L446-L455

Example:

```json
{
  "title": "Data Structures Lecture Notes",
  "description": "Complete lecture notes",
  "resource_type": "NOTE",
  "subject": 1
}
```

---

# 📦 Resource Object

A resource contains fields including:

- `id`
- `uploaded_by_username`
- `subject_code`
- `title`
- `description`
- `file`
- `resource_type`
- `download_count`
- `created_at`
- `subject`
- `uploaded_by`

The generated schema marks server-generated fields such as `id`, `uploaded_by_username`, `subject_code`, `download_count`, `created_at`, and `uploaded_by` as read-only. fileciteturn0file0L400-L445

---

# 📑 OpenAPI Schema

CampusHub exposes its OpenAPI schema through:

```http
GET /api/schema/
```

The endpoint supports schema format selection through the `format` query parameter, including:

```text
/api/schema/?format=json
/api/schema/?format=yaml
```

The schema endpoint also exposes a `lang` query parameter with multiple language choices. fileciteturn0file0L118-L140

The exported project schema is stored as:

```text
backend/schema.yaml
```

---

# 🔑 Using JWT Authentication

After login, use the returned access token in the HTTP Authorization header:

```http
Authorization: Bearer <access_token>
```

Example with Axios:

```javascript
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

api.get("users/profile/", {
  headers: {
    Authorization: `Bearer ${accessToken}`,
  },
});
```

---

# 🌐 CORS Configuration

Because CampusHub uses a decoupled React frontend and Django backend, the backend should be configured to allow requests from the frontend development origin.

Typical development origin:

```text
http://localhost:5173
```

For production, configure CORS to allow only the actual deployed frontend domain.

---

# 📁 Media Files

Uploaded academic resources are stored under the backend media directory:

```text
backend/media/
```

For development, Django can serve uploaded media files through the configured `MEDIA_URL`.

For production deployment, use an appropriate web server or object/file storage solution for media files.

---

# 🧪 Development Workflow

A typical development workflow is:

```text
React Frontend
      │
      │ Axios / HTTP
      ▼
Django REST API
      │
      ├── JWT Authentication
      ├── Departments
      ├── Subjects
      └── Academic Resources
              │
              ▼
           SQLite3
```

---

# 📋 Requirements

The current backend dependency set includes:

```text
asgiref==3.12.1
attrs==26.1.0
Django==6.1.1
django-cors-headers==4.9.0
djangorestframework==3.18.1
djangorestframework-simplejwt==5.5.1
drf-spectacular==0.30.0
inflection==0.5.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
pillow==12.3.0
PyJWT==2.14.0
PyYAML==6.0.3
referencing==0.37.0
rpds-py==2026.6.3
sqlparse==0.6.0
tzdata==2026.4
uritemplate==4.2.0
```

Save these dependencies in:

```text
backend/requirements.txt
```

Then install them with:

```bash
pip install -r requirements.txt
```

---

# 🛡️ Security Notes

Before deploying CampusHub to production:

- Set Django `DEBUG=False`.
- Use a strong Django `SECRET_KEY`.
- Configure `ALLOWED_HOSTS`.
- Configure production CORS origins.
- Use HTTPS.
- Keep JWT secrets and environment-specific credentials outside source control.
- Configure secure media/file serving.
- Avoid committing the SQLite database if it contains sensitive production data.
- Review file-upload validation and allowed file types.

---

# 🎓 Academic Project

**CampusHub** is intended as a **CSE 8th Semester Capstone Project / Thesis**.

### Project Goals

1. Centralize academic resources.
2. Make course materials easier to discover.
3. Organize resources by department, semester, and subject.
4. Provide authenticated resource uploading.
5. Provide a modern REST API for a decoupled frontend.
6. Demonstrate practical full-stack web development skills.

---

# 📜 License

This project is licensed under the **MIT License**.

You may add the full MIT license text in a separate:

```text
LICENSE
```

file.

---

## 👨‍💻 Project Status

**CampusHub** is a full-stack academic resource-sharing project combining:

**Django REST Framework + JWT + OpenAPI + React + Vite + Tailwind CSS + SQLite**

Built for academic learning, experimentation, and capstone/thesis development.
