# 📂 File Read & Write with Error Handling

## Overview
This Python program reads a file provided by the user, applies a modification to its content, and saves the result into a **new file**.  
It includes **error handling** to manage cases where the file does not exist, cannot be read, or cannot be written to.

---

## Features
- ✅ Reads content from a user-specified file
- ✅ Handles common file errors (missing file, permission issues, unexpected errors)
- ✅ Modifies the content (example: converts all text to uppercase)
- ✅ Saves the modified content to a **new file** without overwriting the original

---

## How It Works
1. The user is prompted to **enter the filename** of an existing file.
2. The program attempts to **read** the file:
   - If the file does not exist → Displays an error message.
   - If permission is denied → Displays an error message.
   - If another error occurs → Displays the error.
3. If reading is successful:
   - The text is **modified** (converted to uppercase in this version).
   - A new file is created with the prefix `modified_`.
4. The modified content is **written** to the new file.

---

## Example
**Input File (`example.txt`):**
