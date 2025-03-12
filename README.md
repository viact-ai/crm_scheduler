## Installing uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Install Python 3.11

```bash
uv python install 3.11
```

## Creating a Virtual Environment with Python 3.11

```bash
uv venv --python 3.11
```

## Activating the Virtual Environment

```bash
source .venv/bin/activate
```

## Install packages

```bash
uv pip install .
```

## Run the flow locally

```bash
uv run flows/flow_up_reminder.py
```

# Deploy the flow to cloud

## Create other prefect profile

```bash
prefect profile create oncloud
```

## Set the profile to use

```bash
prefect profile use oncloud
```

## Set API endpoint

```bash
prefect config set PREFECT_API_URL=http://10.11.4.26:4200/api
```

## Deploy the flow to cloud

```bash
uv run deploy/deploy_flow_up_reminder.py
```
