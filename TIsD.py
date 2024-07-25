import pygame as pg
import sys
import random

# Инициализация PyGame
pg.init()

# Размеры экрана
screen_width = 1024
screen_height = 720

# Создание экрана
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Производственный симулятор")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Установка FPS
clock = pg.time.Clock()
FPS = 30

last_update = pg.time.get_ticks()
current_image = 0

DAY_EVENT = pg.USEREVENT + 1
pg.time.set_timer(DAY_EVENT, 3000)

INCREASE_MONEY = pg.USEREVENT + 2
pg.time.set_timer(INCREASE_MONEY, 1000)

font = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 20)
font_mini = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 10)

names = ["Walton", "Bennett", "Paul", "Andrea", "Stewart", "Stefan", "Lee", "Sally", "Wade", "Ava", "Abby", "Dwight",
         "Goodwin", "Don", "Valerie", "Zach", "Leonard", "Gregory", "Lane", "Jaylee", "Alvin", "Alina", "Margaret",
         "Harding", "Viola", "Sybil", "Trista", "Ford", "Lonnie", "Catherine", "Lorelei", "Tracy", "Ramona",
         "Guinevere",
         "Elena", "Angelica", "Leland", "Dwayne", "Percival", "Ulva", "Georgette", "Vincent", "Lane", "Madeline",
         "Marlene", "Elliot", "Rachel", "Philip", "Melody", "Ebenezer", "Armando", "Marisol", "Pastor", "Mercedes"]

surnames = ["Barnett", "Hammond", "Tings", "Richards", "Malone", "Wheeler", "Hunt", "Dixon", "Sherman", "Bush",
            "Hancock",
            "Andrus", "Harry", "Anderson", "Greenwood", "Marshall", "Lynch", "Clem", "McDaniel", "Neal", "Coleman",
            "Parks",
            "Bird", "Ruiz", "Brown", "Rice", "Munoz", "Ramos", "Mitchell", "Hundred", "Berry", "Wheeler", "George",
            "Bishop", "Stokes", "Burrows", "Hicks", "Rhodes", "Tate", "Hargraves", "Simmons", "Cantrell", "Eland",
            "Jensen", "Stevens", "Woolridge", "Garraway", "Cook", "Nicholas", "Smart", "Schmidt", "Anchondo", "Fabela"]

# shop_items = {
#     "Carbon fiber cladding":
#         {
#             "price": 500,
#             "description": "Its carbon fiber cladding",
#             "quality": 50,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Glass":
#         {
#             "price": 50,
#             "description": "Its glass",
#             "quality": 502,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Bumper":
#         {
#             "price": 100,
#             "description": "Its bumper",
#             "quality": 504,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Doors":
#         {
#             "price": 100,
#             "description": "Its doors",
#             "quality": 505,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Headlights":
#         {
#             "price": 100,
#             "description": "Its headlights",
#             "quality": 50,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Rear view mirrors":
#         {
#             "price": 100,
#             "description": "Its rear view mirrors",
#             "quality": 50,
#             "category": "appearance",
#             "image": "123"
#         },
#     "Gearbox":
#         {
#             "price": 100,
#             "description": "Its gearbox",
#             "quality": 50,
#             "category": "transmission",
#             "image": "123"
#         },
#     "Engine":
#         {
#             "price": 100,
#             "description": "Its trunk",
#             "quality": 50,
#             "category": "transmission",
#             "image": "123"
#         },
#     "gimbal drive":
#         {
#             "price": 100,
#             "description": "Its gimbal drive",
#             "quality": 50,
#             "category": "transmission",
#             "image": "123"
#         },
#     "Main transfer":
#         {
#             "price": 100,
#             "description": "Its Main transfer",
#             "quality": 50,
#             "category": "transmission",
#             "image": "123"
#         },
#     "Wheels":
#         {
#             "price": 100,
#             "description": "Its wheels",
#             "quality": 50,
#             "category": "transmission",
#             "image": "123"
#         },
#     "Helm":
#         {
#             "price": 100,
#             "description": "Its helm",
#             "quality": 50,
#             "category": "management mechanisms",
#             "image": "123"
#         },
#     "Shock absorbers":
#         {
#             "price": 100,
#             "description": "Its shock absorbers",
#             "quality": 50,
#             "category": "management mechanisms",
#             "image": "123"
#         },
#     "Elastic spring":
#         {
#             "price": 100,
#             "description": "Its elastic spring",
#             "quality": 50,
#             "category": "management mechanisms",
#             "image": "123"
#         },
#     "Radio":
#         {
#             "price": 100,
#             "description": "Its radio",
#             "quality": 50,
#             "category": "salon",
#             "image": "123"
#         },
#     "Seat":
#         {
#             "price": 100,
#             "description": "Its seat",
#             "quality": 50,
#             "category": "salon",
#             "image": "123"
#         }
# }


