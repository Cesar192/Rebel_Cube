try:
	from colorama import Fore #Испорт цвет текста
except ImportError:
	print("Ошибка, установите модуль colorama")
	quit()
try:
	from progressbar import ProgressBar
except ImportError:
	print("Ошибка, установите модуль progressbar")
	quit()
try:
	from getch import getch #испорт нажатия без Enter
except ImportError:
	print("Ошибка, установите модуль getch")
	quit()
try:
	from mapper import Mapper
except ImportError:
	print("Не найден файл mapper.py")
	quit()
	
from os import system as st
import sqlite3
from time import sleep
	
class Cube:
	def __init__(self):
		self.map = None #Карта
		self.level = 0
		self.level_talk_menu = 1
		self.completed_level = 0 #пройденные уровни, будут засчитаны как новый уровень
		self.moves = 0
		self.score = 0
		self.microscheme = 0
		# ------Движение бота-------
		#easy_bot----
		self.move_left = True
		self.move_down = False
		self.move_right = False
		self.move_up = False
		#--------
		#Босс атаки
		self.activ = True
		self.blaster = False
		#Здоровье босса
		self.health_boss = 18
		#Вещи для атаки босса
		self.give_1 = False
		self.give_2 = False
		self.give_3 = False
		self.give_4 = False
		self.give_5 = False
		self.give_6 = False
		self.give_7 = False
		self.give_8 = False
		self.give_9 = False
		self.spawn_object = True
		#--------Босс 2-------------
		self.health_boss_two = 25
		self.spawn_boss = False
		self.activ_boss = True
		self.object_spawn = True
		self.spawn_two_boss = False
		self.mortire = False
		self.give_11 = False
		self.give_21 = False
		self.give_31 = False
		self.give_41 = False
		self.give_51 = False
		self.first_blas = 1
		self.second_blas = 1
		self.third_blas = 1
		self.fourth_blas = 1
		self.y_first_blas = 1
		self.y_second_blas = 1
		self.y_third_blas = 1
		self.y_fourth_blas = 1
		#Исчезают после окончания
		# --------------------------
		self.new_dialog_menu = False
		self.new_dialog_menu_two = False
		self.new_dialog_menu_three = False
		self.new_dialog_menu_four = False
		self.new_dialog_menu_five = False
		#---------------------------
		#Враг
		self.event_fire_y_one = 1
		self.event_fire_x_two = 1
		#---------------------------
		#Skills---------------------
		self.PowerSkill = False
		self.JumpSkill = False
		self.SpeedSkill = False
		self.KanatSkill = False
		self.Skill_one = False
		self.Skill_two = False
		self.Skill_three = False
		self.Skill_four = False
		#---------------------------
		self.theasures_one = False
		self.theasures_two = False
		#---------------------Враг--
		self.fired_sm = 1
		self.fired_sm_one = 1
		self.fired_sm_one_one = 1
		self.fired_sm_one_one_one = 1
		self.fired_sm_two = 1
		#---------------------------
		
		#Враг Лазер-----------------
		self.lazer_smash = False
		self.clear_smash = False
		#Сохранения
		self.Save_db = sqlite3.connect("DataBase.sqlite3")
		try:
			self.cursor = self.Save_db.cursor()
			self.cursor.execute("""CREATE TABLE SaveData (name_save text, level integer, score integer, PS numeric, JS numeric, SS numeric, KS numeric, talk_level integer, TM numeric, LTM numeric)""")
			self.Save_db.commit()
		except:
			pass
		#---------------------------
	__slots__ = ["map", "level", "level_talk_menu", "new_dialog_menu", "new_dialog_menu_two", "completed_level", "move_left", "move_right", "move_down", "move_up", "moves", "blaster", "health_boss", "activ", "give_1", "give_2", "give_3", "give_4", "give_5", "give_6", "give_7", "give_8", "give_9", "score", "microscheme", "event_fire_y_one", "event_fire_x_two", "spawn_object", "PowerSkill", "JumpSkill", "theasures_one", "fired_sm", "fired_sm_two", "SpeedSkill", "KanatSkill", "Save_db", "cursor", "theasures_two", "new_dialog_menu_three", "new_dialog_menu_four", "new_dialog_menu_five", "Skill_one", "Skill_two", "Skill_three", "Skill_four", "fired_sm_one", "fired_sm_one_one", "fired_sm_one_one_one", "lazer_smash", "clear_smash", "health_boss_two", "spawn_boss", "activ_boss", "mortire", "give_11", "give_21", "give_31", "give_41", "give_51", "first_blas", "second_blas", "third_blas", "fourth_blas", "y_first_blas", "y_second_blas", "y_third_blas", "y_fourth_blas", "spawn_two_boss", "spawn_object", "object_spawn"] #Запрет на использование экземпляров внутри и снаружиw класса для сокращения потребления ОЗУ
	
	def __str__(self):
		return "object ready for run" #Запуск объектов без экземпляра
		
	def __repr__(self):
		return "run object by main" #Запуск объектов без экземпляра в новом объекте
	
	def begin(self):
		horde = 1
		self.map = Mapper.begin_map()
		move = ""
		
		while True:
		#	object.controller(self.map, move)
			using = object.controller(self.map, move, self.level)
			object.render_map(self.map)
			if using == True:
				object.event_talk()
			move = getch()
	
		
		
	@staticmethod
	def controller(map, move, level): #управление
		for y in range(len(map)): #по линий
			for x in range(len(map[y])): #по деталям линий
				if map[y][x] == "◼":
					move = move.lower()
					try:
						if move == "a":
							if map[y][0] != "◼":
								if object.Skill_three == True:								
									if map[y][x-2] == " ":
										map[y][x-2] = "◼"	
										map[y][x] = " "
										return
								elif map[y][x-1] == " ":
									map[y][x-1] = "◼"
									map[y][x] = " "
									object.moves += 1
									return
								
								elif map[y][x-1] != " " and map[y][x-2] == " " and object.Skill_two == True and map[y][x-1] != "E" and map[y][x-1] != "M":
									map[y][x-2] = "◼"
									map[y][x] = " "
									return
									
								elif map[y][x-1] == "$":
									map[y][x-1] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.score += 1
									return
								elif map[y][x-1] == "@" and map[y][x-2] == " " and map[y][0] != "@":
									map[y][x-1] = "◼"
									map[y][x-2] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y][x-1] == "@" and map[y][x-2] == "@" and map[y][x-3] == " " and map[y][0] != "@" and object.Skill_one == True:
									map[y][x-1] = "◼"
									map[y][x-2] = "@"
									map[y][x-3] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y][x-1] == "m":
									map[y][x-1] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.microscheme += 1
									return
								elif map[y][x-1] == "a":
									map[y][x-1] = "◼"
									map[y][x] = " "
									return
									
								elif map[y][x-1] == "M":
									if object.one_quest_check(map):	
										object.completed_level += 1
										object.level_talk_menu = 1
										object.moves = 0
										level_looce = object.completed_level
										object.completed_level = 0
										object.main(level_looce)
										
								elif map[y][x-1] == "E":
									if object.one_quest_check(map):				
										object.completed_level += 1
										object.moves = 0
										object.game(object.level+object.completed_level)
										
							else:
								pass
						elif move == "l" and object.Skill_four == True:
							to_pull = input("[<- A] [D ->] [^ W] [√ S]").lower()
							if to_pull == "a":
								if map[y][x-1] == " " and map[y][x-2] == "@":
									map[y][x-1] = "@"
									map[y][x-2] = " "
									return
							elif to_pull == "d":
								if map[y][x+1] == " " and map[y][x+2] == "@":
									map[y][x+1] = "@"
									map[y][x+2] = " "
									return
							elif to_pull == "w":
								if map[y-1][x] == " " and map[y-2][x] == "@":
									map[y-1][x] = "@"
									map[y-2][x] = " "
									return
							elif to_pull == "s":
								if map[y+1][x] == " " and map[y+2][x] == "@":
									map[y+1][x] = "@"
									map[y+2][x] = " "
									return
							else:
								pass
						elif move == "k":
							if object.PowerSkill == True and object.Skill_one == False:	 
								print("1)Супер Сила [Неактивен]")
							elif object.PowerSkill == True and object.Skill_one == True:	 
								print("1)Супер Сила [Активен]")
							if object.JumpSkill == True and object.Skill_two == False:
								print("2)Прыжок [Неактивен]")
							elif object.JumpSkill == True and object.Skill_two == True:
								print("2)Прыжок [Активен]")
							if object.SpeedSkill == True and object.Skill_three == False:
								print("3)Супер Скорость [Неактивен]")
							elif object.SpeedSkill == True and object.Skill_three == True:
								print("3)Супер Скорость [Активен]")
							if object.KanatSkill == True and object.Skill_four == False:
								print("4)Гарпун [Неактивен]")
							elif object.KanatSkill == True and object.Skill_four == True:
								print("4)Гарпун [Активен]")	
							choose = input("Выбор:")
							if choose == "1":
								if object.PowerSkill == True and object.Skill_one == False:
									object.Skill_one = True
								elif object.PowerSkill == True and object.Skill_one == True:
									object.Skill_one = False
							elif choose == "2":
								if object.JumpSkill == True and object.Skill_two == False:
									object.Skill_two = True
								elif object.JumpSkill == True and object.Skill_two == True:
									object.Skill_two = False
							elif choose == "3":
								if object.SpeedSkill == True and object.Skill_three == False:
									object.Skill_three = True
								elif object.SpeedSkill == True and object.Skill_three == True:
									object.Skill_three = False
							elif choose == "4":
								if object.KanatSkill == True and object.Skill_four == False:
									object.Skill_four = True
								elif object.KanatSkill == True and object.Skill_four == True:
									object.Skill_four = False
							else:
								pass
									
						elif move == "d":
							if map[y][-1] != "◼":
								if object.Skill_three == True:								
									if map[y][x+2] == " ":
										map[y][x+2] = "◼"	
										map[y][x] = " "
										return
											
								elif map[y][x+1] == " ":
									map[y][x+1] = "◼"
									map[y][x] = " "
									object.moves += 1
									return
									
										
								elif map[y][x+1] == "$":
									map[y][x+1] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.score += 1
									return
								elif (map[y][x+1] == "#" or map[y][x+1] == "—" or map[y][x+1] == "|") and map[y][x+2] == " " and object.Skill_two == True:
									map[y][x+2] = "◼"
									map[y][x] = " "
									return
								elif map[y][x+1] == "@" and map[y][x+2] == " " and map[y][-1] != "@":
									map[y][x+1] = "◼"
									map[y][x+2] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y][x+1] == "@" and map[y][x+2] == "@" and map[y][x+3] == " " and map[y][-1] != "@" and object.Skill_one == True:
									map[y][x+1] = "◼"
									map[y][x+2] = "@"
									map[y][x+3] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y][x+1] == "m":
									map[y][x+1] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.microscheme += 1
									return
								elif map[y][x+1] == "a":
									map[y][x+1] = "◼"
									map[y][x] = " "
									return
									
								elif map[y][x+1] == "M":
									if object.one_quest_check(map):	
										object.completed_level += 1
										object.level_talk_menu = 1
										object.moves = 0
										level_looce = object.completed_level
										object.completed_level = 0
										object.main(level_looce)
										
								elif map[y][x+1] == "E":
									if object.one_quest_check(map):
										object.completed_level += 1
										object.moves = 0
										object.game(object.level+object.completed_level)
							else:
								pass
							
						elif move == "w":
							if map[0][x] != "◼":
								if object.Skill_three == True:								
									if map[y-2][x] == " ":
										map[y-2][x] = "◼"	
										map[y][x] = " "
										return
								elif map[y-1][x] == " ":
									map[y][x] = " "
									map[y-1][x] = "◼"
									object.moves += 1
									return
									
								elif map[y-1][x] != " " and map[y-2][x] == " " and object.Skill_two == True and map[y-1][x] != "E" and map[y-1][x] != "M":
									map[y-2][x] = "◼"
									map[y][x] = " "
									return
									
								elif map[y-1][x] == "$":
									map[y-1][x] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.score += 1
									return
								elif map[y-1][x] == "@" and map[y-2][x] == " " and map[0][x] != "@":
									map[y-1][x] = "◼"
									map[y-2][x] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y-1][x] == "@" and map[y-2][x] == "@" and map[y-3][x] == " " and map[0][x] != "@" and object.Skill_one == True:
									map[y-1][x] = "◼"
									map[y-2][x] = "@"
									map[y-3][x] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y-1][x] == "m":
									map[y-1][x] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.microscheme += 1
									return
								elif map[y-1][x] == "a":
									map[y-1][x] = "◼"
									map[y][x] = " "
									return
									
								elif map[y-1][x] == "M":
									if object.one_quest_check(map):	
										object.completed_level += 1
										object.level_talk_menu = 1
										object.moves = 0				
										level_looce = object.completed_level
										object.completed_level = 0
										object.main(level_looce)
											
								elif map[y-1][x] == "E":
									if object.one_quest_check(map):
										object.completed_level += 1
										object.moves = 0
										object.game(object.level+object.completed_level)
							else:
								pass
								
						elif move == "s":
							if map[-1][x] != "◼":
								if object.Skill_three == True:								
									if map[y+2][x] == " ":
										map[y+2][x] = "◼"	
										map[y][x] = " "
										return
								elif map[y+1][x] == " ":
									map[y+1][x] = "◼"
									object.moves += 1
									map[y][x] = " "
									return
									
								elif map[y+1][x] != " " and map[y+2][x] == " " and object.Skill_two == True and map[y+1][x] != "E" and map[y+1][x] != "M":
									map[y+2][x] = "◼"
									map[y][x] = " "
									return
								elif map[y+1][x] == "$":
									map[y+1][x] = "◼"
									object.score += 1
									object.moves += 1
									map[y][x] = " "
									return
								
								elif map[y+1][x] == "@" and map[y+2][x] == " " and map[-1][x] != "@":
									map[y+1][x] = "◼"
									map[y+2][x] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y+1][x] == "@" and map[y+2][x] == "@" and map[y+3][x] == " " and map[-1][x] != "@" and object.Skill_one == True:
									map[y+1][x] = "◼"
									map[y+2][x] = "@"
									map[y+3][x] = "@"
									map[y][x] = " "
									object.moves += 1
									return
								elif map[y+1][x] == "m":
									map[y+1][x] = "◼"
									map[y][x] = " "
									object.moves += 1
									object.microscheme += 1
									return
								elif map[y+1][x] == "a":
									map[y+1][x] = "◼"
									map[y][x] = " "
									return
								elif map[y+1][x] == "M":
									if object.one_quest_check(map):	
										object.completed_level += 1
										object.moves = 0
										object.level_talk_menu = 1
										level_looce = object.completed_level
										object.completed_level = 0
										object.main(level_looce)
								elif map[y+1][x] == "E":
									if object.one_quest_check(map):
										object.completed_level += 1
										object.moves = 0
										object.game(object.level+object.completed_level)
							else:
								pass
								
						elif move == "e" and level == 0 and (map[y+1][x] == "G" or map[y-1][x] == "G" or map[y][x-1] == "G" or map[y][x+1] == "G"):
							object.eventer(object.begin_talk, map)
						#------------------
						elif move == "e" and level == 1 and (map[y+1][x] == "G" or map[y-1][x] == "G" or map[y][x-1] == "G" or map[y][x+1] == "G"):
							if object.level_talk_menu == 1:
								object.eventer(object.text_one, map)
							else:
								object.repeat_eventer(object.text_one_repeat, map)
						#----------------
						elif move == "e" and level == 11 and (map[y+1][x] == "G" or map[y-1][x] == "G" or map[y][x-1] == "G" or map[y][x+1] == "G"):
							if object.level_talk_menu == 1:
								object.eventer(object.text_two, map)
							else:
								object.repeat_eventer(object.text_two_repeat, map)
						#---------------
								
						elif move == "e" and level >= 1 and level <= 9 and (map[y+1][x] == "U" or map[y-1][x] == "U" or map[y][x-1] == "U" or map[y][x+1] == "U"):
						
							object.object_eventer(object.talk_with_thing, map)
						#------------------
						elif move == "e" and level >= 11 and (map[y+1][x] == "U" or map[y-1][x] == "U" or map[y][x-1] == "U" or map[y][x+1] == "U"):
							maps = Mapper.skills_map()
							object.skills(maps)
						#-------------------
						elif move == "e" and level == 1 and level <= 9 and (map[y+1][x] == "S" or map[y-1][x] == "S" or map[y][x-1] == "S" or map[y][x+1] == "S"):
							if object.new_dialog_menu == False:
								object.game(level)
							else:
								print("Сначала поговорите с Джорджем")
								sleep(2)
						elif move == "e" and level == 11 and (map[y+1][x] == "S" or map[y-1][x] == "S" or map[y][x-1] == "S" or map[y][x+1] == "S"):
							if object.new_dialog_menu_two == False:
								object.game(level)
							else:
								print("Поговорите с Джорджем")
						elif move == "e" and (map[y+1][x] == "[" or map[y-1][x] == "[" or map[y][x-1] == "[" or map[y][x+1] == "[" or map[y+1][x] == "]" or map[y-1][x] == "]" or map[y][x-1] == "]" or map[y][x+1] == "]"):
							object.theasure(object.level+object.completed_level)
							
						elif move == "e" and (map[y+1][x] == "C" or map[y-1][x] == "C" or map[y][x-1] == "C" or map[y][x+1] == "C"):						
							object.saves()
						object.moves += 1
					except IndexError:
				#	except Exception as e:
		#				input(f"Ошибка {e}")
						pass
						
	@staticmethod
	def saves():
		name = input("Введите имя сохранения: ")
		object.cursor.execute(f"INSERT INTO SaveData VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, object.level, object.score, object.PowerSkill, object.JumpSkill, object.SpeedSkill, object.KanatSkill, object.level_talk_menu, object.new_dialog_menu, object.new_dialog_menu_two))
		object.Save_db.commit()
		print(f"Сохранение с именем {name} сохранено")
		sleep(2)
		
	@staticmethod
	def one_quest_check(map):
		mas = []
		for y in range(len(map)):
			for x in range(len(map[y])): 
				if map[y][x] == "m":
					mas.append(True)
					
		if any(mas) == True:
			return False
		else:
			return True
			
	@staticmethod
	def theasure(level):
		try:
			if level == 14 and object.theasures_one == False:
				while True:
					print("То что летает долго не махая крыльями")
					response = input("Ответ: ").lower()
					if response == "альбатрос":
						print("В сундуке лежало 5 очков мастерства")
						input("Нажмите <Enter>")
						object.theasures_one = True
						object.score += 5
						break
					else:
						print("Неправильно")
						input("Нажмите <Enter>")
						break
			elif level == 17 and object.theasures_two == False:
				while True:
					print("Невидимое счастье")
					response = input("Ответ: ").lower()
					if response == "wifi":
						print("В сундуке лежало 5 очков мастерства")
						input("Нажмите <Enter>")
						object.theasures_two = True
						object.score += 5
						break
					else:
						print("Неправильно")
						input("Нажмите <Enter>")
						break
						
			else:
				print("Пусто")
				input("Нажмите <Enter>")
		
		except Exception as e:
			print("lol", e)
					
	@staticmethod					
	def eventer(text_func, map):
		for y in range(len(map)):
			for x in range(len(map[y])): 
				if map[y][x] == "◼":
					if map[y+1][x] == "G":
						text_func(map)
						object.level_talk_menu += 1
					elif map[y-1][x] == "G":
						text_func(map)
						object.level_talk_menu += 1
					elif map[y][x+1] == "G":
						text_func(map)
						object.level_talk_menu += 1
					elif map[y][x-1] == "G":
						text_func(map)
						object.level_talk_menu += 1
						
	@staticmethod
	def repeat_eventer(text_func, map):
		for y in range(len(map)):
			for x in range(len(map[y])): 
				if map[y][x] == "◼":
					if map[y+1][x] == "G":
						text_func()
					elif map[y-1][x] == "G":
						text_func()
					elif map[y][x+1] == "G":
						text_func()
					elif map[y][x-1] == "G":
						text_func()
						
	@staticmethod
	def object_eventer(text_func, map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "◼":
					if map[y+1][x] == "U":
						text_func()
					elif map[y-1][x] == "U":
						text_func()
					elif map[y][x+1] == "U":
						text_func()
					elif map[y][x-1] == "U":
						text_func()
						
	@staticmethod
	def func_unit(map):
		count_bot = 1
		count_fire_blasters = 1
		count_fire_turell = 1
		count_fire_super_turell = 1
		count_lazer = 1
		for y in range(len(map)):
			for x in range(len(map[y])):
				try:
					if map[y][x] == "°":
						object.door(map)
					if map[y][x] == "•" and count_bot != 0:
						object.easy_bot(map)
						count_bot -= 1
					if map[y][x] == "±" and count_fire_blasters != 0:
						object.blasters(map)
						object.blasters_two(map)
						count_fire_blasters -= 1
					if map[y][x] == "*" and map[y][x+4] == "*":
						object.doors(map)
					if map[y][x] == "T" and count_fire_turell != 0:
						object.Turell(map)
						count_fire_turell -= 1
					if map[y][x] == "S" and count_fire_super_turell != 0:
						object.SuperTurell(map)
						count_fire_super_turell -= 1
					if map[y][x] == "L":
						object.ClearLazer(map)
					if map[y][x] == "L" and count_lazer != 0:
						object.Lazer(map)
						count_lazer -= 1
				except IndexError:
					pass
					
	@staticmethod
	def Lazer(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "L":
						if object.moves % 3 == 0 and object.lazer_smash == False and object.clear_smash == False:
							for laser in range(0, x):
								map[y][laser] = "—"
							object.lazer_smash = True
							object.clear_smash = True
	@staticmethod
	def ClearLazer(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "L":
					if map[y][x-1] == "—" and object.lazer_smash == True and object.clear_smash == True:
						for laser in range(0, x):
							map[y][laser] = " "
						object.lazer_smash = False
						object.clear_smash = False
	@staticmethod
	def Turell(map):
		first_turell = True
		next_turell = False
		next_second_turell = False
		next_triple_turell = False
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "T" and next_turell == False and first_turell == True:
					if map[y][x-object.fired_sm] == " " or map[y][x-object.fired_sm] == "◼":
						map[y][x-object.fired_sm] = "–"
						if object.fired_sm == 1:
							pass
						else:
							map[y][x-(object.fired_sm-1)] = " "
						object.fired_sm += 1
					#	return
						next_turell = True
						first_turell = False
					else:
						map[y][x-(object.fired_sm-1)] = " "
						object.fired_sm = 1
						next_turell = True
						first_turell = False
					#	return
				elif map[y][x] == "T" and next_turell == True and first_turell == False:	
					if map[y][x-object.fired_sm_one] == " " or map[y][x-object.fired_sm_one] == "◼":
						map[y][x-object.fired_sm_one] = "–"
						if object.fired_sm_one == 1:
							pass
						else:
							map[y][x-(object.fired_sm_one-1)] = " "
						object.fired_sm_one += 1
						next_second_turell = True
						next_turell = False
						
					else:
						map[y][x-(object.fired_sm_one-1)] = " "
						object.fired_sm_one = 1
						next_second_turell = True
						next_turell = False
						
				elif map[y][x] == "T" and next_second_turell == True and next_turell == False:
					if map[y][x-object.fired_sm_one_one] == " " or map[y][x-object.fired_sm_one_one] == "◼":
						map[y][x-object.fired_sm_one_one] = "–"
						if object.fired_sm_one_one == 1:
							pass
						else:
							map[y][x-(object.fired_sm_one_one-1)] = " "
						object.fired_sm_one_one += 1
						next_triple_turell = True
						next_second_turell = False
					else:
						map[y][x-(object.fired_sm_one_one-1)] = " "
						object.fired_sm_one_one = 1
						next_triple_turell = True
						next_second_turell = False
						
				elif map[y][x] == "T" and next_triple_turell == True and next_second_turell == False:	
					if map[y][x-object.fired_sm_one_one_one] == " " or map[y][x-object.fired_sm_one_one_one] == "◼":
						map[y][x-object.fired_sm_one_one_one] = "–"
						if object.fired_sm_one_one_one == 1:
							pass
						else:
							map[y][x-(object.fired_sm_one_one_one-1)] = " "
						object.fired_sm_one_one_one += 1
						return		
					else:
						map[y][x-(object.fired_sm_one_one_one-1)] = " "
						object.fired_sm_one_one_one = 1
						return
						
						
	@staticmethod
	def SuperTurell(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "S":
					if map[y][x-object.fired_sm_two] == " " or map[y][x-object.fired_sm_two] == "◼" or map[y][x-object.fired_sm_two] == "@":
						map[y][x-object.fired_sm_two] = "–"
						if object.fired_sm_two == 1:
							pass
						else:
							map[y][x-(object.fired_sm_two-1)] = " "
						object.fired_sm_two += 1
						return
					else:
						map[y][x-(object.fired_sm_two-1)] = " "
						object.fired_sm_two = 1
						return
						
						
	@staticmethod				
	def doors(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "*" and map[y][x+4] == "*":
					if ((map[y][x-1] == "@" or map[y][x+1] == "@" or map[y-1][x] == "@") and (map[y][x+3] == "@" or map[y][x+5] == "@" or map[y-1][x+4])):
						if map[y+1][x+1] == " " or map[y+1][x+1] == "◼" or map[y+1][x+1] == "@":
							pass
						else:
							map[y+1][x+1] = " "
							map[y+1][x+2] = " "
							map[y+1][x+3] = " "
							return
					else:
						map[y+1][x+1] = "—"
						map[y+1][x+2] = "—"
						map[y+1][x+3] = "—"
						return
							
	@staticmethod
	def check_hero(map):
		mas = []
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "◼":
					mas.append(True)
		if any(mas) == True:
			pass
		else:
			print("Вы проиграли")
			sleep(2)
			object.moves = 0	
			object.completed_level = 0
			object.microscheme = 0
			if object.level >= 1 and object.level <= 10:
				object.level = 1
			elif object.level >= 11 and object.level <= 20:
				object.level = 11
			elif object.level >= 21 and object.level <= 30:
				object.level = 21
			elif object.level >= 31 and object.level <= 40:
				object.level = 31
				
			object.activ = True
			object.blaster = False
			object.health_boss = 18
			object.give_1 = False
			object.give_2 = False
			object.give_3 = False
			object.give_4 = False
			object.give_5 = False
			object.give_6 = False
			object.give_7 = False
			object.give_8 = False
			object.give_9 = False
			object.main(0)
			
	@staticmethod
	def skills(map):
		while True:
			st("clear")
			#for image in Mapper.skills_map():
			for image in map:	
				print("".join(image))
			print(f"Умения: {object.score}$")
			if object.PowerSkill != True:
				print("1)Супер сила 🔓 [20$]")
			elif object.PowerSkill == True:
				print("1)Супер сила Исследовано")
			if object.JumpSkill != True and object.PowerSkill != True:
				print("2)Доступ Закрыт 🔒")
			elif object.JumpSkill != True and object.PowerSkill == True:
				print("2)Прыжок 🔓 [38$]")
			elif object.JumpSkill == True:
				print("2)Прыжок Исследовано")
			if object.SpeedSkill != True and object.JumpSkill != True:
				print("3)Доступ Закрыт 🔒")
			elif object.SpeedSkill != True and object.JumpSkill == True:
				print("3)Скорость 🔓 [43$]")
			elif object.SpeedSkill == True:
				print("3)Скорость Исследовано")
			if object.KanatSkill != True and object.SpeedSkill != True:
				print("4)Доступ Закрыт 🔒")
			elif object.KanatSkill != True and object.SpeedSkill == True:
				print("4)Гарпун 🔓 [50$]")
			elif object.KanatSkill == True:
				print("4)Гарпун Исследовано")
			upgrade = input("[Q]:").lower()
			if upgrade == "q":
				break
			elif upgrade == "1" and object.PowerSkill != True:
				if object.score >= 20:
					print("Навык исследован")
					print("Нажмите K для вызова меню")
					object.score -= 20
					object.PowerSkill = True
					sleep(2)
				else:
					print("Недостаточно очков")
					sleep(1)
			elif upgrade == "2" and object.PowerSkill == True and object.JumpSkill !=  True:
				if object.score >= 38:
					print("Навык исследован")
					print("Нажмите K для вызова меню")
					object.score -= 38
					object.JumpSkill = True
					sleep(2)
				else:
					print("Недостаточно очков")
			elif upgrade == "3" and object.JumpSkill == True and object.SpeedSkill != True:
				if object.score >= 43:
					print("Навык исследован")
					print("Нажмите K для вызова меню")
					object.score -= 43
					object.SpeedSkill = True
					sleep(2)
				else:
					print("Недостаточно очков")
			elif upgrade == "4" and object.SpeedSkill == True and object.KanatSkill != True:
				if object.score >= 50:
					print("Навык исследован")
					print("Нажмите K для вызова меню")
					print("Для вызова гарпуна нажмите кнопку L")
					object.score -= 50
					object.KanatSkill = True
					input("Нажмите <Enter>")
				else:
					print("Недостаточно очков")
					
	@staticmethod
	def door(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "°":
					if map[y][x-1] == "@" or map[y+1][x] == "@" or map[y][x+1] == "@" or map[y-1][x] == "@":
						if map[y+1][x+1] == " " or map[y+1][x+1] == "◼" or map[y+1][x+1] == "@":
							pass
						else:
							map[y+1][x+1] = " "
							map[y+2][x+1] = " " 
							map[y+3][x+1] = " "
					else:
						map[y+1][x+1] = "|"
						map[y+2][x+1] = "|" 
						map[y+3][x+1] = "|"
	@staticmethod
	def blasters(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "±":
					if map[y-object.event_fire_y_one][x] == " " or map[y-object.event_fire_y_one][x] == "◼":
						map[y-object.event_fire_y_one][x] = "|"
						if object.event_fire_y_one == 1:
							pass
						else:
							map[y-(object.event_fire_y_one-1)][x] = " "
						object.event_fire_y_one += 1
						return
					else:
						map[y-(object.event_fire_y_one-1)][x] = " "
						object.event_fire_y_one = 1
						return
	@staticmethod
	def blasters_two(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "±":
					if map[y][x-object.event_fire_x_two] == " " or map[y][x-object.event_fire_x_two] == "◼":
						map[y][x-object.event_fire_x_two] = "–"
						if object.event_fire_x_two == 1:
							pass
						else:
							map[y][x-(object.event_fire_x_two-1)] = " "
						object.event_fire_x_two += 1
						return
					else:
						map[y][x-(object.event_fire_x_two-1)] = " "
						object.event_fire_x_two = 1
						return
							
	@staticmethod
	def easy_bot(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "•" and object.move_left == True:
					map[y][x-7] = "•"
					map[y][x] = " "
					object.move_left = False
					object.move_down = True
					return
						
				elif map[y][x] == "•" and object.move_down == True:
					map[y+7][x] = "•"
					map[y][x] = " "
					object.move_down = False
					object.move_right = True
					return	
						
				elif map[y][x] == "•" and object.move_right == True:
					map[y][x+7] = "•"
					map[y][x] = " "
					object.move_right = False
					object.move_up = True
					return
					
				elif map[y][x] == "•" and object.move_up == True:
					map[y-7][x] = "•"
					map[y][x] = " "
					object.move_up = False
					object.move_left = True
					return
					
	@staticmethod
	def second_boss(map):
		if object.moves == 10 and object.spawn_boss == False:
			map[5][4] = "x"
			object.spawn_boss = True
		elif object.moves == 60 and object.spawn_two_boss == False:
			map[5][30] = "+"
			object.spawn_two_boss == True
		elif object.moves == 14:
			map[14][22] = "a"
			map[11][6] = "@"
		elif object.moves == 70:
			map[15][23] = "a"
			map[6][14] = "@"
		elif object.moves == 130:
			map[14][25] = "a"
			map[3][6] = "@"
		elif object.moves == 200:
			map[14][24] = "a"
			map[5][8] = "@"
		elif object.moves == 260:
			map[14][26] = "a"
			map[4][38] = "@"
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "x" and object.activ_boss == True:
					if map[y][x-object.first_blas] == " " or map[y][x-object.first_blas] == "◼":
						map[y][x-object.first_blas] = "-"
						if object.first_blas == 1:
							pass
						else:
							map[y][x-(object.first_blas-1)] = " "
						object.first_blas += 1
					else:
						map[y][x-(object.first_blas-1)] = " "
						object.first_blas = 1
						
					if map[y][x+object.second_blas] == " " or map[y][x+object.second_blas] == "◼":
						map[y][x+object.second_blas] = "-"
						if object.second_blas == 1:
							pass
						else:
							map[y][x+(object.second_blas-1)] = " "
						object.second_blas += 1
					else:
						map[y][x+(object.second_blas-1)] = " "
						object.second_blas = 1
						
					if map[y-object.third_blas][x] == " " or map[y-object.third_blas][x] == "◼":
						map[y-object.third_blas][x] = "|"
						if object.third_blas == 1:
							pass
						else:
							map[y-(object.third_blas-1)][x] = " "
						object.third_blas += 1
					else:
						map[y-(object.third_blas-1)][x] = " "
						object.third_blas = 1
								
					if map[y+object.fourth_blas][x] == " " or map[y+object.fourth_blas][x] == "◼":
						map[y+object.fourth_blas][x] = "|"
						if object.fourth_blas == 1:
							pass
						else:
							map[y+(object.fourth_blas-1)][x] = " "
						object.fourth_blas += 1
						return
					else:
						map[y+(object.fourth_blas-1)][x] = " "
						object.fourth_blas = 1
						return
	@staticmethod
	def second_boss_two(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "+" and object.activ_boss == True:
					if map[y][x-object.y_first_blas] == " " or map[y][x-object.y_first_blas] == "◼":
						map[y][x-object.y_first_blas] = "-"
						if object.y_first_blas == 1:
							pass
						else:
							map[y][x-(object.y_first_blas-1)] = " "
						object.y_first_blas += 1
					else:
						map[y][x-(object.y_first_blas-1)] = " "
						object.y_first_blas = 1
						
					if map[y][x+object.y_second_blas] == " " or map[y][x+object.y_second_blas] == "◼":
						map[y][x+object.y_second_blas] = "-"
						if object.y_second_blas == 1:
							pass
						else:
							map[y][x+(object.y_second_blas-1)] = " "
						object.y_second_blas += 1
					else:
						map[y][x+(object.y_second_blas-1)] = " "
						object.y_second_blas = 1
						
					if map[y-object.y_third_blas][x] == " " or map[y-object.y_third_blas][x] == "◼":
						map[y-object.y_third_blas][x] = "|"
						if object.y_third_blas == 1:
							pass
						else:
							map[y-(object.y_third_blas-1)][x] = " "
						object.y_third_blas += 1
					else:
						map[y-(object.y_third_blas-1)][x] = " "
						object.y_third_blas = 1
								
					if map[y+object.y_fourth_blas][x] == " " or map[y+object.y_fourth_blas][x] == "◼":
						map[y+object.y_fourth_blas][x] = "|"
						if object.y_fourth_blas == 1:
							pass
						else:
							map[y+(object.y_fourth_blas-1)][x] = " "
						object.y_fourth_blas += 1
						return
					else:
						map[y+(object.y_fourth_blas-1)][x] = " "
						object.y_fourth_blas = 1
						return
							
	@staticmethod
	def first_boss(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "^" and map[y+1][x-1] == "<" and map[y+1][x] == "=" and map[y+1][x+1] == ">":
					if object.moves == 8:
						map[3][8] = "a"
					elif object.moves == 36 and object.activ == True:
						map[3][19] = "a"
					elif object.moves == 61 and object.activ == True:
						map[5][2] = "a"
					elif object.moves == 93 and object.activ == True:
						map[8][5] = "a"
					elif object.moves == 128 and object.activ == True:
						map[7][29] = "a"
					elif object.moves == 160 and object.activ == True:
						map[4][19] = "a"
					elif object.moves == 192 and object.activ == True:
						map[6][1] = "a"
					elif object.moves == 225 and object.activ == True:
						map[9][4] = "a"
					elif object.moves == 263 and object.activ == True:
						map[12][27] = "a"
						
					elif object.moves == 20 and object.activ == True:
						map[y+2][x] = "^"
						map[y+3][x-1] = "<"
						map[y+3][x] = "="
						map[y+3][x+1] = ">"
						
						map[y][x] = " "
						map[y+1][x-1] = " "
						map[y+1][x] = " "
						map[y+1][x+1] = " "
						return
					elif object.moves == 49 and object.activ == True:
						map[y-2][x] = "^"
						map[y-1][x-1] = "<"
						map[y-1][x] = "="
						map[y-1][x+1] = ">"
						
						map[y][x] = " "
						map[y+1][x-1] = " "
						map[y+1][x] = " "
						map[y+1][x+1] = " "
						return
					elif object.moves == 83 and object.activ == True:
						map[y+2][x] = "^"
						map[y+3][x-1] = "<"
						map[y+3][x] = "="
						map[y+3][x+1] = ">"
						
						map[y][x] = " "
						map[y+1][x-1] = " "
						map[y+1][x] = " "
						map[y+1][x+1] = " "
						return
						
	@staticmethod
	def deleted_object(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "@":
					map[y][x] = " "
					return
					
	@staticmethod
	def teleport_hero(map):
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] == "◼":
					map[y][x] = " "
					map[11][10] = "◼"
					return
					
	@staticmethod 
	def check_attack_by_two_boss(map):			
		if object.moves >= 14 and map[14][22] == " " and object.give_11 == False and object.completed_level == 9:
			object.health_boss_two -= 5
			object.give_11 = True
			object.deleted_object(map)
			object.teleport_hero(map)
		if object.moves >= 70 and map[15][23] == " " and object.give_21 == False and object.completed_level == 9:
			object.health_boss_two -= 5
			object.give_21 = True
			object.deleted_object(map)
			object.teleport_hero(map)
		if object.moves >= 130 and map[14][25] == " " and object.give_31 == False and object.completed_level == 9:
			object.health_boss_two -= 5
			object.give_31 = True
			object.deleted_object(map)
			object.teleport_hero(map)
		if object.moves >= 200 and map[14][24] == " " and object.give_41 == False and object.completed_level == 9:
			object.health_boss_two -= 5
			object.give_41 = True
			object.deleted_object(map)
			object.teleport_hero(map)
		if object.moves >= 260 and map[14][26] == " " and object.give_51 == False and object.completed_level == 9:
			object.health_boss_two -= 5
			object.give_51 = True
			object.deleted_object(map)
			object.teleport_hero(map)
		if object.health_boss_two == 0 and object.spawn_object == True:
			object.activ_boss = False
			object.spawn_object = False
			map[8][0] = "M"
			
	@staticmethod					
	def check_attack_by_boss(map):
		try:
			if object.moves >= 8 and map[3][8] == "◼" or map[3][8] == " " and object.give_1 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_1 = True
			if object.moves >= 36 and map[3][19] == "◼" or map[3][19] == " " and object.give_2 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_2 = True
			if object.moves >= 61 and map[5][2] == "◼" or map[5][2] == " " and object.give_3 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_3 = True
			if object.moves >= 93 and map[8][5] == "◼" or map[8][5] == " " and object.give_4 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_4 = True
			if object.moves >= 128 and map[7][29] == "◼" or map[7][29] == " " and object.give_5 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_5 = True
			if object.moves >= 160 and map[4][19] == "◼" or map[4][19] == " " and object.give_6 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_6 = True
			if object.moves >= 192 and map[6][1] == "◼" or map[6][1] == " " and object.give_7 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_7 = True
			if object.moves >= 225 and map[9][4] == "◼" or map[9][4] == " " and object.give_8 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_8 = True
			if object.moves >= 263 and map[12][27] == "◼" or map[12][27] == " " and object.give_9 == False and object.completed_level == 10:
				object.health_boss -= 2
				object.give_9 = True
			if object.health_boss == 0 and object.spawn_object == True:
				object.activ = False
				map[5][25] = "@"
				map[5][26] = "m"
				object.spawn_object = False
		#	for y in range(len(map)):
		#		for x in range(len(map[y])):
		#			if map[y][x] == "•":
		#				map[y][x] = " "
		except Exception as e:
			print("Хех", e)
			input()
			
	@staticmethod
	def attack_first_boss(map):
		try:
			for y in range(len(map)):
				for x in range(len(map[y])):
					if map[y][x] == "^" and map[y+1][x-1] == "<" and map[y+1][x] == "=" and map[y+1][x+1] == ">":
						if object.moves % 3 == 0 and object.blaster == False and object.activ == True:
							for laser in range(0, y):
								map[laser][x] = "|"
							object.blaster = True
							
		except IndexError:
			pass
			
	@staticmethod						
	def clear_first_boss(map):
		try:
			for y in range(len(map)):
				for x in range(len(map[y])):
					if map[y][x] == "^" and map[y+1][x-1] == "<" and map[y+1][x] == "=" and map[y+1][x+1] == ">" and object.activ == True:
						for laser in range(0, y):
							map[laser][x] = " "
						object.blaster = False
						
		except IndexError:
			pass
							
	@staticmethod 
	def render_map(mapping): #обновление карты
		st("clear")
		for place in mapping:
			print("".join(place))
		del place, mapping
	
	@staticmethod
	def event_talk():
		print("Взаимодействие <E>")
		
	@staticmethod
	def begin_talk(map):
		print("Джордж: Приветствую, незнакомец, ты потерялся?")
		sleep(2)
		print("Джордж: Этот профессор совсем с катушек сьехал")
		sleep(2)
		print("Джордж: похищает случайных людей, и проводит ")
		sleep(2)
		print("Джордж: над ними эксперименты")
		sleep(2)
		print("Джордж: надеюсь у тебя есть воспоминания?")
		sleep(2)
		#Сохранения
		object.cursor.execute("SELECT name_save FROM SaveData")
		if object.cursor.fetchall() == []:
			pass
		else:
			object.cursor.execute("SELECT name_save FROM SaveData")					
			for value, i in enumerate(object.cursor.fetchall(), 1):
				print(f"Сохранение {value}: {i[0]}")
			choose_save = input("Пропустить[S] Выбрать[1.2.3]: ").lower()
			if choose_save == "s":
				pass
			else:
				try:
					result = int(choose_save)-1
					object.cursor.execute("SELECT name_save FROM SaveData")
					objects = object.cursor.fetchall()[result]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.level = object.cursor.fetchall()[0][1]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.score = object.cursor.fetchall()[0][2]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.PowerSkill = object.cursor.fetchall()[0][3]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.JumpSkill = object.cursor.fetchall()[0][4]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.SpeedSkill = object.cursor.fetchall()[0][5]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.KanatSkill = object.cursor.fetchall()[0][6]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.level_talk_menu = object.cursor.fetchall()[0][7]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.new_dialog_menu = object.cursor.fetchall()[0][8]
					object.cursor.execute("SELECT * FROM SaveData WHERE name_save=?", objects)
					object.new_dialog_menu_two = object.cursor.fetchall()[0][9]
					object.main()
					#print(object.cursor.fetchall())
					
				except ValueError: 
					print("[Error] Нет такого сохранения")
					input("Нажмите <Enter>")
		#Сохранения
		print("Джордж: Ну и хорошо")
		object.new_dialog_menu = True
		sleep(1)
		object.main(1)
	
	@staticmethod
	def text_one(map):
		print("Джордж: Это моя база, здесь ты можешь насладиться отдыхом")
		sleep(3)
		print("Джордж: Давай начистоту, ты ведь прошёл те испытания что и я?")
		sleep(3)
		print("Джордж: Можешь пожалуйста принести мне", end="")
		print(Fore.GREEN, end="")
		print(" 10 микросхем")
		print(Fore.RESET, end="")
		sleep(4)
		print("Джордж: Тебе достаточно зайти в ", end="")
		print(Fore.LIGHTYELLOW_EX, end="")
		print("портал", end="")
		print(Fore.RESET, end="")
		print(" через стену")
		sleep(3)
		print("Джордж: У тебя возникнет один вопрос, почему же я сам туда не иду")
		sleep(3)
		print("Джордж: Так вот, там очень легко заблудиться, поэтому")
		object.new_dialog_menu = False
		object.new_dialog_menu_two = True
		sleep(3)
		print("Джордж: будь осторожней.")
		sleep(3)
	
	@staticmethod
	def text_one_repeat():
		print("Джордж: пока можешь осмотреться")
		sleep(2)
	
	@staticmethod
	def text_two(map):
		print("Джордж: Ты справился, молодец. А теперь давай попробуем их на деле")
		sleep(2)
		for y in range(len(map)):
			for x in range(len(map[y])):		
				if map[y][x] == "G":
					cord_y = y
					cord_x = x					
					map[y][x] = " "
		for y in range(len(map)):
			for x in range(len(map[y])):		
				if map[y][x] == "U":
					map[y+1][x] = "G"
		object.render_map(map)
		sleep(2)
		print("Джордж: Что такое, чип недоступен вне зоны действия")
		sleep(2)
		for y in range(len(map)):
			for x in range(len(map[y])):		
				if map[y][x] == "U":
					map[y+1][x] = " "
		map[cord_y][cord_x] = "G"
		object.render_map(map)		
		print("Джордж: для тебя хорошие новости, ты можешь улучшить себя")
		sleep(3)
		print("Джордж: Но потом сходи и уничтожь блокировщик доктора")
		sleep(3)
		object.new_dialog_menu_two = False
		print("Джордж: Наверняка он задумал что-то не доброе")
		sleep(3)
	
	@staticmethod
	def text_two_repeat():
		print("Джордж: Иди и уничтожь блокировщики доктора")
		sleep(2)
			
	@staticmethod	
	def talk_with_thing():
		print("Устройство по диагностике и улучшению микросистем, но вы не можете им пользоваться")
		input("Нажмите <Enter>")
		
	def main(self, level=0):
		
		self.level += level
		map = Mapper.menu_map()
		move = ""
		while True:
			object.controller(map, move, self.level)
			object.render_map(map)
			move = getch()
	
	def game(self, level):
		st("clear")
		move = ""
		if level == 1:
			map = Mapper.level_1()
		elif level == 2:
			map = Mapper.level_2()
		elif level == 3:
			map = Mapper.level_3()
		elif level == 4:
			map = Mapper.level_4()
		elif level == 5:
			map = Mapper.level_5()
		elif level == 6:
			map = Mapper.level_6()
		elif level == 7:
			map = Mapper.level_7()
		elif level == 8:
			map = Mapper.level_8()
		elif level == 9:
			map = Mapper.level_9()
		elif level == 10:
			map = Mapper.level_10()
		elif level == 11:
			map = Mapper.level_11()
		elif level == 12:
			map = Mapper.level_12()
		elif level == 13:
			map = Mapper.level_13()
		elif level == 14:
			map = Mapper.level_14()
		elif level == 15:
			map = Mapper.level_15()
		elif level == 16:
			map = Mapper.level_16()
		elif level == 17:
			map = Mapper.level_17()
		elif level == 18:
			map = Mapper.level_18()
		elif level == 19:
			map = Mapper.level_19()
		elif level == 20:
			map = Mapper.level_20()
		object.event_fire_y_one = 1
		object.event_fire_x_two = 1
		object.fired_sm = 1
		object.fired_sm_one = 1
		object.fired_sm_one_one = 1
		object.fired_sm_one_one_one = 1
		object.fired_sm_two = 1
		object.moves = 0
		while True:
			object.controller(map, move, self.level)
			object.func_unit(map)
			object.render_map(map)
			object.check_hero(map)
			if level == 10:
				object.clear_first_boss(map)
				object.attack_first_boss(map)
				object.first_boss(map)
				object.check_attack_by_boss(map)
				print("")
				print("[{:^50}]".format("=" * self.health_boss*2))
			if level >= 1 and level < 11:
				print(f"[{object.microscheme}/10]")
			if level == 20:
				#object.clear_second_boss(map)
			#	object.attack_second_boss(map)
				object.second_boss(map)
				object.second_boss_two(map)
				object.check_attack_by_two_boss(map)
				print("")
				print("[{:^50}]".format("=" * self.health_boss_two*2))
	#		print(f"Пройденные уровни: {object.completed_level}") 
			move = getch()
			
pbar = ProgressBar(maxval=10.0).start()		
if __name__ == "__main__":
	object = Cube()
	for i in range(1, 11):
		pbar.update(i)
		sleep(0.2)
	pbar.finish()
	st("clear")
	del pbar
	print("<WASD> - Движения")
	print("<E> - Взаимодействия")
	input("Нажмите <Enter>")
	object.begin()
		