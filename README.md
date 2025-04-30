# Book Review API

A Django project that provides a REST API for managing books and their reviews. Regular users can create accounts, browse available books, and leave reviews, while administrators can manage book records.

This project uses **Django Admin Interface** to provide an improved and modern look for the Django admin panel.

---

## Table of Contents

1. [How to Run the Project Locally](#how-to-run-the-project-locally)
2. [Django Admin Interface](#django-admin-interface)
3. [Testing Endpoints](#testing-endpoints)
4. [Authentication Mechanism](#authentication-mechanism)
5. [Permissions](#permissions)

---

## How to Run the Project Locally

### Prerequisites

- **Python**: Ensure Python 3.8+ is installed
- **pip**: Python's package manager
- **Virtual Environment Setup**: Recommended to avoid dependency conflicts

### Steps to Run the Project:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BookReview
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

   The API will now be available at `http://127.0.0.1:8000/`.

---

## Django Admin Interface

This project uses the **Django Admin Interface** package to enhance the design of the default Django admin panel. 

The interface offers:
- A responsive and modern UI for the admin dashboard.
- Improved design features for managing books, users, and reviews.

**Admin URL:**  
Access the enhanced admin panel at `http://127.0.0.1:8000/admin/`.

To customize the interface (e.g., themes, colors), add configurations in the **`settings.py`** file under `ADMIN_INTERFACE` options.

To learn more, visit the [Django Admin Interface Documentation](https://pypi.org/project/django-admin-interface/).

---

## Permissions

### Regular Users:
- Users can:
  - Register for the system
  - Authenticate using their credentials to interact with the API
  - View all books or specific books
  - Submit reviews for books
  - View reviews for specific books

- **IMPORTANT:** Users **cannot** add, modify, or delete books. Admins have exclusive access to these operations.

---

### Admins:
- Admin users can:
  - Add, update, and delete books using the `/api/books/add/` and `/api/books/manage/<id>/` endpoints
  - Manage books, reviews, and users via the `/admin/` dashboard

---

## Testing Endpoints

### Authentication Endpoints
1. **Register User**  
   - URL: `POST /api/register/`
   - Request Body:
     ```json
     {
       "username": "testuser",
       "email": "testuser@example.com",
       "password": "securepassword"
     }
     ```

2. **Login to Obtain JWT Token**  
   - URL: `POST /api/token/`
   - Request Body:
     ```json
     {
       "username": "testuser",
       "password": "securepassword"
     }
     ```

3. **Refresh Token**  
   - URL: `POST /api/token/refresh/`
   - Request Body:
     ```json
     {
       "refresh": "<refresh_token>"
     }
     ```

4. **Change Password (Logged-In Users)**
   - URL: `PUT /api/change-password/`
   - Requires Authorization Header (`Bearer <access_token>`)
   - Request Body:
     ```json
     {
       "old_password": "currentpassword",
       "new_password": "newsecurepassword"
     }
     ```

---

### Book Endpoints
1. **View All Books**
   - URL: `GET /api/books/`

2. **View a Single Book**
   - URL: `GET /api/books/<int:pk>/`
   - `<int:pk>` is the ID of the book to retrieve.

3. **Add a New Book (Admin-Only)**  
   - URL: `POST /api/books/add/`
   - **Authorization:** Requires admin privilege
   - Request Body:
     ```json
     {
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald",
       "description": "A classic novel about the American Dream."
     }
     ```

4. **Update or Delete a Book (Admin-Only)**  
   - URL: `PUT` or `DELETE /api/books/manage/<int:pk>/`
   - `<int:pk>` refers to the ID of the book.
   - Requires admin privilege.
   - Example Request Body for updating a book:
     ```json
     {
       "title": "Updated Title",
       "author": "Updated Author",
       "description": "Updated description of the book."
     }
     ```

---

### Review Endpoints
1. **Submit a Review**
   - URL: `POST /api/books/<int:book_id>/reviews/`
   - `<int:book_id>` refers to the ID of the book to review.
   - Requires JWT token.
   - Request Body:
     ```json
     {
       "rating": 5,
       "comment": "A wonderful piece of literature."
     }
     ```

2. **Get All Reviews for a Book**
   - URL: `GET /api/books/<int:book_id>/reviews/`
   - Requires JWT token.

3. **View, Update or Delete a Single Review(Review owner only)**
   - URL: `GET /api/reviews/<int:review_id>/`
   - `<int:review_id>` refers to the ID of the review.
   - Requires JWT token.
   - Use `PUT` or `DELETE` for updating or deleting reviews.

---

## Authentication Mechanism

This project uses **JWT Authentication** provided by `rest_framework_simplejwt`.

1. Users authenticate via `/api/token/` to receive:
   - **Access Token** (used for API calls requiring authentication)
   - **Refresh Token** (to obtain a new access token when expired)

2. Include the access token in the Authorization header for authenticated API calls:
   ```
   Authorization: Bearer <your_access_token>
   ```

3. If the access token expires, use `/api/token/refresh/` to obtain a new token:
   ```json
   {
     "refresh": "<your_refresh_token>"
   }
   ```

---

## Notes
1. Admin features (adding/editing books) are restricted to superusers.
2. The `/admin/` dashboard can be used for managing data directly if needed.
3. Always protect sensitive credentials and tokens.
