# Desktop Cleaner

A simple and effective tool to organize cluttered folders with a single click.

## What is it?

**Desktop Cleaner** is a Python-based desktop application that automatically organizes files in a selected folder by sorting them into subfolders based on their file types. For example, all `.jpg` files go into a "JPG files" folder, `.pdf` files into a "PDF files" folder, and so on. It's especially useful for cleaning up downloads, desktops, or project directories.

## Features

- Automatically sorts files into subfolders based on their extensions  
- Simple and modern graphical interface using `customtkinter`  
- Supports browsing for folders through a file dialog  
- Real-time logs of file movements during the cleaning process  
- Dark mode interface by default  

## How it Works

1. Launch the application.
2. Enter or browse to the folder you want to clean.
3. Click **Start Cleaning**.
4. Watch as files are moved into neatly organized subfolders.

## Requirements

- Python 3.7 or above  
- `customtkinter`  
- `tkinter` (standard with most Python distributions)

Install the required library:

```bash
pip install customtkinter

## How to Run

Save the script as `desktop_cleaner.py` (or use the existing `cleaner.py`), then run:

```bash
python desktop_cleaner.py
