# Dungeons and Dragons Character Helper
A fun little project to experiment with different technologies to learn web development. Using Dungeons and Dragons as a mechanism to show off the different technologies.

## Setup
 1. Open you mac laptop.
 2. Pull this repo.
 3. Open a terminal in the repo directory.
 4. Type `make setup`
 5. (If wanting to edit code)
    - Open another terminal in the repo directory.
    - Type `minikube mount .:/dnd`
 6. Open another terminal in the repo directory.
 7. Type `make up`

## Features
 - Dice Roller
 - Character Generator
 - Race Details
 - Class Details

## Demonstrated Tech
- Python
- Flask
- HTML Templates
- Linters
- Pytest
- Github Actions
- Docker
- Kubernetes
- Pytest
- Code Coverage
- mySQL

## Code Documentation
[Generated Documentation](./docs/code.md)

## Dependencies
- python: Base backend programming language
- Flask: Python  micro web framework
- gunicorn: Python Web Server Gateway Interface HTTP server
- Docker: Containerization Technology
- Docker Desktop: Containerization Visualization
- pytest: Unit Testing tool
- pytest-cov: Code Coverage Tool
- pydoc-markdown: Document generation
- pylint: Python linting
- djlint: HTML Template linting
- Flake8: Python Style linting
- write-good: Markdown linting
- mysql: Database
- hadolint: Dockerfile linting
- minikube: Local instance of Kubernetes
- kube-linter: Kubernetes yaml file linting

## Acknowledgements
- Gary Gygax
- Reddit User Nevertras: For his HTML/CSS Character Sheet
- Stack Overflow Users
- Github Copilot
- ChatGPT

## TODO

## Future Enhancements
- Improve style of pages
  - Improve Styles for Submit buttons / Selectors / Free text fields
  - Nicer backgrounds
  - Dice with icons
- Add missing Character Info as selectable
  - Background
  - Alignment
  - Player name
  - Experience Points
  - Personality / Ideals / Bonds / Flaws
  - Starting Equipment
  - Attacks and Spells
  - Selectable Class Proficiencies
- Features
  - Roll button based on selected stat / save / skill
  - Retrieval of generated characters from storage
  - Generate character based on input stats
