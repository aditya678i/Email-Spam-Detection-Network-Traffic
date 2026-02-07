SPAM_DOMAINS = ["spam.com", "fake-mail.org"]

def is_spam(sender):
    for domain in SPAM_DOMAINS:
        if domain in sender:
            return True
    return False
