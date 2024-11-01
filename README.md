# Dungeons and Dragons Character Helper
A fun little project to experiment with different technologies to learn web development. Using Dungeons and Dragons as a mechanism to show off the different technologies.

## Setup
 1. Open you mac laptop.
 2. Pull this repo.
 3. Open a terminal in the repo directory.
 4. Type `make setup`
 5. (If wanting to edit code)
    - Open another terminal in the repo directory.
    - Type `make mount`
 6. Open another terminal in the repo directory.
 7. Type `make up`

## Features
 - Dice Roller
 - Character Generator
 - Race Details
 - Class Details

## Code Documentation
[Generated Documentation](./docs/code.md)

## Dependencies
- Languages
  - python: Backend
  - html: Templates
  - CSS: Style formatting
  - Javascript: Browser interactions
- Development Tools
  - Docker: Containerization Technology
  - Docker Desktop: Containerization Visualization
  - pydoc-markdown: Document generation
  - minikube: Local instance of Kubernetes
  - mysql: Database Storage of character info
  - Github Actions: For testing in PRs
- Python Plugins
  - Flask: Python  micro web framework
  - gunicorn: Python Web Server Gateway Interface HTTP server
  - pytest: Unit Testing tool
  - pytest-cov: Code Coverage Tool
- Linting
  - pylint: Python linting
  - djlint: HTML Template linting
  - Flake8: Python Style linting
  - write-good: Markdown linting
  - hadolint: Dockerfile linting
  - kube-linter: Kubernetes yaml file linting

## Acknowledgements
- Gary Gygax
- Reddit User Nevertras: For his HTML/CSS Character Sheet
- Stack Overflow Users
- Github Copilot
- ChatGPT

## Future Enhancements
- Improve style of pages
  - Dice with icons
  - Table page
  - Roll Check
- Features
  - New Page
    - Generate character based on input stats
- Bugs
  - Fix killed DBs in Kubernetes mode
