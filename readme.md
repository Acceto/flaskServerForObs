
# OBS installation
Follow the OBS instruction depending of your environment

# OBS settings
tools -> WebSocket server settings

    - Enable Websocket server
    - keep 4455 as server port
    - Generate a password
    - Click on "show connect info" and copy the password in webserver.py

# Usage of the text file
In OBS, click on the add button in the Sources pannel
    - Choose "text"
    - Set "Text input mode" to "From file"
    - Click on browse and enter the path of "infos.txt"


# Setup the python environment
Python >= v3.9 is necessary

> pip install flask flask-cors

> pip install obsws-python==1.7.2

# Run the webserver
> python webserver.py

in a navigator : http://127.0.0.1:5000/
