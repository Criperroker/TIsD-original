import os

import pygame as pg
import sys
import random

# Инициализация PyGame
pg.init()

# Размеры экрана
screen_width = 1200
screen_height = 720

# Создание экрана
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("TIsD")

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
PANKROT_EVENT = pg.USEREVENT + 1
pg.time.set_timer(PANKROT_EVENT, 5000)
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
                },
            "Oven":
                {
                    "price": 100,
                    "description": "Its oven",
                    "quality": 50,
                    "category": "salon",
                    "image": "123"
                },
            "Conditioner":
                {
                    "price": 100,
                    "description": "Its conditioner",
                    "quality": 50,
                    "category": "salon",
                    "image": "123"
                },
            "Ventilation":
                {
                    "price": 100,
                    "description": "Its ventilation",
                    "quality": 50,
                    "category": "salon",
                    "image": "123"
                }
        },
    "maintenance":
        {
            "Oil":
                {
                    "price": 100,
                    "description": "Its oil",
                    "quality": 50,
                    "category": "Maintenance",
                    "image": "Game_ind/GUI/Tehnick/Moduls_of_car/oil.png"
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



def get_non_transparent_rect(image):
    # Загружаем изображение с поддержкой альфа-канала
    image = image.convert_alpha()

    # Получаем размеры изображения
    width, height = image.get_size()

    # Инициализируем границы непрозрачных пикселей
    min_x, min_y = width, height
    max_x, max_y = 0, 0

    # Перебираем все пиксели изображения
    for y in range(height):
        for x in range(width):
            # Получаем цвет пикселя (RGBA)
            r, g, b, a = image.get_at((x, y))
            if a != 0:  # Если пиксель непрозрачный
                # Обновляем границы
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # Создаем прямоугольник, охватывающий все непрозрачные пиксели
    if min_x <= max_x and min_y <= max_y:
        return pg.Rect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)
    else:
        # Если все пиксели прозрачны, возвращаем пустой прямоугольник
        return pg.Rect(0, 0, 0, 0)

def handle_produce_button_click(game):
    game.conveyor.produce_vehicle(LightVehicle())
    print("Производство машины запущено")



def load_image(file, width=None, height=None):
    # Проверяем, является ли file уже объектом Surface
    if isinstance(file, pg.Surface):
        image = file
    elif isinstance(file, (str, bytes, os.PathLike)):
        if os.path.exists(file):
            image = pg.image.load(file).convert_alpha()
        else:
            # Если файл не найден, создаем прозрачное изображение
            image = pg.Surface((width, height), pg.SRCALPHA)
            image.fill((0, 0, 0, 0))  # Полностью прозрачное изображение
    else:
        # Если ни путь, ни Surface не переданы, создаем прозрачное изображение
        image = pg.Surface((width, height), pg.SRCALPHA)
        image.fill((0, 0, 0, 0))  # Полностью прозрачное изображение

    if width and height:
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


def generate_random_orders(n, orders, order_index=None):
    orders = orders
    buttons = []
    for _ in range(n):
        name = random.choice(names)
        surname = random.choice(surnames)
        vehicle_type = random.choice(["Light Vehicle", "Medium Vehicle", "Hard Vehicle"])
        quality = random.choice(["Standard", "High", "Premium"])
        price = random.randint(100, 1000)
        deadline = random.randint(5, 10)
        description = generate_description(vehicle_type)
        popularity = random.randint(1, 10)
        if order_index is None:
            orders.append(Order(vehicle_type, quality, price, deadline, name, surname, description, popularity))
            # Создаем AnimatedButton только для перезагрузки заказов
            reload_order = AnimatedButton("", x=-100, y=-100, total_width=64, total_height=64, func=None, images=reload_button_images)
            buttons.append(reload_order)
        else:
            orders[order_index] = Order(vehicle_type, quality, price, deadline, name, surname, description, popularity)

    return orders, buttons




def generate_shop_window(shop_items):
    items_all = []
    for category, items in shop_items.items():
        for name, details in items.items():
            quality = details['quality']
            price = details['price']
            description = details['description']
            image = details.get('image')  # Путь к изображению, может быть None
            items_all.append(Shop(price=price, quality=quality, category=category, name=name, description=description, image=image))
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

# Загрузка кадров анимации для кнопки перезагрузки
reload_button_images = [
    load_image("Game_ind/GUI/Order_GUI/window_order_open/animation_reload_button/reload_order-1.png", 50, 50),
    load_image("Game_ind/GUI/Order_GUI/window_order_open/animation_reload_button/reload_order-2.png", 50, 50),
    load_image("Game_ind/GUI/Order_GUI/window_order_open/animation_reload_button/reload_order-3.png", 50, 50)

]


class Button:
    def __init__(self, text, x, y, total_width=None, total_height=None, text_font=font, func=None,
                 image="Game_ind/GUI/Base_GUI/Button_GUI/Button.png"):
        self.func = func
        self.x = x
        self.y = y
        self.image = load_image(image, total_width, total_height)

        # Получаем прямоугольник с учетом непрозрачных областей изображения
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)  # Устанавливаем позицию Rect

        self.text = text_render(text)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.text_rect = self.text_rect[0], self.text_rect[1] - 7 # текст по центру кнопки


        self.is_pressed = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.text, self.text_rect)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                if self.func:
                    self.func()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False



