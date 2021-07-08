**Requirements**
1. Raspberry Pi
2. Rasbian installed on the Pi


**Install MU**

In the Raspberry Pi menu, hover over Preferences, and click "Recommommed Software".

In the Recommommed Software application, scroll down unitl you find "MU". Check the box next to it and hit "Apply".

MU will start to install.


**Using MU**

After you open MU, start a new project and copy-paste the code from main.py.

Before you can run the code, open Terminal on your Raspberry Pi and type `crontab -e`.

Scroll to the bottom of the file, and add this line, `@reboot python3 /home/pi/main.py`. Change the directory of the file if needed.


**Save and Run**

Now all you have to do is save and run the python file and a graph of the CPU Tempeature of your Raspberry Pi will show up on screen.
