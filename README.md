# File Integrity Manager (FIM)

## Overview

The File Integrity Manager (FIM) is a Python-based tool designed to create baselines for text files using the SHA256 hash algorithm and monitor file integrity in real time. Whether you need to ensure the security of critical files or detect unauthorized changes, FIM provides a straightforward solution.

## Features

1. **Baseline Creation:**
   - Create or update baselines for text files by calculating and storing SHA256 hashes.
   - Baselines serve as reference points for detecting changes in file integrity.

2. **Real-time Monitoring:**
   - Continuously monitor specified text files to detect any alterations.
   - Compare the current file hash with the baseline hash to identify potential integrity issues.

3. **User-friendly Interface:**
   - Simple command-line interface (CLI) for easy setup and management.
   - Intuitive prompts guide users through the baseline creation and monitoring processes.

## Getting Started

1. **Installation:**
   - Clone the repository to your local machine.
   - Ensure Python (version 3.6 or higher) is installed.
   - Run `pip install hash` to install dependencies.

2. **Usage:**
   - Create a baseline for a text file:
     ```
     python main.py A <file_path>
     ```
   - Monitor a text file:
     ```
     python main.py B <file_path>
     ```

## Example

### Creating a Baseline for a Text File

```bash
python main.py A example.txt
```

### Monitoring a Text File

```bash
python main.py B example.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
