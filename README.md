# juice-shop-api-exploration
Initial idea invalidated after maintainer feedback; documenting API/YAML exploration and learnings.

## Juice Tracker

A command-line tool to view and filter challenges from [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/).

## Features
- Login with Juice Shop account and save session
- List challenges with solved/unsolved status
- Filter challenges (`--solved` / `--unsolved`)
- Progress summary
- Challenges sorted by difficulty (1 → 6)

## Usage
```bash

# Login
python main.py login

# List all challenges
python main.py status

# List only solved or unsolved
python main.py status --solved
python main.py status --unsolved