shop_items = {
    "appearance":
        {
            "Carbon fiber cladding":
                {
                    "price": 500,
                    "description": "Its carbon fiber cladding",
                    "quality": 50,
                    "category": "appearance",
                    "image": "123"
                },
            "Glass":
                {
                    "price": 50,
                    "description": "Its glass",
                    "quality": 502,
                    "category": "appearance",
                    "image": "123"
                },
            "Bumper":
                {
                    "price": 100,
                    "description": "Its bumper",
                    "quality": 504,
                    "category": "appearance",
                    "image": "123"
                },
            "Doors":
                {
                    "price": 100,
                    "description": "Its doors",
                    "quality": 505,
                    "category": "appearance",
                    "image": "123"
                },
            "Headlights":
                {
                    "price": 100,
                    "description": "Its headlights",
                    "quality": 50,
                    "category": "appearance",
                    "image": "123"
                },
            "Rear view mirrors":
                {
                    "price": 100,
                    "description": "Its rear view mirrors",
                    "quality": 50,
                    "category": "appearance",
                    "image": "123"
                },
        },
    "transmission":
        {
            "Gearbox":
                {
                    "price": 100,
                    "description": "Its gearbox",
                    "quality": 50,
                    "category": "transmission",
                    "image": "123"
                },
            "Engine":
                {
                    "price": 100,
                    "description": "Its trunk",
                    "quality": 50,
                    "category": "transmission",
                    "image": "123"
                },
            "gimbal drive":
                {
                    "price": 100,
                    "description": "Its gimbal drive",
                    "quality": 50,
                    "category": "transmission",
                    "image": "123"
                },
            "Main transfer":
                {
                    "price": 100,
                    "description": "Its Main transfer",
                    "quality": 50,
                    "category": "transmission",
                    "image": "123"
                },
            "Wheels":
                {
                    "price": 100,
                    "description": "Its wheels",
                    "quality": 50,
                    "category": "transmission",
                    "image": "123"
                },
        },
    "management mechanisms":
        {
            "Helm":
                {
                    "price": 100,
                    "description": "Its helm",
                    "quality": 50,
                    "category": "management mechanisms",
                    "image": "123"
                },
            "Shock absorbers":
                {
                    "price": 100,
                    "description": "Its shock absorbers",
                    "quality": 50,
                    "category": "management mechanisms",
                    "image": "123"
                },
            "Elastic spring":
                {
                    "price": 100,
                    "description": "Its elastic spring",
                    "quality": 50,
                    "category": "management mechanisms",
                    "image": "123"

                },
        },
    "salon":
        {
            "Radio":
                {
                    "price": 100,
                    "description": "Its radio",
                    "quality": 50,
                    "category": "salon",
                    "image": "123"
                },
            "Seat":
                {
                    "price": 100,
                    "description": "Its seat",
                    "quality": 50,
                    "category": "salon",
                    "image": "123"
                }
        }
}


def wrap_text(text, font, max_width):
    """
    Обертка текста с переносом строк для вмещения в заданную ширину.
    """
    words = text.split(' ')
    wrapped_lines = []
    current_line = ""
    for word in words:
        # Проверяем, не превысит ли добавление слова максимальную ширину
        test_line = current_line + word + " "
        # Получаем размер предполагаемой строки
        line_width, line_height = font.size(test_line)
        if line_width <= max_width:
            # Если предполагаемая строка подходит, добавляем слово к текущей строке
            current_line += word + " "
        else:
            # Если строка слишком длинная, добавляем текущую строку в список и начинаем новую
            wrapped_lines.append(current_line)
            current_line = word + " "
    # Добавляем последнюю строку
    wrapped_lines.append(current_line)
    return wrapped_lines


def handle_produce_button_click(game):
    game.conveyor.produce_vehicle(LightVehicle())
    print("Производство машины запущено")


def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))

    return image


def text_render(text):
    return font.render(str(text), True, 'Black')


