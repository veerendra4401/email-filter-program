import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime

class Email:
    """
    Class to represent an email with subject, sender, and date
    """
    def __init__(self, subject, sender, date):
        self.subject = subject
        self.sender = sender
        self.date = date

def connect_to_email(email_address, password, imap_server="imap.gmail.com"):
    """
    Connect to email server using IMAP
    """
    try:
        # Create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL(imap_server)
        # Authenticate
        imap.login(email_address, password)
        return imap
    except Exception as e:
        print(f"Error connecting to email: {str(e)}")
        return None

def fetch_emails(imap):
    """
    Fetch emails from the inbox
    """
    emails = []
    try:
        # Select the inbox
        status, messages = imap.select("INBOX")
        
        # Get all email IDs
        status, email_ids = imap.search(None, "ALL")
        
        # Convert email IDs to list
        email_ids = email_ids[0].split()
        
        # Get last 10 emails
        for email_id in email_ids[-10:]:
            status, msg_data = imap.fetch(email_id, "(RFC822)")
            email_body = msg_data[0][1]
            email_message = email.message_from_bytes(email_body)
            
            # Get subject
            subject = decode_header(email_message["subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            
            # Get sender
            sender = email_message["from"]
            
            # Get date
            date_str = email_message["date"]
            
            emails.append(Email(subject, sender, date_str))
            
        return emails
    except Exception as e:
        print(f"Error fetching emails: {str(e)}")
        return []

def filter_lead_subjects(emails):
    """
    Filter emails that contain the word 'Lead' (case-insensitive) in their subjects.
    
    Args:
        emails (list): List of Email objects
        
    Returns:
        list: Filtered list containing only emails with 'Lead' in subject
    """
    return [email for email in emails if 'lead' in email.subject.lower()]

def display_email(email):
    """
    Display email details in a formatted way
    """
    print("\n" + "="*50)
    print(f"From: {email.sender}")
    print(f"Date: {email.date}")
    print(f"Subject: {email.subject}")
    print("="*50)

def main():
    # Get email credentials
    email_address = input("Enter your email address:")
    password = input("Enter your email password (for Gmail, use App Password): ")
    
    # Connect to email server
    print("\nConnecting to email server...")
    imap = connect_to_email(email_address, password)
    
    if imap:
        print("Connected successfully!")
        
        # Fetch emails
        print("Fetching emails...")
        emails = fetch_emails(imap)
        
        # Filter and print the results
        lead_emails = filter_lead_subjects(emails)
        
        print(f"\nFound {len(lead_emails)} emails containing 'Lead':")
        for email in lead_emails:
            display_email(email)
            
        # Logout
        imap.logout()
    else:
        print("Failed to connect to email server.")
        print("Please check your email and password and try again.")

if __name__ == "__main__":
    main() 