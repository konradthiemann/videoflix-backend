# Why a Custom Backend?
# The default email backend doesn't allow me to specify the SSL context with the custom certificate authority file provided by certifi.
# By creating a custom backend, I can specify the SSL context and ensure the correct certificates are used during the SSL handshake.

import smtplib
from django.core.mail.backends.smtp import EmailBackend
import ssl
import certifi

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        connection_class = smtplib.SMTP_SSL if self.use_ssl else smtplib.SMTP

        try:
            self.connection = connection_class(
                self.host,
                self.port,
                timeout=self.timeout,
                context=ssl.create_default_context(cafile=certifi.where())
            )

            if not self.use_ssl and self.use_tls:
                self.connection.starttls(context=ssl.create_default_context(cafile=certifi.where()))
            
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if self.fail_silently:
                return False
            raise
