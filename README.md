# Storage MinIO API

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MinIO](https://img.shields.io/badge/MinIO-C7202C?style=for-the-badge&logo=minio&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PM2](https://img.shields.io/badge/PM2-Process_Manager-2B037A?style=for-the-badge&logo=pm2&logoColor=white)

A lightweight, scalable storage microservice designed to handle file operations seamlessly across any distributed architecture. This API acts as an efficient and independent bridge between client applications and MinIO object storage servers. By abstracting the complexity of direct storage interactions, it provides secure, high-performance endpoints for single file uploads, concurrent batch processing, and reliable downloads. Its fully decoupled nature makes it an ideal plug-and-play solution for any project requiring robust file management.

## 🏗️ Architecture & Tech Stack

-   **Framework:** FastAPI (Python)
-   **Storage Server:** MinIO
-   **Process Management:** PM2
-   **Infrastructure:** Docker & Docker Compose (Multi-architecture optimized AMD64/ARM64)
-   **Data Validation:** Pydantic

### 🚀 Key Features
-   **High Performance:** Fully asynchronous capabilities provided by FastAPI and Uvicorn.
-   **Secure File Handling:** Strict path traversal protection and local directory validation before any MinIO transaction.
-   **Batch Uploads:** Concurrent thread-based processing for uploading multiple files to buckets simultaneously.
-   **Flexible Deployment:** "Plug and play" architecture ready for Dockerized environments or bare-metal PM2 setups using isolated virtual environments.

---

## 📂 Repository Structure

~~~text
storage_minio/
├── app/
│   ├── controllers/          # Route handlers and API endpoints definition
│   ├── core/                 # Configuration, environment variables, and constants
│   ├── models/               # Pydantic schemas for request/response payloads
│   ├── services/             # Core business logic and MinIO client integrations
│   └── main.py               # FastAPI application entry point
├── logs/                     # Persistent PM2 application logs directory
├── docker-compose.yml        # Multi-container orchestration
├── Dockerfile                # Multi-stage optimized image build
├── ecosystem.config.js       # PM2 advanced configuration file
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md
~~~

---

## 🚀 Getting Started

### Prerequisites
-   Python 3.10+
-   MinIO Server (Local or Remote)
-   Docker & Docker Compose *(For containerized execution)*
-   Node.js & PM2 *(For bare-metal production execution)*

### Environment Setup
This project uses a `.env` file for configuration. Before starting the application, you must create your local environment file:

1. Copy the example file:
   ~~~bash
   cp .env.example .env
   ~~~
2. Open `.env` and fill in your MinIO credentials, target endpoints, and the temporary working directory.

---

### Installation & Execution

**Option A: Running with Docker (Recommended)**
~~~bash
git clone https://github.com/JozRamirez10/Storage-MinIO.git
cd Storage-MinIO

# 1. Create your local environment file
cp .env.example .env

# STOP 🛑: Open the .env file in your editor and configure your MinIO credentials!

# 2. Build and run the container in detached mode
docker compose up -d --build
~~~

**Option B: Running in Production with PM2**
~~~bash
git clone https://github.com/JozRamirez10/Storage-MinIO.git
cd Storage-MinIO

# 1. Create your local environment file and fill it out
cp .env.example .env

# 2. Create the virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Start the application using PM2 (Uses the venv automatically)
pm2 start ecosystem.config.js
pm2 save
~~~

**Option C: Running locally for Development**
~~~bash
git clone https://github.com/JozRamirez10/Storage-MinIO.git
cd Storage-MinIO

# 1. Create your local environment file and fill it out
cp .env.example .env

# 2. Create the virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run the development server with live reload
uvicorn app.main:app --host 0.0.0.0 --port 7003 --reload
~~~

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request.