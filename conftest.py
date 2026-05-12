import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

fake_llama_cpp = types.ModuleType("llama_cpp")
fake_llama_cpp.Llama = object
sys.modules["llama_cpp"] = fake_llama_cpp