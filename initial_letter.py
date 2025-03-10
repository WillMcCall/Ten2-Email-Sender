import emails
import csv
import time

def main():
    email_addresses = []
    
    with open('files/email_addresses.csv', mode='r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            email_addresses.append(row[0])
        
    for email in email_addresses:
        emails.send_email(email, "I'm Going Overseas this Summer!", "initial_email")
        time.sleep(5)   # Avoid throttling for spam filters
        
    print("\n\33[32mSuccessfully sent emails!\33[0m")

if __name__ == "__main__":
    main()
