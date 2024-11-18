class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60: #chang from age >= 60 to age > 60 [This line does not trigger any abnormally]
            return 100
        else :
            return None