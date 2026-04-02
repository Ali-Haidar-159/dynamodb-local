# DynamoDB Local CRUD Playground

Small Python project to practice CRUD and filter operations against a local DynamoDB instance using Docker Compose.

## What’s Inside
- `table_create.py` creates the `Products` table.
- `insert_data.py` inserts single or batch items.
- `read_data.py` reads one item or scans all.
- `update_data.py` updates an item.
- `delete_data.py` deletes an item.
- `filters.py` scans and filters items by `productId`.
- `main.py` is the entry point to run any operation.

## Prerequisites
- Python 3.10+ (venv recommended)
- Docker + Docker Compose

## Setup
## Clone
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

## Install And Run
1. Start DynamoDB Local and the admin UI:
```bash
docker compose up -d
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install boto3
```

3. Create the table:
```bash
python3 table_create.py
```

4. Run operations:
```bash
python3 main.py
```

## Notes
- DynamoDB Local is exposed on `http://localhost:8000`.
- The admin UI is available at `http://localhost:8001`.
- Edit `main.py` to choose which operations to run.

## Example Data Model
`Products` table:
- Partition key: `productId` (Number)
- Attributes: `name`, `product_name`, `price`

## Project Layout
```
.
├─ docker-compose.yml
├─ table_create.py
├─ insert_data.py
├─ read_data.py
├─ update_data.py
├─ delete_data.py
├─ filters.py
└─ main.py
```
