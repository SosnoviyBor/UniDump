DROP TABLE IF EXISTS med_recipes;
CREATE TABLE IF NOT EXISTS med_recipes (
	tech_id	INTEGER NOT NULL,
	component_id	INTEGER NOT NULL,
	amount	INTEGER NOT NULL,
	FOREIGN KEY(component_id) REFERENCES components(id),
	FOREIGN KEY(tech_id) REFERENCES med_cooking_techs(id)
);
DROP TABLE IF EXISTS orders_done;
CREATE TABLE IF NOT EXISTS orders_done (
	order_id	INTEGER,
	FOREIGN KEY(order_id) REFERENCES orders(id),
	PRIMARY KEY(order_id)
);
DROP TABLE IF EXISTS med_cooking_techs;
CREATE TABLE IF NOT EXISTS med_cooking_techs (
	id	INTEGER AUTO_INCREMENT,
	name	TEXT NOT NULL,
	recipe	TEXT NOT NULL,
	time	TEXT,
	PRIMARY KEY(id)
);
DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders (
	id	INTEGER AUTO_INCREMENT,
	doc_full_name	TEXT,
	customer_full_name	TEXT NOT NULL,
	age	INTEGER NOT NULL,
	diagnosis	TEXT,
	full_recipe_id	INTEGER NOT NULL,
	order_issue_time	TEXT NOT NULL,
	PRIMARY KEY(id)
);
DROP TABLE IF EXISTS components;
CREATE TABLE IF NOT EXISTS components (
	id	INTEGER AUTO_INCREMENT,
	name	TEXT NOT NULL,
	storage_method	TEXT,
	crit_norm	BLOB NOT NULL,
	amount	INTEGER,
	PRIMARY KEY(id)
);
DROP TABLE IF EXISTS customer_recipes;
CREATE TABLE IF NOT EXISTS customer_recipes (
	id	INTEGER NOT NULL AUTO_INCREMENT,
	med_id	INTEGER NOT NULL,
	amount	INTEGER NOT NULL,
	usage	TEXT,
	PRIMARY KEY(id)
);
DROP TABLE IF EXISTS customer_recipes_dict;
CREATE TABLE IF NOT EXISTS customer_recipes_dict (
	id	INTEGER NOT NULL,
	recipe_id	INTEGER NOT NULL,
	FOREIGN KEY(recipe_id) REFERENCES customer_recipes(id)
);
DROP TABLE IF EXISTS meds;
CREATE TABLE IF NOT EXISTS meds (
	id	INTEGER NOT NULL AUTO_INCREMENT,
	manufacturer	TEXT NOT NULL,
	type	TEXT NOT NULL,
	name	TEXT NOT NULL,
	storage_method	TEXT,
	price	REAL NOT NULL,
	amount	INTEGER,
	crit_norm	REAL,
	tech_id	INTEGER UNIQUE,
	FOREIGN KEY(tech_id) REFERENCES med_cooking_techs(id),
	PRIMARY KEY(id)
);
INSERT INTO med_recipes VALUES (1,5,100);
INSERT INTO med_recipes VALUES (1,6,10);
INSERT INTO med_recipes VALUES (2,5,100);
INSERT INTO med_recipes VALUES (2,7,20);
INSERT INTO med_recipes VALUES (3,8,0.12);
INSERT INTO med_recipes VALUES (3,9,4);
INSERT INTO med_recipes VALUES (3,10,4);
INSERT INTO med_recipes VALUES (3,11,10);
INSERT INTO med_recipes VALUES (3,12,4);
INSERT INTO med_recipes VALUES (4,2,30);
INSERT INTO med_recipes VALUES (4,3,10);
INSERT INTO med_recipes VALUES (4,4,20);
INSERT INTO med_recipes VALUES (5,13,1);
INSERT INTO med_recipes VALUES (5,14,1000);
INSERT INTO med_recipes VALUES (5,15,24);
INSERT INTO med_recipes VALUES (6,1,100);
INSERT INTO med_recipes VALUES (6,16,84);
INSERT INTO med_recipes VALUES (6,15,12);
INSERT INTO med_recipes VALUES (6,17,50);
INSERT INTO orders_done VALUES (1);
INSERT INTO orders_done VALUES (2);
INSERT INTO orders_done VALUES (4);
INSERT INTO med_cooking_techs VALUES (1,'Мазь із календули','Помістіть у фарфорову або емальовану ємність і підігрійте на водяній бані до рідкого стану 100 г вазеліну або ланоліну. Додайте 10 г сухих розмелених язичкових (помаранчевих) квіток календули. Зверніть увагу – кошики залишаються для інших випадків. Завадіть, нагрійте 10 хвилин, накрийте кришкою і поставте в темне тепле місце. Через добу суміш помістіть на водяну баню, нагрійте до рідкого стану, не даючи загуснути, процідіть через дрібне сито або марлю в баночку з темного скла.','1 день');
INSERT INTO med_cooking_techs VALUES (2,'Мазь із арніки','Помістіть у фарфорову або емальовану ємність і підігрійте на водяній бані до рідкого стану 100 г вазеліну або ланоліну. Додайте 20 г сухих розмелених квіток арніки. Зверніть увагу – кошики залишаються для інших випадків. Завадіть, нагрійте 10 хвилин, накрийте кришкою і поставте в темне тепле місце. Через добу суміш помістіть на водяну баню, нагрійте до рідкого стану, не даючи загуснути, процідіть через дрібне сито або марлю в баночку з темного скла.','1 день');
INSERT INTO med_cooking_techs VALUES (3,'Мікстура Дрягіна','Налити дистильовану воду у ємністьРозчинити кодеїн у водіПроцедити розчинДодати хлоралгідратДодати бромід натріюДодати настоянку з корінням валер''яниДодати настоянку валер''яни','1год');
INSERT INTO med_cooking_techs VALUES (4,'Чай з імбирем','Насипати повний пакетик чайного листя, вичавити половинку кільця лимону, нарізати трохи імбирю та залити окропом. Подавати у фірменному стакантчику та із трубочкою','2хв');
INSERT INTO med_cooking_techs VALUES (5,'Настоянка на кобрі','Вбити кобру (обов''язково голими руками) Відрізати головуНарізати її циліндрами довжиною 5 смЗасипати коброві циліндри у ємністьЗалити літром горілкиДрібно нарізати 2 стручки гострого перцю','3 дні');
INSERT INTO med_cooking_techs VALUES (6,'Порошок для підняття із мертвих','Натерти корінь мандрагориНатерти корінь женьшенюДрібно нарізати гострий перецьНасипати соліПеретовкти в ступці, висушити','2год');
INSERT INTO orders VALUES (1,'Біс Й.З.','Марина М.М.',26,'Не придумав',1,'05.11.2021 16:10');
INSERT INTO orders VALUES (2,'Перерва А.В.','Ян П.І.',20,'Серйозна інтоксикація організму',2,'06.11.2021 9:00');
INSERT INTO orders VALUES (3,'Букасов  М.М.','Вовк Є.А.',25,'Приблеми з диханням (Душний дуже)',3,'06.11.2021 20:00');
INSERT INTO orders VALUES (4,'Поліщук В.М.','Поліщук Б.І.',18,'Повірте, якийсь діагноз у нього точно був',4,'06.11.2021 12:00');
INSERT INTO components VALUES (1,'Корінь мандрагори','Зберігати по 1 штуці в окремому контейнеру для кожної. Зберігати за температури нижче 0С','10',25);
INSERT INTO components VALUES (2,'Чайне листя','Зберігати в закритій ємності','200',400);
INSERT INTO components VALUES (3,'Лимон','Зберігати в холодильнику. Вімкненому','2',6);
INSERT INTO components VALUES (4,'Імбир','Зберігати в холодильнику. Вімкненому','2',6);
INSERT INTO components VALUES (5,'Вазилін',NULL,'500',1000);
INSERT INTO components VALUES (6,'Квіти календули','Зберігати в сухому та холодному місці','50',56);
INSERT INTO components VALUES (7,'Квіти арніки','Зберігати в сухому та холодному місці','60',90);
INSERT INTO components VALUES (8,'Кодеїн',NULL,'12',24);
INSERT INTO components VALUES (9,'Хлоралгідрат',NULL,'40',60);
INSERT INTO components VALUES (10,'Бромід натрію',NULL,'40',60);
INSERT INTO components VALUES (11,'Настоянка з корінням валер''яни','Зберігати в холодильнику. Вімкненому','600',1000);
INSERT INTO components VALUES (12,'Настоянка влер''яни','Зберігати в холодильнику. Вімкненому','40',60);
INSERT INTO components VALUES (13,'Кобра (жива)','Годувати мишами 3 рази на день','2',3);
INSERT INTO components VALUES (14,'Горілка','Зберігати подалі від співробітників, схильних до алкоголізму','2000',4000);
INSERT INTO components VALUES (15,'Гострий перець','Зберігати в холодильнику. Вімкненому','30',60);
INSERT INTO components VALUES (16,'Корінь женьшеню','Зберігати в холодильнику. Вімкненому','200',400);
INSERT INTO components VALUES (17,'Сіль кухонна','Зберігати в закритій ємності','300',500);
INSERT INTO components VALUES (18,'Дистильована вода',NULL,'400',666);
INSERT INTO customer_recipes VALUES (1,4,2,'текст 1');
INSERT INTO customer_recipes VALUES (2,7,1,'текст 2');
INSERT INTO customer_recipes VALUES (3,11,100,'текст 3');
INSERT INTO customer_recipes VALUES (4,1,1,'текст 4');
INSERT INTO customer_recipes VALUES (5,2,1,'текст 5');
INSERT INTO customer_recipes VALUES (6,9,1,'текст 6');
INSERT INTO customer_recipes VALUES (7,10,1,'текст 7');
INSERT INTO customer_recipes_dict VALUES (1,1);
INSERT INTO customer_recipes_dict VALUES (1,2);
INSERT INTO customer_recipes_dict VALUES (2,3);
INSERT INTO customer_recipes_dict VALUES (3,4);
INSERT INTO customer_recipes_dict VALUES (3,5);
INSERT INTO customer_recipes_dict VALUES (4,6);
INSERT INTO customer_recipes_dict VALUES (4,7);
INSERT INTO meds VALUES (1,'Власне','Мазь','Мазь із календули',NULL,32.4,NULL,NULL,1);
INSERT INTO meds VALUES (2,'Власне','Мазь','Мазь із арніки',NULL,38.4,NULL,NULL,2);
INSERT INTO meds VALUES (3,'Власне','Мікстура','Мікстура Дрягіна','Зберігати у герметичній пляшці при холодній температурі',123.45,NULL,NULL,3);
INSERT INTO meds VALUES (4,'Власне','Розчин','Чай з імбирем','Зберігати не треба - пийте зараз',12.0,NULL,NULL,4);
INSERT INTO meds VALUES (5,'Власне','Настоянка','Настоянка на кобрі','Зберігати у герметичній пляшці при холодній температурі',250.0,NULL,NULL,5);
INSERT INTO meds VALUES (6,'Власне','Порошок','Порошок для підняття із мертвих','Зберігати якнайдалі від дітей та органів влади',500.0,NULL,NULL,6);
INSERT INTO meds VALUES (7,'Імпортоване','Таблетки','Аскорбінки','Зберігати подалі від дітей',12.8,100,20.0,NULL);
INSERT INTO meds VALUES (8,'Імпортоване','Таблетки','Парацетамол',NULL,92.0,50,15.0,NULL);
INSERT INTO meds VALUES (9,'Імпортоване','Мазь','Зірка','Зберігати в холодному місці',12.5,240,30.0,NULL);
INSERT INTO meds VALUES (10,'Імпортоване','Мазь','Спасатель','Зберігати в холодному місці',57.84,50,15.0,NULL);
INSERT INTO meds VALUES (11,'Імпортоване','Таблетки','Активований вуголь','Зберігати в сухому та темному місці',4.2,100,20.0,NULL);
INSERT INTO meds VALUES (12,'Імпортоване','Таблетки','Но-шпа','Зберігати в недоступному для дітей місці',70.17,134,15.0,NULL);
INSERT INTO meds VALUES (13,'Імпортоване','Настоянка','Настоянка бояришнику','Зберігати у герметичній пляшці при холодній температурі',15.0,100,10.0,NULL);
INSERT INTO meds VALUES (14,'Імпортоване','Таблетки','Аскорбінки з смаком яблука','Подалі від дітей',10.5,100,30.0,NULL);
COMMIT;
