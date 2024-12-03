# pyrate

###### Google Play Store apps *rating* script.

---

## Getting Started

This script allows you to collect reviews from Google Play Store applications, process them, and save the results in an organized Excel file. The setup includes pre-configured runner files for VS Code and PyCharm for ease of execution.

## Prerequisites

- Python 3.13.0 or higher

Ensure you have Python 3.13.0 installed. If not, download it from the [official Python website](https://www.python.org/downloads/). If yu currently use other Python versions, consider using a Pyenv tool.

## Setting up the enviroment

### 1. Create and Activate a Virtual Environment

Using a virtual environment ensures package dependencies are isolated for this project.

#### For macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install the Required Packages

You can install the dependencies using the provided `requirements.txt` file or manually via `pip` command.

#### Install using requirements.txt:

```bash
pip install -r requirements.txt
```

#### Or install manually:

```bash
pip install google-play-scraper pandas openpyxl python-dotenv
```

### 3 .env file

Create a `.env` file in the root of your project directory. This file will store the environment variables required for the script. A centralised enpoint to add the required information for the script.

#### Example `.env`

```.env
GOOGLE_APP_ID=<Google Play App ID>
LANGUAGE=es  # Language code (e.g., 'es' for Spanish, 'en' for English)
COUNTRY=es   # Country code (e.g., 'es' for Spain, 'us' for USA)
```

#### Inputs

- `GOOGLE_APP_ID`: The Google Play Store app ID (e.g., `com.example.app`).
- `LANGUAGE`: The desired language for the reviews.
- `COUNTRY`: The target country for the reviews.

---

## Running the Script

You can use pre-configured runner files for VS Code and PyCharm to streamline execution.

### Using VS Code
1. **Select the Python interpreter**:
   - Press `Ctrl + Shift + P`.
   - Select `Python: Select Interpreter`.
   - Choose the `.venv` interpreter located at:
     - **macOS/Linux**: `.venv/bin/python`
     - **Windows**: `.venv/Scripts/python`

2. **Run the script**:
   - Open `src/main.py`.
   - Press `F5` to execute the script.

3. **Using launch.json**:
   The project includes a `launch.json` file in the `.vscode` folder for debugging and running the script with predefined settings.

### Using PyCharm
1. Open the project in PyCharm.
2. Select the pre-configured runner in `Run/Debug Configurations` under the name `Main`.
3. Press `Shift + F10` to execute or `Shift + F9` to debug.
4. Ensure PyCharm is set to use the `.venv` environment.

### Classic

Still, you can run using terminal for a classical approach. Being on the proyect's directory, run:

```bash
python ./src/main.py
```

---

## Output

The script saves the collected reviews in an Excel file under the `out` directory:

- **File Name**: `reviews.xlsx`
- **Sheets**:
  - `Google Play`: Reviews from the Google Play Store.

---

## Notes

- Reviews are saved in Excel format with duplicate prevention. 
- For additional app review sources, extend the script or create new sheets in the Excel file. Contributing is welcome!

---

## Troubleshooting

1. **Permission Denied for Excel File**:  
   Ensure the Excel file (`reviews.xlsx`) is closed before running the script.

2. **Environment Not Configured**:  
   Double-check your `.env` file and make sure the `GOOGLE_APP_ID`, `LANGUAGE`, and `COUNTRY` values are set.

3. **Installation Issues**:  
   If pip fails to install a package, try upgrading pip:
   ```bash
   python -m pip install --upgrade pip
   ```

---

## Contributing

Feel free to fork the repository, improve the code, and submit pull requests. I have tried to gather reviews from Apple App Store but never succeded, help on this regard is welcome!

---

## License

This project is licensed under the GNU AGPL-3.0 License. See [`LICENSE.md`](https://github.com/juan-miii/pyrate/blob/master/LICENSE) for more information.