class AnimatedButton(Button):
    def __init__(self, text, x, y, total_width=None, total_height=None, text_font=font, func=None,
                 images=None, hover_images=None):
        super().__init__(text, x, y, total_width=total_width, total_height=total_height, text_font=text_font, func=func,
                         image=images[0])  # Передаем первое изображение как основное для кнопки

        self.images = images  # Здесь сохраняются все кадры анимации
        self.hover_images = hover_images if hover_images else images  # Кадры анимации при наведении
        self.current_frame = 0  # Текущий кадр анимации
        self.last_update = pg.time.get_ticks()  # Время последнего обновления кадра
        self.animation_speed = 150  # Скорость анимации в миллисекундах
        self.is_hovered = False  # Флаг наведения курсора

    def update(self):
        if self.is_hovered:
            now = pg.time.get_ticks()
            if now - self.last_update > self.animation_speed:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.hover_images)
                self.image = self.hover_images[self.current_frame]  # Установка текущего кадра
        else:
            self.image = self.images[0]  # Устанавливаем первый кадр по умолчанию, если не наведено

    def draw(self, screen):
        # Отрисовка текущего кадра изображения
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.text, self.text_rect)

    def check_hover(self, mouse_pos):
        # Проверяем, наведен ли курсор на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)



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

    def reload_order(self, index_order):
        pass


