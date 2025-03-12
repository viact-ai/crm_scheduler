FROM prefecthq/prefect:3-python3.11

# Install `uv` package manager
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./
COPY blocks/* ./blocks/

# Install dependencies using `uv`
RUN uv pip install .

# Set the command to start the Prefect worker
CMD ["prefect", "worker", "start", "-p", "default-pool"]