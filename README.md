# Rnold

LeetCode-style website for basics of programming in R language

## Developer Commands

- **Activating Virtual Environment:** `source .venv/bin/activate`
- **Running development server:** in the root directory run `uv run fastapi dev`
  - **SwaggerUI:** use `/doc`
  - **Redoc:** use `/redoc`

### FastAPI & Python Jargon

- Endpoint = path
- HTTP method = operation/path operation
- `@something` syntax is called a decorator in python
  - `@app.get()` is an example of a path operation decorator. The function that comes below it is called a *path operation function*
