docker build . -t pynita
docker run -it \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -e DISPLAY=$DISPLAY \
        --user user \
        -v $(pwd):/app \
        pynita python3 pynita_gui_main.py