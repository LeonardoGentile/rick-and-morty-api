import os
from sys import path
import uvicorn

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
path.append(PROJECT_ROOT)

if __name__ == "__main__":
    uvicorn.run('src.main:app', reload=True, host="127.0.0.1", port=8000, log_level="info")
