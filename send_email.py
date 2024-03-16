"""Send Email Functions"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from params import Params

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)

def send_email(receiver_email: str, subject: str, html: str):
    """Send Email"""
    logger = logging.getLogger("send_email")
    logger.debug("Start Send Email")
    logger.debug("Cust: %s, Sub: %s, Html: %s", receiver_email, subject, html)
    port = Params.SendPulse.port
    smtp_server = Params.SendPulse.server
    login = Params.SendPulse.username  # paste your login generated by Mailtrap
    password = Params.SendPulse.password  # paste your password generated by Mailtrap

    sender_email = Params.SendPulse.sender
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part2 = MIMEText(html, "html")
    message.attach(part2)

    # send your email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    send_email("jakumpe@kumpes.com", "Test Email", "This is a <b>TEST</b>.")
