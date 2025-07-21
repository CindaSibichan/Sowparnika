# utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
# utils.py (below send_contact_email function or separately)
import gspread
from google.oauth2.service_account import Credentials


def send_contact_email(name, phone, email):
    subject = 'New Contact Submission'
    from_email = settings.EMAIL_HOST_USER  # Replace with your verified sending email
    # to_email = ['hello@infideck.com']
    to_email = ['cindasibichan2002@gmail.com']

    # Plain text (fallback)
    text_content = f"""
    New contact submission:

    Name: {name}
    Phone: {phone}
    Email: {email}
    """

    # HTML version of the email
    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2 style="color: #333;">New Contact Submission</h2>
        <table style="width: 100%; max-width: 600px; border-collapse: collapse;">
          <tr>
            <td style="padding: 8px; font-weight: bold;">Name:</td>
            <td style="padding: 8px;">{name}</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: bold;">Phone:</td>
            <td style="padding: 8px;">{phone}</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: bold;">Email:</td>
            <td style="padding: 8px;">{email}</td>
          </tr>
        </table>
        <p style="margin-top: 20px;">Please follow up with the sender if needed.</p>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    save_to_google_sheet(name, phone, email)





def save_to_google_sheet(name, phone, email):
    # Define scopes
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Load credentials from JSON
    credentials = Credentials.from_service_account_file(
        'newapp/credentials/sowparnika-001-607ea631f22a.json', scopes=scope
    )

    # Authorize and open the sheet
    client = gspread.authorize(credentials)
    
    # Use the spreadsheet ID from your link
    spreadsheet_id = '1wik8eeviAO3q5vp2t5BRlwZ8osXRDDN8rc7F8qfHu0A'
    sheet = client.open_by_key(spreadsheet_id).sheet1

    # Append the data
    sheet.append_row([name, phone, email])
