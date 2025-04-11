import re
import smtplib
import imaplib
import email
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from email.header import decode_header

load_dotenv()

# Variables de entorno
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def decode_mime_header(header):
    """Decodifica un encabezado MIME de forma segura."""
    decoded_parts = decode_header(header)
    return ''.join(
        (part.decode(encoding or 'utf-8', errors='ignore') if isinstance(part, bytes) else part)
        for part, encoding in decoded_parts
    )


def read_email():
    """Lee el último correo no leído y extrae el canal de YouTube si está presente."""
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "(UNSEEN)")
        if status != "OK" or not messages[0]:
            print("No new emails found.")
            return None

        latest_email_id = messages[0].split()[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            print("Error fetching email.")
            return None

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                sender = msg.get("From", "")
                subject = decode_mime_header(msg.get("Subject", ""))
                body = ""

                # Ignorar correos de rebote
                if "mailer-daemon" in sender.lower() or "delivery" in subject.lower():
                    print("Skipping bounce-back email.")
                    return None

                # Extraer el cuerpo del correo
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        try:
                            payload = part.get_payload(decode=True)
                            decoded_payload = payload.decode(part.get_content_charset() or 'utf-8', errors="ignore")
                            if content_type == "text/plain":
                                body += decoded_payload
                                break
                            elif content_type == "text/html" and not body:
                                body += re.sub(r"<[^>]+>", "", decoded_payload)
                        except Exception as e:
                            print(f"Error decoding email body: {e}")

                else:
                    try:
                        payload = msg.get_payload(decode=True)
                        body = payload.decode(msg.get_content_charset() or 'utf-8', errors="ignore")
                    except Exception as e:
                        print(f"Error decoding email body: {e}")

                # Buscar canal de YouTube
                match = re.search(r"(?:youtube\.com\/(?:channel\/|c\/|@))([\w\-@]+)", body)
                mail.logout()  # Cerrar conexión IMAP

                if match:
                    return {"sender": sender, "subject": subject, "channel_name": match.group(1)}

                print("No YouTube channel found in the email.")
                return {"sender": sender, "subject": subject, "channel_name": None}

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading email: {e}")
        return None


def get_youtube_channel_info(channel_name):
    """Obtiene la información del canal de YouTube (subs y videos)."""
    try:
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

        search_response = youtube.search().list(
            q=channel_name,
            type="channel",
            part="id"
        ).execute()

        if not search_response.get("items"):
            print(f"No channel found: {channel_name}")
            return None

        channel_id = search_response["items"][0]["id"]["channelId"]

        channel_response = youtube.channels().list(
            id=channel_id,
            part="statistics"
        ).execute()

        stats = channel_response["items"][0]["statistics"]
        return {
            "subscriber_count": stats.get("subscriberCount", "Unknown"),
            "video_count": stats.get("videoCount", "Unknown")
        }
    
    except Exception as e:
        print(f"Error fetching YouTube channel info: {e}")
        return None


def send_email_reply(recipient, subject, body):
    """Envía un correo de respuesta con la información del canal."""
    try:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("Email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")


def main_flow():
    """Flujo principal: procesa correos y obtiene info de YouTube."""
    email_info = read_email()
    if not email_info:
        print("No email to process.")
        return

    recipient = email_info["sender"]
    channel_name = email_info["channel_name"]

    if not channel_name:
        print("Email found, but no YouTube channel link detected.")
        return

    channel_info = get_youtube_channel_info(channel_name)
    if not channel_info:
        print(f"Could not fetch info for channel: {channel_name}")
        return

    subscribers = channel_info["subscriber_count"]
    videos = channel_info["video_count"]

    reply_subject = f"Información del canal {channel_name}"
    reply_body = f"Este canal tiene {subscribers} suscriptores y {videos} videos."

    send_email_reply(recipient, reply_subject, reply_body)


