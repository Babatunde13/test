FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN echo "ls"
# # Runs the alembic configuration to update the DB URI based on env var
# RUN python /app/configure_alembic.py 

# # Run migration
RUN alembic upgrade head


EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]