# Objective

Scrapes the questions and it's options from the google form

## Setup

1. Clone the repo
2. Navigate to `assessments_creator` directory
3. Create a virtual environment with name `env`

```bash
python -m venv env
```

2. Activate the virtual environment -

```bash
source env/bin/activate
```

3. Update the pip

```bash
python -m pip install --upgrade pip
```

4. Install the dependencies -

```bash
pip install -r requirements.txt
```

5. Run the application -

```bash
python main.py
```


## Testing

```bash
pytest
```