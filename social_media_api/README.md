# 📌 Social Media API

A Django REST Framework-powered social media backend with custom user authentication, posts, and comments.
Users can register, log in with token authentication, create posts, comment on posts, and follow other users.

## 🚀 Features

### Custom User model with:

 - bio, profile picture, and followers

  -Token-based Authentication using DRF

### CRUD operations for:

    - Posts (with title & content)

    - Comments (linked to posts & users)

### Permissions:

    - Users can only edit/delete their own posts & comments

    - Pagination for posts & comments

### Filtering & search on posts:

    - Search by title or content

    - Ordering by created_at or updated_at

## API EndPoints
### Authentication

POST /api/accounts/register/ → Register a new user

POST /api/accounts/login/ → Login and retrieve token

GET /api/accounts/me/ → Get current logged-in user details

### Posts

GET /api/posts/ → List all posts (paginated, searchable, orderable)

POST /api/posts/ → Create a new post (auth required)

GET /api/posts/{id}/ → Retrieve a single post

PUT /api/posts/{id}/ → Update a post (owner only)

DELETE /api/posts/{id}/ → Delete a post (owner only)

### Comments

GET /api/comments/ → List all comments (paginated)

POST /api/comments/ → Add a new comment (auth required)

GET /api/comments/{id}/ → Retrieve a single comment

PUT /api/comments/{id}/ → Update a comment (owner only)

DELETE /api/comments/{id}/ → Delete a comment (owner only)