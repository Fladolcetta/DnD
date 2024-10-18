# Dungeons and Dragons Character Helper
A fun little project to experiment with different technologies to learn web development. Using Dungeons and Dragons as a mechanism to show off the different technologies.

## Setup
 1. Open you mac laptop.
 2. Pull this repo.
 3. Open a terminal.
 4. Type `minikube mount .:/dnd`
 5. Open another terminal.
 6. Type `make setup`
 7. Type `make refresh`
 8. Type `make upk8s`

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

## Acknowledgements
- Gary Gygax
- Reddit User Nevertras: For his HTML/CSS Character Sheet
- Stack Overflow Users
- Github Copilot
- ChatGPT

## TODO

### Repo TODOS
- Add Kubernetes
  - Switch to k3d

## Future Enhancements
- Improve style of pages
  - Headers for home button
  - Move generated data into a text area to the side with a scroll bar.
    - Dice
    - Class info
    - Race info
  - Improve Styles for Submit buttons / Selectors / Free text fields
  - Shared Styles / Home buttons
  - Nicer backgrounds
  - Icons for options in Home with labels
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
