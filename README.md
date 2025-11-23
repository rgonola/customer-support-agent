# Customer Support Agent

AI-powered customer support system with LangGraph workflow orchestration, RAG (Retrieval-Augmented Generation), and intelligent routing.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI GPT-4o-mini for intelligent customer support
- 🔍 **RAG with ChromaDB**: Vector database for knowledge base retrieval
- 🎯 **Smart Routing**: Automatic categorization (Technical, Billing, General)
- 😊 **Sentiment Analysis**: Detects customer sentiment (Positive, Neutral, Negative)
- 🔄 **LangGraph Workflows**: State-based conversation management
- 🚀 **Production Ready**: FastAPI backend with NGINX reverse proxy
- 📊 **Real-time & REST APIs**: WebSocket and HTTP endpoints

## Quick Start

### Prerequisites

- AWS EC2 instance or Azure Virtual Machine (Ubuntu 24.04 LTS)
- OpenAI API key
- Domain name (optional, for HTTPS)

### Deployment on Cloud Ubuntu VM

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git ~/customer-support-agent
cd ~/customer-support-agent
```

2. **Run the setup script:**
```bash
sudo chmod +x deployment/ec2/setup.sh
sudo deployment/ec2/setup.sh
```

3. **Configure your OpenAI API key:**
```bash
sudo nano ~/customer-support-agent/backend/.env
# Add: OPENAI_API_KEY=sk-your-actual-key-here
```

4. **Restart the service:**
```bash
sudo systemctl restart support-agent
```

5. **Access your application:**
- Frontend: `http://YOUR-EC2-IP/`
- API Docs: `http://YOUR-EC2-IP/docs`
- Health Check: `http://YOUR-EC2-IP/health`

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── agents/          # AI agent modules
│   │   ├── config/          # Configuration
│   │   ├── database/        # ChromaDB integration
│   │   ├── models/          # Pydantic schemas
│   │   ├── workflows/       # LangGraph workflows
│   │   └── main.py          # FastAPI application
│   ├── data/                # Knowledge base JSON
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   ├── index.html           # Web UI
│   └── static/              # CSS, JS, images
└── deployment/
     ├── ec2/                  # EC2 deployment files
          ├── setup.sh         # Automated setup script
          ├── nginx/           # NGINX configuration
          └── systemd/         # Systemd service

```

### **1. Backend Directory (`backend/`):**

This folder contains the server-side code and logic for your application.

* **agents/**:

  * This folder likely contains modules related to the **AI agents** that handle specific tasks in your app. AI agents are components that process requests, make decisions, and interact with the user or other parts of the system.

* **config/**:

  * This folder is for **configuration files**. These files contain the settings that determine how the application behaves (e.g., API keys, database settings).

* **database/**:

  * This folder is where the database-related code is located. It handles things like storing and retrieving data from a database. **ChromaDB** is likely the database system you're using here for storing and managing information.

* **models/**:

  * This folder contains the **data models**. Models are Python classes that define how data is structured and stored in the application (e.g., user data, support queries).

* **workflows/**:

  * This folder likely contains **LangGraph workflows**, which is a framework for defining how various tasks or processes are handled in your application, like routing or processing different types of requests.

* **main.py**:

  * This is usually the **main entry point** for the application. When you run your application, this file will be executed to start the backend server (in this case, it uses **FastAPI**, a web framework for building APIs).

* **data/**:

  * This folder stores **data files** related to your application, like pre-trained models, configuration data, or other resources needed by your app.

* **requirements.txt**:

  * This is a **dependencies file** that lists all the external libraries and tools needed to run your application. You install them by running `pip install -r requirements.txt` in Python.

* **.env.example**:

  * This file contains a template for **environment variables**. Environment variables are used to store sensitive information like database credentials or API keys. You would copy this file to `.env` and fill in your specific settings.

---

### **2. Frontend Directory (`frontend/`):**

This folder contains the **client-side** part of the application, which is what the user interacts with.

* **index.html**:

  * This is the **main webpage** of your application. It's the HTML file that gets loaded when a user opens the website in their browser.

* **static/**:

  * This folder contains **static files** like **CSS** (styles), **JavaScript** (scripts), and **images**. These files are necessary for styling and interactivity in the web application.

---

### **3. Deployment Directory (`deployment/`):**

This folder contains the files related to deploying and running the application on a cloud server (e.g., AWS EC2).

* **ec2/**:

  * This folder contains **deployment files** specific to setting up and running your application on an **AWS EC2 instance** (a virtual machine in the cloud).

  * **setup.sh**:

    * A **bash script** that automates the setup of the application on the server. It will install necessary dependencies, configure the server, and set up your application.

  * **nginx/**:

    * Contains **NGINX configuration files**. **NGINX** is a web server that serves your web pages and acts as a **reverse proxy** to forward requests to the backend.

  * **systemd/**:

    * Contains files related to **systemd**, which is used to manage services on Linux systems. Here, it would manage the backend service, ensuring it runs continuously in the background (e.g., the FastAPI application).

---

### **In Summary:**

* **Backend**: Deals with the logic, database, AI processing, and workflows that power your application.
* **Frontend**: Deals with the user interface (UI) and client-side behavior (what users see and interact with).
* **Deployment**: Contains files for setting up and running your application on a cloud platform like **AWS EC2**, including configuring web servers and background services.

---

This structure helps separate different parts of the application for easier development, testing, and maintenance.


## Tech Stack

- **Backend**: FastAPI, Python 3.12
- **AI**: OpenAI GPT-4o-mini, LangChain, LangGraph
- **Database**: ChromaDB (vector database)
- **Web Server**: NGINX
- **Process Manager**: Systemd
- **Frontend**: Vanilla HTML/CSS/JavaScript

