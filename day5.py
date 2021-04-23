from datetime import datetime, timedelta
import inspect

NOW = datetime.now()


class Promo:
    def __init__(self, name, expire):
        self.n = name
        self.e = expire

    @property
    def expired(self):
        if self.e > NOW:
            return False
        else:
            return True


past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo("twitter", past_time)
future_date = NOW + timedelta(days=1)
newsletter_promo = Promo("newsletter", future_date)

print(bool(twitter_promo.expired))
print(bool(newsletter_promo.expired))
assert "property" in inspect.getsource(Promo)