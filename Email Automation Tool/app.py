import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "u043@gmail.com"  # Replace with your email
receiver_emails = emails = ["abc@gmail.com"]

 # List of recipient emails
cc_email = "ba@gmail.com"  # Single CC email
subject=" "
# Function to extract first name from email
def extract_first_name(email):
    name_part = email.split('@')[0].split('.')[0]
    first_name = ''.join([char for char in name_part if char.isalpha()])
    return first_name.capitalize()

# Loop through each recipient to personalize the email
for receiver_email in receiver_emails:
    first_name = extract_first_name(receiver_email)
    
    # Updated email body with your provided content
    body = f"""<html>
<body>
    <p>Hello {first_name},</p>
</body>
</html>"""

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email  # Send to only this individual recipient
    message["Cc"] = cc_email  # Add the CC recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))  # HTML format

    # Combine "To" and "Cc" recipients for sending the email
    all_recipients = [receiver_email] + [cc_email]  # Add CC to the list of recipients

    # SMTP server and login details (for Gmail in this case)
    smtp_server = "smtp.gmail.com"  # Correct SMTP server for Gmail
    smtp_port = 587
    password = " "  # Replace with your app-specific password

    # Establish the SMTP connection
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            
            # Send the email to the current recipient and CC
            server.sendmail(sender_email, all_recipients, message.as_string())
            print(f"Email sent successfully to {first_name} and CC recipient!")
    except Exception as e:
        print(f"An error occurred: {e}")
