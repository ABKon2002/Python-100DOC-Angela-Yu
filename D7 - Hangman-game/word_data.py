import random
fruggies = [
    "apple", "banana", "grape", "orange", "peach", "pear", "plum", "cherry", "mango", "lemon",
    "lime", "blueberry", "strawberry", "raspberry", "blackberry", "watermelon", "cantaloupe",
    "honeydew", "kiwi", "papaya", "pineapple", "pomegranate", "apricot", "fig", "guava", "lychee",
    "nectarine", "persimmon", "quince", "tangerine", "cucumber", "tomato", "carrot", "potato",
    "onion", "garlic", "ginger", "broccoli", "cauliflower", "spinach", "lettuce", "kale",
    "zucchini", "squash", "eggplant", "pepper", "mushroom", "corn", "peas", "beans", "asparagus",
    "artichoke", "okra", "radish", "turnip", "parsnip", "beet", "celery", "fennel", "leek",
    "scallion", "shallot", "chive", "basil", "mint", "oregano", "rosemary", "thyme", "parsley",
    "cilantro", "dill", "bay", "sage", "marjoram", "tarragon", "chicken", "beef", "pork", "lamb",
    "turkey", "duck", "goose", "rabbit", "venison", "fish", "salmon", "trout", "tuna", "halibut",
    "cod", "haddock", "snapper", "tilapia", "sardine", "anchovy", "mackerel", "crab", "lobster",
    "shrimp", "prawn", "clam", "mussel", "scallop", "oyster", "octopus", "squid", "cuttlefish",
    "coconut", "almond", "walnut", "pecan", "cashew", "pistachio", "hazelnut", "macadamia",
    "peanut", "chestnut", "sunflower", "pumpkin", "sesame", "chia", "flax", "hemp", "poppy",
    "quinoa", "barley", "oat", "wheat", "rye", "cornmeal", "rice", "bulgur", "couscous",
    "farro", "spelt", "buckwheat", "millet", "sorghum", "teff", "amaranth", "kamut", "wildrice",
    "maple", "honey", "molasses", "syrup"
]

food_words = [
    "burger", "fries", "pizza", "taco", "sandwich", "sushi", "steak", "chicken", "bacon", "sausage",
    "nuggets", "salad", "pasta", "lasagna", "omelette", "pancakes", "waffles", "burrito", "nachos", "quesadilla",
    "guacamole", "hummus", "falafel", "shawarma", "gyro", "ravioli", "curry", "dumplings", "springrolls", "samosa",
    "bruschetta", "croissant", "bagel", "donut", "pretzel", "muffin", "brownie", "cupcake", "cookie", "gelato",
    "icecream", "yogurt", "smoothie", "milkshake", "latte", "espresso", "mocha", "frappuccino", "tea", "lemonade",
    "cola", "sprite", "fanta", "pepsi", "mountaindew", "rootbeer", "gingerale", "icedtea", "coffee", "water",
    "popcorn", "chips", "crackers", "granola", "trailmix", "jerky", "olives", "pickles", "cheese", "butter",
    "creamcheese", "ketchup", "mustard", "mayonnaise", "sriracha", "tabasco", "vinegar", "soysauce", "wasabi", "miso",
    "sourdough", "baguette", "ciabatta", "focaccia", "tortilla", "pita", "naan", "biscuit", "scone", "fudge",
    "caramel", "toffee", "marshmallow", "jelly", "jam", "marmalade", "honey"
]

sports_words = [
    "cricket", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "rugby", "volleyball",
    "badminton", "swimming", "cycling", "running", "marathon", "triathlon", "athletics", "wrestling", "boxing", "fencing",
    "judo", "karate", "taekwondo", "archery", "shooting", "skating", "skiing", "snowboarding", "surfing", "kayaking",
    "rowing", "sailing", "canoeing", "diving", "gymnastics", "handball", "lacrosse", "softball", "tabletennis", "squash",
    "racquetball", "polo", "equestrian", "cristiano", "messi", "ronaldo", "lebron", "jordan", "federer", "nadal", "djokovic",
    "bolt", "phelps", "usain", "simone", "biles", "ali", "maradona", "pele", "zidane", "beckham", "ronaldinho", "neymar",
    "sachin", "kohli", "dhoni", "lara", "warne", "ponting", "kallis", "muralitharan", "sanga", "dravid", "rohit",
    "bumrah", "babar", "waseem", "imran", "afridi", "akram", "malinga", "jayawardene", "tendulkar", "dekhock",
    "maxwell", "smith", "warner", "steven", "jasonroy", "morgan", "bairstow", "buttler", "stokes", "root",
    "archer", "hazlewood", "starc", "cummins", "lyon", "finch", "carey", "zampa"
]

iconic_personalities = [
    "einstein", "newton", "darwin", "curie", "tesla", "edison", "galileo", "hawking", "aristotle", "plato",
    "socrates", "daVinci", "michelangelo", "shakespeare", "mozart", "beethoven", "bach", "chopin", "tchaikovsky", "brahms",
    "freud", "jung", "pavlov", "skinner", "erikson", "piaget", "kafka", "orwell", "huxley", "hemingway",
    "fitzgerald", "steinbeck", "twain", "joyce", "dostoevsky", "tolstoy", "gandhi", "mandela", "martinluther", "king",
    "lincoln", "washington", "jefferson", "franklin", "roosevelt", "churchill", "stalin", "lenin", "napoleon", "caesar",
    "alexander", "genghis", "marco", "columbus", "magellan", "armstrong", "gagarin", "tesla", "ford", "jobs",
    "gates", "buffett", "bezos", "musk", "zuckerberg", "bernanke", "greenspan", "powell", "kennedy", "reagan",
    "clinton", "obama", "biden", "merkel", "thatcher", "nelson", "elizabeth", "victoria", "catherine", "theresa",
    "marieantoinette", "joanofarc", "cleopatra", "brontë", "austen", "woolf", "bradbury", "asimov", "clarke", "gibson"
]

def genAny():
    customList = []
    for i in range(10):
        customList.append(random.choice(fruggies))
        customList.append(random.choice(food_words))
        customList.append(random.choice(sports_words))
        customList.append(random.choice(iconic_personalities))
    random.shuffle(customList)
    return customList
