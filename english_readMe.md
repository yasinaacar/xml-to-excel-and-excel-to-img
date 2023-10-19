# XML To Excel & Excel To Image

## Project Description

This project addresses the need of a business to access information about products provided by the collaborating company, which is presented in XML format. The business only wants to focus on product names and image tags, without dealing with other details in the XML file. 

In response to these requirements, this project allows seamless access to the desired data - product names and image tags.

## Project Features

- **xml-to-excel.py Script:** This script saves the XML file in the project folder as a .xml file and generates an Excel file based on specified tags.
- **excel-to-img.py Script:** This script automatically visits image URLs in the Excel file, downloads, and saves the images.
- **Logging Mechanism:** Successful and unsuccessful download operations are logged in the folder where downloaded images are saved.

## Installation

1. Download the project folder to your local machine.
2. Open the project folder in an editor of your choice, and you're ready to start using/testing the application.

## Usage

1. Save the XML file in the project folder with the .xml extension.
2. Run the `xml-to-excel.py` script and enter the name of the XML file you want to process into the variable named `xml_file` in the script.
   - The script will create an Excel file based on the tags specified in the XML file. (The desired data will be saved in the created Excel table.)
3. Run the `excel-to-img.py` script and enter the name of the created Excel file into the variable named `df`.
   - The script will automatically visit image URLs in the Excel file, download, and save the images.
4. Downloaded images will be saved in the specified folder in the project directory, and the download status will be printed to the console.

Feel free to reach out if you have any questions or need further assistance!
