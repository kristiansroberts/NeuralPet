import datetime
import os
import tempfile
import unittest
import sqlite3
from unittest.mock import patch
from pathlib import Path


from data.database import * #importing everything from database for testing purposes, allows access to helper functions like row_to_creature without needing to import the whole service layer
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

    def test_save_and_load_creature(self):
        c = self.make_creature()
        save_creature(c)
        row = load_creature()
        self.assertIsNotNone(row)
        self.assertEqual(row["name"], c.name)
        self.assertEqual(row["species"], c.species)
        self.assertEqual(row["age"], c.age)
        self.assertEqual(row["energy"], c.energy)
        self.assertEqual(row["fullness"], c.fullness)
        self.assertEqual(row["happiness"], c.happiness)

    def test_none_returned_when_no_creature(self):
        row = load_creature()
        self.assertIsNone(row)

    def test_save_overwrites_existing(self):
        c = self.make_creature(energy=80)
        save_creature(c)
        c.energy = 50
        save_creature(c)
        row = load_creature()
        self.assertEqual(row["energy"], 50)

    def test_delete_creature(self):
        c = self.make_creature()
        save_creature(c)
        delete_creature()
        row = load_creature()
        self.assertIsNone(row)

    def test_row_to_creature(self):
        c = self.make_creature()
        save_creature(c)
        row = load_creature()
        loaded = row_to_creature(row)
        self.assertIsInstance(loaded, Creature)
        self.assertEqual(loaded.name, "Testy")
        self.assertEqual(loaded.species, "TestSpecies")
        self.assertEqual(loaded.energy, 80)
        self.assertEqual(loaded.fullness, 90)