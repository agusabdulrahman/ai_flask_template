# Flask framework AI

AI project

### Setup project

```bash
# clone this repo and then setup the .env file

cp .env.example .env
```

### Running with Docker

```bash
docker compose up -d --build
```

### Running without Docker

**Requirements:**

- Python 3.12

- Mac / Linux / Windows

```bash
# Linux or Mac
python3 -m venv .venv

# Windows (bash)
python -m venv .venv
```

```bash
# Windows (bash)
source .venv/Scripts/activate

# Linux or Mac
source .venv/bin/activate
```

```bash
pip install --no-cache-dir -r requirements.txt
```

```bash
python app.py
```

### Structure folder

```
flask-framework/
├── app/
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── get_data.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main_routes.py
│
│   ├── services/
│   │   └── /
│   │   │   └── model/
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── utils.py
│   │
│   ├── __init__.py
│   │
│   └── cofig.py
│
├── testing/
│       └── test_prediction.py
│
├── .dockerignore
├── .env.example
├── Dockerfile
├── README.md
├── requirements.txt
└── app.py
```
