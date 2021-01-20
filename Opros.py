import sqlite3
import django as db


conn = sqlite3.connect('opros.db')
cursor = conn.cursor()


def createTB():
	cursor.execute('''
		CREATE TABLE if not exists client_opros(
			id integer primary key autoincrement,
			title varchar (128),
			date datetime,
			start_dttm datetime default current_timestamp,
			end_dttm datetime default (datetime('2999-12-31 23:59:59')),
			relise varchar(128),
			otvet varchar(128)
		)''')

	cursor.execute('''
		CREATE VIEW if not exists v_opros as
			select
				title,
				relise
			from client_opros
			;
		''')

def addOpros(title, relise):
	cursor.execute('''
		INSERT INTO client_opros (title, relise) values(? , ?);
		''', [title, relise])
	conn.commit()




def clientVopros(title, relise):
	cursor.execute('''
		name = input('Введите имя (не обязательно) : ')
		otvet = input('Введите ответ: ')
		x = input('Хотите пройти еще опрос? Yes/N')
		if x = 'Yes':
			return dableOpros
		else:
			break
	''')



def deleteOpros(title):
 	cursor.execute('''
 		delete from client_opros
 		where title = ?
 		''', [title])
 	conn.commit()



def updateOpros(title, relise):
	column_list = [f'{key} = ?' for key in kwargs.keys()]

	query = f'''
	UPDATE client_opros
	set {' , '.join(column_list)}
	where title = ?
	'''

	cursor.execute(query, [*kwargs.values(), title])
	conn.commit()



def getTable(tableName):
	cursor.execute(f'select * from {tableName}')
	result = cursor.fetchall()
	return result

createTB()

addOpros('Вопрос 1', 'Какая сегодня погода?')
addOpros('Вопрос 2', 'Какая сегодня температура?')
addOpros('Вопрос 3', 'Какой сегодня день недели?')
addOpros('Вопрос 4', 'Какое сегодня число?')
addOpros('Вопрос 5', 'Какой сегодня месяц?')


#deleteOpros('Вопрос 1')


for row in getTable('v_opros'):
		print(row)
