# 📸 Social Media Website

A full-featured social media web application built with **Django**, inspired by Instagram-style functionality. Users can sign up, share photo posts, follow others, like posts, explore content, and manage their profiles.

---

## 🚀 Features

- **User Authentication** — Sign up, log in, and log out securely using Django's built-in auth system
- **Photo Posts** — Upload images with captions; posts are displayed in a feed
- **Feed** — Home feed shows posts from the logged-in user and everyone they follow, ordered by newest first
- **Like / Unlike** — Toggle likes on any post; like counts update in real time
- **Follow / Unfollow** — Follow other users and see their content in your feed
- **User Profiles** — View any user's profile with their posts, follower count, and following count
- **Edit Profile** — Update your bio, location, and profile picture
- **Explore Page** — Browse all posts from every user on the platform
- **Search** — Search for users by username or posts by caption
- **Post Deletion** — Delete your own posts directly from your profile page

---

## 🛠️ Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Backend      | Python 3.13, Django 6.0.4         |
| Database     | SQLite3 (via Django ORM)          |
| Frontend     | HTML5, CSS3, Django Templates     |
| Media Storage| Local filesystem (`/media/`)      |
| Static Files | Django `staticfiles` framework    |
| ASGI/WSGI    | asgiref 3.11.1                    |

---

## 📁 Project Structure

```
Social Media Website/
├── env/                        # Python virtual environment
└── socialmedia/                # Django project root
    ├── manage.py
    ├── db.sqlite3              # SQLite database
    ├── media/                  # User-uploaded files
    │   ├── blank-profile-picture.png
    │   ├── post_images/        # Uploaded post images
    │   └── profile_images/     # Uploaded profile pictures
    ├── static/
    │   └── css/
    │       └── app.css         # Global stylesheet
    ├── templates/              # HTML templates
    │   ├── main.html           # Home feed
    │   ├── signup.html         # Registration page
    │   ├── loginn.html         # Login page
    │   ├── explore.html        # Explore all posts
    │   ├── profile.html        # User profile page
    │   ├── edit_profile.html   # Edit profile form
    │   ├── profile_upload.html # Profile image upload
    │   ├── search.html         # Search bar
    │   ├── search_user.html    # Search results
    │   └── modal.html          # Post modal/detail view
    ├── socialmedia/            # Django project config
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── user_auth/              # Main Django app
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── admin.py
        ├── apps.py
        └── migrations/
```

---

## 🗄️ Data Models

### `ProfileModel`
Extends Django's built-in `User` with social profile data.

| Field        | Type         | Description                        |
|--------------|--------------|------------------------------------|
| `user`       | ForeignKey   | Linked Django User                 |
| `id_user`    | IntegerField | Primary key matching user ID       |
| `bio`        | TextField    | User biography                     |
| `profileimg` | ImageField   | Profile picture (default provided) |
| `location`   | CharField    | User location                      |

### `Post`
Represents a photo post.

| Field        | Type         | Description                        |
|--------------|--------------|------------------------------------|
| `id`         | UUIDField    | Unique post identifier             |
| `user`       | CharField    | Username of the poster             |
| `image`      | ImageField   | Post image                         |
| `caption`    | TextField    | Post caption                       |
| `created_at` | DateTimeField| Timestamp of creation              |
| `no_of_likes`| IntegerField | Total like count                   |

### `LikePost`
Tracks which user liked which post (prevents duplicate likes).

| Field     | Type      | Description     |
|-----------|-----------|-----------------|
| `post_id` | CharField | ID of the post  |
| `username`| CharField | Username of liker|

### `Followers`
Tracks follow relationships between users.

| Field      | Type      | Description              |
|------------|-----------|--------------------------|
| `follower` | CharField | Username of the follower |
| `user`     | CharField | Username being followed  |

---

## 🔗 URL Routes

| URL Pattern                  | View              | Description                    |
|------------------------------|-------------------|--------------------------------|
| `/`                          | `home`            | Home feed (login required)     |
| `/signup/`                   | `signup`          | User registration              |
| `/loginn/`                   | `loginn`          | User login                     |
| `/logoutt/`                  | `logoutt`         | User logout                    |
| `/upload/`                   | `upload`          | Upload a new post              |
| `/like-post/<id>`            | `likes`           | Like or unlike a post          |
| `/explore`                   | `explore`         | Browse all posts               |
| `/profile/<username>`        | `profile`         | View/edit user profile         |
| `/delete/<id>`               | `delete`          | Delete a post                  |
| `/search-results/?q=<query>` | `search_results`  | Search users and posts         |
| `/follow`                    | `follow`          | Follow or unfollow a user      |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### Steps

**1. Clone or extract the project**
```bash
cd "Social Media Website/socialmedia"
```

**2. Create and activate a virtual environment**
```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

**3. Install dependencies**
```bash
pip install django pillow
```

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Create a superuser (optional, for Django admin)**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Open in your browser**
```
http://127.0.0.1:8000/
```

---

## ⚠️ Important Notes

> **Do not use in production without addressing the following:**

- **Secret Key** — The `SECRET_KEY` in `settings.py` is hardcoded and publicly exposed. Generate a new one and store it in an environment variable.
- **Debug Mode** — `DEBUG = True` must be set to `False` in production.
- **ALLOWED_HOSTS** — Add your domain or IP to `ALLOWED_HOSTS` before deploying.
- **Database** — SQLite is used for development only. Switch to PostgreSQL or MySQL for production.
- **Media Files** — Configure a proper media file server (e.g., AWS S3, Cloudinary) for production deployments.

---

## 📄 License

This project is open source and free to use for educational and personal purposes.
