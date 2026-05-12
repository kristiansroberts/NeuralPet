import unittest
import types
import sys
from datetime import datetime

from entity.creature import Creature
import services.action as action

# llama_cpp uses C++ bindings that are not compatible with the testing environment
# its also resource intensive and not necessary for testing so we fake it



class TestAction(unittest.TestCase):
    def make_creature(**kwargs):
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
    
    def test_parse_command(self):
        creature = TestAction.make_creature()
        command = "/feed"
        result = action.parse_command(command)
        self.assertTrue(result == "feed")
    
    def test_local_intent_parse(self):
        creature = TestAction.make_creature(known_tricks=["sit"])
        play = "I want to play"
        feed = "I want to feed you"
        rest = "Go rest"
        teach = "Teach you roll over"
        perform = "Perform sit"

        parsed_play = action.local_intent_parse(play, creature.known_tricks)
        self.assertEqual(parsed_play["intent"], "play")

        parsed_feed = action.local_intent_parse(feed, creature.known_tricks)
        self.assertEqual(parsed_feed["intent"], "feed")
        
        parsed_rest = action.local_intent_parse(rest, creature.known_tricks)
        self.assertEqual(parsed_rest["intent"], "rest")

        parsed_teach = action.local_intent_parse(teach, creature.known_tricks) 
        self.assertEqual(parsed_teach["intent"], "teach")
        
        parsed_perform = action.local_intent_parse(perform, creature.known_tricks)
        self.assertEqual(parsed_perform["intent"], "perform")
    
    def test_apply_user_input(self):
        creature = TestAction.make_creature(known_tricks=["sit"])
        feed = "I want to feed you"
        result_feed = action.apply_user_input(creature, feed)
        self.assertEqual(result_feed["intent"], "feed")
        self.assertTrue(result_feed["action_result"]["success"])

        play = "I want to play"
        result_play = action.apply_user_input(creature, play)
        self.assertEqual(result_play["intent"], "play")
        self.assertTrue(result_play["action_result"]["success"])

        rest = "Go rest"
        result_rest = action.apply_user_input(creature, rest)
        self.assertEqual(result_rest["intent"], "rest")
        self.assertTrue(result_rest["action_result"]["success"])

        teach = "Teach you roll over"
        result_teach = action.apply_user_input(creature, teach)
        self.assertEqual(result_teach["intent"], "teach")
        self.assertTrue(result_teach["action_result"]["success"])