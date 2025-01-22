# recommend-llm
Recommendation results received from llm
```commandline
docker build -f Dockerfile.dev -t recommend-llm:dev .
// docker run -d -p 8001:8001 --name recommend-llm-dev recommend-llm:dev
docker-compose up --build
```