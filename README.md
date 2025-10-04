# Specificatie Generator

Generates a Microsoft Word specification document (`specificatie.docx`) from a DBML file (`database.dbml`).

This small utility reads the DBML model using `pydbml` and writes a formatted `.docx` file with one table per database table, listing columns, types and basic constraints.

## Features
- Parses `database.dbml` in the current working directory
- Produces `specificatie.docx` with a table for each DB table
- Marks primary keys and nullable/not-null information

## Requirements
- Python 3.8+ (the project was developed against CPython on Windows)
- The Python packages listed in `requirements.txt`

## Installation
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the required packages:

```powershell
pip install -r requirements.txt
```

3. Place your `database.dbml` in the same folder as `main.py`.

## Usage
Run the script from the project directory where `main.py` and `database.dbml` are located:

```powershell
python main.py
```

After running, `specificatie.docx` will be created/overwritten in the same folder.

## Example
With a `database.dbml` describing a `users` table and a `posts` table, running the script will create a Word document containing one Word table per DB table with columns, types, nullable info and a PK indicator.

## Implementation notes
- The script uses `pydbml` to parse the DBML file and `python-docx` to generate .docx files.
- The generated table uses the `Table Grid` style. You can tweak `main.py` to change styling or add more metadata (indexes, comments, default values).

## Troubleshooting
- If you see import errors, ensure the virtual environment is active and `pip install -r requirements.txt` completed successfully.
- If `database.dbml` is not found, confirm the file name and working directory.

## Contributing
Small fixes and improvements are welcome. If you add features (like index export, constraints, or nicer formatting), include an updated `requirements.txt` and a short usage note.

## License
This repository has no explicit license file. Add `LICENSE` if you want to set one.

## Files of interest
- `main.py` — script that converts `database.dbml` -> `specificatie.docx`
- `requirements.txt` — pinned runtime dependencies (created alongside this README)