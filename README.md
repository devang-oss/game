# Choose-Your-Own-Adventure (terminal)

A small modular choose-your-own-adventure game written in Python.

Features
- Runs in terminal
- Player choices determine the path
- Multiple endings
- Modular scene files (add scenes by creating new modules)

Run
- From the project root:
  - python main.py
- Or directly:
  - python -m game.cli

Add a new scene
- Create `game/scenes/new_scene.py`
- Import `register_scene` from `game.scenes`
- Create a `Scene` instance and call `register_scene(scene)

Testing
- Install dev deps:
  - pip install -r requirements.txt
- Run tests:
  - pytest

License
- MIT
