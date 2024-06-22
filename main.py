from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging
import sqlite3

def init_db():
    conn = sqlite3.connect("llm_response.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY,
            context TEXT,
            question TEXT,
            answer TEXT,
            rating INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

init_db()

app = FastAPI()
logging.basicConfig(level=logging.INFO)
