# Task Manager API

A Django REST Framework-based Task Management System with full CRUD operations, filtering, searching, and CLI support.

## Features

- **RESTful API** for task management (Create, Read, Update, Delete)
- **Filtering** by status and priority
- **Search** functionality across title and description
- **CLI Interface** for command-line task management
- **Validation** for task fields (title, due date, priority, status)
- **Auto-timestamp** tracking for task creation

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /var/www/Python/Treeshainfotech/task_manager
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at: `http://localhost:8000/api/`

---

## API Endpoint Documentation

### Base URL
```
http://localhost:8000/api/
```

### Endpoints

#### 1. List All Tasks
- **URL**: `/api/tasks/`
- **Method**: `GET`
- **Description**: Retrieve all tasks with optional filtering and searching
- **Query Parameters**:
  - `status`: Filter by status (`pending` or `completed`)
  - `priority`: Filter by priority (`low`, `medium`, or `high`)
  - `search`: Search in title and description

**Example Request**:
```bash
# Get all tasks
curl http://localhost:8000/api/tasks/

# Filter by status
curl http://localhost:8000/api/tasks/?status=pending

# Filter by priority
curl http://localhost:8000/api/tasks/?priority=high

# Search tasks
curl http://localhost:8000/api/tasks/?search=meeting

# Combined filters
curl http://localhost:8000/api/tasks/?status=pending&priority=high
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs",
    "status": "pending",
    "priority": "high",
    "created_at": "2026-01-07T10:30:00Z",
    "due_date": "2026-01-15T23:59:59Z"
  }
]
```

---

#### 2. Get Single Task
- **URL**: `/api/tasks/{id}/`
- **Method**: `GET`
- **Description**: Retrieve a specific task by ID

**Example Request**:
```bash
curl http://localhost:8000/api/tasks/1/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive README and API docs",
  "status": "pending",
  "priority": "high",
  "created_at": "2026-01-07T10:30:00Z",
  "due_date": "2026-01-15T23:59:59Z"
}
```

---

#### 3. Create New Task
- **URL**: `/api/tasks/`
- **Method**: `POST`
- **Description**: Create a new task
- **Required Fields**: `title`
- **Optional Fields**: `description`, `status`, `priority`, `due_date`

**Example Request**:
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New task",
    "description": "Task description",
    "priority": "medium",
    "status": "pending",
    "due_date": "2026-01-20T18:00:00Z"
  }'
```

**Response** (201 Created):
```json
{
  "id": 2,
  "title": "New task",
  "description": "Task description",
  "status": "pending",
  "priority": "medium",
  "created_at": "2026-01-07T12:00:00Z",
  "due_date": "2026-01-20T18:00:00Z"
}
```

**Validation Rules**:
- Title cannot be empty or whitespace only
- Due date cannot be in the past
- Priority must be: `low`, `medium`, or `high`
- Status must be: `pending` or `completed`

---

#### 4. Update Task (Full Update)
- **URL**: `/api/tasks/{id}/`
- **Method**: `PUT`
- **Description**: Update all fields of a task

**Example Request**:
```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated task title",
    "description": "Updated description",
    "priority": "high",
    "status": "completed",
    "due_date": "2026-01-25T18:00:00Z"
  }'
```

---

#### 5. Update Task (Partial Update)
- **URL**: `/api/tasks/{id}/`
- **Method**: `PATCH`
- **Description**: Update specific fields of a task

**Example Request**:
```bash
# Mark task as completed
curl -X PATCH http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'

# Update priority only
curl -X PATCH http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"priority": "high"}'
```

---

#### 6. Delete Task
- **URL**: `/api/tasks/{id}/`
- **Method**: `DELETE`
- **Description**: Delete a specific task

**Example Request**:
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/
```

**Response** (204 No Content)

---

## CLI Usage Examples

The task manager includes a command-line interface for managing tasks directly from the terminal.

### Basic CLI Commands

#### 1. List All Tasks
```bash
python manage.py taskcli list
```

**Output**:
```
1. Complete documentation | pending | high
2. Review code | pending | medium
3. Fix bug | completed | low
```

---

#### 2. Add a New Task
```bash
# Add task with default priority (medium)
python manage.py taskcli add --title "New task"

# Add task with specific priority
python manage.py taskcli add --title "Urgent task" --priority high
```

