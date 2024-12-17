import typing
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

def format_response(message: str = None,
                    data: typing.Union[dict, list] = None,
                    status_code: int = 200):
    status = "success" if status_code >= 200 <= 299 else "error"
    return JSONResponse({
        "status": status,
        "data": data,
        "message": message
    })

@app.get("/")
def hello_world():
    return format_response("Hello World")