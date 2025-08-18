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

```bash
python3 -m venv .venv
or
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
│   ├── sensor/
│   │   ├── cod/
│   │   │   ├── model/
│   │   │   │   ├── model_cod.pkl
│   │   │   │   └── performance_model_cod.txt
│   │   │   ├── __ini__.py
│   │   │   ├── data_cleaning
│   │   │   ├── predict.py
│   │   │   ├── train_single_line.py
│   │   │   └── training_multiline.py
│   │   └── hrt/
│   │       ├── model/
│   │       │   ├── model_hrt.pkl
│   │       │   └── performance_model_hrt.txt
│   │       ├── __ini__.py
│   │       ├── data_cleaning
│   │       ├── predict.py
│   │       ├── train_single_line.py
│   │       └── training_multiline.py
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
└── wsgi.py
```
