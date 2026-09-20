# Django Signup & Login System

A beginner-friendly Django web application focused on learning user authentication, registration, profile management, form validation, email integration, and basic business logic.

This project was built to understand how a Django application handles the complete user account flow from registration to login and profile management.

---

## Features

- User registration / signup
- User login / authentication
- User logout
- Protected profile page
- Profile information display
- Profile information update
- Django form validation
- Password hashing using Django authentication
- Welcome email after successful registration
- Gmail SMTP integration
- Gmail App Password authentication
- Django messages for success/error feedback
- Crispy Forms for cleaner form rendering
- Responsive and user-friendly Bootstrap interface
- Reusable `base.html` template
- Authentication-aware navigation
- Form submission loading states
- Basic business logic for account management

---

## User Flow

```text
                    Home
                     |
          +----------+----------+
          |                     |
      Create Account          Login
          |                     |
          v                     v
   Registration Form       Authentication
          |                     |
          v                     v
    Validate Form          Login Success
          |                     |
          v                     v
     Create User            Dashboard
          |
          v
    Send Welcome Email
          |
          v
       Login Page
          |
          v
       Profile
          |
          +----------------------+
          |
          v
    View Account Information
          |
          v
      Update Profile
