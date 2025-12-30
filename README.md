# 🟣 PurpleMerit – Full Stack Intern Assessment

A full-stack web application built as part of the **Backend Developer Intern assessment** for **PurpleMerit Technologies**.  
The project includes a **FastAPI backend** with JWT authentication and a **React (Hooks) frontend**, fully deployed and production-ready.

---

## 🚀 Live Deployment

### 🌐 Frontend (Vercel)
https://purplemerit-frontend.vercel.app

### 🔗 Backend API (Render)
https://purplemerit-backend-emzo.onrender.com

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- MongoDB (Atlas)
- JWT Authentication
- Pydantic
- Passlib (bcrypt)
- Render (Deployment)

### Frontend
- React (Hooks)
- Vite
- Axios
- React Router
- Vercel (Deployment)

---

## ✨ Features

### 🔐 Authentication
- User Signup & Login
- JWT-based authentication
- Token persistence
- Secure logout

### 👤 User Features
- View profile
- Update full name
- Change password
- Protected routes

### 👑 Admin Features
- Admin-only dashboard
- View all users
- Activate / Deactivate users
- Pagination support
- Role-based UI access

### 🎨 UI & UX
- Client-side validation
- Error & success messages
- Protected routing
- Responsive design
- Navigation bar with logout

---

## 🔒 Security Highlights
- JWT authentication
- Role-based access control
- Password hashing using bcrypt
- CORS configured for production (Vercel + Render)
- Admin-only endpoints protected at API level

---

## 📁 Project Structure

### Backend

app/
├── routes/
│ ├── auth.py
│ └── users.py
├── security.py
├── database.py
├── config.py
└── main.py

### Frontend
src/
├── api/
├── auth/
├── profile/
├── admin/
├── context/
├── components/
└── App.jsx


---

## ⚙️ Environment Variables (Backend)

Create a `.env` file with the following:

MONGO_URI=your_mongodb_uri
DATABASE_NAME=purplemerit
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60


---

## 🧪 API Documentation

Swagger UI is available at:
https://purplemerit-backend-emzo.onrender.com/docs


---

## 🧠 Key Learnings

- JWT authentication flow
- Role-based authorization
- CORS handling for deployed frontend
- SPA routing configuration for Vercel
- Secure password handling
- Debugging real-world deployment issues

---

## 📦 Deployment Notes

- Backend deployed on **Render**
- Frontend deployed on **Vercel**
- Fully integrated and production-ready

---

## 🙌 Author

**Yash Joshi**  
Backend / Full-Stack Developer  
GitHub: https://github.com/yashjoshi1

---

## ✅ Status

**✔ Assessment Completed Successfully**