class Shop:
    def __init__(self, price, quality, category, name, description, image=None):
        self.price = price
        self.quality = quality
        self.name = name
        self.description = description
        self.category = category

        if image: # если image е равен None (передали)
            self.image = load_image(image, 64, 64)  # Загружаем картинку
            non_transparent_rect = get_non_transparent_rect(self.image)  # Функция, которая получает rect без фона
            self.rect = non_transparent_rect  # Установка позиции картинки
        else:
            self.image = pg.Surface((64, 64), pg.SRCALPHA)
            self.rect = self.image.get_rect()

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
        self.selected_button = None
        self.pankrot_mode = True

        self.reload_limits = 5
        self.save_days = 0
        self.is_saved_day = False

        self.order_start_x = 473  # X-координата, с которой начинается первый заказ
        self.order_start_y = 30  # Y-координата, с которой начинается первый заказ
        self.reload_order_button_y = 128

        self.items_start_x = 480  # X-координата, с которой начинается первый заказ
        self.items_start_y = 41  # Y-координата, с которой начинается первый заказ

        self.INCREASE_COINS = pg.USEREVENT + 2
        pg.time.set_timer(self.INCREASE_COINS, 1000)
        self.DECREASE = pg.USEREVENT + 3
        pg.time.set_timer(self.DECREASE, 1000)

        self.conveyor_image = load_image(
            "Game_ind/Base/conveir_all/conveir_up/1c/conveir_up_64x64.png", 400, 700)
        self.money_image = load_image("Game_ind/GUI/Base_GUI/money/money_64x64.png", 64, 64)
        self.money_image_rect = get_non_transparent_rect(self.money_image)
        self.money_image_rect.topleft = (screen_width / 15, 40)

        self.popularity_image = load_image("Game_ind/GUI/Base_GUI/Popularity/100%/popularity100_64x64.png", 64, 64)
        self.popularity_image_rect = get_non_transparent_rect(self.popularity_image)
        self.popularity_image_rect.topleft = (screen_width / 15, 120)

        self.windowGUIorder = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 460, 440)
        self.windowGUIorder_image_rect = get_non_transparent_rect(self.popularity_image)

        self.ButtonGuiOrder = Button("Orders", 650, 10, total_width=120, total_height=120, func=self.toggle_orders_window)

        self.ButtonGuiShop = Button("Shop", 790, 10, total_width=120, total_height=120, func=self.toggle_shop_window)

        self.OrderGui = load_image("Game_ind/GUI/Order_GUI/order_mini/order_mini.png", 346, 256)
        self.OrderGui_image_rect = get_non_transparent_rect(self.OrderGui)

        self.showcase_of_products = load_image("Game_ind/GUI/Shop_GUI/showcase_of_products.png", 280, 240)
        self.showcase_of_products_image_rect = get_non_transparent_rect(self.showcase_of_products)

        self.pankrot_image = load_image("Game_ind/GUI/Base_GUI/Icons_for_ideas/Pankrot_icon.png", 32, 32)
        self.pankrot_image_rect = get_non_transparent_rect(self.pankrot_image)

        self.transmission_tab_image = load_image("Game_ind/GUI/Shop_GUI/transmission_tab.png", 64, 64)
        self.transmission_tab_image_rect = get_non_transparent_rect(self.transmission_tab_image)

        # self.reload_order_rect = self.reload_order.get_rect()
        pg.time.set_timer(self.money + 1, 500)

        self.money_text = text_render(f"{self.money}")
        self.money_text_rect = self.money_text.get_rect()
        self.money_text_rect.center = (800, 129)

        self.popularity_text = text_render(f"{self.popularity}%")
        self.popularity_text_rect = self.popularity_text.get_rect()

        self.show_orders_window = False  # Флаг для отображения окна заказов
        self.show_shop_window = False
        self.orders_button_rect = pg.Rect(self.ButtonGuiOrder.rect)  # Позиция и размеры кнопки "Заказы"

        self.orders, self.reload_buttons = generate_random_orders(5, self.orders)

        self.info_window_width = 527  # Примерная ширина окна информации
        self.info_window_height = 528  # Примерная высота окна информации

        # Пример загрузки изображения
        example_image = load_image("Game_ind/Tehnick/Moduls_of_car/oil.png", 400, 400)

        # Получение прямоугольника непрозрачной области изображения
        self.non_transparent_rect = get_non_transparent_rect(example_image)
        print("Непрозрачная область изображения:", self.non_transparent_rect)

        # Выводим прямоугольник на экран для наглядности
        self.example_image = example_image
        self.example_image_rect = self.non_transparent_rect

    def toggle_orders_window(self):
        if not self.show_shop_window:
            self.show_orders_window = not self.show_orders_window
            if not self.show_orders_window:
                # Прячем кнопки, не очищая список
                for button in self.reload_buttons:
                    button.rect.topleft = (-100, -100)
            print("Orders window toggled")
        elif self.show_shop_window:
            self.show_orders_window = not self.show_orders_window
            self.show_shop_window = not self.show_shop_window
            if not self.show_orders_window:
                # Прячем кнопки, не очищая список
                for button in self.reload_buttons:
                    button.rect.topleft = (-100, -100)
            print("Orders and Shop windows toggled")

    def draw_orders_window(self):
        padding = 77  # Отступ между заказами

        # Отрисовка окна заказов
        screen.blit(self.windowGUIorder, (450, 97))  # Позиция окна заказов

        for index, order in enumerate(self.orders):
            order_y_position = self.order_start_y + (index * padding)
            reload_y_position = self.reload_order_button_y + (index * padding)
            order.rect.topleft = (self.order_start_x, order_y_position)
            # Отрисовка каждого заказа здесь
            screen.blit(self.OrderGui, order.rect.topleft)
            screen.blit(self.reload_buttons[index].image, (order.rect.right, reload_y_position))

        for index, order in enumerate(self.orders):
            order_y_position = self.order_start_y + (index * padding)
            order.rect.topleft = (self.order_start_x, order_y_position + 95)

        for index, button in enumerate(self.reload_buttons):
            order_y_position = self.order_start_y + (index * padding)
            button.rect.topleft = (self.orders[index].rect.right + 8, order_y_position + 103)
            # pg.draw.rect(screen, "Black", button.rect)

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
        if not self.show_orders_window:
            self.show_shop_window = not self.show_shop_window
            print("Shop window toggled")
        elif self.show_orders_window:
            self.show_shop_window = not self.show_shop_window
            self.show_orders_window = not self.show_orders_window
            if not self.show_orders_window:
                # Прячем кнопки, не очищая список
                for button in self.reload_buttons:
                    button.rect.topleft = (-100, -100)
            print("Shop and Orders windows toggled")

    def draw_shop_window(self, mode):
        shop_index = 0
        padding = 85
        self.windowGUIshop = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 390, 530)
        screen.blit(self.windowGUIshop, (450, 97))

        for item in range(len(self.items_all)):
            if self.items_all[item].category == mode:
                item_y_position = self.items_start_y + (shop_index * padding)
                self.items_all[item].rect.topleft = (self.items_start_x, item_y_position)
                # Отрисовка каждого шаблона для товара(картинка)
                screen.blit(self.showcase_of_products, self.items_all[item].rect.topleft)

                pg.draw.rect(screen, (255, 0, 0), self.items_all[item].rect, 2)
                print(self.items_all[item].name)
                shop_index += 1

        shop_index = 0
        for item in range(len(self.items_all)):
            if self.items_all[item].category == mode:
                items_y_position = self.items_start_y + (shop_index * padding)
                self.items_all[item].rect.topleft = (self.items_start_x, items_y_position + 90)
                # pg.draw.rect(screen, "Black", self.items_all[item].rect)
                shop_index += 1

        y_start = 140

        for item in self.items_all:
            if item.category == mode:

                shop_name = f"{item.name}"
                shop_price = f"{item.price}"
                shop_quality = f"Quality: {item.quality}"
                screen.blit(font_mini.render(shop_name, True, BLACK), (575, y_start + 10))
                screen.blit(font_mini.render(shop_price, True, BLACK), (720, y_start + 52))
                screen.blit(font_mini.render(shop_quality, True, BLACK), (576, y_start + 52))
                screen.blit(item.image, (200, 200))
                print(item.rect)

                y_start += 85

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

    def lose_money(self, amount):
        self.popularity -= amount
        if self.money <= 0:
            self.pankrot_mode = True

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
        screen.blit(self.money_image, self.money_image_rect)
        screen.blit(text_render(self.money), (screen_width / 15 + 60, 65))
        screen.blit(self.popularity_image, self.popularity_image_rect)
        screen.blit(text_render(str(self.popularity) + "%"), (screen_width / 15 + 60, 145))

        self.ButtonGuiOrder.draw(screen)
        self.ButtonGuiShop.draw(screen)

        if self.show_orders_window:
            self.draw_orders_window()

        if self.show_shop_window:
            self.draw_shop_window(mode="maintenance")

        if self.selected_order:
            # Путь к изображению окна информации о заказе
            info_window_image_path = "Game_ind/GUI/Order_GUI/window_order_open/window_order_open.png"
            accept_order = "Game_ind/GUI/Order_GUI/window_order_open/accept_order_button.png"
            reject_order = "Game_ind/GUI/Order_GUI/window_order_open/reject_order_button.png"
            # Загрузка и отрисовка окна информации о заказе
            info_window_image = load_image(info_window_image_path, self.info_window_width, self.info_window_height)
            accept_order_image = load_image(accept_order, 100, 100)
            reject_order_image = load_image(reject_order, 100, 100)
            info_window_x = 50  # Начальная X-координата для окна информации
            info_window_y = 0  # Начальная Y-координата для окна информации
            screen.blit(info_window_image, (info_window_x, info_window_y))
            screen.blit(accept_order_image, (info_window_x + 20, info_window_y + 328))
            screen.blit(reject_order_image, (info_window_x + 140, info_window_y + 328))

            # Отрисовка текста описания заказа
            description_text = font_mini.render(self.selected_order.description, True, WHITE)

            info_text_x = info_window_x + 30  # Небольшой отступ от края окна информации
            info_text_y = info_window_y + 200  # Небольшой отступ от края окна информации
            # screen.blit(description_text, (info_text_x, info_text_y))
            self.draw_description(self.selected_order.description, font_mini, screen, info_text_x, info_text_y,
                                  self.info_window_width - 60)  # Уменьшить ширину для отступов
            screen.blit(font_mini.render(self.selected_order.name, True, WHITE), (100, 140))
            screen.blit(font_mini.render(self.selected_order.surname, True, WHITE), (350, 140))
            screen.blit(font_mini.render("Accept", True, WHITE), (info_window_x + 46, info_window_y + 368))
            screen.blit(font_mini.render("Reject", True, WHITE), (info_window_x + 168, info_window_y + 368))


        screen.blit(self.example_image, (100, 100))

        # Смещение rect на позицию изображения
        rect_with_offset = self.example_image_rect.move(100, 100)
        pg.draw.rect(screen, (255, 0, 0), rect_with_offset, 2)


