from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

if __name__ == "__main__":
    uvicorn.run("asgi:app", host="0.0.0.0", port=8000, reload=True)



