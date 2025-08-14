# Academic-Document-Analyser-and-Generator (CLI)

A Python CLI tool that:
- Analyzes academic papers for structure, references, writing style, and plagiarism.
- Generates citations in APA, MLA, Chicago, and IEEE formats.

## Features
- Structure check (Abstract, Introduction, Conclusion, References)
- Reference validation
- Writing style analysis
- Plagiarism check against corpus
- Citation generator for 4 styles

## How to Run
```bash
python Academic_Document_Analysis_and_Generation.py
 Academic Paper Analyzer (CLI Tool)

## Installation
### 1. Download the Project
Click the green **Code** button at the top right → **Download ZIP**,  
or clone with:
```bash
git clone https://github.com/LogicPhantomX/Academic-Document-Analyser-and-Generation.git

## Extract the ZIP

If downloaded as ZIP, unzip it into a folder on your computer.

## Ensure Python is Installed

This project works with Python 3.8+.
Check your Python version:

python --version


## Arguments:

Argument	Description

--paper	Path to the academic paper text file
--refs	Path to the reference list text file
--container_dir	Path to folder containing container documents for plagiarism detection
--output	File path to save the JSON report



---

## Citation Generation Mode

Generate citations in multiple formats:

pythonAcademic_Document_Analysis_and_Generation.py

Follow prompts to select citation style and enter details.


---

## Sample Output

JSON Report Example:

{
    "structure_analysis": "Well-organized paper with minor formatting issues.",
    "citation_check": "All citations match reference list.",
    "plagiarism_score": "5% similarity with corpus",
    "writing_style": "Clear and formal academic tone."
}

