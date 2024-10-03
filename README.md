# CrackIt

## Description
 CrackIt is a Python-based tool that utilizes brute force algorithms to crack user-defined passwords. It estimates the time taken to crack the password and provides an estimated time if the password cannot be cracked within 45 seconds. This project helps assess the password strength against brute force password cracking attacks.

## Features
- **Brute Force Password Assessment**: Tests the strength of user-defined passwords against brute force methods.
- **Time Tracking**: Displays the time taken to attempt to crack the password.
- **Estimated Time**: If the password isn't cracked within 60 seconds, the application shows an estimated time required based on the complexity of the password.
- **Simple GUI**: Built using HTML and CSS for a user-friendly experience.

## Installation
To run this project, ensure you have Python installed on your machine. Then, follow these steps:

 **Clone the Repository**:
   ```bash
   git clone https://github.com/HaraPrasadTripathy/CrackIt.git
   cd CrackIt

## Usage
   python app.py

### Example
1. **Enter the Password**: Input the password you want to assess in the provided text field.
   
2. **Start Assessment**: Click the "Crack Password" button to initiate the assessment process.

3. **Results**: After some time, the application will display the results. For example:

   Password to assess: mySecret123
   Assessing...
   Time taken: 12 seconds

   If the password isn't cracked within 60 seconds, you might see: Time Exceeded. Estimated time to crack: 1770.12 seconds.


