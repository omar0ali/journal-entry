# Journal Entry
> Before launching the app, ensure that Python 3.x is installed on your system. Please visit: https://www.python.org/downloads/ download and install python in your system.


### CLI Accounting Journal Entry
The go-to solution for efficient and accurate accounting journal entries. This CLI application is tailored for professionals, accountants, and businesses seeking a digital platform to record and manage their financial transactions seamlessly. As a CLI app, it's designed for simplicity and speed, allowing you to record debit and credit transactions seamlessly from the command line.

1. Straightforward Commands: Easily input debit and credit transactions using simple, intuitive commands for quick journal entry creation.
2. Portability: Carry out your accounting tasks from any terminal or command prompt, ensuring flexibility and convenience.
3. Quick Setup: Get started in no time with a hassle-free setup process, allowing you to focus on managing your journal entries effortlessly.

> **Portable Version:** Download a portable version from the 'Releases' section on GitHub. This version allows you to run the application without installation. You can download the zip file.

> **Installable Version:** For a more integrated experience, check the 'Releases' section for an installable version. Follow the provided instructions to install the application on your system. Unfortunately this only available on Windows.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/omar0ali/statement-of-account.git

2. Navigate to the project directory:
    ```bash
    cd journal-entry
    ```
3. Create a virtual environment (you may choose a different name for your virtual environment):
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    * On Windows
        ```shell
        .\venv\Scripts\activate
        ``` 
    * On Mac or linux
        ```bash
        source venv/bin/activate
        ``` 
    Your command prompt or terminal prompt should change to indicate that you are now in the virtual environment.
5. Install project dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```
This will install all the required packages listed in the requirements.txt file.
## Run the project
Open terminal or command prompt on windows. Go to the directory where is the main.py is located and execute the app using the following command.

```
python3 main.py
```

### Deactivating the Virtual Environment
When you're done working on the project, you can deactivate the virtual environment:
```
deactivate
```

## Using the Standalone Executable
To make it easy for users to run your Python application, a standalone executable has been created using PyInstaller. Follow these steps to use the executable on your machine:

- Download the standalone executable for your operating system:
  - [Download for Windows](link_to_windows_executable)
  - [Download for macOS](link_to_macos_executable)
  - [Download for Linux](link_to_linux_executable)

### Step 2: Extract (if applicable)

- If you downloaded a zip archive, extract the contents to a directory of your choice.

### Step 3: Run the Executable

- **On Windows:**
  - Double-click on `your_app.exe` to run the application.

- **On macOS/Linux:**
  - Double-click on `your_app` to run the application.
  - Alternatively, open a terminal.
  - Navigate to the directory where the executable is located.
  - Run the following command:

    ```bash
    ./main.py
    ```

### Upcoming Features
GUI Version: I am also planning on making a graphical user interface version of this application in the feature. Stay tuned for a more intuitive and visually enhanced experience.