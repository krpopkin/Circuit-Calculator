# Circuit Calculator

A desktop application built with Tkinter to perform basic formula calculations, including profit and circuit sum computations.

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)

## About

Circuit Calculator is a Python-based desktop GUI application leveraging the Tkinter library. It provides:

- **Profit Calculation**: Multiply cost by margin.  
- **Circuit Sum Calculation**: Sum values across up to five circuit inputs.

With a simple interface, users select the formula, enter parameters, and receive outputs.

## Features

- **Interactive GUI** using Tkinter.  
- **Multiple Formulas**: Profit and Circuit Sum.  
- **Dynamic Input Fields** that appear based on selected formula.  
- **Clear and Reset** functionality for quick parameter changes.

## Prerequisites

- Python 3.x  
- Tkinter (included in standard library)  

## Installation

1. **Clone** the repository  
   ```bash
   git clone https://github.com/krpopkin/Circuit-Calculator.git
   cd Circuit-Calculator
   ```

2. (Optional) **Use a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**  
   No external dependencies beyond the Python standard library.

## Usage

Run the application with:

```bash
python circuit_calculator.py
```

- Click on **Profit** or **Circuit Sum**.  
- Enter the required parameters.  
- Click **=** to compute and display the result.

## Project Structure

```
Circuit-Calculator/
├── .gitattributes
├── circuit_calculator.py    # Main Tkinter application
└── README.md                # Project documentation
```

## Contributing

1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/foo`).  
3. Commit your changes (`git commit -m "Add feature"`).  
4. Push to the branch (`git push origin feature/foo`).  
5. Open a Pull Request.

## License

This project is unlicensed. You can add an [MIT](https://opensource.org/licenses/MIT) or other open-source license as needed.

## Author

**Ken Popkin**  
*GitHub:* [@krpopkin](https://github.com/krpopkin)  
*Email:* krpopkin@gmail.com