def generate_description(vehicle_type):
    # Словарь характеристик для разных типов транспорта
    features = {
        "Light Vehicle": ["compact size", "fuel efficiency", "modern design", "urban style"],
        "Medium Vehicle": ["increased power", "advanced safety", "luxurious interior", "spacious cabin"],
        "Hard Vehicle": ["reinforced chassis", "powerful engine", "4x4 capability", "heavy-duty performance"]
    }

    # Словарь свойств, общих для всех типов транспорта
    properties = ["with cutting-edge technology", "featuring autonomous driving",
                  "equipped with state-of-the-art entertainment system", "with eco-friendly materials"]

    # Выбираем случайное свойство для типа транспорта
    selected_feature = random.choice(features[vehicle_type])
    # Выбираем случайное общее свойство
    selected_property = random.choice(properties)

    # Формируем полное описание
    full_description = f"I would like {vehicle_type} model {selected_feature} {selected_property}."
    return full_description


def generate_random_orders(n):
    orders = []
    for _ in range(n):
        name = random.choice(names)
        surname = random.choice(surnames)
        vehicle_type = random.choice(["Light Vehicle", "Medium Vehicle", "Hard Vehicle"])
        quality = random.choice(["Standard", "High", "Premium"])
        price = random.randint(100, 1000)
        deadline = random.randint(5, 10)
        description = generate_description(vehicle_type)
        popularity = random.randint(1, 10)
        orders.append(Order(vehicle_type, quality, price, deadline, name, surname, description, popularity))
    return orders


def generate_shop_window(shop_items):
    items_all = []
    for item in shop_items:
        category = item
        for item1 in shop_items[item]:
            name = item1
            quality = shop_items[item][name]['quality']
            price = shop_items[item][name]['price']
            description = shop_items[item][name]['description']

            items_all.append(Shop(price=price, quality=quality, category=category, name=name, description=description))
    print(items_all)

    return items_all


background_image = load_image("Game_ind/GUI/Base_GUI/Backraund/Backraund.png", screen_width, screen_height)

conveyor_images_path = [
    "Game_ind/Base/conveir_all/conveir_up/1c/conveir_up_64x64.png",
    "Game_ind/Base/conveir_all/conveir_up/2c/conveir_up_64x64_2.png",
    "Game_ind/Base/conveir_all/conveir_up/3c/conveir_up_64x64_3.png",
    "Game_ind/Base/conveir_all/conveir_up/4c/conveir_up_64x64_4.png",
    "Game_ind/Base/conveir_all/conveir_up/5c/conveir_up_64x64_5.png",
    "Game_ind/Base/conveir_all/conveir_up/6c/conveir_up_64x64_6.png",
    "Game_ind/Base/conveir_all/conveir_up/7c/conveir_up_64x64_7.png",
    "Game_ind/Base/conveir_all/conveir_up/8c/conveir_up_64x64_8.png",
    "Game_ind/Base/conveir_all/conveir_up/9c/conveir_up_64x64_9.png",
    "Game_ind/Base/conveir_all/conveir_up/10c/conveir_up_64x64_10.png",
    "Game_ind/Base/conveir_all/conveir_up/11c/conveir_up_64x64_11.png",
    "Game_ind/Base/conveir_all/conveir_up/12c/conveir_up_64x64_12.png",
    "Game_ind/Base/conveir_all/conveir_up/13c/conveir_up_64x64_13.png",
    "Game_ind/Base/conveir_all/conveir_up/14c/conveir_up_64x64_14.png",
    "Game_ind/Base/conveir_all/conveir_up/15c/conveir_up_64x64_15.png",
    "Game_ind/Base/conveir_all/conveir_up/16c/conveir_up_64x64_16.png",
    "Game_ind/Base/conveir_all/conveir_up/17c/conveir_up_64x64_17.png",
    "Game_ind/Base/conveir_all/conveir_up/18c/conveir_up_64x64_18.png",
    "Game_ind/Base/conveir_all/conveir_up/19c/conveir_up_64x64_19.png",
    "Game_ind/Base/conveir_all/conveir_up/20c/conveir_up_64x64_20.png"

]

conveyor_images = [load_image(file, width=400, height=700) for file in conveyor_images_path]


