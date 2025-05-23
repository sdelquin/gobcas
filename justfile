# Run program
run:
    #!/usr/bin/env bash
    export FLASK_APP=main &&
    export FLASK_ENV=development
    uv run flask run

# Sync uv
[macos]
sync:
    uv sync --no-group prod

# Sync uv
[linux]
sync:
    uv sync --no-dev --group prod

# Deploy
deploy: && sync
    git pull
