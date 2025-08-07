# 🚀 FastAPI Hello App with Docker & GitHub Actions CI

This is a simple FastAPI application containerized using Docker and automated with GitHub Actions for CI/CD. It also includes optional Redis integration.

---


🗂️ Project Structure

ffastapi-hello/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── docker.yml
└── README.md


## 🐳 How to Run the App using Docker Compose

1. Clone the repository:
  
   git clone https://github.com/hpal99/fastapi-hello.git
   cd fastapi-hello
2. Run the app with Docker Compose: docker-compose up

3. Access the app:http://localhost:8000

⚙️ CI/CD Pipeline (GitHub Actions)

1. Every time you push code to the main branch:

2. GitHub Actions builds the Docker image.

3. Logs in securely to Docker Hub using GitHub Secrets.

4. Pushes the latest image to your Docker Hub repository.

5. Workflow File: .github/workflows/docker-build-push.yml

6. Secrets used:

DOCKER_USERNAME

DOCKER_PASSWORD (or Access Token)

📚 Key Learnings & Challenges Faced
🔄 Docker Hub 404 Issue: Faced 404 while pushing – resolved by verifying DockerHub repo visibility and using correct username.

🔐 Secrets Management: Learned how to securely pass Docker credentials to GitHub Actions.

🐍 FastAPI Import Error: Initially had an invalid import in main.py – fixed and verified during container test.

🧪 Testing Locally: Ensured app works with Docker Compose before deploying.

🔁 Debugging CI Failures: Gained experience interpreting GitHub Actions logs and retrying after fixing small YAML errors.

🌟 Improvements for Future
Add unit tests and integrate testing in CI workflow.

Push image with version tags (e.g., v1.0, latest) for better tracking.

Deploy to a cloud provider (e.g., Azure App Service or AWS ECS).

Set up GitHub Container Registry as an alternative to Docker Hub.



