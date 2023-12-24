
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Streamlit Version](https://img.shields.io/badge/streamlit-1.29-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# Lease Agreement Generator 

## Overview
This Lease Agreement Generator is a Streamlit-powered application designed to automate the creation of customized lease agreements. Users can input tenant and property details, and the app will generate a downloadable DOCX file containing the lease agreement.

## Features
- User-friendly interface with Streamlit.
- Customizable fields for tenant and property details.
- Automated replacement of placeholders in a DOCX template.
- Downloadable, filled-in lease agreement in DOCX format.
- Preview of the lease agreement before downloading.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone [repository URL]
cd [repository directory]
pip install -r requirements.txt
```

## Usage

To run the application:

```bash
streamlit run app.py
```

Navigate to the provided URL to access the web interface.

## How It Works

1. **Input Data**: Enter details like tenant name, property address, rent details, etc.
2. **Template Processing**: The app uses the `python-docx` library to fill in a DOCX template with the provided details.
3. **Preview and Download**: Preview the lease agreement and download it as a DOCX file.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under [MIT License](LICENSE).



Replace `[repository]` and `[repository URL]` with your GitHub repository's information. 

## Dependencies
- Streamlit
- python-docx
- reportlab
- base64

## Support

For support, please open an issue on the GitHub repository or contact the maintainers.

## App Screenshot 
![Screenshot 2023-12-24 at 5.38.09 AM.png](..%2F..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202023-12-24%20at%205.38.09%E2%80%AFAM.png)