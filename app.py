from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from argon2 import PasswordHasher

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="change-this-later")
templates = Jinja2Templates(directory="templates")
ph = PasswordHasher()
