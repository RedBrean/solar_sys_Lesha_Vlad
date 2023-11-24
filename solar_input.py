# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject

from solar_main import output_scale

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star": 
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    l = line.split()
    star.color=str(l[2])
    star.R=float(l[1])
    star.m=float(l[3])
    star.x=float(l[4])
    star.y=float(l[5])
    star.Vx=float(l[6])
    star.Vy=float(l[7])
    # DONTFIXME: probebly done yet

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    l = line.split()
    planet.R=float(l[1])
    planet.color=str(l[2])
    planet.m=float(l[3])
    planet.x=float(l[4])
    planet.y=float(l[5])
    planet.Vx=float(l[6])
    planet.Vy=float(l[7])
    # DONTFIXME: probebly done yet

nextWritedTime = 0 #sorry...

def write_space_objects_data_to_file(output_filename, space_objects, physical_time):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    if(physical_time < 500):
        out_file = open(output_filename, "w")
        out_file.write("Start writing\n")
        return
    with open(output_filename, 'a') as out_file:

        years = int(physical_time) // 31536000
        days = int(physical_time) % 31536000 // 86400
        hours = int(physical_time) % 86400 // 3600
        minutes = int(physical_time) % 3600 // 60
        seconds = int(physical_time) % 60

        hours = str(hours)
        minutes = str(minutes)
        seconds = str(seconds)
        hours = "0"*(2-len(hours)) + hours
        minutes = "0"*(2-len(minutes)) + minutes
        seconds = "0"*(2-len(seconds)) + seconds

        global nextWritedTime, output_scale

        if(len(space_objects) == 0 or physical_time < nextWritedTime):
            return

        nextWritedTime += output_scale

        out_file.write(f"Date: {years} y, {days} d, time: {hours}:{minutes}:{seconds}\n")
        for obj in space_objects:
            out_file.write(f"Type : {obj.obj.type}, R = {obj.obj.R}, color = {obj.obj.color}, x = {obj.obj.x}, y = {obj.obj.y}, vx = {obj.obj.Vx}, vy = {obj.obj.Vy}\n")
        out_file.write("\n-----------------------------------------------\n")
        

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
# нет

if __name__ == "__main__":
    print("This module is not for direct call!")
