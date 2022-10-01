docker build --platform linux/amd64 -t wetty .
docker tag wetty registry.heroku.com/digital-raiders-nasa22/web
docker push registry.heroku.com/digital-raiders-nasa22/web
heroku container:release web
