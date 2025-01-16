import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# give the Email details 
sender_email = "xyz@gmail.com"  # Replace with your email
receiver_emails = ["abc@gmail.com"]  # List of recipient emails
cc_email = "cc@gmail.com"  # Single CC email
subject = "add subject line of your email"

# Function to extract first name from email
def extract_first_name(email):
    # Split by '@' to remove the domain, then split by '.' to handle cases like "firstname.lastname"
    name_part = email.split('@')[0].split('.')[0]
    # If the name contains numbers (like in Sree17232), remove digits to extract the first name
    first_name = ''.join([char for char in name_part if char.isalpha()])
    return first_name.capitalize()

# Loop through each recipient to personalize the email
for receiver_email in receiver_emails:
    first_name = extract_first_name(receiver_email)
    
    # Updated email body with your provided content
    body = f"""<html>
<body>
    <p>Hello {first_name},</p>
    <p>Add Body </p>
</body>
</html>"""



    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)  # All primary recipients (To)
    message["Cc"] = cc_email  # Add the single CC recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))  # HTML format

    # Combine "To" and "Cc" recipients for sending the email
    all_recipients = receiver_emails + [cc_email]  # Add CC to the list of recipients

    # SMTP server and login details (for Gmail in this case)
    smtp_server = "smtp.gmail.com"  # Correct SMTP server for Gmail
    smtp_port = 587
    password = "app password"  # Replace with your app-specific password

    # Establish the SMTP connection
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            
            # Send email to all recipients (To and Cc)
            server.sendmail(sender_email, all_recipients, message.as_string())
            print(f"Email sent successfully to {first_name} and CC recipient!")
    except Exception as e:
        print(f"An error occurred: {e}")
