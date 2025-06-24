
#CLASS 1

class City:
    def __init__(self, name, country, population, language, costOfLiving, airport): 
        self.name = name
        self.country = country
        self.population = population
        self.language = language
        self.costOfLiving = costOfLiving
        self.airport = airport
    def Organisation(self, Organisation):    
        return f"{self.name} is a very {Organisation} city."
    def Hospitality(self, Hospitality):
        return f"{self.name} has very {Hospitality} people."

city1 = City("Kampala", "Uganda", "2000000", "English", "$280", "Entebbe Interational Airport") 
print(city1.Organisation("disorganised"))
print(city1.Hospitality("hospitable"))

city2 = City("Stuttgart", "Germany", "635911", "German", "$2716", "Stuttgart Interational Airport") 
print(city2.Organisation("clean"))
print(city2.Hospitality("mean"))

city3 = City("London", "England", "8866180", "English", "$3361", "Heathrow Interational Airport") 
print(city3.Organisation("organised"))
print(city3.Hospitality("mean"))

city4 = City("Johannesberg", "South Africa", "5500000", "English", "$1080", "O.R. Tambo Interational Airport") 
print(city4.Organisation("organised"))
print(city4.Hospitality("happy"))

city5 = City("Nairobi", "Kenya", "5325000", "English and Swahili", "$462", "Jommo Kenyatta Interational Airport") 
print(city5.Organisation("organised"))
print(city5.Hospitality("welcoming"))

#CLASS 2

class Phone:
    def __init__(self, name, type, price, capacity, simcards): 
        self.name = name
        self.type = type
        self.price = price
        self.capacity = capacity
        self.simcards = simcards
    def Battery(self, Battery):    
        return f"{self.name} has a {Battery} battery."
    def Camera(self, Camera):
        return f"{self.name} has very {Camera} quality cameras."

phone1 = Phone("Iphone", "Smart phone", "$650", "128GB", "Single-sim") 
print(phone1.Battery("poor"))
print(phone1.Camera("high"))

phone2 = Phone("Itel", "Feature phone", "$10", "50MB", "Double-sim") 
print(phone2.Battery("good"))
print(phone2.Camera("poor"))
    
phone3 = Phone("Samsung", "Smart phone", "$560", "128GB", "Single-sim") 
print(phone3.Battery("fairly good"))
print(phone3.Camera("good"))

phone4 = Phone("Nokia", "Feature phone", "$20", "50MB", "Double-sim") 
print(phone4.Battery("good"))
print(phone4.Camera("poor"))

phone5 = Phone("Google pixel", "Smart phone", "$475", "128GB", "Single-sim") 
print(phone5.Battery("fairly good"))
print(phone5.Camera("good"))

#CLASS 3

class Dog_breed:
    def __init__(self, name, origin, color, size, lifespan): 
        self.name = name
        self.origin = origin
        self.color = color
        self.size = size
        self.lifespan = lifespan
    def Temperament(self, Temperament):    
        return f"A {self.name} is a {Temperament} dog."
    def Common_use(self, Common_use):
        return f"{self.name} is usually used for {Common_use}."

breed1 = Dog_breed("Chihuahua", "Mexico", ["White", "Fawn", "Black", "Chocolate", "Cream"], "very small", "12-20 years") 
print(breed1.Temperament("very lively, alert and bold"))
print(breed1.Common_use("companionship"))

breed2 = Dog_breed("GermanShepherd", "Germany", ["Black and Tan", "Sable", "Black"], "large", "9-13 years") 
print(breed2.Temperament("very loyal, courageous and intelligent"))
print(breed2.Common_use("security purposes"))

breed3 = Dog_breed("Labrador Retreiver", "Canada", ["Black", "Yellow", "Chocolate"], "medium to large", "10-12 years") 
print(breed3.Temperament("very friendly, outgoing and intelligent"))
print(breed3.Common_use("hunting and companionship"))

breed4 = Dog_breed("Dachshund", "Germany", ["Red","Black and Tan", "Chocolate", "Black", "Dapple"], "small", "12-16 years") 
print(breed4.Temperament("very curious, brave and stubborn"))
print(breed4.Common_use("hunting and companionship"))

breed5 = Dog_breed("Siberian Husky", "Siberia", ["Black and White","Red and White"], "medium", "12-15 years") 
print(breed5.Temperament("very friendly, energetic and free-spirited"))
print(breed5.Common_use("companionship"))

#CLASS 4

class Mercedes_benz:
    def __init__(self, name, engine_size, horsepower, top_speed, size): 
        self.name = name
        self.engine_size = engine_size
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.size = size
    def Functionality(self, Functionality):    
        return f"A {self.name} is a {Functionality} car."
    def Appearance(self, Appearance):
        return f"{self.name} is a {Appearance} car."

C_Class = Mercedes_benz("C-Class 300", "2.0L inline-4 turbocharged", "255hp", "209 km/hr", "compact") 
print(C_Class.Functionality("daily travel and business"))
print(C_Class.Appearance("comfortable"))
   
Gle = Mercedes_benz("GLE350", "2.0L inline-4 turbocharged", "255hp", "209 km/hr", "Mid-size SUV") 
print(Gle.Functionality("family and travel"))
print(Gle.Appearance("roomy luxurious"))

Amg = Mercedes_benz("AMG GT", "4.0L V8 biturbo", "523-720 hp", "310-325 km/hr", "2-door coupe") 
print(Amg.Functionality("sports"))
print(Amg.Appearance("track ready"))

GClass = Mercedes_benz( "G 550", "4.0L V8 biturbo", "416 hp", "209-240 km/hr", "Full-size SUV") 
print(GClass.Functionality("serious off-road"))
print(GClass.Appearance("luxurious"))

SClass = Mercedes_benz( "S 580", "4.0L V8 biturbo with EQ Boost", "496 hp", "209-250 km/hr", "Full-size Sedan") 
print(SClass.Functionality("executive travel"))
print(SClass.Appearance("comfortable"))

#CLASS 5

class Shoe_brand:
    def __init__(self, name, origin, style, price_range, target_market): 
        self.name = name
        self.origin = origin
        self.styler = style
        self.price_range = price_range
        self.target_market = target_market
    def Comfort(self, Comfort):    
        return f"{self.name} is a very {Comfort} shoe."
    def Durability(self, Durability):
        return f"{self.name} is a {Durability} shoe."

brand1 = Shoe_brand( "Nike", "USA", "Athletic", "$60-$250", "Athletes") 
print(brand1.Comfort("comfortable"))
print(brand1.Durability("long lasting"))

brand2 = Shoe_brand( "Clarks", "UK", "official and casual", "$80-$200", "Professionals") 
print(brand2.Comfort("comfortable"))
print(brand2.Durability("long lasting"))

brand3 = Shoe_brand( "Adidas", "Germany", "Athletic", "$60-$300", "Athletes") 
print(brand3.Comfort("comfortable"))
print(brand3.Durability("long lasting"))

brand4 = Shoe_brand( "New Balance", "USA", "Athletic", "$70-$250", "Athletes") 
print(brand4.Comfort("comfortable"))
print(brand4.Durability("long lasting"))

brand5 = Shoe_brand( "Dr. Martens", "UK", "Boots", "$100-$250", "Heavy duty workers") 
print(brand5.Comfort("comfortable"))
print(brand5.Durability("long lasting"))



