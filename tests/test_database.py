import datetime
import os
import tempfile
import unittest
import sqlite3
from unittest.mock import patch
from pathlib import Path


from data.database import initialize_db
from entity.creature import Creature
#unittests for database interactions like saving and loading creatures

class TestDatabase(unittest.TestCase):
    def setUp(self): # use a temporary file for the database as we dont want test interacting with the real thing.
        self.tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.tmp.close()
        self.db_path = Path(self.tmp.name)
        self.patcher = patch("data.database.DB_PATH", self.db_path)
        self.patcher.start()
        initialize_db()
    
    def tearDown(self):
        self.patcher.stop()
        os.unlink(self.db_path)

    def make_creature(self, **kwargs):
        defaults = dict(
            name="Testy",
            species="TestSpecies",
            age=2,
            energy=80,
            fullness=90,
            happiness=85,
            memory=[],
            known_tricks=[],
            created_at=datetime.now(),
            last_interaction=datetime.now(),
            last_decay_check=datetime.now(),
        )
        defaults.update(kwargs)
        return Creature(**defaults)
    
    def test_initialize_creates_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='creature'")
            table = cursor.fetchone()
            self.assertIsNotNone(table)

    # def test_save_and_load_creature(self):
        
    #     pass

    # def test_row_to_creature(self):
    #     # This test would involve creating a mock database row and ensuring that the row_to_creature function correctly converts it into a Creature object.
    #     pass