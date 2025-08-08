# 🚀 FastAPI Hello App with Docker & GitHub Actions CI

This is a simple FastAPI application containerized using Docker and automated with GitHub Actions for CI/CD. It also includes Redis integration.

---


🗂️ Project Structure

-hello/
├── app/
│   └── main.py        # FastAPI app
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── .github/
│   └── workflows/
│       └── docker-fastapibuild-push.yml
└── README.md

## 🐳 How to Run the App using Docker Compose

1. Clone the repository:
  
   git clone https://github.com/hpal99/fastapi-hello.git
   cd fastapi-hello
2. Run the app with Docker Compose: 
   docker-compose up

3. Access the app:http://localhost:8000

4. CI pipeline explanation (GitHub Actions) — step-by-step

*What it does:

1. Runs on every push to main.

2. Checks out the repo, logs in to Docker Hub using secrets, builds the image, and pushes the image to your registry.

3. What you must add in GitHub repo settings:

DOCKER_USERNAME — your Docker Hub username (case-sensitive, not email)
DOCKER_PASSWORD — your Docker Hub password or Personal Access Token 


# 📚 Key Learnings & Challenges Faced

🔄 Docker Hub 404 Issue: Faced 404 while pushing – resolved by verifying DockerHub repo visibility and using correct username.

🔐 Secrets Management: Learned how to securely pass Docker credentials to GitHub Actions.

🐍 FastAPI Import Error: Initially had an invalid import in main.py – fixed and verified during container test.

🧪 Testing Locally: Ensured app works with Docker Compose before deploying.

🔁 Debugging CI Failures: Gained experience interpreting GitHub Actions logs and retrying after fixing small YAML errors.

# 🌟 Improvements for Future
1. Add unit tests and integrate testing in CI workflow.

2. Push image with version tags (e.g., v1.0, latest) for better tracking.

3. Deploy to a cloud provider (e.g., Azure App Service or AWS ECS).

4. Set up GitHub Container Registry as an alternative to Docker Hub.

Useful commands (cheat-sheet)
#build & run locally
docker compose up --build

#follow logs
docker compose logs -f web

#show containers
docker ps

#inspect health details
docker ps

#stop & remove
docker compose down

