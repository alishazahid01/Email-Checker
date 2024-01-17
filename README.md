Email Existence Checker Documentation
Introduction

This Python script is designed to check the existence of email addresses by verifying the presence of valid Mail Exchanger (MX) records associated with the specified domain. It can be used to filter out existing email addresses from a list of potentially valid ones. This documentation provides an overview of the code structure, usage, and dependencies.
Getting Started

To use the Email Existence Checker script, follow these steps:

    Clone or download this repository to your local machine.

    Install the dnspython library, which is required for DNS resolution:


pip install dnspython

Create a text file (e.g., rawemails.txt) containing a list of email addresses to be checked, with one email address per line.

Open the Python script in a code editor and configure the following variables:

    domain_to_check: The domain against which you want to check email existence.
    input_filename: The name of the input file containing the list of email addresses.
    output_filename: The name of the output file where valid email addresses will be saved.

Run the script using the command:

    python email_checker.py

Code Structure

The Email Existence Checker script consists of the following components:
1. Checking Email Existence


def check_email_existence(email, domain):
    full_email = f"{email}@{domain}"
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True
    except dns.resolver.NXDOMAIN:
        return False

This function takes an email address and a domain as input and checks if valid MX records exist for the domain. If valid records are found, it returns True, indicating that the email address is potentially valid; otherwise, it returns False.
2. Filtering Existing Emails

def filter_existing_emails(email_list, domain):
    existing_emails = []
    for email in email_list:
        if check_email_existence(email, domain):
            existing_emails.append(email)
    return existing_emails

This function takes a list of email addresses and a domain and filters out the email addresses that have valid MX records associated with the specified domain. It returns a list of existing email addresses.
3. Saving Valid Emails to File


def save_valid_emails_to_file(valid_emails, output_filename):
    with open(output_filename, 'w') as f:
        for email in valid_emails:
            f.write(email + '\n')

This function takes a list of valid email addresses and an output filename. It saves the valid email addresses to the specified output file, with each email address on a separate line.
4. Main Execution

The main part of the script reads the list of email addresses from an input file, filters them to identify existing email addresses, and then saves the valid email addresses to an output file.
Usage

    Run the Python script to start the email existence checking process:

    python email_checker.py

    The script will check each email address in the input file against the specified domain's MX records.

    If valid email addresses are found, they will be saved to the output file (valid_emails.txt by default).

    The script will print a message indicating the number of valid email addresses found and their storage location.

Conclusion

This documentation provides an overview of the Email Existence Checker script, which helps identify valid email addresses by verifying the existence of MX records for a specified domain. You can customize and use this script to filter out valid email addresses from a list, making it useful for various email-related applications.
