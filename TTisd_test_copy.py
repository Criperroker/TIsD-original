import os

import pygame as pg
import sys
import random

# Инициализация PyGame
pg.init()

# Размеры экрана
screen_width = 1400
screen_height = 720

# Создание экрана
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("TIsD")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Установка FPS
clock = pg.time.Clock()
FPS = 60

alfa_type = 0
fade_speed = 25

last_update = pg.time.get_ticks()
current_image = 0

DAY_EVENT = pg.USEREVENT + 1
pg.time.set_timer(DAY_EVENT, 3000)

INCREASE_MONEY = pg.USEREVENT + 2
PANKROT_EVENT = pg.USEREVENT + 1
pg.time.set_timer(PANKROT_EVENT, 5000)
pg.time.set_timer(INCREASE_MONEY, 1000)

font = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 20)
font_medium = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 15)
font_mini = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 10)
font_description = pg.font.Font("Game_ind/Better VCR 6.1.ttf", 8)

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

empty_model = {
    "name": "",
    "appearance_items": [],
    "salon_items": [],
    "transmission": [],
    "management mechanisms": []
}

model_machine = {
    "Light model":
        {
            "category": "Light model",
            "speed": 100,
            "power": 130,
            "quality": 10,
            "production_cost": 5,
            "image": "Game_ind/GUI/Storage_GUI/Light_model.png",
            "base_price": 150
        },
    "Medium model":
        {
            "category": "Medium model",
            "speed": 80,
            "power": 180,
            "quality": 10,
            "production_cost": 15,
            "image": "Game_ind/GUI/Storage_GUI/Light_model.png",
            "base_price": 200

        },
    "Heavy model":
        {
            "category": "Heavy model",
            "speed": 60,
            "power": 200,
            "quality": 10,
            "production_cost": 25,
            "image": "Game_ind/GUI/Storage_GUI/Light_model.png",
            "base_price": 350
        }
}

