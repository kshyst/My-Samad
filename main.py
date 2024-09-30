import Reservation
import Token
import json

data = None
with open('JSONs/Credentials.json') as f:
  data = json.load(f)

print(Reservation.beautifyReservationOptionsList(Reservation.getThisWeekReservationOptionsList(Token.getAccessToken( data['username'], data['password']) , "1")))
