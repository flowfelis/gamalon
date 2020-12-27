# Gamalon Analytics Home Assignment

## Libraries used:
* Flask
* Flask-SQLAlchemy(ORM)
* Flask-Marshmallow(for serializing)
* Flask-Migrate(keep track of db model changes)

## How to start?
#### 1. Clone the repo

#### 2. Install dependencies
`pip install -r requirements.txt`

#### 3. Create postgresql database
```bash
sudo -u postgres psql
CREATE DATABASE gamalon_db;
CREATE USER gamalon_user WITH ENCRYPTED PASSWORD '1';
GRANT ALL PRIVILEGES ON DATABASE gamalon_db TO gamalon_user;
```

#### 4. Create db modal
`flask db upgrade`

#### 5. Start the app
`export FLASK_APP=app && export FLASK_ENV=development && flask run`