# ciao
# may the coding begin

# ideas:
# what do i want this program to do?:
# open spotify and start playing lo-fi/aadi good lo-fi
# open cmc and collect diamonds
# open crypto bubbles to the weekly performance one
# open Google Calendar and see today's schedule


# general imports:
import time

# file imports:
from CMC_Diamonds import collect_diamonds
from Crypto_Opener import open_crypto

collect_diamonds()
time.sleep(5)
print("done the first thing")

open_crypto()
print("done the second thing")
