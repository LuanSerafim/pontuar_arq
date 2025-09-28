from fastapi import FastAPI
from routes import auth
import uvicorn

app = FastAPI(title="Pontuar .arq API")

# Inclui as rotas de autenticação
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Backend .arq funcionando 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
