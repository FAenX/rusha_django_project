FROM python:3.8

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - 
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update\
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools18 unixodbc-dev\
    && echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' 

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

 