**Output**:
```
Task created: 4
```

---

#### 3. Mark Task as Completed
```bash
python manage.py taskcli complete --id 1
```

**Output**:
```
Task marked as completed
```

---

#### 4. Delete a Task
```bash
python manage.py taskcli delete --id 2
```

**Output**:
```
Task deleted
```

---

### CLI Command Reference

| Command | Required Arguments | Optional Arguments | Description |
|---------|-------------------|-------------------|-------------|
| `list` | None | None | Display all tasks |
| `add` | `--title` | `--priority` | Create new task |
| `complete` | `--id` | None | Mark task as completed |
| `delete` | `--id` | None | Delete a task |

**Priority Options**: `low`, `medium` (default), `high`

---

## Project Structure

```
task_manager/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── tasks/                 # Tasks app
│   ├── management/        # Custom management commands
│   │   └── commands/
│   │       └── taskcli.py # CLI implementation
│   ├── migrations/        # Database migrations
│   ├── models.py          # Task model
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   └── urls.py            # App URL configuration
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## Data Model

### Task Model

| Field | Type | Options | Description |
|-------|------|---------|-------------|
| `id` | Integer | Auto-generated | Primary key |
| `title` | String (200) | Required | Task title |
| `description` | Text | Optional | Detailed description |
| `status` | String | `pending` (default), `completed` | Task status |
| `priority` | String | `low`, `medium` (default), `high` | Task priority |
| `created_at` | DateTime | Auto-generated | Creation timestamp |
| `due_date` | DateTime | Optional | Task deadline |

---

## Assumptions Made

1. **Database**: SQLite is used for development. For production, consider PostgreSQL or MySQL.

2. **Authentication**: No authentication is implemented. All endpoints are publicly accessible. For production, implement:
   - Token-based authentication (DRF Token Auth)
   - Session authentication
   - JWT authentication

3. **Due Date Format**: 
   - The API accepts ISO 8601 datetime format
   - Due date validation only checks if it's not in the past (date comparison, not datetime)
   - The model uses `DateTimeField` to store full timestamp

4. **Pagination**: Not implemented. For large datasets, consider adding:
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 10
   }
   ```

5. **CORS**: Not configured. For frontend integration, install and configure `django-cors-headers`.

6. **Error Handling**: Basic validation is in place. Extended error handling can be added for production.

7. **Task Ordering**: Tasks are ordered by creation date (newest first) in the API.

8. **CLI Limitations**: 
   - CLI only supports basic operations
   - Cannot set due_date or description through CLI (API only)
   - CLI uses simpler output format for readability

9. **Testing**: Test files are generated but not implemented. Consider adding comprehensive test coverage.

10. **Environment Variables**: Secret key and debug settings are hardcoded. For production, use environment variables or `.env` files.

---

## Testing the API

### Using curl

```bash
# Create a task
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task", "priority": "high"}'

# List all tasks
curl http://localhost:8000/api/tasks/

# Get specific task
curl http://localhost:8000/api/tasks/1/

# Update task
curl -X PATCH http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'

# Delete task
curl -X DELETE http://localhost:8000/api/tasks/1/
```

### Using Python requests

```python
import requests

BASE_URL = "http://localhost:8000/api/tasks/"

# Create task
response = requests.post(BASE_URL, json={
    "title": "Python test task",
    "priority": "medium"
})
print(response.json())

# List tasks
response = requests.get(BASE_URL)
print(response.json())
```

---

## Dependencies

```
asgiref==3.11.0
Django==6.0.1
django-filter==25.2
djangorestframework==3.16.1
sqlparse==0.5.5
```

---

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   python manage.py runserver 8001  # Use different port
   ```

2. **Migration errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Module not found errors**
   ```bash
   pip install -r requirements.txt  # Reinstall dependencies
   ```

4. **CLI command not found**
   - Ensure `__init__.py` files exist in `tasks/management/` and `tasks/management/commands/`
   - Restart the Django development server

---

## Future Enhancements

- User authentication and authorization
- Task assignments to users
- Tags/categories for tasks
- File attachments
- Task comments
- Email notifications
- Recurring tasks
- Task history/audit log
- API rate limiting
- Comprehensive test coverage

---

## License

This project is for educational/development purposes.

---

## Contact

For issues or questions, please contact the development team at Treeshainfotech.
