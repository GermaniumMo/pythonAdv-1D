from fastapi import FastAPI
from routers import recipes, categories
import os
from dotenv import load_dotenv
from database import get_db_connection

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

app.include_router(categories.router)
app.include_router(recipes.router)

@app.on_event("startup")
def startup():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        Create table if not exists categories (
            id integer primary key autoincrement,
            name text unique not null
        )
    ''')

    cursor.execute('''
        Create table if not exists recipes (
            id integer primary key autoincrement,
            name text not null,
            description text,
            ingredients text,
            instructions text,
            cuisine text,
            difficulty text,
            category_id integer,
            foreign key (category_id) references categories (id)
        )
    ''')
    conn.commit()
    conn.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI with SQLite project"}