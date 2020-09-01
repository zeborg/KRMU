# KRMU-Attendance-Downloader
Attendance downloader for KRMU Students.

## How do I use this script?
This script is currently usable **only in Linux**, but will be usable in Windows as well after the next commit.
\
If you're on Linux, follow the steps below to use this script:
1. Clone this repository.
1. Create a **Python virtual environment** and install the necessary dependencies in it by activating the environment and typing `pip install -r requirements.txt` in the terminal.
1. Once the dependencies are installed, type `python script.py` to run the script. The output will look similar to the one shown in the image below. *(yes, my attendance is pretty bad)*
\
![](https://i.ibb.co/SfPrLdr/attd-krmu.png)
1. The attendance screenshot will be available inside the newly created `Screenshots` folder in the same directory as the `script.py` file. The screenshot looks similar to the one shown below.
\
![](https://i.ibb.co/DzLKJjY/790e594820c6.png)

**NOTE:**
If you're facing the following error: `selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable may have wrong permissions. Please see https://sites.google.com/a/chromium.org/chromedriver/home`
\
Please make sure to check the ***Execute*** option in the `chromedriver` file properties as shown below.
\
![](https://i.ibb.co/3pGCxFT/Screenshot-from-2020-09-01-18-42-40.png)
