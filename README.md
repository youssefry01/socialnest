# SocialNest

[![Render App](https://img.shields.io/badge/Render-Live%20App-46E3B7?logo=render&logoColor=white)](https://socialnest-iviz.onrender.com)

A modern, full-featured social media platform built with Django. SocialNest allows users to create accounts, share posts with images, follow other users, like posts, and manage their profiles—all with a beautiful, responsive user interface.

![Django](https://img.shields.io/badge/Django-5.2.5-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite)
![Pillow](https://img.shields.io/badge/Pillow-11.3.0-8BC34A?style=flat-square)

## 🚀 Features

### User Management
- **User Registration & Authentication**
  - Custom registration form with optional email, first name, and last name
  - Username validation (max 15 characters)
  - Secure password validation and hashing
  - Session-based authentication
  - Password change functionality in profile settings

- **User Profiles**
  - Customizable profile pages with avatar uploads
  - Bio section (up to 500 characters)
  - Profile editing with image upload support
  - View follower/following counts
  - Display user posts on profile pages

### Social Features
- **Follow System**
  - Follow/unfollow other users
  - View followers and following lists
  - Track follower/following counts

- **Posts**
  - Create posts with optional titles
  - Rich text content support
  - Multiple image uploads per post
  - Like/unlike posts
  - View individual post pages
  - Delete your own posts
  - Chronological feed of all posts

### User Interface
- Modern, responsive design with Tailwind CSS
- Clean and intuitive navigation
- Mobile-friendly layout
- Font Awesome icons for enhanced UX
- Professional form styling with validation feedback

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.2.5
- **Database**: SQLite3 (development)
- **Image Processing**: Pillow 11.3.0
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Icons**: Font Awesome
- **Python**: 3.x

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd socialnest
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   env\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
socialnest/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3                # SQLite database (development)
│
├── posts/                    # Posts application
│   ├── models.py            # Post and PostImage models
│   ├── views.py             # Post-related views
│   ├── forms.py             # Post creation form
│   ├── urls.py              # Post URL patterns
│   ├── admin.py             # Admin configuration
│   ├── templates/           # Post templates
│   └── migrations/          # Database migrations
│
├── users/                    # Users application
│   ├── models.py            # Profile model
│   ├── views.py             # User authentication & profile views
│   ├── forms.py             # Registration & profile forms
│   ├── urls.py              # User URL patterns
│   ├── admin.py             # Admin configuration
│   ├── templates/           # User templates
│   └── migrations/          # Database migrations
│
├── core/                     # Core application
│   └── urls.py              # Core URL patterns
│
├── socialnest/               # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── templates/                # Global templates
│   ├── layout.html          # Base template
│   └── about.html           # About page
│
├── static/                    # Static files (CSS, JS)
│   ├── css/
│   └── js/
│
└── media/                     # User-uploaded files
    ├── avatars/             # User profile pictures
    └── posts/               # Post images
```

## 🗄️ Database Models

### User (Django Built-in)
- Standard Django User model with authentication

### Profile
- `user`: OneToOne relationship with User
- `bio`: Text field (max 500 characters)
- `avatar`: Image field for profile pictures
- `following`: ManyToMany relationship (self-referential)
- `created_at`: Timestamp
- `updated_at`: Timestamp

### Post
- `title`: CharField (max 75 characters, optional)
- `body`: TextField (required)
- `date`: DateTimeField (auto-created)
- `author`: ForeignKey to User
- `likes`: ManyToMany relationship with User

### PostImage
- `post`: ForeignKey to Post
- `image`: ImageField
- `uploaded_at`: DateTimeField

## 🎯 Key Features Explained

### Registration System
- Custom `UserRegistrationForm` extends Django's `UserCreationForm`
- Optional fields: email, first name, last name
- Username limited to 15 characters
- Automatic profile creation upon registration

### Profile Management
- Edit profile information (name, email, bio, avatar)
- Change password with old password verification
- View profile with post count, follower/following stats

### Post System
- Create posts with optional title and body
- Upload multiple images per post
- Like/unlike functionality
- Delete own posts
- View all posts in chronological feed

### Follow System
- Follow/unfollow users
- Asymmetric following (not mutual)
- Display follower and following counts

## 🔐 Security Features

- CSRF protection on all forms
- Password hashing with Django's built-in hashers
- Session-based authentication
- Login required decorators for protected views
- Secure file upload handling
- Password validation (minimum length, complexity)

## 🎨 UI/UX Features

- Responsive design for all screen sizes
- Clean, modern interface
- Intuitive navigation
- Form validation with error messages
- Loading states and transitions
- Icon-based navigation
- Professional color scheme

## 📝 Usage Examples

### Creating a Post
1. Log in to your account
2. Navigate to "New Post" from the navigation
3. Enter post content (title optional)
4. Upload one or more images
5. Click "Create Post"

### Following a User
1. Visit any user's profile page
2. Click the "Follow" button
3. The button will change to "Following" when active

### Editing Profile
1. Go to your profile page
2. Click "Edit Profile"
3. Update your information, avatar, or password
4. Click "Save Changes"

### Accessing Admin Panel
1. Create a superuser: `python manage.py createsuperuser`
2. Navigate to `/admin/`
3. Log in with superuser credentials

## 🚧 Future Enhancements

Potential features for future development:
- Comments on posts
- Direct messaging between users
- Post sharing functionality
- Hashtag support
- Search functionality
- Email notifications
- Real-time updates
- API endpoints for mobile apps

## 🙏 Acknowledgments

- Django framework and community
- Tailwind CSS for styling utilities
- Font Awesome for icons
- All contributors and users
