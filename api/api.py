from fastapi import FastAPI

from api.responeses import CustomJSONResponse

app = FastAPI(
    default_response_class=CustomJSONResponse
)


@app.get('/')
def test_view():
    return {
        "ok": True,
    }



@app.get('/second')
def second_view():
    return {
        "second_ok": True,
    }