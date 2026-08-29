from fastapi import APIRouter
from app.routes.practice_api001 import router as router_api_practice001
from app.routes.practice_api002 import router as router_api_practice002
from app.routes.practice_api003 import router as router_api_practice003

router = APIRouter()

router.include_router(router_api_practice001)
router.include_router(router_api_practice002)
router.include_router(router_api_practice003)