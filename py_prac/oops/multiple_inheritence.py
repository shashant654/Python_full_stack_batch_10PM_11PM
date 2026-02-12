

# Multiple inheritence 

=> in this case , one child class can inherit more than one parent class.

class Grandfather:
                    grandfather_assets = "Grand Vitara"

class Father:
                    def father_assets(self):
                                        print("this is father assets")

class Diwakar(Grandfather,Father):
                    shop = "Fashion king"


diwakar_obj = Diwakar()
print(diwakar_obj.grandfather_assets)
diwakar_obj.father_assets()

# -------------------------------------------------------


# class Grandfather:
#                     grandfather_assets = "Grand Vitara"

# grand_obj = Grandfather()

# print(grand_obj.grandfather_assets)