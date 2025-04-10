ignore_git = """
# Byte-compiled / cache
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
venv/
.venv/
env/
ENV/

# Environment variables / secrets
.env
.env.*

# VS Code settings
.vscode/

# Mac & Windows system files
.DS_Store
Thumbs.db

# Logs
*.log

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
coverage.xml
.cache
pytest_cache/

# mypy
.mypy_cache/
.dmypy.json

# PyInstaller
build/
dist/
*.spec

# Docker related
*.pid
*.seed
docker-compose.override.yml
"""

ignore_docker = """
# Python cache and compiled files
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
venv/
.venv/
env/

# Git repo and config
.git
.gitignore

# Dockerfile and config
.dockerignore
Dockerfile*
docker-compose*

# Local configuration and environment
.env
.env.*

# Logs
*.log

# VS Code project files
.vscode/

# System files
.DS_Store
Thumbs.db
"""

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content.strip())
    print(f"✅ Created {filename}")

if __name__ == "__main__":
    write_file(".gitignore", ignore_git)
    write_file(".dockerignore", ignore_docker)
