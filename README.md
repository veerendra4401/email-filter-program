# Email Subject Filter

This Python script can filter emails containing the word "Lead" (case-insensitive) in their subjects. It can either read from your actual email inbox or use example data.

## Features

- Connect to your email inbox (Gmail supported)
- Case-insensitive filtering of email subjects
- Displays full email details (Subject, Sender, Date)
- Clean and formatted output
- Well-documented code with docstrings

## Requirements

- Python 3.x
- Required Python packages:
  ```bash
  pip install secure-smtplib
  ```

## Usage

1. Run the script using Python:
   ```bash
   python email_filter.py
   ```

2. The script will ask for:
   - Your email address
   - Your password (For Gmail, use App Password - see below)

### For Gmail Users:
1. Enable 2-Step Verification in your Google Account
2. Generate an App Password:
   - Go to Google Account settings
   - Search for "App Passwords"
   - Generate a new app password
   - Use this password in the script instead of your regular password

## Example Output

```
Enter your email address: your.email@gmail.com
Enter your email password: ************

Connecting to email server...
Connected successfully!
Fetching emails...

Found 2 emails containing 'Lead':
==================================================
From: website@company.com
Date: Thu, 15 Mar 2024 09:30:21 -0700
Subject: New Lead from Contact Form
==================================================

==================================================
From: sales@company.com
Date: Thu, 15 Mar 2024 11:45:33 -0700
Subject: Sales Lead: Potential Client Meeting
==================================================
```

## Modifying Input

If you don't want to connect to email, the script will fall back to example data. You can modify the example emails in the `main()` function of `email_filter.py`. 