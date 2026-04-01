# FastAPI101_task_tracker

# для запуска
# docker build . --tag fastapi
# docker run -p 80:80 fastapi

# docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app

echo "# FastAPI101_task_tracker" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:lafayette007/FastAPI101_task_tracker.git
git push -u origin main

# selectel
# git
sudo apt-get update
sudo apt-get install git

# docker
https://docs.docker.com/engine/install/ubuntu/

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update


sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
