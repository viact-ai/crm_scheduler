# /// script
# dependencies = ["prefect"]
# ///

"""
# Deploy a flow from a git repository

This example shows how to deploy a flow from a git repository.
It assumes you have a work pool named `process`. You can implicitly create the
work pool by starting a worker:

```bash
prefect worker start --pool process --type process
```
"""

from prefect import flow
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret
from prefect.client.schemas.schedules import CronSchedule


def deploy():
    print(f"deploy deploy flow... {Secret.load('github')}")
    # flow.from_source will actually clone the repository to load the flow
    flow.from_source(
        # Here we are using GitHub but it works for GitLab, Bitbucket, etc.
        source=GitRepository(
            url="https://github.com/viact-ai/crm_scheduler.git",
        ),
        entrypoint="flows/flow_up_reminder.py:flow_up_reminder",
    ).deploy(
        name="flow-up-reminder",
        schedules=[
            # Run the flow every minute on the minute
            CronSchedule(cron="* * * * *"),
        ],
        work_pool_name="default-pool",
    )


if __name__ == "__main__":
    print(f"Deploying flow... {Secret.load('github')}")
    deploy()
