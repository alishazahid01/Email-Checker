import dns.resolver

def check_email_existence(email, domain):
    full_email = f"{email}@{domain}"
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True
    except dns.resolver.NXDOMAIN:
        return False

def filter_existing_emails(email_list, domain):
    existing_emails = []
    for email in email_list:
        if check_email_existence(email, domain):
            existing_emails.append(email)
    return existing_emails

def save_valid_emails_to_file(valid_emails, output_filename):
    with open(output_filename, 'w') as f:
        for email in valid_emails:
            f.write(email + '\n')

domain_to_check = 'indeed.com'
input_filename = 'rawemails.txt'
output_filename = 'valid_emails.txt'

with open(input_filename, 'r') as f:
    emails_to_check = [line.strip() for line in f.readlines()]

existing_emails = filter_existing_emails(emails_to_check, domain_to_check)

if existing_emails:
    save_valid_emails_to_file(existing_emails, output_filename)
    print(f"Valid emails saved to {output_filename}")
else:
    print(f"No valid emails found for {domain_to_check}")
