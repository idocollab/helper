# Helper.py 🛠️
> A Python utility module to handle user input errors gracefully and improve input validation in your projects.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/yourusername/helper.py?style=social)

---
## check tutorial.py for example usage.
## Table of Contents
- [About](#about)
- [Features](#features)
- [Functions](#functions)
  - [get_input()](#get_input)
  - [log_setup()](#log_setup)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots / GIFs](#screenshots--gifs)
- [Developer & Contact](#developer--contact)
- [License](#license)

---

## About
`helper.py` is a **lightweight Python module** designed to make user input safe and smooth.  
It prevents crashes from invalid input, provides **custom error messages**, and loops until valid input is received.  

Perfect for **beginners and advanced users** looking for a **robust input handler** for their projects.  

> ⚡ **Why use it?** Saves time, reduces bugs, and makes your project user-friendly.

---

## Features
- ✅ Handles **invalid data types** (numbers, strings, etc.)  
- ✅ Prevents crashes from **unknown key inputs** (Ctrl, Shift, Alt)  
- ✅ Loops input until valid data is entered  
- ✅ **Custom error messages** for every input  
- ✅ **Customizable prompts**  
- ✅ Optional **positive number validation**  
- ✅ Built-in **logging setup** for debugging and tracking  

---

## Functions

### `get_input()`
Safely takes user input with validation.

**Parameters:**

| Parameter    | Type        | Default        | Description |
|--------------|------------|----------------|-------------|
| `command`    | `str`      | —              | The input prompt to display. Example: `number = get_input("Enter a number: ")` |
| `data_type`  | `type`     | `str`          | Expected data type (e.g., `int`, `float`). Do **not** pass as string. |
| `error`      | `str`      | `"Wrong Data..."` | Custom error message if input is invalid. |
| `num_check`  | `bool`     | `False`        | If `True`, input must be a positive number. |

**Example Usage:**
        ```python
        from helper import get_input

        # Basic input
        name = get_input("Enter your name: ")

        # Input with specific type and custom error
        age = get_input("Enter your age: ", data_type=int, error="Please enter a valid number!")

        # Positive number check
        score = get_input("Enter a positive score: ", data_type=float, num_check=True)

        💡 Tip: Always specify data_type for number inputs to avoid invalid data.


-Second function : log_setup()

Sets up a logging system for your project.

Parameters: None (prompts for a filename).
If an invalid filename is given, logs are saved in look.log

Usage:
          import logging
          from helper import log_setup

          # Initialize logging
          log_setup()

          # Example log messages
          logging.info("Application started successfully.")
          logging.warning("This is a warning message.")
          logging.error("This is an error message.")

⚠️ Note: Don’t forget to import logging in your main Python file.
💡 Tip: Use logging to track user activity and debug your code effectively.

# Developer & Contact
This module will be continuously updated. For latest resources and updates:
**
Instagram: @idocollab<br>
Email: shivampy.dev@gmail.com
**

Words from the developer: “Stay connected for updates and more helpful tools.
