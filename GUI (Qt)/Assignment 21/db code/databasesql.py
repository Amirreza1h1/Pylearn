import sqlite3
from main import PRODUCTS
import Media
import Film
import Clip
import Series
import Documentary
import Actor

class Db:
    def __init__(self):
        # Initialize the database connection
        self.conn = sqlite3.connect("media_database.db")
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Create tables if they do not already exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Film (
                id TEXT PRIMARY KEY, title TEXT, genre TEXT, release_date TEXT, rating TEXT, 
                casts TEXT, duration TEXT, director TEXT, language TEXT, media_type TEXT, 
                description TEXT, awards TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clip (
                id TEXT PRIMARY KEY, title TEXT, genre TEXT, release_date TEXT, rating TEXT, 
                casts TEXT, duration TEXT, director TEXT, language TEXT, media_type TEXT, 
                description TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Series (
                id TEXT PRIMARY KEY, title TEXT, genre TEXT, release_date TEXT, rating TEXT, 
                casts TEXT, seasons TEXT, director TEXT, language TEXT, media_type TEXT, 
                description TEXT, episodes TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Documentary (
                id TEXT PRIMARY KEY, title TEXT, genre TEXT, release_date TEXT, rating TEXT, 
                casts TEXT, duration TEXT, director TEXT, language TEXT, media_type TEXT
            )
        ''')
        self.conn.commit()

    def read(self):
        # Read data from each table and populate PRODUCTS list
        self._read_media('Film', Film, has_awards=True)
        self._read_media('Clip', Clip)
        self._read_media('Series', Series, has_episodes=True)
        self._read_media('Documentary', Documentary)

    def _read_media(self, table_name, media_class, has_awards=False, has_episodes=False):
        # Helper function to read media data from each table
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            casts = [Actor(*cast.split(',')) for cast in row[5].split("//")]
            awards = row[11].split("//") if has_awards and row[11] else []
            episodes = row[12] if has_episodes and row[12] else None
            
            # Append the object to PRODUCTS
            PRODUCTS.append(media_class(
                *row[:5], casts, *row[6:10], row[10], awards if has_awards else episodes
            ))

    def write(self):
        # Write data to each table
        for obj in PRODUCTS:
            media_type = type(obj).__name__
            casts_info = "//".join([f"{cast.name},{cast.age},{cast.nationality},{cast.height}" for cast in obj.casts])

            if media_type == 'Film':
                awards_info = "//".join(obj.awards) if hasattr(obj, 'awards') else ""
                self.cursor.execute('''
                    INSERT OR REPLACE INTO Film (id, title, genre, release_date, rating, casts, 
                    duration, director, language, media_type, description, awards) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (obj.id, obj.title, obj.genre, obj.release_date, obj.rating, casts_info, obj.duration, 
                      obj.director, obj.language, media_type, obj.description, awards_info))

            elif media_type == 'Clip':
                self.cursor.execute('''
                    INSERT OR REPLACE INTO Clip (id, title, genre, release_date, rating, casts, 
                    duration, director, language, media_type, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (obj.id, obj.title, obj.genre, obj.release_date, obj.rating, casts_info, obj.duration, 
                      obj.director, obj.language, media_type, obj.description))

            elif media_type == 'Series':
                self.cursor.execute('''
                    INSERT OR REPLACE INTO Series (id, title, genre, release_date, rating, casts, 
                    seasons, director, language, media_type, description, episodes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (obj.id, obj.title, obj.genre, obj.release_date, obj.rating, casts_info, obj.seasons, 
                      obj.director, obj.language, media_type, obj.description, obj.episodes))

            elif media_type == 'Documentary':
                self.cursor.execute('''
                    INSERT OR REPLACE INTO Documentary (id, title, genre, release_date, rating, casts, 
                    duration, director, language, media_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (obj.id, obj.title, obj.genre, obj.release_date, obj.rating, casts_info, obj.duration, 
                      obj.director, obj.language, media_type))

        self.conn.commit()

    def close(self):
        # Close the database connection
        self.conn.close()
