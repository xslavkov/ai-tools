# Basic python 3 docker

For those who don't want to run localy python for some reason, you can run pyhon in docker. 

## Build
Just run in `docker/python` directory

```
docker build -t python .
```

>This will create image. If you need extra library, append them to `requirements.txt` and run build again.

## Run
You can just run any local python script by 

```bash
docker run -it --rm --name python -v "$PWD":/app/src -w /app/src python python <your script>
```

There is shortcut script for that. Just go to your local python script location and run
```bash
./run.sh <your script>
```

> your script will be usually will be accessing some local resources (files), then go to your script directory and run `run.sh` relative to that path, i.e. `../docker/python/run.sh <your script>`

> you might need add right to run the script by  on your machine

```bash
chmod +x run.sh
```

> windows users might need to rename `run.sh` to `run.bat` but I haven't tested that yet.
