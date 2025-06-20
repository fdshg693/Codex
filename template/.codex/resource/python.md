### python environment
1. python path
    - /opt/homebrew/bin/python3
2. python version
    - 3.13.3
3. python packages
    - /Users/seiwan/.local/bin/uv uv 0.7.13
    
### Python Development Guidelines 

1. **Use `uv` for Dependency Management**
   - Install and manage Python dependencies using [`uv`](https://github.com/astral-sh/uv) for speed and reproducibility.

2. **Lint with Ruff**
   - Use [`ruff`](https://docs.astral.sh/ruff/) for linting Python code. Ensure your code passes all lint checks before committing.

3. **Test with Pytest**
   - Write and run tests using [`pytest`](https://docs.pytest.org/). All code must be covered by tests and pass before merging.

4. **Type Check with mypy**
   - Use [`mypy`](https://mypy-lang.org/) for static type checking. All code must pass type checks.

5. **Follow Modern Python Practices**
   - Use type annotations, f-strings, comprehensions, and other modern Python features.
   - Prefer explicit, readable, and maintainable code.

6. **Automate Where Possible**
   - Use pre-commit hooks or CI to enforce linting, testing, and type checking.
