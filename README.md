# parts

This is a sample Altium Designer library that can be maintained in a traceable way.

## Description

The library is file-based, and **SchLib** and **PcbLib** files are maintained by librarians. An auto-generated **XLSX file** is used to collect components' parameters and models, serving as a database for Altium. The XLSX file is produced from **CSV files** using a Python script. The CSV files are also maintained by librarians.

### Features

- Multiple librarians can maintain the library simultaneously.
- Users have their own clones of the library, allowing uninterrupted work during maintenance or update routines by librarians or when the main repository is unavailable.
- Unintended changes in spreadsheets are easily identified due to the plain-text nature of CSV files.
- Each change in the library includes a comment, author's name, and date.

## Getting Started

### Prerequisites

Users should have knowledge of Altium Designer and its library and database management. Refer to the Altium documentation links in the "See also" section below. Additionally, users should know how to run a Python script from the command line.

### Installation

1. Install Python.
2. Install the following packages:
   - `pandas`
   - `xlsxwriter`

### Configuration

Add the **Parts.DbLib** file to your Altium Designer project.

### Usage

1. Clone the provided sample.
2. Organize and rename the directory structure on your disk (e.g., on drive C):

```
parts
-- altium
-- Parts_db
```

3. Run the `csv2xlsx.py` script from the command line to generate the XLSX file.

### Troubleshooting

Ensure that Altium Designer is closed before updating the XLSX file.

## References

### See also

- [Working with File-based Component Libraries in Altium Designer](https://www.altium.com/ru/documentation/altium-designer/working-with-file-based-component-libraries/)
- [Working with Database Libraries in Altium Designer](https://www.altium.com/documentation/altium-designer/working-with-database-libraries)

### License

This project is licensed under the [MIT License](LICENSE.md).
