# unfortunately, this module cannot be called email as that conflicts with a standard python library

class Email(object):
    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def flush(self):
        from smtplib import SMTP
        import settings, logging

        if not self.messages:
            return

        msg = 'To: ' + settings.to_addr + '\n'
        msg += 'From: ' + settings.from_addr + '\n'
        if len(self.messages) == 1:
            msg += 'Subject: mmonitor: ' + self.messages[0][:200] + '\n'
        else:
            msg += 'Subject: mmonitor: multiple notices\n'
        msg += '\n\n'
        msg += '\n'.join(self.messages)
        msg += '\n\n'

        logging.info('sending mail:\n%s', '\n'.join(self.messages))
        smtp = SMTP(settings.smtp_host, 25)
        smtp.ehlo_or_helo_if_needed()
        smtp.sendmail(settings.from_addr, settings.to_addr, msg)
        smtp.close()
        self.messages = []
