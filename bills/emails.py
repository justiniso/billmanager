from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def send_new_bill_notification(bill):
	subject = "A friendly payment reminder"
	to = bill.recipient.username
	from_email = 'noreplybillmanager@gmail.com'

	ctx = Context({  
		'bill': bill
	})

	html = get_template('email/new_bill_notification.html')
	html_content = html.render(ctx)

	msg = EmailMultiAlternatives(subject, "HTML content failed", from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