# Игровой цикл
game = Game()
running = True
while running:
    mouse_pos = pg.mouse.get_pos()  # Получаем текущую позицию курсора

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Обработка событий (например, нажатие кнопок)
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = pg.mouse.get_pressed()
            if mouse_pressed[0] or mouse_pressed[2]:
                if game.selected_order and not game.selected_order.rect.collidepoint(event.pos):
                    game.selected_order = None

                if game.show_orders_window:
                    for order in game.orders:
                        if order.rect.collidepoint(event.pos):
                            if game.selected_order == order:
                                game.selected_order = None
                            else:
                                game.selected_order = order
                            break

                if game.show_shop_window:
                    for item in game.items_all:
                        if item.rect.collidepoint(event.pos):
                            if game.money >= item.price:
                                game.money -= item.price

        if event.type == DAY_EVENT:
            game.day += 1

            if game.reload_limits == 0 and game.is_saved_day == False:
                game.save_days = game.day
                game.is_saved_day = True
            if game.save_days + 10 == game.day:
                game.reload_limits = 5
                game.is_saved_day = False

        if event.type == PANKROT_EVENT:
            if game.pankrot_mode:
                game.popularity -= 1

        if event.type == INCREASE_MONEY:
            game.money += 1

        if event.type == pg.MOUSEBUTTONDOWN and game.orders_button_rect.collidepoint(event.pos):
            mouse_pressed = pg.mouse.get_pressed()
            if mouse_pressed[0]:
                game.ButtonGuiOrder.is_clicked(event)
        game.ButtonGuiShop.is_clicked(event)

        if event.type == pg.MOUSEBUTTONDOWN and game.show_orders_window:
            mouse_pressed = pg.mouse.get_pressed()
            if mouse_pressed[0]:
                for button in game.reload_buttons:
                    if button.rect.collidepoint(event.pos) and game.reload_limits > 0:
                        game.reload_limits -= 1
                        print(game.reload_limits)
                        order_index = game.reload_buttons.index(button)
                        game.selected_button = button  # Запоминаем выбранный заказ
                        game.orders[order_index] = generate_random_orders(1, game.orders, order_index=order_index)[0][
                            order_index]
                        print(game.reload_buttons[game.reload_buttons.index(button)])
                        break  # Выходим из цикла, так как заказ найден

    # Переход к следующему изображению
    now = pg.time.get_ticks()
    if now - last_update > FPS:
        last_update = 0
        current_image = (current_image + 1) % len(conveyor_images)

    # Заполнение экрана фоном
    screen.blit(background_image, (0, 0))
    screen.blit(conveyor_images[current_image], (210, 0))

    # Обновление анимации кнопок reload
    for button in game.reload_buttons:
        button.check_hover(mouse_pos)  # Проверяем, наведен ли курсор на кнопку
        button.update()
        button.draw(screen)

    # Отрисовка остальных элементов игры
    game.draw()

    # Обновление экрана
    pg.display.flip()

    # Время кадра
    clock.tick(FPS)

# Завершение PyGame
pg.quit()
sys.exit()

# сделать вкладки магазина - доделать полностью функционал магазина. Начать делать концепт склада
