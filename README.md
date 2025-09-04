# Python Flask Games Web Application

A simple Flask web application featuring games like Stone Paper Scissors and Spin Wheel.

## Features

- Stone Paper Scissors game
- Spin Wheel game
- Dockerized application
- Automated deployment to Docker Hub using GitHub Actions

## Prerequisites

- Python 3.x
- Docker
- Docker Hub account (for deployment)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/wecloudheroes/pythoncopilot.git
cd pythoncopilot
```

2. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Docker

### Local Docker Build

Build the Docker image:
```bash
docker build -t pythoncopilot .
```

Run the container:
```bash
docker run -p 5000:5000 pythoncopilot
```

### Docker Hub Deployment

The application is automatically built and pushed to Docker Hub using GitHub Actions when changes are pushed to the main branch.

To pull and run the latest version from Docker Hub:
```bash
docker pull [your-dockerhub-username]/pythoncopilot:latest
docker run -p 5000:5000 [your-dockerhub-username]/pythoncopilot:latest
```

## GitHub Actions

The repository includes a GitHub Actions workflow that automatically:
1. Builds the Docker image
2. Pushes it to Docker Hub

Required GitHub Secrets:
- `DOCKER_HUB_USERNAME`: Your Docker Hub username
- `DOCKER_HUB_ACCESS_TOKEN`: Your Docker Hub access token

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
