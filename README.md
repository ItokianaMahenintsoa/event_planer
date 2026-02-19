 1. Create main.py
 2. Create folders : database, models, routes
 3. Create __init__.py file in the folders : database, models, routes
 4. Create database.py in database folder
 5. Create in routes and models folders a users.py file and events.py file
 6. Create Event Model in models/events.py
 7. Create a Config class in models/events.py: it was an exemple of an Event Object
 8. Create User Model in models/users.py and Config class inside
 9. Create UserSignIn Model in the same file and the Config class inside
 10. Create signup route
 11. Install beanie
 12. Create connection.py in database folder and initialize data
 13. Update Events and Users Models 
 14. Use Events and Users Model in connection.py
 15. Create .env and add DATABASE_URL inside 
 16. Create database class and CRUD methods inside
 17. Update Route files
 18. Create a store folder
 19. Run this code : mongod --dbpath store
 20. Create auth folder
 21. Create init, authenticate, hash_password, jwt_handler python files inside
 22. Install argon2 password hashing : pip install argon2-cffi
 23. Update hash_password.py to create HashPassword class with argon2 hashing (no 72-byte limit)
 24. **FIX: Add Beanie initialization on app startup** - Added @app.on_event("startup") decorator in main.py calling Settings().initialize_database()
 25. **FIX: Add default DATABASE_URL and SECRET_KEY** - Updated database/connection.py to provide default MongoDB connection string and JWT secret key
 26. **FIX: Replace bcrypt with argon2** - Switched from bcrypt to argon2-cffi due to version incompatibility and 72-byte limitation
 27. **FIX: Change signin endpoint to JSON** - Replaced OAuth2PasswordRequestForm with UserSignIn model for JSON request body instead of form-data
 28. **FIX: Activate UserSignIn model** - Uncommented UserSignIn model in models/users.py for signin endpoint
 29. Update Events route to verify if user is authenticate 
 30. Add Creator field in Event models and update post, update and delete events routes
 31. Add CORS middleware in main.py
 32. Install pytest pytest-asyncio httpx 
 33. Create pytest.ini in the app source folder
 34. Create tests folder add __init__.py and test_arthmetic_operations.py inside
 35. Create conftesst.py in tests folder to setting up the test environment
 


## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB running or accessible
- Virtual environment (venv)

### Installation
```bash
pip install -r requirements.txt
```

### Environment Configuration
Create `.env` file (optional - has defaults):
```
DATABASE_URL=mongodb://localhost:27017/event_planner
SECRET_KEY=your-secret-key-change-me-in-production
```

### Run MongoDB
```bash
mongod --dbpath store
```

### Start Application
```bash
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

## Key Technologies
- **FastAPI** - Web framework
- **Beanie** - MongoDB ODM
- **Argon2** - Password hashing (secure, no character limit)
- **Motor** - Async MongoDB driver
- **Pydantic v2** - Data validation
- **python-jose** - JWT token generation

## API Endpoints

### User Routes
- `POST /user/signup` - Register a new user (accepts JSON)
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password",
    "events": []
  }
  ```
- `POST /user/signin` - User login (returns JWT token, accepts JSON)
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password"
  }
  ```

### Event Routes
- `POST /event/` - Create a new event
- `GET /event/` - Get all events
- `GET /event/{id}` - Get event by ID
- `PUT /event/{id}` - Update event
- `DELETE /event/{id}` - Delete event


