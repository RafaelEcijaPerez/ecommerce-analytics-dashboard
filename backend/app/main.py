from fastapi import FastAPI

app = FastAPI(title="Ecommerce Analytics API")

@app.get("/")
def root():
    return {"message": "API funcionando"}