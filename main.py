import json

from MySamad import Token, Selfs
from decouple import config

data = None
with open('JSONs/Credentials.json') as f:
  data = json.load(f)

print(config("u_name"))

#print(Reservation.getWeekDayName("2021-12-25"))
#print(Reservation.beautifyReservationOptionsList(Reservation.getThisWeekReservationOptionsList(Token.getAccessToken( data['username'], data['password']) , "1")))
#print(Reservation.beautifyReservationOptionsList(Reservation.getThisWeekReservationOptionsList(Token.getAccessToken( data['username'], data['password']) , "3" , 0)))

#print(Reservation.beautifyReservedFoodsList(Reservation.getThisWeekReserverdFoodsList(Token.getAccessToken(config("u_name"), config("p_word")) , "1")))

print(Selfs.get_self_list(Token.getAccessToken(config("u_name"), config("p_word"))))
