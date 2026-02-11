# Beginner Python Projects

A small set of beginner-friendly Python CLI projects focused on core programming basics:

- input/output
- loops and conditionals
- functions and refactoring
- simple external library usage (`qrcode`)

## Projects

1. `01-dice-rolling-game.py`
2. `02-number-guessing-game.py`
3. `03-rock-paper-scissors.py`
4. `03.1-refactoring-modularizing-code.py`
5. `03.2-refactoring-applying-the-dry-principle.py`
6. `06-QR-code-generator.py`

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python 01-dice-rolling-game.py
```

Replace the filename to run any other project.

## Notes

- This repository targets beginners, so files include pseudocode and short inline explanations.
- No sensitive files should be committed; local environment and editor files are ignored via `.gitignore`.

## Troubleshooting

If `import qrcode` fails:

```bash
venv\Scripts\activate
pip install -r requirements.txt
python -c "import qrcode; print('qrcode is ready')"
```

In VS Code, also select the interpreter from `venv\Scripts\python.exe`.
