from prefect.blocks.system import Secret
from prefect_sqlalchemy import DatabaseCredentials
import os

github_access_token = os.environ.get("GITHUB_ACCESS_TOKEN", "123")
access_token_secret = Secret(value=github_access_token)
access_token_secret.save("access-token", overwrite=True)


db_username = os.environ.get("POSTGRES_USER", "postgres")
db_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
db_host = os.environ.get("POSTGRES_HOST", "100.122.186.37")
db_port = os.environ.get("POSTGRES_PORT", "5444")
db_database = os.environ.get("POSTGRES_DB", "crm_db")
# Define database credentials
db_credentials = DatabaseCredentials(
    driver="postgresql+psycopg2",
    username=db_username,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_database,
)

# Save the credentials block
db_credentials.save(name="postgres-db", overwrite=True)
