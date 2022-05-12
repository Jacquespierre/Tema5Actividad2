BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "clientes" (
	"codigo"	INTEGER NOT NULL,
	"dni"	TEXT NOT NULL UNIQUE,
	"apellidos"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"direccion"	TEXT,
	"provincia"	TEXT,
	"sexo"	TEXT NOT NULL,
	"formapago"	TEXT NOT NULL,
	"fechaalta"	TEXT,
	"envio"	INTEGER,
	PRIMARY KEY("codigo" AUTOINCREMENT)
);
INSERT INTO "clientes" VALUES (1,'24680297D','Martinez Martinez','David','Casa Cordellas ,','Zaragoza','Hombre','Efectivo','05/04/2021',0);
INSERT INTO "clientes" VALUES (2,'25225560B','Garcia Garcia','Javier','Doctor Fleming , 11','Barcelona','Hombre','Tarjeta','15/11/2021',0);
INSERT INTO "clientes" VALUES (3,'00547093S','Fernandez Fernandez','Jesus','Bertrand I Serra , 11, 3R.','Zaragoza','Hombre','Transferencia','11/01/2021',3);
INSERT INTO "clientes" VALUES (4,'69522927E','Perez Perez','Jose Luis','Carrió , 12, 5È A','Zaragoza','Hombre','Efectivo','14/09/2021',1);
INSERT INTO "clientes" VALUES (5,'63163249M','Jimenez Jimenez','Angel','Pirineus , 10','Tarragona','Hombre','Tarjeta','17/12/2020',0);
INSERT INTO "clientes" VALUES (6,'70249930H','Gonzalez Ruiz','Daniel','Jacint Verdaguer , 43','Valencia','Hombre','Transferencia','01/08/2021',1);
INSERT INTO "clientes" VALUES (7,'09707468L','Ruiz Saenz','Maria Angeles','Nou , 9, 2N.','Girona','Mujer','Efectivo','29/11/2020',2);
INSERT INTO "clientes" VALUES (8,'56885768Y','Lopez Gonzalez','Laura','Jacint Verdaguer , 52, 3R, 1A.','Tarragona','Mujer','Tarjeta','22/02/2021',0);
INSERT INTO "clientes" VALUES (9,'03418360P','Saenz Lopez','Ana Maria','Joan Miró , 10','Barcelona','Mujer','Transferencia','16/08/2022',1);
INSERT INTO "clientes" VALUES (10,'86084616D','Rodriguez Gomez','Carmen','Jaume Galobart , 12','Tarragona','Mujer','Efectivo','15/10/2021',1);
INSERT INTO "clientes" VALUES (11,'31938624L','Gomez Rodriguez','Lucia','Pintor Sert , 12, 1R., 1A.','Lleida','Mujer','Tarjeta','17/04/2021',1);
INSERT INTO "clientes" VALUES (12,'86986824L','Moreno Moreno','Sara','Bellavista , 30','Valencia','Mujer','Transferencia','01/03/2022',2);
INSERT INTO "clientes" VALUES (13,'47385365Y','Hernandez Alonso','Marta','Monturiol , 10, 1R.','Zaragoza','Mujer','Efectivo','19/10/2022',0);
INSERT INTO "clientes" VALUES (14,'47924877F','Sanchez Pascual','Maria Jesus','Jacint Verdaguer , 52, 2N., 4A.','Girona','Mujer','Tarjeta','29/05/2021',1);
INSERT INTO "clientes" VALUES (15,'31727083D','Alonso Hernandez','Ana','Casa Nova ,','Lleida','Mujer','Transferencia','26/11/2020',0);
INSERT INTO "clientes" VALUES (16,'34440222E','Pascual Gil','Cristina','De La Caça , 12, 1R., C','Lleida','Mujer','Efectivo','03/06/2022',1);
INSERT INTO "clientes" VALUES (17,'32344443A','Gil Diez','Raquel','Pintor Sert , 12, 2N., 1A.','Valencia','Mujer','Tarjeta','28/08/2020',3);
INSERT INTO "clientes" VALUES (18,'55311947Y','Marin Marin','Maria Luisa','Casa Sara ,','Zaragoza','Mujer','Transferencia','30/11/2020',0);
INSERT INTO "clientes" VALUES (19,'00342073V','Diez Ezquerro','Maria Isabel','Artès , 1, 1R, 1A.','Tarragona','Mujer','Efectivo','12/04/2022',3);
INSERT INTO "clientes" VALUES (20,'54361688S','Alvarez Sanchez','Elena','General Prim , 11, 2N.','Barcelona','Mujer','Tarjeta','10/04/2020',1);
INSERT INTO "clientes" VALUES (21,'40608543L','Gutierrez Rubio','Isabel','Cau De La Guineu , 4','Valencia','Mujer','Transferencia','04/04/2021',3);
INSERT INTO "clientes" VALUES (22,'61676974J','Martin Calvo','Paula','Joan Sanmartí , 12, 2N., 2A.','Tarragona','Mujer','Efectivo','05/12/2022',1);
INSERT INTO "clientes" VALUES (23,'92331882S','Calvo Saez','Beatriz','Prol. Padró , 1, 3R. 1A.','Lleida','Mujer','Tarjeta','05/09/2021',3);
INSERT INTO "clientes" VALUES (24,'54129072K','Blanco Ibañez','Rosa Maria','Sallent , 22, 2N.','Madrid','Mujer','Transferencia','11/07/2020',3);
INSERT INTO "clientes" VALUES (25,'20792026A','Ezquerro Blanco','Julia','Joan Miró , 3','Barcelona','Mujer','Efectivo','04/05/2020',1);
INSERT INTO "clientes" VALUES (26,'79012671N','Rubio Garrido','Pilar','Lluís Castells , 12, 2N.','Girona','Mujer','Tarjeta','06/09/2021',2);
INSERT INTO "clientes" VALUES (27,'25547946Y','Ibañez Gutierrez','Irene','Sant Valentí , 12, 1R.','Barcelona','Mujer','Transferencia','05/11/2021',2);
INSERT INTO "clientes" VALUES (28,'28196095G','Muñoz Alvarez','Maria Dolores','Àngel Guimerà , 43, 2N','Girona','Mujer','Efectivo','05/09/2022',2);
INSERT INTO "clientes" VALUES (29,'01031767X','Garrido Muñoz','Susana','Jaume Galobart , 11','Salamanca','Mujer','Tarjeta','09/03/2021',3);
INSERT INTO "clientes" VALUES (30,'40027892A','Saez Palacios','Andrea','Avinguda Tres , 3, 1R., 1A.','Girona','Mujer','Transferencia','05/05/2022',3);
INSERT INTO "clientes" VALUES (31,'33909795K','Diaz Santamaria','Silvia','Jacint Verdaguer , 52, 2N., 1A.','Madrid','Mujer','Efectivo','19/12/2021',0);
INSERT INTO "clientes" VALUES (32,'43286287B','Ramirez Benito','Angela','Diputació , 10','Barcelona','Mujer','Tarjeta','16/03/2021',2);
INSERT INTO "clientes" VALUES (33,'48120985V','Palacios Ramirez','Alba','Vic , 39, 1R., 2A.','Lleida','Mujer','Transferencia','20/12/2020',3);
INSERT INTO "clientes" VALUES (34,'28278804M','Ortega Ochoa','Alicia','German Duran , 21','Tarragona','Mujer','Efectivo','03/11/2022',0);
INSERT INTO "clientes" VALUES (35,'82512761P','Benito Diaz','Juan','Bellavista , 30','Zaragoza','Hombre','Tarjeta','25/04/2021',1);
INSERT INTO "clientes" VALUES (36,'63801752M','Santamaria Ortega','Ivan','Nou , 7, 2N.','Zaragoza','Hombre','Transferencia','05/07/2020',1);
INSERT INTO "clientes" VALUES (37,'54508096M','Romero Leon','Mario','Manelic , 1','Lleida','Hombre','Efectivo','15/10/2020',2);
INSERT INTO "clientes" VALUES (38,'38206321D','Ochoa Herce','Felix','De La Pesca , 1, 1R., 1A.','Barcelona','Hombre','Tarjeta','27/03/2020',0);
INSERT INTO "clientes" VALUES (39,'84866681Q','Leon Martin','Victor','Pirineus , 34','Lleida','Hombre','Transferencia','07/05/2020',3);
INSERT INTO "clientes" VALUES (40,'73615398B','Dominguez Gabarri','Rafael','Prol. Jacint Verdaguer , 1, 2N., 2A.','Lleida','Hombre','Efectivo','03/12/2022',0);
INSERT INTO "clientes" VALUES (41,'X8136223L','Herce Sainz','Enrique','Mallorca , 11','Pontevedra','Hombre','Tarjeta','10/03/2021',2);
INSERT INTO "clientes" VALUES (42,'Z4205235N','Peña Dominguez','Juan Jose','Sant Benet , 12, 2N.','Zaragoza','Hombre','Transferencia','13/07/2021',1);
INSERT INTO "clientes" VALUES (43,'Z8050649X','Gabarri Merino','Jose Manuel','Prol. Padró , 1, 2N., 2A.','Lleida','Hombre','Efectivo','22/01/2022',1);
INSERT INTO "clientes" VALUES (44,'Y7321987C','Merino Romero','Marcos','Artès , 1, 2N., 2A.','Lleida','Hombre','Tarjeta','13/07/2021',0);
INSERT INTO "clientes" VALUES (45,'X6636955Y','Torres Peña','Ricardo','Joan Xxiii , 12, 1R, 2A.','Barcelona','Hombre','Transferencia','05/04/2021',3);
INSERT INTO "clientes" VALUES (46,'Y5025749X','Sainz Cordon','Jose Ignacio','Bertrand I Serra , 11, 3R.','Madrid','Hombre','Efectivo','23/05/2022',1);
INSERT INTO "clientes" VALUES (47,'Y0848528A','Sanz Castillo','Ignacio','La Sardana , 1','Zaragoza','Hombre','Tarjeta','11/10/2022',0);
INSERT INTO "clientes" VALUES (48,'Y4695857F','Castillo Espinosa','Andres','Galileu , 12','Barcelona','Hombre','Transferencia','27/01/2021',2);
INSERT INTO "clientes" VALUES (49,'Y8901491E','Ortiz Miguel','Gonzalo','Sant Valentí , 11','Tarragona','Hombre','Efectivo','08/12/2020',0);
INSERT INTO "clientes" VALUES (50,'X7253999Y','Cordon Muro','Julio','Joan Xxiii , 43','Girona','Hombre','Tarjeta','08/03/2022',1);
INSERT INTO "clientes" VALUES (51,'70373620Z','Arocas Pasadas','Estefania','De La Pau , 1','Barcelona','Mujer','Transferencia','14/09/2022',3);
INSERT INTO "clientes" VALUES (52,'45444092W','Viso Gilabert','Queralt','Sant Antoni Maria Claret , 11','Tarragona','Mujer','Efectivo','01/07/2020',2);
INSERT INTO "clientes" VALUES (53,'47126967J','Ayala Ferreras','Joan','Avinguda Tres , 1, 3R., 1A.','Zaragoza','Hombre','Tarjeta','02/04/2021',2);
INSERT INTO "clientes" VALUES (54,'25149091V','Baez Tejado','Joan','Prol. Padró , 1, 2N., 1A.','Tarragona','Hombre','Transferencia','25/11/2022',0);
INSERT INTO "clientes" VALUES (55,'17871028M','Bastardes Soto','Marc','Sant Joan , 0, C, 3R. A','Barcelona','Hombre','Efectivo','19/08/2022',2);
INSERT INTO "clientes" VALUES (56,'21866250N','Anguera Vilafranca','Josep','Prol. Jacint Verdaguer , 1, 1R., 1A.','Valencia','Hombre','Tarjeta','16/09/2022',0);
INSERT INTO "clientes" VALUES (57,'74976579Y','Pascual Aloy','Esther','Joan Xxiii , 11, 1R., 1A.','Madrid','Mujer','Transferencia','15/03/2022',1);
INSERT INTO "clientes" VALUES (58,'43547721G','Vallés Girvent','Laura','Lluís Castells , 12, 1R.','Girona','Mujer','Efectivo','02/10/2021',2);
INSERT INTO "clientes" VALUES (59,'44140778Y','Raya Garcia','Raquel','Padró , 83','Barcelona','Mujer','Tarjeta','28/11/2020',3);
INSERT INTO "clientes" VALUES (60,'50306194L','Andreu Cruz','Joan','Sant Iscle , 1','Zaragoza','Hombre','Transferencia','07/11/2020',3);
INSERT INTO "clientes" VALUES (61,'70049667Q','Baraldés Comas','Maria Isabel','Montserrat , 10','Tarragona','Mujer','Efectivo','16/07/2021',0);
INSERT INTO "clientes" VALUES (62,'25076596H','Berengueras Cullerés','Adrià','Prol. Jacint Verdaguer , 1, 1R., 2A.','Zaragoza','Hombre','Tarjeta','11/02/2022',3);
INSERT INTO "clientes" VALUES (63,'18172824H','López De Pablo Garcia Uceda','Gerard','Trabucaires , 12','Zaragoza','Hombre','Transferencia','19/05/2022',1);
INSERT INTO "clientes" VALUES (64,'94719330V','Arnau Moreno','Eliot','Jacint Verdaguer , 49, 4T., 2A.','Zaragoza','Hombre','Efectivo','23/01/2022',1);
INSERT INTO "clientes" VALUES (65,'68152579Z','Raya Gavilan','Jordi','Manelic , 1','Girona','Hombre','Tarjeta','15/05/2020',3);
INSERT INTO "clientes" VALUES (66,'53257213T','Zambudio Figuls','Lluís','Verge De Fàtima , 6, Bx., 2A.','Madrid','Hombre','Transferencia','31/07/2020',0);
INSERT INTO "clientes" VALUES (67,'89323483Q','Bidault Cullerés','Laura','Sant Joan , 0, D, 3R. A','Madrid','Mujer','Efectivo','12/06/2020',2);
INSERT INTO "clientes" VALUES (68,'30305456N','Biosca Fontanet','Jordi','Galileu , 12','Tarragona','Hombre','Tarjeta','12/09/2021',0);
INSERT INTO "clientes" VALUES (69,'51705658W','Zafra Figuls','Dounya','Esports , 12','Madrid','Mujer','Transferencia','09/08/2022',2);
INSERT INTO "clientes" VALUES (70,'40432804T','Aleu Icart','Julio','Josep Boixaderas , 1','Barcelona','Hombre','Efectivo','05/07/2020',3);
INSERT INTO "clientes" VALUES (71,'08530094S','Badia Torné','Andreu','Cervantes , 1, 1R.','Valencia','Hombre','Tarjeta','13/03/2021',2);
INSERT INTO "clientes" VALUES (72,'46941904P','Morales Gese','Ramon','Cervantes , 9, 1R.','Girona','Hombre','Transferencia','16/06/2021',0);
INSERT INTO "clientes" VALUES (73,'60044831L','Blanco Fontanet','David-Jese','Joan Xxiii , 39','Valencia','Hombre','Efectivo','10/12/2021',3);
INSERT INTO "clientes" VALUES (74,'42806069X','Alvarez Fernández','Aran','Doctor Barnard , 10','Girona','Hombre','Tarjeta','11/11/2021',3);
INSERT INTO "clientes" VALUES (75,'27926280W','Garcia Almoguera','Gemma','Esports , 12','Tarragona','Mujer','Transferencia','30/11/2022',2);
INSERT INTO "clientes" VALUES (76,'03025064N','Libori Figueras','Ivan','De La Pau , 8','Barcelona','Hombre','Efectivo','15/04/2022',2);
INSERT INTO "clientes" VALUES (77,'08272111T','Bidault Pueyo','David','Sant Valentí , 11','Valencia','Hombre','Tarjeta','06/06/2021',1);
INSERT INTO "clientes" VALUES (78,'92793871A','Benitez Jose','Xavier','Prol. Padró , 1, 2N., 2A.','Lleida','Hombre','Transferencia','14/06/2020',3);
INSERT INTO "clientes" VALUES (79,'09403162A','Pascual Flores','Mario','Vic , 30 (Torroella)','Barcelona','Hombre','Efectivo','08/02/2021',1);
INSERT INTO "clientes" VALUES (80,'04886981X','Ayala Torné','Jesus','Sant Iscle , 6','Lleida','Hombre','Tarjeta','24/11/2021',0);
INSERT INTO "clientes" VALUES (81,'68631177M','Listan Figueras','Gemma','Jaume Balmes , 70, 3R, 1A.','Tarragona','Mujer','Transferencia','24/11/2022',1);
INSERT INTO "clientes" VALUES (82,'84183878Z','Rasero Gavilan','Silvia','German Duran , 27, 3R., 1A.','Girona','Mujer','Efectivo','04/07/2020',3);
INSERT INTO "clientes" VALUES (83,'19808463N','Arnalot Puig','Albert','Sant Joan , 11','Zaragoza','Hombre','Tarjeta','19/03/2022',2);
INSERT INTO "clientes" VALUES (84,'76889680J','Moliner Garrido','Maria','Puig , 1','Lleida','Mujer','Transferencia','30/10/2021',0);
INSERT INTO "clientes" VALUES (85,'22445019D','Galobart Garcia','Berta','Prol. Jacint Verdaguer , 1, 2N., 2A.','Madrid','Mujer','Efectivo','08/12/2022',2);
INSERT INTO "clientes" VALUES (86,'Y3532269N','López Garrigassait','Berta','Ramon I Cajal , 81, 2N.','Valencia','Mujer','Tarjeta','22/10/2022',2);
INSERT INTO "clientes" VALUES (87,'X6691969G','Sánchez Gómez','Mireia','Moragues , 10','Lleida','Mujer','Transferencia','26/08/2022',1);
INSERT INTO "clientes" VALUES (88,'Z2599796L','Alavedra Sunyé','Gemma','Prol. Padró , 1, 3R., 2A.','Girona','Mujer','Efectivo','04/10/2020',3);
INSERT INTO "clientes" VALUES (89,'Z9409720B','Aligué Bonvehí','Maria Isabel','Francesc De Vitòria , 11, 4T 2A','Barcelona','Mujer','Tarjeta','21/01/2021',0);
INSERT INTO "clientes" VALUES (90,'X8844479J','Mas Franch','Toni','Albéniz , 22, 2N.','Tarragona','Hombre','Transferencia','20/01/2022',3);
INSERT INTO "clientes" VALUES (91,'Y6800388S','Aloy Compte','Alejandro','Tres Roures , 10, 4T 2A','Barcelona','Hombre','Efectivo','03/06/2020',3);
INSERT INTO "clientes" VALUES (92,'X7990513Z','Asensio Vega','Joan Martí','Prol. Padró , 1, 2N., 1A.','Tarragona','Hombre','Tarjeta','18/10/2022',2);
INSERT INTO "clientes" VALUES (93,'Y5696509K','Bidault Pérez','Ingrid','Albéniz , 13, 2N., 1A.','Girona','Mujer','Transferencia','26/10/2021',0);
INSERT INTO "clientes" VALUES (94,'X5901688A','Aloy Codinachs','Oliver','Font Del Gat , 1','Zaragoza','Hombre','Efectivo','10/05/2022',0);
INSERT INTO "clientes" VALUES (95,'Y0750566K','Altimiras Armenteros','Sandra','Montcau , 1','Lleida','Mujer','Tarjeta','16/02/2021',2);
INSERT INTO "clientes" VALUES (96,'Z9509455H','Belmonte Sánchez','Jordi','Monturiol , 1','Lleida','Hombre','Transferencia','23/10/2020',3);
INSERT INTO "clientes" VALUES (97,'X3515208A','Bajona Garcia','Marc','Vilatorrada , 6','Lleida','Hombre','Efectivo','27/09/2022',1);
INSERT INTO "clientes" VALUES (98,'Y0075870F','Aguilar Rodriguez','Jordina','Jaume Galobart , 11','Valencia','Mujer','Tarjeta','07/12/2021',1);
INSERT INTO "clientes" VALUES (99,'Y4074883X','Barriga Soto','Maria José','Sant Genís , 25','Valencia','Mujer','Transferencia','29/01/2021',2);
INSERT INTO "clientes" VALUES (100,'Z7925019Y','Avila Masjuan','Raquel','Verge De Fàtima , 2, 3R., 1A.','Barcelona','Mujer','Efectivo','08/11/2022',2);
COMMIT;
