# **Keylogger - Python Version**

---

**Hello friends,**

This is a simple yet powerful **keylogger** that I have created using Python. The main advantage of using this keylogger is its **cross-platform compatibility**, meaning it can run on any platform that supports Python, such as:

- **Windows**
- **Linux**
- **macOS**

---

## **Key Features:**

- **Cross-Platform Compatibility:**  
  This keylogger is designed to work seamlessly across all major operating systems. Whether you're using Windows, Linux, or macOS, as long as Python is installed, this tool will work without issues.

- **Keyboard Event Logging:**  
  It logs every keypress in real-time. Special keys such as space, backspace, and enter are handled uniquely for ease of reading:
  - **Space** is logged as a blank space.
  - **Backspace** is logged as "backspace" for clarity.
  - **Enter** is logged with a newline.

- **Mouse Event Logging:**  
  Unlike many basic keyloggers, this one also logs mouse actions such as button presses, releases, and scroll events, along with the exact coordinates of the cursor, providing an extra layer of detail.

- **Simple and Lightweight Code:**  
  The keylogger's code is minimal and highly customizable. Users can modify or extend the functionality easily, whether it's adding timestamps, changing logging formats, or filtering specific keys or actions.

- **No Installation Needed (Portable Python Support):**  
  You don't need to have Python installed on the target machine. By using a portable version of Python (e.g., WinPython), you can run the keylogger on any machine without relying on pre-installed software.

- **Multithreading for Real-Time Event Capture:**  
  The keylogger uses multithreading to handle both keyboard and mouse events simultaneously, ensuring smooth and accurate logging without delays or missed events.

- **Output Log File:**  
  All logged data is saved to a file called `keylog.txt`. Each keypress and mouse action is written in a human-readable format, making it easy to review the recorded events.

---

## **Advantages Over Existing Keyloggers:**

- **Cross-Platform & Portable:**  
  While many keyloggers are platform-specific, this Python-based keylogger works across multiple operating systems and can be run from a portable environment without requiring installation.

- **Customizable:**  
  Unlike most commercial keyloggers, this script is open-source and highly customizable. You can modify the behavior of the keylogger, add features like timestamps, or even change how certain keys are logged.

- **Educational & Transparent:**  
  This keylogger is open-source, meaning you can review, modify, and learn from the code. It's perfect for educational purposes and experimenting with how keylogging works at a fundamental level.

- **Lightweight:**  
  Many commercial keyloggers come with a lot of unnecessary bloat. This keylogger focuses only on logging keyboard and mouse events, keeping it lightweight and efficient.

---

## **Installation Instructions:**

### **Prerequisites (If Python is Installed):**
Ensure that **Python 3.x** is installed on your system.  
Install the required libraries by running:

```bash
pip install keyboard pynput
```

### **Running with Portable Python:**
1. Download a portable version of Python (e.g., WinPython).
2. Place the portable Python folder and the `keylogger.py` script in the same directory.
3. Execute the keylogger using the included `.bat` file (Windows only).

### **Converting to Executable (Optional):**
If you want to run the keylogger without installing Python, you can convert the script to a standalone executable using **PyInstaller**:

```bash
pyinstaller --onefile keylogger.py
```

The executable can then be run directly on the target system without requiring Python.

---

## **How It Works:**

- **Keyboard Hook:**  
  The script listens for key events using the `keyboard` library and logs them as they occur. Special handling for keys like space, backspace, and enter ensures that the log is human-readable.

- **Mouse Listener:**  
  The `pynput` library is used to monitor mouse actions, capturing clicks and scrolls along with the cursor's position. This adds additional detail to the log that many traditional keyloggers may miss.

- **Logging:**  
  All captured events (both keyboard and mouse) are saved to the `keylog.txt` file, which can be reviewed later to analyze the actions performed.

---

## **Usage:**

1. Run the `keylogger.py` script directly from the command line or use the included `run_keylogger.bat` file for easy execution (Windows).
2. The keylogger will begin capturing keyboard and mouse events and will log them to `keylog.txt` in the same directory.
3. To stop the keylogger, you can simply close the terminal or press **Ctrl + C**.

---

**Important Notes:**

- **Ethical Use Only:**  
  This tool is for educational purposes only. Unauthorized use of keyloggers on systems you don't own or have explicit consent to monitor is illegal and unethical.

- **Privacy:**  
  Always ensure that you have proper consent before using keyloggers, as they can compromise the privacy of individuals.
