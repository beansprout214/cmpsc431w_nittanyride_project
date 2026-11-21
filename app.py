import sqlite3
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="temp")
templates = Jinja2Templates(directory="templates")
ph = PasswordHasher()

def get_db():
  return sqlite3.connect("nittanyRide.db")

@app.get("/login")
def login_page(request: Request):
  return templates.TemplateResponse(request, "login.html", {"error": None})
  
@app.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
  email = email.strip().lower()
  connection = get_db()
  cursor = connection.cursor()
  row = cursor.execute("SELECT password FROM User WHERE email_address = ?",(email,)).fetchone()
  if row and row[0]:
    stored_hash = row[0]
  if stored_hash:
    try:
      ph.verify(stored_hash,password)
    except (VerifyMismatchError, InvalidHashError):
      connection.close()
      return templates.TemplateResponse(request,"login.html",{"error":"Invalid email or password"}, status_code=401)
  else:
    connection.close()
    return templates.TemplateResponse(request,"login.html",{"error":"Invalid email or password"}, status_code=401)
  support = cursor.execute("SELECT 1 FROM Support_Staff WHERE support_email_address = ?",(email,)).fetchone()
  driver = cursor.execute("SELECT 1 FROM Driver WHERE driver_email_address = ?",(email,)).fetchone()
  rider = cursor.execute("SELECT 1 FROM Rider WHERE rider_email_address = ?",(email,)).fetchone()
  connection.close()
  role = None
  if support:
    role = "support"
  elif driver:
    role = "driver"
  elif rider:
    role = "rider"
  if not role:
    return templates.TemplateResponse(request,"login.html",{"error":"User has no role (e.g. Rider, Driver, Support)"}, status_code=401)
  request.session.clear()
  request.session["email"] = email
  request.session["role"] = role
  return RedirectResponse(url="/" + request.session["role"],status_code=303)

@app.get("/rider")
def rider_page(request: Request):
  if "email" not in request.session:
    return RedirectResponse(url="/login",status_code=303)
  if request.session["role"] != "rider":
    raise HTTPException(status_code=403, detail="Not allowed")
  return templates.TemplateResponse(
    request, "rider.html", {"email":request.session["email"],"role":request.session["role"]}
  )

@app.get("/driver")
def driver_page(request: Request):
  if "email" not in request.session:
    return RedirectResponse(url="/login",status_code=303)
  if request.session["role"] != "driver":
    raise HTTPException(status_code=403, detail="Not allowed")
  return templates.TemplateResponse(
    request, "driver.html", {"email":request.session["email"],"role":request.session["role"]}
  )

@app.get("/support")
def support_page(request: Request):
  if "email" not in request.session:
    return RedirectResponse(url="/login",status_code=303)
  if request.session["role"] != "support":
    raise HTTPException(status_code=403, detail="Not allowed")
  return templates.TemplateResponse(
    request, "support.html", {"email":request.session["email"],"role":request.session["role"]}
  )

@app.get("/logout")
def logout(request: Request):
  request.session.clear()
  return RedirectResponse(url="/login",status_code=303)

@app.get("/")
def blank(request: Request):
  return RedirectResponse(url="/login",status_code=303)