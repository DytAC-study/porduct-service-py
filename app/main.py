from fastapi import FastAPI
from app.routes import products
from app.config import load_env
from fastapi.middleware.cors import CORSMiddleware

# 加载环境变量
load_env()

app = FastAPI()

# CORS 允许所有来源（可在生产环境限制）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(products.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
