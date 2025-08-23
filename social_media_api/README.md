# Social Media API Documentation

## Authentication

* **Register** → `POST /api/accounts/register/`
* **Login** → `POST /api/accounts/login/` → returns auth token
* **Profile** → `GET /api/accounts/me/` (requires token)

## User Relationships

* **Follow User** → `POST /api/accounts/follow/<user_id>/`
* **Unfollow User** → `POST /api/accounts/unfollow/<user_id>/`

## Posts

* **List / Create Posts** → `GET/POST /api/posts/`
* **Retrieve / Update / Delete Post** → `GET/PUT/DELETE /api/posts/<id>/`
* **Like Post** → `POST /api/posts/<id>/like/`
* **Unlike Post** → `POST /api/posts/<id>/unlike/`
* Supports pagination + filtering by title/content

## Comments

* **List / Create Comments** → `GET/POST /api/comments/`
* **Retrieve / Update / Delete Comment** → `GET/PUT/DELETE /api/comments/<id>/`

## Feed

* **Get Feed** → `GET /api/feed/` (shows posts from followed users, newest first)

## Notifications

* **List Notifications** → `GET /api/notifications/`
* **Mark Notification as Read** → `PATCH /api/notifications/<id>/read/`

### Notes

* All endpoints require authentication (except register/login).
* Use token-based auth: `Authorization: Token <your_token>`
