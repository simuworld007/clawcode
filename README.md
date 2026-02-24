[![CI](https://github.com/simuworld007/clawcode/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/simuworld007/clawcode/actions/workflows/ci.yml)

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

Development

- Tests are run from the repository root: `pytest -q` (CI runs pytest across projects).
- Add new projects as subdirectories; maintain a README.md inside each project for details.

Contributing

- Open a PR against main. CI will run tests automatically.

License

- Add a LICENSE file if you want to publish this repository publicly.
