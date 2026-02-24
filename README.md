[![CI](https://github.com/simuworld007/clawcode/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/simuworld007/clawcode/actions/workflows/ci.yml) [![Codespaces](https://img.shields.io/badge/Codespaces-ready-blue?logo=github)](https://github.com/simuworld007/clawcode/codespaces)

# ClawCode — Projects

This repository is a workspace for small demo and utility projects. Each project lives in its own subdirectory under the repository root.

Current projects

- todo-cli/ — A minimal command-line todo application (Python). See `todo-cli/README.md` for usage and development notes.

Quick start

1. Clone the repository:
   git clone git@github.com:simuworld007/clawcode.git
   cd clawcode
2. For Python projects, create a virtual environment in the repo root (recommended):
   python -m venv .venv
   source .venv/bin/activate
3. Install and run a subproject (example: todo-cli):
   cd todo-cli
   pip install -e .
   python -m todo_cli.main add "Buy milk"

Run in GitHub Codespaces

- Open this repository in Codespaces: https://github.com/simuworld007/clawcode/codespaces
- Or from the repo page: Code → Codespaces → Create codespace on main
- The repository includes a `.devcontainer` configuration that prepares a Python 3.11 container, creates a `.venv`, installs the package in editable mode and test dependencies.

Development

- Tests are run from the repository root: `pytest -q` (CI runs pytest across projects).
- Add new projects as subdirectories; maintain a README.md inside each project for details.

Contributing

- Open a PR against main. CI will run tests automatically.

Badges and links

- CI badge shows workflow status. Click it to view the latest run.
- Codespaces link opens the Codespaces panel for this repository.

License

- Add a LICENSE file if you want to publish this repository publicly.
