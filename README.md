# Employee_workload

# Employee Workload Statistics System — Step-by-Step Guide

This README provides a detailed, step-by-step explanation of the Employee Workload Statistics System project, including all main files and their roles, and how to run each version of the system.

---

## Project Structure Overview

```
Employee_Workload_Statistics_System/
├── main.cpp                # C++ (GTKmm) GUI application
├── main_load.cpp           # (Purpose not detailed; possibly a helper for main.cpp)
├── main_m.py               # Python (Tkinter) GUI application
├── employee_workload.csv   # Data file for Python Tkinter app
├── main.py                 # Python (PyQt5) GUI application
├── employee_data.csv       # Data file for Python PyQt5 app
├── Readme.md               # General project overview
├── README_STEP_BY_STEP.md  # (This file)
├── ...                     # Other files (configs, report, video, etc.)
```

---

## 1. Python Tkinter Application (`main_m.py`)

### Purpose
A desktop GUI for managing employee workload using Tkinter. Data is stored in `employee_workload.csv`.

### Step-by-Step Usage
1. **Install Python 3** (if not already installed).
2. **Install Tkinter** (usually included with Python).
3. **Navigate to the directory:**
   ```bash
   cd Employee_Workload_Statistics_System
   ```
4. **Run the application:**
   ```bash
   python main_m.py
   ```
5. **Features:**
   - Add, modify, and delete employee work entries.
   - Search/filter by Employee ID or Product Category.
   - View data in a table.
   - Export data, generate reports, and view employee rankings.

### Data File
- `employee_workload.csv` is automatically created/updated.


---

## 2. Python PyQt5 Application (`main.py`)

### Purpose
A modern desktop GUI for managing employee workload with PyQt5. Data is stored in `employee_data.csv`.

### Step-by-Step Usage
1. **Install Python 3** (if not already installed).
2. **Install PyQt5:**
   ```bash
   pip install PyQt5
   ```
3. **Navigate to the project root:**
   ```bash
   cd ..
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```
5. **Features:**
   - Add, update, and delete employee records.
   - View statistics (employee rankings by completion count).
   - Data table for all entries.

### Data File
- `employee_data.csv` is used for persistent storage.


---

## 3. C++ GTKmm Application (`main.cpp`)

### Purpose
A C++ GUI application using GTKmm for employee workload management. Data can be saved to CSV and Excel. Includes PDF report generation.

### Step-by-Step Usage
1. **Install GTKmm, xlnt (for Excel), and libharu/poppler (for PDF) as needed.**
2. **Compile the application:**
   ```bash
   g++ main.cpp -o workload_app `pkg-config --cflags --libs gtkmm-3.0` -lxlnt -lharu
   ```
   (Adjust library flags as required for your environment)
3. **Run the application:**
   ```bash
   ./workload_app
   ```
4. **Features:**
   - Add, update, and delete employee records.
   - Save/load data from CSV/Excel.
   - Generate PDF reports.
   - View statistics (employee rankings by completion count).

### Data File
- Data is saved to `employee_data.xlsx` or CSV as implemented.


---

## 4. Other Files
- `Readme.md`: General project overview (less detailed than this file).
- `Employee Workload Statistics System - Report_report.pdf`: Example output report.
- `video record.mp4`: (Optional) Demonstration video.


---

## Notes
- Each version is independent; you can use either Python GUI (Tkinter or PyQt5) or the C++ GUI.
- Data files are not shared between all apps (they use their own CSVs).
- For further details, see code comments in each file.

---

## Troubleshooting
- **Python Import Errors:** Ensure required modules are installed (`pip install PyQt5`).
- **C++ Compilation Issues:** Make sure all dependencies are installed and library paths are set correctly.

---

## Contact
For questions or contributions, see the main `Readme.md` or open an issue in your repository.

