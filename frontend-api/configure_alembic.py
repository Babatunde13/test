import os
from dotenv import load_dotenv

load_dotenv()

def update_alembic_config_url():
    print(os.environ.get("SQLALCHEMY_DATABASE_URL"))
    alembic_ini_path = 'alembic.ini'
    with open(alembic_ini_path, 'r') as f:
        lines = f.readlines()
    with open(alembic_ini_path, 'w') as f:
        for line in lines:
            if line.startswith('sqlalchemy.url = '):
                print(line)
                line = f'sqlalchemy.url = {os.environ.get("SQLALCHEMY_DATABASE_URL")}\n'
            f.write(line)

if __name__ == '__main__':
    update_alembic_config_url()