class Button:
    def __init__(self, text, x, y, visible_width, visible_height, total_width, total_height, text_font=font, func=None):
        self.func = func
        self.x = x
        self.y = y
        self.image = load_image('Game_ind/GUI/Base_GUI/Button_GUI/Button.png', total_width, total_height)
        # self.rect = self.image.get_bounding_rect()
        self.visible_rect = pg.Rect(x, y + 24, visible_width, visible_height)

        self.rect = self.visible_rect

        self.text = text_render(text)
        self.text_rect = self.text.get_rect()
        self.text_font = text_font
        self.text_rect.center = self.rect.center

        self.is_pressed = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.text, self.text_rect)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                if self.func:
                    self.func()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False


class Conveyor:
    def __init__(self):
        self.production_cost = 5
        self.production_speed = 30
        self.production_stability = 30

    def upgrade_speed(self, amount):
        self.production_speed = self.production_speed + amount - (self.production_stability // 5)
        if self.production_speed > 100:
            self.production_speed = 100

    def upgrade_stability(self, amount):
        self.production_speed = self.production_stability + amount - (self.production_speed // 5)
        if self.production_stability > 100:
            self.production_stability = 100


class Order:
    def __init__(self, vehicle_type, quality, price, deadline, name, surname, description, popularity):
        self.vehicle_type = vehicle_type
        self.quality = quality
        self.price = price
        self.deadline = deadline
        self.name = name
        self.surname = surname
        self.description = description
        self.popularity = popularity
        self.is_completed = False
        self.rect = pg.Rect(0, 0, 346, 64)

    def complete_order(self):
        # Логика для начисления денег и популярности
        self.is_completed = True

    def draw(self, screen):
        # pg.draw.rect(screen, "black", self.rect)
        pass


class Shop:
    def __init__(self, price, quality, category, name, description):
        self.price = price
        self.quality = quality
        self.name = name
        self.description = description
        self.category = category
        self.rect = pg.Rect(0, 0, 278, 71)

    def buy(self):
        pass


class Vehicle:
    def __init__(self, speed, power, mass):
        self.speed = speed
        self.power = power
        self.mass = mass
        self.quality = 20


class LightVehicle(Vehicle):
    def __init__(self):
        super().__init__(speed=60, power=50, mass=40)


class MediumVehicle(Vehicle):
    def __init__(self):
        super().__init__(speed=60, power=200, mass=60)


class HardVehicle(Vehicle):
    def __init__(self):
        super().__init__(speed=50, power=200, mass=70)


class Game:
    def __init__(self):
        self.money = 1000
        self.popularity = 100
        self.money_sec = 1
        self.chance_of_orders = 10
        self.orders = []
        self.items_all = generate_shop_window(shop_items)
        self.conveyor = Conveyor()
        self.day = 0
        self.selected_order = None

        self.order_start_x = 473  # X-координата, с которой начинается первый заказ
        self.order_start_y = 30  # Y-координата, с которой начинается первый заказ

        self.items_start_x = 480
        self.items_start_y = 41

        self.INCREASE_COINS = pg.USEREVENT + 2
        pg.time.set_timer(self.INCREASE_COINS, 1000)
        self.DECREASE = pg.USEREVENT + 3
        pg.time.set_timer(self.DECREASE, 1000)

        self.conveyor_image = load_image(
            "Game_ind/Base/conveir_all/conveir_up/1c/conveir_up_64x64.png", 400, 700)
        self.money_image = load_image("Game_ind/GUI/Base_GUI/money/money_64x64.png", 64, 64)
        self.popularity_image = load_image("Game_ind/GUI/Base_GUI/Popularity/100%/popularity100_64x64.png", 64, 64)
        self.windowGUI = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 390, 440)
        self.ButtonGuiOrder = Button("Orders", 650, 10, 124, 58, 120, 120, func=self.toggle_orders_window)
        self.ButtonGuiShop = Button("Shop", 790, 10, 122, 58, 120, 120, func=self.toggle_shop_window)
        self.OrderGui = load_image("Game_ind/GUI/Order_GUI/order_mini/order_mini.png", 346, 256)
        self.showcase_of_products = load_image("Game_ind/GUI/Shop_GUI/showcase_of_products.png", 280, 220)

        pg.time.set_timer(self.money + 1, 500)

        self.money_text = text_render(f"{self.money}")
        self.money_text_rect = self.money_text.get_rect()
        self.money_text_rect.center = (800, 129)

        self.popularity_text = text_render(f"{self.popularity}%")
        self.popularity_text_rect = self.popularity_text.get_rect()

        self.show_orders_window = False  # Флаг для отображения окна заказов
        self.show_shop_window = False
        self.orders_button_rect = pg.Rect(self.ButtonGuiOrder.rect)  # Позиция и размеры кнопки "Заказы"

        self.orders = generate_random_orders(5)

        self.info_window_width = 527  # Примерная ширина окна информации
        self.info_window_height = 528  # Примерная высота окна информации

    def toggle_orders_window(self):
        if self.show_shop_window == False:
            self.show_orders_window = not self.show_orders_window
            print("4")
        elif self.show_shop_window == True:
            self.show_orders_window = not self.show_orders_window
            self.show_shop_window = not self.show_shop_window

    def draw_orders_window(self):
        padding = 77  # Отступ между заказами

        # Отрисовка окна заказов
        screen.blit(self.windowGUI, (450, 97))  # Позиция окна заказов

        for index, order in enumerate(self.orders):
            order_y_position = self.order_start_y + (index * padding)
            order.rect.topleft = (self.order_start_x, order_y_position)
            # Отрисовка каждого заказа здесь
            screen.blit(self.OrderGui, order.rect.topleft)

        for index, order in enumerate(self.orders):
            order_y_position = self.order_start_y + (index * padding)
            order.rect.topleft = (self.order_start_x, order_y_position + 95)
            # order.draw(screen)

        y_start = 130  # Начальная позиция для текста заказов

        for order in self.orders:
            # order_text = f"{order.vehicle_type}: ${order.price}, Deadline: Day {order.deadline}"
            order_name = f"{order.name}"
            order_surname = f"{order.surname}"
            order_text = f"I would like {order.vehicle_type} model with..."
            order_price = f"${order.price}"
            screen.blit(font_mini.render(order_name, True, WHITE), (486, y_start))
            screen.blit(font_mini.render(order_surname, True, WHITE), (610, y_start))
            screen.blit(font_mini.render(order_price, True, WHITE), (485, y_start + 45))
            screen.blit(font_mini.render(order_text, True, WHITE), (488, y_start + 28))

            y_start += 77

    def toggle_shop_window(self):
        if self.show_orders_window == False:
            self.show_shop_window = not self.show_shop_window
            print("5")
        elif self.show_orders_window == True:
            print("6")
            self.show_shop_window = not self.show_shop_window
            self.show_orders_window = not self.show_orders_window

    def draw_shop_window(self, mode):
        shop_index = 0
        padding = 80
        screen.blit(self.windowGUI, (450, 97))
        # for index, item in enumerate(self.items_all):
        #     if item.category == mode:
        #         #item_y_position = self.items_start_y + (index * padding)
        #         #item.rect.topleft = (self.items_start_x, item_y_position)
        #         item_y_position = self.items_start_y + (index * padding)
        #         item.rect.topleft = (self.items_start_x, item_y_position)
        #         # Отрисовка каждого заказа здесь
        #         screen.blit(self.showcase_of_products, item.rect.topleft)

        for item in range(len(self.items_all)):
            if self.items_all[item].category == mode:
                item_y_position = self.items_start_y + (shop_index * padding)
                self.items_all[item].rect.topleft = (self.items_start_x, item_y_position)
                # Отрисовка каждого шаблона для товара(картинка)
                screen.blit(self.showcase_of_products, self.items_all[item].rect.topleft)
                shop_index += 1

        shop_index = 0
        for item in range(len(self.items_all)):
            if self.items_all[item].category == mode:
                items_y_position = self.items_start_y + (shop_index * padding)
                self.items_all[item].rect.topleft = (self.items_start_x, items_y_position + 90)
                #pg.draw.rect(screen, "Black", self.items_all[item].rect)
                shop_index += 1

        y_start = 140


        for item in self.items_all:
            if item.category == mode:
                shop_name = f"{item.name}"
                shop_price = f"{item.price}"
                shop_quality = f"Quality: {item.quality}"
                screen.blit(font_mini.render(shop_name, True, BLACK), (575, y_start))
                screen.blit(font_mini.render(shop_price, True, BLACK), (720, y_start + 40))
                screen.blit(font_mini.render(shop_quality, True, BLACK), (576, y_start + 40))

                y_start += 80

    def update(self):
        pass

    def process_orders(self):
        for order in self.orders:
            if not order.completed and order.deadline == self.day:
                order.completed = True
                self.money += order.price
                self.popularity += 2
        self.orders = [order for order in self.orders if not order.completed]

    def lose_popularity(self, amount):
        self.popularity -= amount
        if self.popularity < 0:
            self.popularity = 0

    def add_orders(self, order):
        self.orders.append(order)

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False

    def draw_description(self, description, font, screen, x, y, max_width):
        wrapped_description = wrap_text(description, font, max_width)
        line_height = font.get_linesize()
        for line in wrapped_description:
            line_surface = font.render(line, True, WHITE)
            screen.blit(line_surface, (x, y))
            y += line_height + 10  # Смещаем Y на высоту строки для отрисовки следующей строки

    def draw(self):
        screen.blit(self.money_image, (screen_width / 15, 40))
        screen.blit(text_render(self.money), (screen_width / 15 + 60, 65))
        screen.blit(self.popularity_image, (screen_width / 15, 120))
        screen.blit(text_render(str(self.popularity) + "%"), (screen_width / 15 + 60, 145))
        self.ButtonGuiOrder.draw(screen)
        self.ButtonGuiShop.draw(screen)

        if self.show_orders_window:
            self.draw_orders_window()

        if self.show_shop_window:
            self.draw_shop_window(mode="appearance")

        if self.selected_order:
            # Путь к изображению окна информации о заказе
            info_window_image_path = "Game_ind/GUI/Order_GUI/window_order_open/window_order_open.png"
            # Загрузка и отрисовка окна информации о заказе
            info_window_image = load_image(info_window_image_path, self.info_window_width, self.info_window_height)
            info_window_x = 50  # Начальная X-координата для окна информации
            info_window_y = 0  # Начальная Y-координата для окна информации
            screen.blit(info_window_image, (info_window_x, info_window_y))

            # Отрисовка текста описания заказа
            description_text = font_mini.render(self.selected_order.description, True, WHITE)

            info_text_x = info_window_x + 30  # Небольшой отступ от края окна информации
            info_text_y = info_window_y + 200  # Небольшой отступ от края окна информации
            # screen.blit(description_text, (info_text_x, info_text_y))
            self.draw_description(self.selected_order.description, font_mini, screen, info_text_x, info_text_y,
                                  self.info_window_width - 60)  # Уменьшить ширину для отступов
            screen.blit(font_mini.render(self.selected_order.name, True, WHITE), (100, 140))
            screen.blit(font_mini.render(self.selected_order.surname, True, WHITE), (350, 140))


# Игровой цикл
game = Game()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Обработка событий (например, нажатие кнопок)
        if event.type == pg.MOUSEBUTTONDOWN:
            if game.selected_order and not game.selected_order.rect.collidepoint(event.pos):
                # Если клик был вне окна информации, сбрасываем выбранный заказ
                game.selected_order = None

            if game.show_orders_window:
                for order in game.orders:
                    if order.rect.collidepoint(event.pos):
                        # Если кликнули по заказу, который уже выбран, закрываем окно информации
                        if game.selected_order == order:
                            game.selected_order = None
                        else:
                            # Иначе открываем окно информации для нового заказа
                            game.selected_order = order
                        break  # Выходим из цикла, так как заказ найден

            if game.show_shop_window:
                for item in game.items_all:
                    if item.rect.collidepoint(event.pos):
                        if game.money >= item.price:
                            game.money -= item.price

        if event.type == DAY_EVENT:
            game.day += 1
            print(f'День номер {game.day}')

        if event.type == INCREASE_MONEY:
            game.money += 1

        if event.type == pg.MOUSEBUTTONDOWN and game.orders_button_rect.collidepoint(event.pos):
            game.ButtonGuiOrder.is_clicked(event)
        game.ButtonGuiShop.is_clicked(event)

        if event.type == pg.MOUSEBUTTONDOWN and game.show_orders_window:
            for order in game.orders:
                if order.rect.collidepoint(event.pos):
                    game.selected_order = order  # Запоминаем выбранный заказ
                    break  # Выходим из цикла, так как заказ найден

    # Переход к следующему изображению
    now = pg.time.get_ticks()
    if now - last_update > FPS:
        last_update = 0
        current_image = (current_image + 1) % len(conveyor_images)

    # Заполнение экрана цветом
    screen.blit(background_image, (0, 0))
    screen.blit(conveyor_images[current_image], (210, 0))
    game.draw()

    # Обновление экрана
    pg.display.flip()

    # Время кадра
    clock.tick(FPS)

# Завершение PyGame
pg.quit()
sys.exit()
#goida