shop_items = {
    "appearance":
        {
            "Carbon fiber cladding":
                {
                    "price": 500,
                    "description": "Its carbon fiber cladding",
                    "quality": 50,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/Carbon fiber cladding.png",
                    "account": 0
                },
            "Glass":
                {
                    "price": 50,
                    "description": "Its glass",
                    "quality": 502,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/glass.png",
                    "account": 0
                },
            "Bumper":
                {
                    "price": 100,
                    "description": "Its bumper",
                    "quality": 504,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0

                },
            "Doors":
                {
                    "price": 100,
                    "description": "Its doors",
                    "quality": 505,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Headlights":
                {
                    "price": 100,
                    "description": "Its headlights",
                    "quality": 50,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Rear view mirrors":
                {
                    "price": 100,
                    "description": "Its rear view mirrors",
                    "quality": 50,
                    "category": "appearance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
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
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Shock absorbers":
                {
                    "price": 100,
                    "description": "Its shock absorbers",
                    "quality": 50,
                    "category": "management mechanisms",
                    "image": "Game_ind/Tehnick/Moduls_of_car/Shock absorbers.png",
                    "account": 0
                },
            "Engine":
                {
                    "price": 100,
                    "description": "Its trunk",
                    "quality": 50,
                    "category": "transmission",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Сlutch":
                {
                    "price": 100,
                    "description": "Its gimbal drive",
                    "quality": 50,
                    "category": "transmission",
                    "image": "Game_ind/Tehnick/Moduls_of_car/clutch.png",
                    "account": 0
                },
            "Main transfer":
                {
                    "price": 100,
                    "description": "Its Main transfer",
                    "quality": 50,
                    "category": "transmission",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Wheels":
                {
                    "price": 100,
                    "description": "Its wheels",
                    "quality": 50,
                    "category": "transmission",
                    "image": "Game_ind/Tehnick/Moduls_of_car/wheels.png",
                    "account": 0
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
                    "image": "Game_ind/Tehnick/Moduls_of_car/helm.png",
                    "account": 0
                },

            "Elastic spring":
                {
                    "price": 100,
                    "description": "Its elastic spring",
                    "quality": 50,
                    "category": "management mechanisms",
                    "image": "Game_ind/Tehnick/Moduls_of_car/elastic_spring.png",
                    "account": 0

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
                    "image": "Game_ind/Tehnick/Moduls_of_car/radio.png",
                    "account": 0
                },
            "Seat":
                {
                    "price": 100,
                    "description": "Its seat",
                    "quality": 50,
                    "category": "salon",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Oven":
                {
                    "price": 100,
                    "description": "Its oven",
                    "quality": 50,
                    "category": "salon",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Conditioner":
                {
                    "price": 100,
                    "description": "Its conditioner",
                    "quality": 50,
                    "category": "salon",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },
            "Ventilation":
                {
                    "price": 100,
                    "description": "Its ventilation",
                    "quality": 50,
                    "category": "salon",
                    "image": "Game_ind/Tehnick/Moduls_of_car/ventilation.png",
                    "account": 0
                }
        },
    "maintenance":
        {
            "Gas":
                {
                    "price": 100,
                    "description": "Its oil",
                    "quality": 50,
                    "category": "Maintenance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                },

            "Oil":
                {
                    "price": 100,
                    "description": "Its oil",
                    "quality": 50,
                    "category": "Maintenance",
                    "image": "Game_ind/Tehnick/Moduls_of_car/not_image.png",
                    "account": 0
                }
        },

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


# def get_non_transparent_rect(image):
#     # Загружаем изображение с поддержкой альфа-канала
#     image = image.convert_alpha()
#
#     # Получаем размеры изображения
#     width, height = image.get_size()
#
#     # Инициализируем границы непрозрачных пикселей
#     min_x, min_y = width, height
#     max_x, max_y = 0, 0
#
#     # Перебираем все пиксели изображения
#     for y in range(height):
#         for x in range(width):
#             # Получаем цвет пикселя (RGBA)
#             r, g, b, a = image.get_at((x, y))
#             if a != 0:  # Если пиксель непрозрачный
#                 # Обновляем границы
#                 min_x = min(min_x, x)
#                 min_y = min(min_y, y)
#                 max_x = max(max_x, x)
#                 max_y = max(max_y, y)
#
#     # Создаем прямоугольник, охватывающий все непрозрачные пиксели
#     if min_x <= max_x and min_y <= max_y:
#         return pg.Rect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)
#     else:
#         # Если все пиксели прозрачны, возвращаем пустой прямоугольник
#         return pg.Rect(0, 0, 0, 0)

def get_non_transparent_rect(image):
    mask = pg.mask.from_surface(image)
    rect = mask.get_bounding_rects()
    if rect:
        return rect[0]
    else:
        return pg.Rect(0, 0, 0, 0)


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
    order_image = []
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
            reload_order = AnimatedButton("", x=-100, y=-100, total_width=53, total_height=55, func=None,
                                          images=reload_button_images)
            animation_order = AnimatedOrder("", x=0, y=0, total_width=346, total_height=256, func=None,
                                            images=gui_order_window_images)
            buttons.append(reload_order)
            order_image.append(animation_order)
        else:
            orders[order_index] = Order(vehicle_type, quality, price, deadline, name, surname, description, popularity)

    return orders, buttons, order_image


def generate_create_window(Vichile_model):
    models = []
    for name, property in model_machine.items():
        quality = property['quality']
        speed = property['speed']
        production_cost = property['production_cost']
        power = property['power']
        category = property['category']
        image = property.get("image")
        base_price = property['base_price']
        models.append(
            Vehicle(quality=quality, speed=speed, production_cost=production_cost, power=power, category=category,
                    image=image, base_price=base_price))
    return models


def generate_shop_window(shop_items):
    items_all = []
    for category, items in shop_items.items():
        for name, details in items.items():
            quality = details['quality']
            price = details['price']
            description = details['description']
            image = details.get('image')  # Путь к изображению, может быть None
            account = details['account']
            items_all.append(
                Shop(price=price, quality=quality, category=category, name=name, description=description, image=image,
                     account=account))
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

gui_order_window_images = [
    load_image("Game_ind/GUI/Order_GUI/animation_order_mini/order_mini-1.png.png", 346, 256),
    load_image("Game_ind/GUI/Order_GUI/animation_order_mini/order_mini-2.png.png", 346, 256),
    load_image("Game_ind/GUI/Order_GUI/animation_order_mini/order_mini-3.png.png", 346, 256),
    load_image("Game_ind/GUI/Order_GUI/animation_order_mini/order_mini-4.png.png", 346, 256)
]


class Button:
    def __init__(self, text, x, y, total_width=None, total_height=None, text_font=font, func=None,
                 image="Game_ind/GUI/Base_GUI/Button_GUI/Button.png"):
        self.func = func
        self.x = x
        self.y = y
        self.image_def = load_image(image, total_width, total_height)
        self.image = self.image_def

        # Получаем непрозрачный прямоугольник
        non_transparent_rect = get_non_transparent_rect(self.image)
        self.offset_x = non_transparent_rect.x
        self.offset_y = non_transparent_rect.y
        self.non_transparent_rect = non_transparent_rect

        # Устанавливаем self.rect в позицию кнопки с размером непрозрачной области
        self.rect = pg.Rect(self.x, self.y, non_transparent_rect.width, non_transparent_rect.height)

        # Рендерим текст и центрируем его на кнопке
        self.text = text_render(text)
        self.text_rect = self.text.get_rect(center=self.rect.center)

        self.is_pressed = False
        self.is_hovered = False

        self.hovered_button = "Game_ind/GUI/Base_GUI/Button_GUI/Button_2.png"
        self.hovered_button_image = load_image(self.hovered_button, total_width, total_height)
        # Получаем непрозрачный прямоугольник для изображения при наведении
        hovered_non_transparent_rect = get_non_transparent_rect(self.hovered_button_image)
        self.hover_offset_x = hovered_non_transparent_rect.x
        self.hover_offset_y = hovered_non_transparent_rect.y
        self.hover_non_transparent_rect = hovered_non_transparent_rect

    def update(self):
        if self.is_hovered:
            self.image = self.hovered_button_image
            self.current_offset_x = self.hover_offset_x
            self.current_offset_y = self.hover_offset_y
            self.rect.size = self.hover_non_transparent_rect.size
        else:
            self.image = self.image_def
            self.current_offset_x = self.offset_x
            self.current_offset_y = self.offset_y
            self.rect.size = self.non_transparent_rect.size

    def draw(self, screen):
        # Рисуем изображение с учетом смещения
        screen.blit(self.image, (self.x - self.current_offset_x, self.y - self.current_offset_y))
        # Рисуем текст
        screen.blit(self.text, self.text_rect)
        # Для отладки: рисуем прямоугольник

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

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


class AnimatedOrder(Button):
    def __init__(self, text, x, y, total_width=None, total_height=None, text_font=font, func=None,
                 images=None, hover_images=None):
        super().__init__(text, x, y, total_width=total_width, total_height=total_height, text_font=text_font, func=func,
                         image=images[0])  # Передаем первое изображение как основное для кнопки

        self.images = images  # Здесь сохраняются все кадры анимации
        self.hover_images = hover_images if hover_images else images  # Кадры анимации при наведении
        self.current_frame = 0  # Текущий кадр анимации
        self.last_update = pg.time.get_ticks()  # Время последнего обновления кадра
        self.animation_speed = 100  # Скорость анимации в миллисекундах
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
        pass

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
    def __init__(self, price, quality, category, name, description, image=None, account=None):
        self.price = price
        self.quality = quality
        self.name = name
        self.description = description
        self.category = category
        self.account = account

        if image:
            # Загрузка и масштабирование изображения только один раз
            self.original_image = load_image(image, 128, 200)
            self.image = pg.transform.scale(self.original_image, (70, 70))  # Масштабируем сразу
            self.rect = get_non_transparent_rect(self.image)
        else:
            self.image = pg.Surface((200, 200), pg.SRCALPHA)
            self.rect = self.image.get_rect()

    def draw(self, screen, x, y):
        # Отрисовываем изображение без повторной трансформации
        screen.blit(self.image, (x, y))

    def update(self):
        pass


class Storage:
    def __init__(self, level):
        self.level = level


class Vehicle:
    def __init__(self, quality, speed, power, production_cost, category, image=None, base_price=None):
        self.speed = speed
        self.power = power
        self.quality = quality
        self.production_cost = production_cost
        self.category = category
        self.base_price = base_price

        if image:
            # Загрузка и масштабирование изображения только один раз
            self.original_image = load_image(image, 278, 71)
            self.image = pg.transform.scale(self.original_image, (150, 200))  # Масштабируем сразу
            self.rect = get_non_transparent_rect(self.image)
        else:
            self.image = pg.Surface((96, 96), pg.SRCALPHA)
            self.rect = self.image.get_rect()

    def draw(self, screen, x, y):
        # Отрисовываем изображение без повторной трансформации
        print()
        screen.blit(self.image, (x, y))


class Game:
    def __init__(self):
        self.popularity = 100
        self.money_sec = 1
        self.chance_of_orders = 10
        self.orders = []
        self.items_all = generate_shop_window(shop_items)
        self.model = generate_create_window(model_machine)
        self.conveyor = Conveyor()
        self.day = 0
        self.selected_order = None
        self.selected_button = None
        self.storage = Storage(1)
        self.pankrot_mode = True
        self.in_storage = False
        self.flag_model_mode = 1

        self.accept_order = "Game_ind/GUI/Order_GUI/window_order_open/accept_order_button.png"
        self.reject_button_rect = None
        accept_order_image = load_image(self.accept_order, 100, 100)

        self.reject_order = "Game_ind/GUI/Order_GUI/window_order_open/reject_order_button.png"
        reject_order_image = load_image(self.reject_order, 100, 100)

        self.level_buy_storage = "Game_ind/GUI/Base_GUI/Button_GUI/Button.png"
        self.level_buy_storage_image = load_image(self.level_buy_storage, 150, 150).convert_alpha()
        self.level_buy_storage_rect = get_non_transparent_rect(self.level_buy_storage_image).move(685, 73)

        self.description_level_storage = "Game_ind/GUI/Base_GUI/Description/description_1type.png"
        self.description_level_storage_image = load_image(self.description_level_storage, 150, 150).convert_alpha()
        self.description_level_storage_rect = get_non_transparent_rect(self.description_level_storage_image).move(685,
                                                                                                                  73)
        self.occupy_button = "Game_ind/GUI/Base_GUI/Button_GUI/Button.png"
        self.occupy_button_text = "Occupy 1000$"
        self.occupy_button_image = load_image(self.occupy_button, 200, 150)
        self.occupy_button_rect = get_non_transparent_rect(self.occupy_button_image).move(470, 478)
        self.credit_button_image = load_image(self.occupy_button, 125, 150)

        self.give_button = "Game_ind/GUI/Base_GUI/Button_GUI/Button.png"
        self.give_button_text = "Give 1000$"
        self.give_button_image = load_image(self.give_button, 200, 150)
        self.give_button_rect = get_non_transparent_rect(self.give_button_image).move(820, 478)

        self.credit = 10000
        self.credit_mode = True

        self.expenses_full = 0

        self.expenses_of_buy_item = 0

        self.expenses_dont_orders = 0

        self.payment_of_credit = 0

        self.percent_for_credit = 100

        self.money = 1000 + self.credit

        self.shop_mode = "appearance"
        self.storage_filter_mode = ""
        self.model_mode = "Light model"
        self.light_model_image = load_image("Game_ind/GUI/Storage_GUI/Light_model.png", 128, 200)
        self.shop_rects = []

        self.storage_window_x = 500
        self.storage_window_y = 97

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

        self.info_window_width = 527  # Примерная ширина окна информации
        self.info_window_height = 528  # Примерная высота окна информации

        self.info_window_x = 50  # Начальная X-координата для окна информации
        self.info_window_y = 0  # Начальная Y-координата для окна информации

        self.accept_button_rect = get_non_transparent_rect(accept_order_image).move(self.info_window_x + 20,
                                                                                    self.info_window_y + 328)
        self.reject_button_rect = get_non_transparent_rect(reject_order_image)

        self.info_window_image = load_image("Game_ind/GUI/Order_GUI/window_order_open/window_order_open.png",
                                            self.info_window_width, self.info_window_height)

        self.Button_closed_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button_closed.png", 40, 40)
        self.Button_closed_rect = get_non_transparent_rect(self.Button_closed_image).move(self.storage_window_x + 690,
                                                                                          self.storage_window_y + 35)

        self.conveyor_image = load_image(
            "Game_ind/Base/conveir_all/conveir_up/1c/conveir_up_64x64.png", 400, 700)
        self.money_image = load_image("Game_ind/GUI/Base_GUI/money/money_64x64.png", 64, 64)
        self.money_image_rect = get_non_transparent_rect(self.money_image).move((screen_width / 30, 40))
        self.accept_order_image = load_image(self.accept_order, 100, 100)
        self.reject_order_image = load_image(self.reject_order, 100, 100)

        self.popularity_image = load_image("Game_ind/GUI/Base_GUI/Popularity/100%/popularity100_64x64.png", 64, 64)
        self.popularity_image_rect = get_non_transparent_rect(self.popularity_image).move((screen_width / 30, 120))

        self.windowGUIorder = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 460, 440)
        self.windowGUIorder_image_rect = get_non_transparent_rect(self.popularity_image)
        self.day_image = load_image("Game_ind/GUI/Base_GUI/Day/Day.png", 64, 64)
        self.day_image_rect = get_non_transparent_rect(self.day_image).move((screen_width / 30, 190))

        self.creater_button_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 120, 120)
        self.creater_toggle = False

        self.appearance_button_image = load_image("Game_ind/GUI/Shop_GUI/appearance_tab.png", 90, 90)
        self.salon_tab_image = load_image("Game_ind/GUI/Shop_GUI/salon_tab.png", 89, 89)
        self.transmission_tab_image = load_image("Game_ind/GUI/Shop_GUI/transmission_tab.png", 88, 88)
        self.management_mechanisms_tab_image = load_image("Game_ind/GUI/Shop_GUI/management_mechanisms_tab.png", 88, 88)

        self.button_next_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button_next.png", 40, 40)
        self.button_after_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button_after.png", 40, 40)

        self.button_model_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 120, 100)
        self.button_accept_model_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 120, 100)

        self.appearance_bar_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 150, 100)
        self.management_mechanisms_bar_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 180, 100)
        self.transmission_bar_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 150, 100)
        self.salon_bar_image = load_image("Game_ind/GUI/Base_GUI/Button_GUI/Button.png", 150, 100)

        self.button_next_rect = get_non_transparent_rect(self.button_next_image).move(self.storage_window_x + 475,
                                                                                      self.storage_window_y + 245)
        self.button_after_rect = get_non_transparent_rect(self.button_after_image).move(self.storage_window_x + 300,
                                                                                        self.storage_window_y + 245)

        self.in_storage_image = load_image("Game_ind/GUI/Shop_GUI/in_storage.png", 32, 32)
        self.in_storage_rect = get_non_transparent_rect(self.in_storage_image).move(765, 120)

        self.ButtonGuiOrder = Button("Orders", 650, 20, total_width=120, total_height=120,
                                     func=self.toggle_orders_window)

        self.ButtonGuiShop = Button("Shop", 790, 20, total_width=120, total_height=120, func=self.toggle_shop_window)

        self.ButtonGuiWarehouse = Button("Storage", 930, 20, total_width=120, total_height=120,
                                         func=self.toggle_storage_window)

        self.ButtonGuiFinance = Button("Finance", 1070, 20, total_width=120, total_height=120,
                                       func=self.toggle_finance_window)

        self.main_buttons = [self.ButtonGuiShop, self.ButtonGuiWarehouse, self.ButtonGuiOrder, self.ButtonGuiFinance]

        self.OrderGui = load_image("Game_ind/GUI/Order_GUI/order_mini/order_mini.png", 346, 256)
        self.OrderGui_image_rect = get_non_transparent_rect(self.OrderGui)

        self.windowGUIshop = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 390, 530)

        self.showcase_of_products = load_image("Game_ind/GUI/Shop_GUI/showcase_of_products.png", 280, 240)
        self.showcase_of_products_image_rect = get_non_transparent_rect(self.showcase_of_products)

        self.pankrot_image = load_image("Game_ind/GUI/Base_GUI/Icons_for_ideas/Pankrot_icon.png", 32, 32)
        self.pankrot_image_rect = get_non_transparent_rect(self.pankrot_image)

        self.storage_icon_image = load_image("Game_ind/GUI/Storage_GUI/storage_icon.png", 310, 224)
        self.storage_icon_rect = get_non_transparent_rect(self.storage_icon_image)

        pg.time.set_timer(self.money + 1, 500)

        self.money_text = text_render(f"{self.money}")
        self.money_text_rect = self.money_text.get_rect()
        self.money_text_rect.center = (800, 129)

        self.popularity_text = text_render(f"{self.popularity}%")
        self.popularity_text_rect = self.popularity_text.get_rect()

        self.show_orders_window = False  # Флаг для отображения окна заказов
        self.show_shop_window = False
        self.show_storage_window = False
        self.show_finance_window = False

        self.orders_button_rect = pg.Rect(self.ButtonGuiOrder.rect)  # Позиция и размеры кнопки "Заказы"
        self.storage_button_rect = pg.Rect(self.ButtonGuiWarehouse.rect)  # Позиция и размеры кнопки "Склад"
        self.finance_button_rect = pg.Rect(self.ButtonGuiFinance.rect)  # Позиция и размеры кнопки "Финансы"

        self.orders, self.reload_buttons, self.orders_images = generate_random_orders(5, self.orders)

        # Пример загрузки изображения
        example_image = load_image("Game_ind/GUI/Shop_GUI/appearance_tab.png", 400, 400)

        # Получение прямоугольника непрозрачной области изображения
        self.non_transparent_rect = get_non_transparent_rect(example_image)
        print("Непрозрачная область изображения:", self.non_transparent_rect)

        # Выводим прямоугольник на экран для наглядности
        self.example_image = example_image
        self.example_image_rect = self.non_transparent_rect

        # Задаем единый размер для всех товаров
        self.item_width = 96  # Ширина
        self.item_height = 96  # Высота
        self.item_size = (self.item_width, self.item_height)

        self.storage_scroll_offset = 0
        self.storage_scroll_speed = 20
        self.storage_max_scroll = 0

    def toggle_orders_window(self):
        if not self.show_orders_window:
            self.show_orders_window = True
            self.show_shop_window = False
            self.show_storage_window = False
            self.show_finance_window = False
            if not self.show_orders_window:
                # Прячем кнопки, не очищая список
                for button in self.reload_buttons:
                    button.rect.topleft = (-100, -100)
            print("Orders window toggled")
        elif self.show_orders_window:
            self.show_orders_window = not self.show_orders_window
            if self.show_orders_window == False:
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
            # screen.blit(self.OrderGui, order.rect.topleft)
            screen.blit(self.reload_buttons[index].image, (order.rect.right, reload_y_position))
            screen.blit(self.orders_images[index].image, order.rect.topleft)

        for index, order in enumerate(self.orders):
            order_y_position = self.order_start_y + (index * padding)
            order.rect.topleft = (self.order_start_x, order_y_position + 95)

        for index, button in enumerate(self.reload_buttons):
            order_y_position = self.order_start_y + (index * padding)
            button.rect.topleft = (self.orders[index].rect.right + 6, order_y_position + 103)
            # pg.draw.rect(screen, "Black", button.rect)

        for index, button in enumerate(self.orders_images):
            order_y_position = self.order_start_y + (index * padding)
            button.rect.topleft = (self.orders[index].rect.left, order_y_position + 90)
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
        if not self.show_shop_window:
            self.show_shop_window = True
            self.show_orders_window = False
            self.show_storage_window = False
            self.show_finance_window = False
            for button in self.reload_buttons:
                button.rect.topleft = (-100, -100)
        elif self.show_shop_window:
            self.show_shop_window = not self.show_shop_window

            if not self.show_shop_window:
                # Прячем кнопки, не очищая список
                for button in self.reload_buttons:
                    button.rect.topleft = (-100, -100)

    def draw_shop_window(self, mode):
        shop_index_item = 0
        shop_index_text = 0
        padding = 87
        self.windowGUIshop = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 390, 570)
        screen.blit(self.windowGUIshop, (450, 97))
        self.shop_rects = []

        # Обновляем кнопки вкладок
        self.appearance_button_rect = get_non_transparent_rect(self.appearance_button_image).move(480, 65)
        self.salon_tab_rect = get_non_transparent_rect(self.salon_tab_image).move(642, 60)
        self.transmission_tab_rect = get_non_transparent_rect(self.transmission_tab_image).move(562, 60)
        self.management_mechanisms_tab_rect = get_non_transparent_rect(self.management_mechanisms_tab_image).move(722,
                                                                                                                  60)

        # Отрисовка вкладок
        screen.blit(self.appearance_button_image, (480, 65))
        screen.blit(self.salon_tab_image, (642, 60))
        screen.blit(self.transmission_tab_image, (562, 60))
        screen.blit(self.management_mechanisms_tab_image, (722, 60))

        # Обрабатываем только товары в текущей вкладке
        for item in self.items_all:
            if item.category == mode:
                # Если товар находится в текущей вкладке
                item_y_position = self.items_start_y + (shop_index_item * padding)

                # Отрисовка фона витрины
                screen.blit(self.showcase_of_products, (self.items_start_x, item_y_position))
                screen.blit(self.in_storage_image, (765, 120 + item_y_position))
                self.in_storage_rect = get_non_transparent_rect(self.in_storage_image).move(765, 120 + item_y_position)
                pg.draw.rect(screen, "Red", self.in_storage_rect, 2)

                # Обновляем Rect витрины только для текущего элемента
                showcase_rect = self.showcase_of_products_image_rect.move(self.items_start_x, item_y_posit
                ion)
                item.rect = showcase_rect
                if item.rect not in self.shop_rects:
                    self.shop_rects.append(item.rect)

                # Рассчитываем координаты для центрирования изображения внутри витрины
                image_x = self.items_start_x + 15
                image_y = item_y_position + 100

                # Отрисовка изображения товара
                screen.blit(item.image, (image_x, image_y))
                shop_index_item += 1
            else:
                # Перемещаем элементы, которые не принадлежат текущей вкладке, за пределы экрана
                item.rect.topleft = (-100, -100)

        # Отрисовка текста для каждого товара в текущей вкладке
        for index, item in enumerate(self.items_all):
            if item.category == mode:
                text_y_position = 128 + (shop_index_text * padding)
                shop_name = f"{item.name}"
                shop_price = f"{item.price}$"
                shop_quality = f"Quality: {item.quality}%"
                shop_description = f"{item.description}"
                shop_account = f"{item.account}"

                # Отрисовка текста рядом с товарами
                screen.blit(font_mini.render(shop_name, True, BLACK), (575, text_y_position + 17))
                screen.blit(font_mini.render(shop_price, True, BLACK), (720, text_y_position + 52))
                screen.blit(font_mini.render(shop_quality, True, BLACK), (576, text_y_position + 52))
                screen.blit(font_description.render(shop_description, True, BLACK), (580, text_y_position + 33))
                screen.blit(font.render(shop_account, True, WHITE), (800, text_y_position + 29))

                shop_index_text += 1

    def toggle_storage_window(self):
        if not self.show_storage_window:
            self.show_storage_window = True
            self.show_orders_window = False
            self.show_shop_window = False
            self.show_finance_window = False
            for button in self.reload_buttons:
                button.rect.topleft = (-100, -100)
        elif self.show_storage_window:
            self.show_storage_window = not self.show_storage_window

    def draw_storage_window(self):
        padding = 85
        # Параметры окна склада (без изменений)
        storage_window_x = 500
        storage_window_y = 97
        storage_window_width = 520
        storage_window_height = 450

        # Параметры области отображения предметов
        items_display_x = storage_window_x + 15
        items_display_y = storage_window_y + 10
        items_display_width = storage_window_width / 2 + 20
        items_display_height = storage_window_height

        # Загрузка и отрисовка окна склада
        self.windowGUIStorage = load_image("Game_ind/GUI/Storage_GUI/window_storage.png", storage_window_width,
                                           storage_window_height + 120)
        screen.blit(self.windowGUIStorage, (storage_window_x, storage_window_y))
        levelup = f"Level {self.storage.level}"

        # Отрисовка вкладок
        self.appearance_button_rect = get_non_transparent_rect(self.appearance_button_image).move(814, 328)
        self.salon_tab_rect = get_non_transparent_rect(self.salon_tab_image).move(894, 328)
        self.transmission_tab_rect = get_non_transparent_rect(self.transmission_tab_image).move(894, 355)
        self.management_mechanisms_tab_rect = get_non_transparent_rect(self.management_mechanisms_tab_image).move(814,
                                                                                                                  355)

        self.creater_button_rect = get_non_transparent_rect(self.creater_button_image).move(839, 270)
        pg.draw.rect(screen, "RED", self.creater_button_rect)

        screen.blit(self.appearance_button_image, (814, 328))
        screen.blit(self.salon_tab_image, (894, 322))
        screen.blit(self.transmission_tab_image, (894, 355))
        screen.blit(self.management_mechanisms_tab_image, (816, 355))

        screen.blit(self.creater_button_image, (839, 270))
        screen.blit(font_mini.render("Creater", True, BLACK), (870, 318))

        screen.blit(self.level_buy_storage_image, (685, 73))
        screen.blit(font.render(levelup, True, BLACK), (707, 130))

        # Создаем список предметов для отображения
        content_items = [item for item in self.items_all if item.account > 0 and (
                item.category == self.storage_filter_mode or self.storage_filter_mode == "")]

        if len(content_items) != 0:
            # content_height = len(content_items) * padding + self.showcase_of_products.get_height() - 225 # Рабочая
            content_height = len(content_items) * padding + self.showcase_of_products.get_height() - 145
            print(content_height)
        else:
            content_height = 0

        # Обновляем максимальное смещение прокрутки
        self.storage_max_scroll = max(0,
                                      content_height - self.showcase_of_products.get_height() - 200)  # Рабочая, но не влезает

        # Создаем поверхность для контента с обновленной высотой
        # content_surface = pg.Surface((items_display_width, content_height), pg.SRCALPHA) # Рабочая, но большая
        if content_height > 85:
            content_surface = pg.Surface((items_display_width, content_height - 85),
                                         pg.SRCALPHA)  # Рабочая, но не влезает
            # print(content_height)
            content_surface.fill((0, 0, 0, 0))  # Прозрачный фон
        elif content_height <= 85:
            content_surface = pg.Surface((0, 0),
                                         pg.SRCALPHA)  # Рабочая, но не влезает
            # print(content_height)
            content_surface.fill((0, 0, 0, 0))  # Прозрачный фон

        y_start = 0
        for item in content_items:
            item_y_position = y_start

            # Отрисовка масштабированного изображения витрины
            content_surface.blit(self.showcase_of_products, (0, item_y_position - 85))
            # print(item_y_position)

            # Корректируем позиции для изображения товара и текста
            image_x = 15
            image_y = item_y_position + 15  # Размещаем изображение товара в верхней части витрины
            scaled_item_image = pg.transform.scale(item.image, (64, 64))  # При необходимости изменяем размер
            content_surface.blit(scaled_item_image, (image_x, image_y))

            # Позиции текста
            text_x_offset = 100
            text_start_y = image_y + 15

            # Отрисовка текста
            content_surface.blit(font_mini.render(item.name, True, BLACK), (text_x_offset, text_start_y))
            content_surface.blit(font_description.render(item.description, True, BLACK),
                                 (text_x_offset, text_start_y + 15))
            content_surface.blit(font_description.render(f"Количество: {item.account}", True, BLACK),
                                 (text_x_offset, text_start_y + 30))

            y_start += padding  # Переходим к позиции следующего элемента

        # Отображаем поверхность контента на экране с учетом прокрутки
        viewport_rect = pg.Rect(0, self.storage_scroll_offset, items_display_width, items_display_height)
        pg.draw.rect(screen, "Red", viewport_rect, 2)
        screen.blit(content_surface, (items_display_x + 10, items_display_y + 75), area=viewport_rect)

        if self.creater_toggle:
            self.windowGUIcreater = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 500, 570)
            screen.blit(self.windowGUIcreater, (storage_window_x + 250, storage_window_y + 20))

            self.windowGUIcreaterin = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64_white.png", 250,
                                                 250)
            self.windowmodel = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64_blue_whitegrid.png", 250,
                                          250)
            windowGUIcreaterin_x = 780
            windowGUIcreaterin_y = 407
            screen.blit(self.windowmodel, (storage_window_x + 280, storage_window_y + 50))
            screen.blit(self.windowGUIcreaterin, (windowGUIcreaterin_x, windowGUIcreaterin_y))

            screen.blit(self.Button_closed_image, (storage_window_x + 690, storage_window_y + 35))
            screen.blit(self.button_next_image, (storage_window_x + 475, storage_window_y + 245))
            screen.blit(self.button_after_image, (storage_window_x + 300, storage_window_y + 245))

            screen.blit(self.button_model_image, (storage_window_x + 345, storage_window_y + 13))
            screen.blit(font_mini.render(self.model_mode, True, BLACK), (storage_window_x + 360, storage_window_y + 53))

            screen.blit(self.button_accept_model_image, (storage_window_x + 570, storage_window_y + 500))
            screen.blit(font_mini.render("Finished", True, BLACK), (storage_window_x + 600, storage_window_y + 540))

            screen.blit(self.appearance_bar_image, (storage_window_x + 560, storage_window_y + 63))
            screen.blit(font_mini.render("Appearance", True, BLACK), (storage_window_x + 590, storage_window_y + 103))
            screen.blit(self.management_mechanisms_bar_image, (storage_window_x + 550, storage_window_y + 163))
            screen.blit(font_mini.render("Management mechanisms", True, BLACK), (storage_window_x + 555, storage_window_y + 203))
            screen.blit(self.transmission_bar_image, (storage_window_x + 560, storage_window_y + 263))
            screen.blit(font_mini.render("Transmission", True, BLACK), (storage_window_x + 590, storage_window_y + 303))
            screen.blit(self.salon_bar_image, (storage_window_x + 560, storage_window_y + 363))
            screen.blit(font_mini.render("Salon", True, BLACK), (storage_window_x + 610, storage_window_y + 403))

            for model in self.model:
                if model.category == self.model_mode:
                    screen.blit(model.image, (storage_window_x + 330, storage_window_y + 82))
                    screen.blit(font.render("Specifications", True, BLACK),
                                (windowGUIcreaterin_x + 20, windowGUIcreaterin_y + 20))
                    screen.blit(font_mini.render(f'Speed: {model.speed}km/h', True, BLACK),
                                (windowGUIcreaterin_x + 25, windowGUIcreaterin_y + 60))
                    screen.blit(font_mini.render(f'Quality: {model.quality}%', True, BLACK),
                                (windowGUIcreaterin_x + 25, windowGUIcreaterin_y + 75))
                    screen.blit(font_mini.render(f'Power: {model.power} horse/power', True, BLACK),
                                (windowGUIcreaterin_x + 25, windowGUIcreaterin_y + 90))
                    screen.blit(font_mini.render(f'Production cost: {model.production_cost} units', True, BLACK),
                                (windowGUIcreaterin_x + 25, windowGUIcreaterin_y + 105))
                    screen.blit(font_mini.render(f'Base price: {model.base_price}$', True, BLACK),
                                (windowGUIcreaterin_x + 25, windowGUIcreaterin_y + 120))

    def toggle_finance_window(self):
        if not self.show_finance_window:
            self.show_finance_window = True
            self.show_storage_window = False
            self.show_orders_window = False
            self.show_shop_window = False
            for button in self.reload_buttons:
                button.rect.topleft = (-100, -100)
        elif self.show_finance_window:
            self.show_finance_window = not self.show_finance_window

    def draw_finance_window(self):
        self.windowGUIFinace = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64.png", 650, 500)
        self.windowGUIFinacein = load_image("Game_ind/GUI/Base_GUI/window_GUI/window_gui_64x64_white.png", 550, 350)
        screen.blit(self.windowGUIFinace, (420, 97))

        screen.blit(self.windowGUIFinacein, (470, 130))

        screen.blit(self.occupy_button_image, (470, 478))
        screen.blit(font_medium.render(self.occupy_button_text, True, BLACK), (500, 538))

        screen.blit(self.give_button_image, (820, 478))
        screen.blit(font_medium.render(self.give_button_text, True, BLACK), (860, 538))

        screen.blit(self.credit_button_image, (683, 478))
        screen.blit(font_medium.render(str(self.credit) + "$", True, BLACK), (710, 538))

        self.expenses_full_text = f"All expenses: {self.expenses_full}"
        self.expenses_of_buy_item_text = f"Purchase of items: {self.expenses_of_buy_item}"
        self.expenses_dont_orders_text = f"Unfulfilled orders: {self.expenses_dont_orders}"
        self.payment_of_credit_text = f"Payment of credit: {self.payment_of_credit}"

        screen.blit(font_medium.render(self.expenses_full_text, True, BLACK), (530, 160))
        screen.blit(font_medium.render(self.expenses_of_buy_item_text, True, BLACK), (535, 185))
        screen.blit(font_medium.render(self.expenses_dont_orders_text, True, BLACK), (535, 210))
        screen.blit(font_medium.render(self.payment_of_credit_text, True, BLACK), (535, 235))
        print(self.payment_of_credit)

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
        screen.blit(text_render(self.money), (screen_width / 15 + 30, 75))
        screen.blit(self.popularity_image, self.popularity_image_rect)
        screen.blit(text_render(str(self.popularity) + "%"), (screen_width / 15 + 30, 155))
        screen.blit(self.day_image, self.day_image_rect)
        screen.blit(text_render(str(self.day) + " " + "Days"), (screen_width / 15 + 30, 240))

        self.ButtonGuiOrder.draw(screen)
        self.ButtonGuiShop.draw(screen)
        self.ButtonGuiWarehouse.draw(screen)

        if self.show_orders_window:
            self.draw_orders_window()

        if self.show_shop_window:
            self.draw_shop_window(mode=self.shop_mode)

        if self.show_storage_window:
            self.draw_storage_window()

        if self.show_finance_window:
            self.draw_finance_window()

        if self.selected_order:
            # Загрузка и отрисовка окна информации о заказе

            screen.blit(self.info_window_image, (self.info_window_x, self.info_window_y))
            screen.blit(self.accept_order_image, (self.info_window_x + 20, self.info_window_y + 328))
            screen.blit(self.reject_order_image, (self.info_window_x + 140, self.info_window_y + 328))
            self.accept_button_rect = get_non_transparent_rect(self.accept_order_image).move(self.info_window_x + 20,
                                                                                             self.info_window_y + 328)

            self.reject_button_rect = get_non_transparent_rect(self.reject_order_image).move(self.info_window_x + 140,
                                                                                             self.info_window_y + 328)
            # Отрисовка текста описания заказа
            description_text = font_mini.render(self.selected_order.description, True, WHITE)

            info_text_x = self.info_window_x + 30  # Небольшой отступ от края окна информации
            info_text_y = self.info_window_y + 200  # Небольшой отступ от края окна информации
            # screen.blit(description_text, (info_text_x, info_text_y))
            self.draw_description(self.selected_order.description, font_mini, screen, info_text_x, info_text_y,
                                  self.info_window_width - 60)  # Уменьшить ширину для отступов
            screen.blit(font_mini.render(self.selected_order.name, True, WHITE), (100, 140))
            screen.blit(font_mini.render(self.selected_order.surname, True, WHITE), (350, 140))
            screen.blit(font_mini.render("Accept", True, WHITE), (self.info_window_x + 46, self.info_window_y + 368))
            screen.blit(font_mini.render("Reject", True, WHITE), (self.info_window_x + 168, self.info_window_y + 368))

        # Смещение rect на позицию изображения
        rect_with_offset = self.example_image_rect.move(100, 100)


