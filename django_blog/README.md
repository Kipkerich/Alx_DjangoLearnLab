## 📝 Django Blog Application

A simple blog application built with Django and Bootstrap, featuring user authentication, blog posts management, and a comment system.

## 🚀 Features

**User Authentication**

- Register, login, and manage profiles

- Profile editing with account & profile info

**Blog Posts**

- Create, Read, Update, Delete (CRUD) operations

- Only authenticated users can create posts

- Only post authors can update or delete their posts

- Post list & detail pages are accessible to all users

**Comments**

- Add comments under blog posts

- Authenticated users can create, update, or delete their own comments

- Each comment shows author & timestamps

**UI/UX**

- Responsive templates styled with Bootstrap 5

- User-friendly forms and confirmation pages



## 📂 Project Structure

blog_project/
│── blog/                 # Blog app
│   ├── models.py         # Post & Comment models
│   ├── views.py          # CRUD views for posts & comments
│   ├── urls.py           # URL patterns
│   ├── templates/blog/   # HTML templates
│       ├── base.html
│       ├── post_list.html
│       ├── post_detail.html
│       ├── post_form.html
│       ├── confirm_form.html
│       ├── comment_form.html
│── requirements.txt
│── README.md

## API Endpoints(DRF)
| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| GET    | `/api/posts/`      | List all posts              |
| GET    | `/api/posts/<id>/` | Retrieve single post        |
| POST   | `/api/posts/`      | Create new post (auth only) |
| PUT    | `/api/posts/<id>/` | Update post (author only)   |
| DELETE | `/api/posts/<id>/` | Delete post (author only)   |


### Screenshots

### Profile Page
![Profile Page](blog/templates/static/profile_page.png)
