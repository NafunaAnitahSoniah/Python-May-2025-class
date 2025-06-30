
#CLASS 1

class City:
    def __init__(self, name, country, population, language, costOfLiving, airport): 
        self.name = name
        self.country = country
        self.population = population
        self.language = language
        self.costOfLiving = costOfLiving
        self.airport = airport
    def organisation(self, organisation):    
        return f"{self.name} is a very {organisation} city."
    def hospitality(self, hospitality):
        return f"{self.name} has very {hospitality} people."

city1 = City("Kampala", "Uganda", "2000000", "English", "$280", "Entebbe Interational Airport") 
print(city1.organisation("disorganised"))
print(city1.hospitality("hospitable"))

city2 = City("Stuttgart", "Germany", "635911", "German", "$2716", "Stuttgart Interational Airport") 
print(city2.organisation("clean"))
print(city2.hospitality("mean"))

city3 = City("London", "England", "8866180", "English", "$3361", "Heathrow Interational Airport") 
print(city3.organisation("organised"))
print(city3.hospitality("mean"))

city4 = City("Johannesberg", "South Africa", "5500000", "English", "$1080", "O.R. Tambo Interational Airport") 
print(city4.organisation("organised"))
print(city4.hospitality("happy"))

city5 = City("Nairobi", "Kenya", "5325000", "English and Swahili", "$462", "Jommo Kenyatta Interational Airport") 
print(city5.organisation("organised"))
print(city5.hospitality("welcoming"))

#CLASS 2

class Phone:
    def __init__(self, name, type, price, capacity, simcards): 
        self.name = name
        self.type = type
        self.price = price
        self.capacity = capacity
        self.simcards = simcards
    def battery(self, battery):    
        return f"{self.name} has a {battery} battery."
    def camera(self, camera):
        return f"{self.name} has very {camera} quality cameras."

phone1 = Phone("Iphone", "Smart phone", "$650", "128GB", "Single-sim") 
print(phone1.battery("poor"))
print(phone1.camera("high"))

phone2 = Phone("Itel", "Feature phone", "$10", "50MB", "Double-sim") 
print(phone2.battery("good"))
print(phone2.camera("poor"))
    
phone3 = Phone("Samsung", "Smart phone", "$560", "128GB", "Single-sim") 
print(phone3.battery("fairly good"))
print(phone3.camera("good"))

phone4 = Phone("Nokia", "Feature phone", "$20", "50MB", "Double-sim") 
print(phone4.battery("good"))
print(phone4.camera("poor"))

phone5 = Phone("Google pixel", "Smart phone", "$475", "128GB", "Single-sim") 
print(phone5.battery("fairly good"))
print(phone5.camera("good"))

#CLASS 3

class Dog_breed:
    def __init__(self, name, origin, color, size, lifespan): 
        self.name = name
        self.origin = origin
        self.color = color
        self.size = size
        self.lifespan = lifespan
    def temperament(self, temperament):    
        return f"A {self.name} is a {temperament} dog."
    def common_use(self, common_use):
        return f"{self.name} is usually used for {common_use}."

breed1 = Dog_breed("Chihuahua", "Mexico", ["White", "Fawn", "Black", "Chocolate", "Cream"], "very small", "12-20 years") 
print(breed1.temperament("very lively, alert and bold"))
print(breed1.common_use("companionship"))

breed2 = Dog_breed("GermanShepherd", "Germany", ["Black and Tan", "Sable", "Black"], "large", "9-13 years") 
print(breed2.temperament("very loyal, courageous and intelligent"))
print(breed2.common_use("security purposes"))

breed3 = Dog_breed("Labrador Retreiver", "Canada", ["Black", "Yellow", "Chocolate"], "medium to large", "10-12 years") 
print(breed3.temperament("very friendly, outgoing and intelligent"))
print(breed3.common_use("hunting and companionship"))

breed4 = Dog_breed("Dachshund", "Germany", ["Red","Black and Tan", "Chocolate", "Black", "Dapple"], "small", "12-16 years") 
print(breed4.temperament("very curious, brave and stubborn"))
print(breed4.common_use("hunting and companionship"))

breed5 = Dog_breed("Siberian Husky", "Siberia", ["Black and White","Red and White"], "medium", "12-15 years") 
print(breed5.temperament("very friendly, energetic and free-spirited"))
print(breed5.common_use("companionship"))

#CLASS 4

class Mercedes_benz:
    def __init__(self, name, engine_size, horsepower, top_speed, size): 
        self.name = name
        self.engine_size = engine_size
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.size = size
    def functionality(self, functionality):    
        return f"A {self.name} is a {functionality} car."
    def appearance(self, appearance):
        return f"{self.name} is a {appearance} car."

C_Class = Mercedes_benz("C-Class 300", "2.0L inline-4 turbocharged", "255hp", "209 km/hr", "compact") 
print(C_Class.functionality("daily travel and business"))
print(C_Class.appearance("comfortable"))
   
Gle = Mercedes_benz("GLE350", "2.0L inline-4 turbocharged", "255hp", "209 km/hr", "Mid-size SUV") 
print(Gle.functionality("family and travel"))
print(Gle.appearance("roomy luxurious"))

Amg = Mercedes_benz("AMG GT", "4.0L V8 biturbo", "523-720 hp", "310-325 km/hr", "2-door coupe") 
print(Amg.functionality("sports"))
print(Amg.appearance("track ready"))

GClass = Mercedes_benz( "G 550", "4.0L V8 biturbo", "416 hp", "209-240 km/hr", "Full-size SUV") 
print(GClass.functionality("serious off-road"))
print(GClass.appearance("luxurious"))

SClass = Mercedes_benz( "S 580", "4.0L V8 biturbo with EQ Boost", "496 hp", "209-250 km/hr", "Full-size Sedan") 
print(SClass.functionality("executive travel"))
print(SClass.appearance("comfortable"))

#CLASS 5

class Shoe_brand:
    def __init__(self, name, origin, style, price_range, target_market): 
        self.name = name
        self.origin = origin
        self.styler = style
        self.price_range = price_range
        self.target_market = target_market
    def comfort(self, comfort):    
        return f"{self.name} is a very {comfort} shoe."
    def durability(self, durability):
        return f"{self.name} is a {durability} shoe."

brand1 = Shoe_brand( "Nike", "USA", "Athletic", "$60-$250", "Athletes") 
print(brand1.comfort("comfortable"))
print(brand1.durability("long lasting"))

brand2 = Shoe_brand( "Clarks", "UK", "official and casual", "$80-$200", "Professionals") 
print(brand2.comfort("comfortable"))
print(brand2.durability("long lasting"))

brand3 = Shoe_brand( "Adidas", "Germany", "Athletic", "$60-$300", "Athletes") 
print(brand3.comfort("comfortable"))
print(brand3.durability("long lasting"))

brand4 = Shoe_brand( "New Balance", "USA", "Athletic", "$70-$250", "Athletes") 
print(brand4.comfort("comfortable"))
print(brand4.durability("long lasting"))

brand5 = Shoe_brand( "Dr. Martens", "UK", "Boots", "$100-$250", "Heavy duty workers") 
print(brand5.comfort("comfortable"))
print(brand5.durability("long lasting"))



