PPE-Leap Project Repository
===========================

This project include an SDK provided by the [official Leap Motion website](https://developer.leapmotion.com/ "Leap Motion website"). 

### SDK Details

**Version:** 2.3.1  
**Build:** 31549  

### Dependencies

Make sure you have [Python](https://www.python.org/downloads/ "Python 2.7.x") in version 2.7.x

##### On Linux (Ubuntu):

1. Install PyOpenGL

    ```bash
    sudo apt-get install python-opengl
    ```
    
2. Install the Leap Motion drivers and service/daemon software.

* Download the [Leap SDK (LTS)](https://developer.leapmotion.com/sdk/v2/ "Leap SDK (LTS)").

* For 32-bit systems, run: 
```bash
sudo dpkg --install Leap-version-x86.deb
```
* For 64-bit systems, run: 
```bash
sudo dpkg --install Leap-version-x64.deb
```
    > You may see an error message of leap.service, do not worry.

##### On Windows:

1. Install PyOpenGL

* Download the installer from [this link](https://pypi.python.org/pypi/PyOpenGL/3.0.2 "PyOpenGl Windows").

2. Install the Leap Motion drivers and service/daemon software.

* Download the [Leap SDK (LTS)](https://developer.leapmotion.com/sdk/v2/ "Leap SDK (LTS)").
* run Leap_Motion_Installer_version.exe

### Running the Project

##### On Linux (Ubuntu):

1. Open the terminal and run the Leap service:

    ```bash
    sudo leapd
    ```

    > Keep this running!

2. In the src folder, run the desired project:

    ```bash
    python leap.py
    ```

##### On Windows:

1. Make sure the Leap Service is running.
2. In the src folder, run the desired project:
    
    ```bash
    python leap.py
    ```
    
### Links
- [Python 2.7.x](https://www.python.org/downloads/ "Python 2.7.x").
- [PyOpenGl Windows](https://pypi.python.org/pypi/PyOpenGL/3.0.2 "PyOpenGl Windows").
- [Leap SDK (LTS)](https://developer.leapmotion.com/sdk/v2/ "Leap SDK (LTS)").

### Author
Gustavo Zanoni - [LinkedIn](https://br.linkedin.com/in/gustavo-zanoni-6371a791 "LinkedIn Link")