# Игровой цикл
game = Game()
running = True
while running:
    mouse_pos = pg.mouse.get_pos()  # Получаем текущую позицию курсора
    # print(mouse_pos)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Обработка событий (например, нажатие кнопок)
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = pg.mouse.get_pressed()
            if mouse_pressed[0] or mouse_pressed[2]:
                if game.selected_order and not game.selected_order.rect.collidepoint(
                        event.pos) and not game.accept_button_rect.collidepoint(
                        event.pos) and not game.reject_button_rect.collidepoint(event.pos):
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
                    if game.appearance_button_rect.collidepoint(event.pos):
                        game.shop_mode = "appearance"

                    if game.management_mechanisms_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "management mechanisms"

                    if game.salon_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "salon"

                    if game.transmission_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "transmission"

                    for item in game.items_all:
                        pg.draw.rect(screen, "Red", item.rect, 2)
                        if item.rect.collidepoint(event.pos):
                            if game.money >= item.price:
                                game.money -= item.price
                                game.expenses_of_buy_item += item.price
                                game.expenses_full += item.price
                                item.account += 1
                                print(item.name)
                                break
                        elif game.in_storage_rect.collidepoint(event.pos) and mouse_pressed[1]:
                            if game.money >= item.price * 5:
                                game.money -= item.price * 5
                                game.expenses_of_buy_item += item.price * 5
                                game.expenses_full += item.price * 5
                                item.account += 5
                                print(item.name)
                                break

                if game.show_shop_window:
                    if game.appearance_button_rect.collidepoint(event.pos):
                        game.shop_mode = "appearance"

                    if game.management_mechanisms_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "management mechanisms"

                    if game.salon_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "salon"

                    if game.transmission_tab_rect.collidepoint(event.pos):
                        game.shop_mode = "transmission"

                if game.show_storage_window:
                    if game.appearance_button_rect.collidepoint(event.pos):
                        if game.storage_filter_mode == "":
                            game.storage_filter_mode = "appearance"
                            game.storage_scroll_offset = 0
                        else:
                            game.storage_filter_mode = ""
                            game.storage_scroll_offset = 0

                    elif game.management_mechanisms_tab_rect.collidepoint(event.pos):
                        if game.storage_filter_mode == "":
                            game.storage_filter_mode = "management mechanisms"
                            game.storage_scroll_offset = 0
                        else:
                            game.storage_filter_mode = ""
                            game.storage_scroll_offset = 0

                    elif game.salon_tab_rect.collidepoint(event.pos):
                        if game.storage_filter_mode == "":
                            game.storage_filter_mode = "salon"
                            game.storage_scroll_offset = 0
                        else:
                            game.storage_filter_mode = ""
                            game.storage_scroll_offset = 0

                    elif game.transmission_tab_rect.collidepoint(event.pos):
                        if game.storage_filter_mode == "":
                            game.storage_filter_mode = "transmission"
                            game.storage_scroll_offset = 0
                        else:
                            game.storage_filter_mode = ""
                            game.storage_scroll_offset = 0

                if game.show_storage_window:
                    if game.Button_closed_rect.collidepoint(event.pos):
                        game.creater_toggle = not game.creater_toggle

                    elif game.creater_button_rect.collidepoint(event.pos):
                        game.creater_toggle = not game.creater_toggle

                    elif game.button_next_rect.collidepoint(event.pos):
                        if game.model_mode == "Light model":
                            game.model_mode = "Medium model"
                            break
                        elif game.model_mode == "Medium model":
                            game.model_mode = "Heavy model"
                            break

                    elif game.button_after_rect.collidepoint(event.pos):
                        if game.model_mode == "Medium model":
                            game.model_mode = "Light model"
                            break
                        elif game.model_mode == "Heavy model":
                            game.model_mode = "Medium model"
                            break

                if event.type == pg.MOUSEBUTTONDOWN and game.storage_button_rect.collidepoint(event.pos):
                    mouse_pressed = pg.mouse.get_pressed()
                    if mouse_pressed[0]:
                        game.ButtonGuiWarehouse.is_clicked(event)
                        if game.creater_toggle:
                            game.creater_toggle = False

                if event.type == pg.MOUSEBUTTONDOWN and game.finance_button_rect.collidepoint(event.pos):
                    mouse_pressed = pg.mouse.get_pressed()
                    if mouse_pressed[0]:
                        game.ButtonGuiFinance.is_clicked(event)

                if game.show_finance_window:
                    if game.occupy_button_rect.collidepoint(event.pos):
                        if game.credit >= 1000 and game.credit_mode and game.money >= 1000:
                            game.money -= 1000
                            game.credit -= 1000
                            print(game.credit)
                            if game.credit == 0:
                                game.credit_mode = False

                    elif game.give_button_rect.collidepoint(event.pos):
                        if game.credit < 15000:
                            game.credit_mode = True
                            game.credit += 1000
                            game.money += 1000
                            print(game.credit)

                if game.accept_button_rect.collidepoint(event.pos):
                    if game.money >= 500:
                        game.money -= 500

        if event.type == DAY_EVENT:
            game.day += 1
            if game.credit_mode and int(game.day / 2) == float(game.day / 2):
                game.money -= int(game.credit // game.percent_for_credit * 3)
                game.expenses_full += int(game.credit // game.percent_for_credit * 3)
                game.payment_of_credit += int(game.credit // game.percent_for_credit * 3)
                print(game.payment_of_credit)
                print(game.credit // game.percent_for_credit * 3)

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

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:  # Прокрутка вверх
                if game.show_storage_window:
                    game.storage_scroll_offset = max(game.storage_scroll_offset - game.storage_scroll_speed, 0)
            if event.button == 5:  # Прокрутка вниз
                if game.show_storage_window:
                    game.storage_scroll_offset = min(game.storage_scroll_offset + game.storage_scroll_speed,
                                                     game.storage_max_scroll)

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

    for order in game.orders_images:
        order.check_hover(mouse_pos)  # Проверяем, наведен ли курсор на кнопку
        order.update()
        order.draw(screen)

    for button in game.main_buttons:
        button.check_hover(mouse_pos)  # Проверяем, наведен ли курсор на кнопку
        button.update()
        button.draw(screen)

    if game.level_buy_storage_rect.collidepoint(mouse_pos):

        if alfa_type < 255:
            alfa_type += fade_speed
            if alfa_type > 255:
                alfa_type = 255
    else:
        if alfa_type > 0:
            alfa_type -= fade_speed

        if alfa_type < 0:
            alfa_type = 0
    # Отрисовка остальных элементов игры
    game.draw()
    game.description_level_storage_image.set_alpha(alfa_type)

    # Обновление экрана
    pg.display.flip()

    # Время кадра
    clock.tick(FPS)

# Завершение PyGame
pg.quit()
sys.exit()

# сделать вкладки магазина - доделать полностью функционал магазина. Начать делать концепт склада
