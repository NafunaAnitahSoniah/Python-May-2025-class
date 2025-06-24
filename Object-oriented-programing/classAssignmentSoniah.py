 #Create atleast 5 classes with atleast 2 methods and 5 objects for each class


#Class 1

class City:
    name = "Kampala"
    country = "Uganda"
    population = 2000000
    language = "English"
    costOfLiving = "$280" 
    airport = "Entebbe International Airport"
    def Organisation():
        return("This is a very disorganised city")
    def Hospitality():
        return("This city has very welcoming people")

city2 = City()
city2.name = "Stuttgart"
city2.country = "Germany"
city2.population = 635911
city2.language = "German"
city2.costOfLiving = "$2716" 
city2.airport = "Stuttgart International Airport" 

city3 = City()
city3.name = "London"
city3.country = "England"
city3.population = 8866180
city3.language = "English"
city3.costOfLiving = "$3361" 
city3.airport = "Heathrow International Airport"

city4 = City()
city4.name = "Johannesberg"
city4.country = "South Africa"
city4.population = 5500000
city4.language = "English"
city4.costOfLiving = "$1080" 
city4.airport = "O.R. Tambo International Airport"

city5 = City()
city5.name = "Nairobi"
city5.country = "Kenya"
city5.population = 5325000
city5.language = "English and Swahili"
city5.costOfLiving = "$462" 
city5.airport = "Jommo Kenyatta International Airport"

#Class 2

class Phone:
    name = "Iphone"
    type = "Smart phone"
    price = "$650"
    capacity = "128GB"
    simcards = "Single-sim" 
    def Battery():
        return("This phone has poor battery")
    def Camera():
        return("This phone has high quality cameras")
    
phone2 = Phone()
phone2.name = "Itel"
phone2.type = "Feature phone"
phone2.price = "$10"
phone2.capacity = "50MB"
phone2.simcards = "Double-sim" 

phone3 = Phone()
phone3.name = "Samsung"
phone3.type = "Smart phone"
phone3.price = "$560"
phone3.capacity = "128GB"
phone3.simcards = "Single-sim" 

phone4 = Phone()
phone4.name = "Nokia"
phone4.type = "Feature phone"
phone4.price = "$20"
phone4.capacity = "50MB"
phone4.simcards = "Double-sim" 

phone5 = Phone()
phone5.name = "Google pixel"
phone5.type = "Smart phone"
phone5.price = "$475"
phone5.capacity = "128GB"
phone5.simcards = "Single-sim" 

# Class 3
 
class Dog_breed:
    name = "Chihuahua"
    origin = "Mexico"
    color = ["White", "Fawn", "Black", "Chocolate", "Cream"]
    size = "very small"
    lifespan = "12-20 years"
    def Temperament():
        return("This dog is lively, alert and bold")
    def Common_use():
        return("This dog is usually used as a companion and can be trained.")

breed2 = Dog_breed()
breed2.name = "GermanShepherd"
breed2.origin = "Germany"
breed2.color = ["Black and Tan", "Sable", "Black"]
breed2.size = "large"
breed2.lifespan = "9-13 years"

breed3 = Dog_breed()
breed3.name = "Labrador Retriever"
breed3.origin = "Canada"
breed3.color = ["Black", "Yellow", "Chocolate"]
breed3.size = "medium to large"
breed3.lifespan = "10-12 years"

breed4 = Dog_breed()
breed4.name = "Dachshund"
breed4.origin = "Germany"
breed4.color = ["Red","Black and Tan", "Chocolate", "Black", "Dapple"]
breed4.size = "small"
breed4.lifespan = "12-16 years"

breed5 = Dog_breed()
breed5.name = "Siberian Husky"
breed5.origin = "Siberia"
breed5.color = ["Black and White","Red and White"]
breed5.size = "medium"
breed5.lifespan = "12-15 years"

#class 4

class Mercedes_benz:
    name = "C-Class 300"
    engine_size = "2.0L inline-4 turbocharged"
    horsepower = "255hp"
    top_speed = "209 km/hr"
    size = "compact"
    def Functionality():
        return("This is a very luxurious car")
    def Appearance():
        return("This is a very beautiful car")

Gle = Mercedes_benz()
Gle.name = "GLE350"
Gle.engine_size = "2.0L inline-4 turbo"
Gle.horsepower = "255-375 hp"
Gle.top_speed = "209 km/hr"
Gle.size = "Mid-size SUV"

Amg = Mercedes_benz()
Amg.name = "AMG GT"
Amg.engine_size = "4.0L V8 biturbo"
Amg.horsepower = "523-720 hp"
Amg.top_speed = "310-325 km/hr"
Amg.size = "2-door coupe"


GClass = Mercedes_benz()
GClass.name = "G 550"
GClass.engine_size = "4.0L V8 biturbo"
GClass.horsepower = "416 hp"
GClass.top_speed = "209-240 km/hr"
GClass.size = "Full-size SUV"

SClass = Mercedes_benz()
SClass.name = "S 580"
GClass.engine_size = "4.0L V8 biturbo with EQ Boost"
SClass.horsepower = "496 hp"
SClass.top_speed = "209-250 km/hr"
SClass.size = "Full-size Sedan"

# Class 5
class Shoe_brand:
    name = "Nike"
    origin = "USA"
    style = "Athletic"
    price_range = "$60-$250"
    target_market = "Athletes"
    def Comfort():
        return("This is a very comfortable shoe")
    def Durability():
        return("They are long lasting")

brand2 = Shoe_brand()
brand2.name = "Clarks"
brand2.origin = "UK"
brand2.style = "official and casual"
brand2.price_range = "$80-$200"
brand2.target_market = "Professionals"


brand3 = Shoe_brand()
brand3.name = "Adidas"
brand3.origin = "Germany"
brand3.style = "Athletic"
brand3.price_range = "$60-$300"
brand3.target_market = "Athletes"


brand4 = Shoe_brand()
brand4.name = "New Balance"
brand4.origin = "USA"
brand4.style = "Athletic"
brand4.price_range = "$70-$250"
brand4.target_market = "Athletes"


brand5 = Shoe_brand()
brand5.name = "Dr. Martens"
brand5.origin = "UK"
brand5.style = "Boots"
brand5.price_range = "$100-$250"
brand5.target_market = "Heavy duty workers"