# workshop
Workshop (FastAPI)

### start app
```uvicorn app:app --host 0.0.0.0 --port 7000 --reload```

### create db (database.sqlite3)
/workshop/src:
```python```

```from workshop.database import engine```

```from workshop.tables import Base```

```Base.metadata.create_all(engine)```