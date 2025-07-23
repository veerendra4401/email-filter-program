def filter_lead_subjects(subjects):
    """
    Filter email subjects that contain the word 'Lead' (case-insensitive).
    
    Args:
        subjects (list): List of email subject strings
        
    Returns:
        list: Filtered list containing only subjects with 'Lead'
    """
    return [subject for subject in subjects if 'lead' in subject.lower()]

def main():
    # Example input as given in the task
    email_subjects = [
        "New Lead from Form",
        "Daily Report",
        "Zoom Invite",
        "Cybersecurity Lead"
    ]
    
    # Filter and print the results
    lead_subjects = filter_lead_subjects(email_subjects)
    
    # Print results exactly as shown in the expected output
    for subject in lead_subjects:
        print(subject)

if __name__ == "__main__":
    main() 
