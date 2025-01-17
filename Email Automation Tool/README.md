## Email Automation Tool

### Project Description:
The **Email Automation Tool** is a Python-based application designed to automate the process of sending personalized emails to multiple recipients. The tool allows you to send HTML-formatted emails with dynamic content, ensuring that each recipient gets a unique, personalized experience. It also includes support for **CC** recipients.

This tool is useful for a variety of tasks such as:
- Sending job application emails
- Marketing campaigns
- Event invitations
- Personalized outreach

By leveraging the `smtplib` and `email.mime` libraries in Python, the application connects to an email server (such as Gmail) to send emails securely. The email content can be customized, and the recipient list can be defined dynamically within the script.

### Key Features:
- **Personalized Emails**: The tool extracts the first name from each email address and personalizes the greeting in the email body.
- **HTML Email Format**: Allows for more sophisticated and rich content, including HTML tags, styles, and links.
- **CC Functionality**: Option to send a carbon copy (CC) of the email to another recipient.
- **Dynamic Subject & Content**: Easily customizable subject line and body content.
- **Easy Setup**: Simple configuration to start sending emails quickly.

---

## How to Use This Project

### Prerequisites:
Before running the Email Automation Tool, you need to ensure you have the following:
- **Python 3.x** installed on your local machine.
- Sender Email Setup : An **email account** (e.g., Gmail) with **app-specific password** enabled (for Gmail, this is necessary when 2-step verification is enabled).
- A list of **recipient emails** that you want to send the email to.
  
1. Sender Email Setup (Gmail-specific)
Why is this important?
When sending emails programmatically through Gmail's SMTP server, Google requires extra security to prevent unauthorized access to your account. This is particularly important for apps and scripts that will send emails automatically.

Steps to Set Up Gmail for Sending Emails:
Enable 2-Step Verification:

Google’s 2-Step Verification adds an extra layer of security to your account by requiring you to verify your identity with both your password and a second factor (such as your phone).
To enable 2-step verification:

Go to your Google Account settings.
Under the "Security" section, enable 2-Step Verification.
Follow the prompts to link your phone and set up a backup method.
Create an App-Specific Password:

After enabling 2-step verification, you need to create an App-Specific Password. This password is used to let your script log in to your Gmail account without needing to manually enter your regular password.
To create an App-Specific Password:

Go to the Google App Passwords page.
Select Mail from the drop-down list and choose Other (Custom name) for the app name.
Enter a name (e.g., "Python Email Script") and click Generate.
Google will provide a unique app password. Use this password in the Python script instead of your regular Gmail password:
python
Copy
password = "your-app-specific-password"  # Use the generated app password here
This setup ensures that Gmail's security system won't block your script from sending emails automatically.

### Installation:

1. **Clone the Repository**:
   - First, clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/<your-github-username>/Email-Automation-Tool.git
   ```

2. **Install Required Python Libraries**:
   This tool uses Python's built-in libraries `smtplib` and `email`, so there’s no need to install external dependencies. However, you should ensure Python is properly installed on your machine.

3. **Configure Email Details**:
   - Open the Python script (`email_automation.py`) and configure the email sender, recipients, and content.
   - **Sender Email**: Replace `"your-email@gmail.com"` with your actual email address.
   - **Recipient Emails**: Add the recipient emails in the `receiver_emails` list.
   - **CC Email**: Set the CC email address in `cc_email`.

### Configuration Example:

```python
sender_email = "your-email@gmail.com"  # Replace with your email
receiver_emails = [
    "recipient1@example.com",
    "recipient2@example.com",
    "recipient3@example.com"
    # Add more emails here
]
cc_email = "cc-recipient@example.com"  # Single CC email
subject = "Java Full-Stack Developer | Open to Onsite and Remote Positions"
```

### Modify the Email Body:
The email body is in HTML format and can be customized for your needs. Here’s an example:
```html
<html>
<body>
    <p>Hello {first_name},</p>
    <p>I am [Your Name], a Senior Software Developer with expertise in Java, Spring Boot, and AWS.</p>
    <p>I am currently seeking new opportunities and would love to discuss how my skills can contribute to your clients' success.</p>
    <p>Best regards,<br>[Your Name]</p>
</body>
</html>
```
This body is automatically personalized by the script, so the recipient's name is added dynamically.

---

### Running the Script:

1. **Run the Script**:
   Once the configuration is complete, open your terminal or command prompt, navigate to the directory where the script is located, and run:
   ```bash
   python email_automation.py
   ```

2. **Sending the Email**:
   The script will loop through all recipients, extract their first name, and send a personalized email with the specified subject and body. It will also include the CC recipient in each email.

### Example Output:
After running the script, you'll see the following output for each recipient:
```
Email sent successfully to [First Name] and CC recipient!
```

---

## Notes:
- **Sender Email Setup**: If using Gmail, make sure you’ve enabled **2-step verification** and generated an **app-specific password**. This is necessary to allow the script to send emails via Gmail's SMTP server.
- **Email Rate Limits**: Be cautious when sending bulk emails to avoid being flagged as spam. It's recommended to test the tool with a small batch of emails first.
- **Logging**: You can add logging features to track the progress of each email sent.

---

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Conclusion:
With this **Email Automation Tool**, you can easily send personalized emails to a list of recipients, manage CC functionality, and customize the content. It’s an efficient way to automate outreach for job applications, marketing, and other email communications.
