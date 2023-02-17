-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: audiroDB
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Gift`
--

DROP TABLE IF EXISTS `Gift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Gift` (
  `GIFT_ID` bigint NOT NULL AUTO_INCREMENT,
  `USER_ID` bigint NOT NULL,
  `SPOT_ID` bigint NOT NULL,
  `SONG_ID` bigint NOT NULL,
  `GIFT_IMG` varchar(200) NOT NULL,
  `IS_OPEN` tinyint(1) NOT NULL DEFAULT '1',
  `GIFT_TAG` varchar(100) DEFAULT NULL,
  `REG_TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `GIFT_LIKE` int NOT NULL DEFAULT '0',
  `GIFT_FEEDBACK1` int NOT NULL DEFAULT '0',
  `GIFT_FEEDBACK2` int NOT NULL DEFAULT '0',
  `GIFT_FEEDBACK3` int NOT NULL DEFAULT '0',
  `GIFT_FEEDBACK4` int NOT NULL DEFAULT '0',
  `IS_MANITO` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`GIFT_ID`),
  KEY `USER_ID` (`USER_ID`),
  KEY `SPOT_ID` (`SPOT_ID`),
  KEY `SONG_ID` (`SONG_ID`),
  CONSTRAINT `Gift_ibfk_1` FOREIGN KEY (`USER_ID`) REFERENCES `User` (`USER_ID`) ON DELETE CASCADE,
  CONSTRAINT `Gift_ibfk_2` FOREIGN KEY (`SPOT_ID`) REFERENCES `Spot` (`SPOT_ID`) ON DELETE CASCADE,
  CONSTRAINT `Gift_ibfk_3` FOREIGN KEY (`SONG_ID`) REFERENCES `Song` (`SONG_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Gift`
--

LOCK TABLES `Gift` WRITE;
/*!40000 ALTER TABLE `Gift` DISABLE KEYS */;
INSERT INTO `Gift` VALUES (1,4,1,1,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg',0,NULL,'2023-02-15 08:38:39',1,20,28,21,35,0),(4,1,1,1,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg',1,NULL,'2023-02-15 08:38:42',2,2,1,2,1,0),(5,14,1,1,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg',1,NULL,'2023-02-15 08:39:36',36,46,12,9,8,0),(6,14,1,2,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg',1,NULL,'2023-02-15 08:39:40',12,10,12,10,9,0),(7,14,1,3,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg',1,NULL,'2023-02-15 08:39:42',11,5,5,14,6,1),(10,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_105602.png',0,NULL,'2023-02-16 02:23:20',0,2,1,3,1,0),(11,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_112741.png',0,NULL,'2023-02-16 02:27:42',0,0,0,0,0,0),(12,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_112830.png',0,NULL,'2023-02-16 02:28:32',0,0,0,0,0,1),(13,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_113119.png',0,NULL,'2023-02-16 02:31:21',0,0,0,0,0,1),(14,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_113341.png',0,NULL,'2023-02-16 02:33:43',0,0,0,0,0,1),(15,19,1,1,'http://i8a402.p.ssafy.io/gift_images/1/230216_114005.png',0,NULL,'2023-02-16 02:40:07',0,1,2,2,2,1),(18,19,1,2,'http://i8a402.p.ssafy.io/gift_images/1/230216_180352.png',0,NULL,'2023-02-16 09:03:54',0,0,0,0,0,1),(24,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230216_220415.png',1,NULL,'2023-02-16 13:04:15',0,1,2,1,2,0),(25,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230217_000441.png',1,NULL,'2023-02-16 15:04:42',0,0,0,0,0,1),(26,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230217_102710.png',1,NULL,'2023-02-17 01:27:11',0,2,7,4,7,0),(27,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230217_105432.png',1,NULL,'2023-02-17 01:54:33',0,0,0,0,0,1),(28,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230217_111837.png',1,NULL,'2023-02-17 02:18:38',0,0,0,0,0,1),(29,19,1,4,'http://i8a402.p.ssafy.io/gift_images/1/230217_114024.png',1,NULL,'2023-02-17 02:40:24',0,0,0,0,0,1);
/*!40000 ALTER TABLE `Gift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Musicmate`
--

DROP TABLE IF EXISTS `Musicmate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Musicmate` (
  `MUSICMATE_ID` bigint NOT NULL AUTO_INCREMENT,
  `USER_ID` bigint NOT NULL,
  `MATE_ID` bigint NOT NULL,
  `IS_MATE` tinyint(1) NOT NULL DEFAULT '1',
  `IS_BLOCK` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`MUSICMATE_ID`),
  KEY `FK3pm5dpqt5le508wradpoproat` (`MATE_ID`),
  KEY `FKs77rdbjtr13tjx1ery13ef49f` (`USER_ID`),
  CONSTRAINT `FK3pm5dpqt5le508wradpoproat` FOREIGN KEY (`MATE_ID`) REFERENCES `User` (`USER_ID`),
  CONSTRAINT `FKs77rdbjtr13tjx1ery13ef49f` FOREIGN KEY (`USER_ID`) REFERENCES `User` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Musicmate`
--

LOCK TABLES `Musicmate` WRITE;
/*!40000 ALTER TABLE `Musicmate` DISABLE KEYS */;
INSERT INTO `Musicmate` VALUES (1,2,3,1,0),(2,12,1,1,0),(3,12,2,1,0),(6,5,7,1,0),(7,5,8,1,0),(16,14,18,1,0),(17,7,14,1,0);
/*!40000 ALTER TABLE `Musicmate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Postcard`
--

DROP TABLE IF EXISTS `Postcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Postcard` (
  `POSTCARD_ID` bigint NOT NULL AUTO_INCREMENT,
  `SEND_ID` bigint NOT NULL,
  `SPOT_ID` bigint NOT NULL,
  `SONG_ID` bigint NOT NULL,
  `POSTCARD_IMG` varchar(200) NOT NULL,
  `REG_TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`POSTCARD_ID`),
  KEY `SEND_ID` (`SEND_ID`),
  KEY `SPOT_ID` (`SPOT_ID`),
  KEY `SONG_ID` (`SONG_ID`),
  CONSTRAINT `Postcard_ibfk_1` FOREIGN KEY (`SEND_ID`) REFERENCES `User` (`USER_ID`) ON DELETE CASCADE,
  CONSTRAINT `Postcard_ibfk_2` FOREIGN KEY (`SPOT_ID`) REFERENCES `Spot` (`SPOT_ID`) ON DELETE CASCADE,
  CONSTRAINT `Postcard_ibfk_3` FOREIGN KEY (`SONG_ID`) REFERENCES `Song` (`SONG_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Postcard`
--

LOCK TABLES `Postcard` WRITE;
/*!40000 ALTER TABLE `Postcard` DISABLE KEYS */;
INSERT INTO `Postcard` VALUES (1,2,1,1,'IMGE PATH ~~~','2023-02-06 15:50:34',NULL),(20,18,1,1,'경로 이름','2023-02-17 01:18:37','안녕ㅎㅎ'),(21,18,1,1,'경로 이름','2023-02-17 01:50:02','안녕ㅎㅎgg'),(22,19,1,1,'경로 이름','2023-02-17 01:57:39','안녕adadaa'),(23,19,1,1,'../resource/saved_images/','2023-02-17 01:59:30','123456890'),(24,19,1,1,'../resource/saved_images/','2023-02-17 02:47:33','1234'),(25,19,1,1,'../resource/saved_images/','2023-02-17 02:48:54','100'),(26,19,1,1,'../resource/saved_images/230217_025252.png','2023-02-17 02:53:05','55555'),(27,19,1,4,'../resource/saved_images/230217_102754.png','2023-02-17 10:28:06','11111'),(28,19,1,4,'../resource/saved_images/230217_114216.png','2023-02-17 11:42:34','0000');
/*!40000 ALTER TABLE `Postcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Song`
--

DROP TABLE IF EXISTS `Song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Song` (
  `SONG_ID` bigint NOT NULL AUTO_INCREMENT,
  `SONG_IMG` varchar(200) NOT NULL,
  `SONG_TITLE` varchar(50) NOT NULL,
  `SINGER` varchar(50) NOT NULL,
  `SONG_URL` varchar(200) NOT NULL,
  PRIMARY KEY (`SONG_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Song`
--

LOCK TABLES `Song` WRITE;
/*!40000 ALTER TABLE `Song` DISABLE KEYS */;
INSERT INTO `Song` VALUES (1,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg','Ditto','New Jeans','https://www.youtube.com/watch?v=6bVUjsUi9sw'),(2,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg','hype boy','New Jeans','https://www.youtube.com/watch?v=11cta61wi0g'),(3,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg','hype boy','New Jeans','https://www.youtube.com/watch?v=11cta61wi0g'),(4,'https://cdn.discordapp.com/attachments/1056882470429138968/1068081563310506014/Notes_230126_170914.jpg','hype boy','New Jeans','https://www.youtube.com/watch?v=11cta61wi0g'),(5,'https://cdnimg.melon.co.kr/cm2/album/images/111/66/539/11166539_20230207143921_500.jpg','파이팅 해야지 (Feat. 이영지)','부석순 (SEVENTEEN)','https://www.youtube.com/watch?v=mBXBOLG06Wc'),(6,'https://cdnimg.melon.co.kr/cm2/album/images/109/03/868/10903868_20220330103544_500.jpg','사건의 지평선','윤하 (YOUNHA)','https://www.youtube.com/watch?v=BBdC1rl5sKY'),(7,'https://cdnimg.melon.co.kr/cm2/album/images/111/46/937/11146937_20230112154123_500.jpg','VIBE (feat. Jimin of BTS)','태양','https://www.youtube.com/watch?v=cXCBiF67jLM'),(8,'https://cdnimg.melon.co.kr/cm2/album/images/110/78/496/11078496_20221014153848_500.jpg','ANTIFRAGILE','LE SSERAFIM (르세라핌)','https://www.youtube.com/watch?v=pyf8cbqyfPs'),(9,'https://cdnimg.melon.co.kr/cm2/album/images/110/11/565/11011565_20220801102637_500.jpg','Attention','NewJeans','https://www.youtube.com/watch?v=js1CtxSY38I'),(10,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/153/11158153_20230126154403_500.jpg','Sugar Rush Ride','투모로우바이투게더','https://www.youtube.com/watch?v=cJ0WobKRPT8'),(11,'https://cdnimg.melon.co.kr/cm2/album/images/110/34/298/11034298_20220822101843_500.jpg','After LIKE','IVE (아이브)','https://www.youtube.com/watch?v=F0B7HDiY-10'),(12,'https://cdnimg.melon.co.kr/cm2/album/images/107/35/654/10735654_20211008114339_500.jpg','사랑은 늘 도망가','임영웅','https://www.youtube.com/watch?v=LKQ-18LoFQk'),(13,'https://cdnimg.melon.co.kr/cm2/album/images/111/24/139/11124139_20221215162633_500.jpg','Candy','NCT DREAM','https://www.youtube.com/watch?v=zuoSn3ObMz4'),(14,'https://cdnimg.melon.co.kr/cm2/album/images/111/15/007/11115007_20221202105416_500.jpg','마이웨이 (MY WAY) (Prod. R.Tee)','저스디스 (JUSTHIS)','https://www.youtube.com/watch?v=y4Ok11V6fz8'),(15,'https://cdnimg.melon.co.kr/cm2/album/images/111/15/359/11115359_20221202124614_500.jpg','잘가요','주호','https://www.youtube.com/watch?v=yfeaSjN1kSo'),(16,'https://cdnimg.melon.co.kr/cm2/album/images/110/00/171/11000171_20220708163659_500.jpg','그때 그 순간 그대로 (그그그)','WSG워너비 (가야G)','https://www.youtube.com/watch?v=kZvzjX35KxY'),(17,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/153/11158153_20230126154403_500.jpg','Happy Fools (feat. Coi Leray)','투모로우바이투게더','https://www.youtube.com/watch?v=OwRuCfYl_n4'),(18,'https://cdnimg.melon.co.kr/cm2/album/images/111/30/072/11130072_20221226144743_500.jpg','그댄 행복에 살텐데 (2022)','최유리','https://www.youtube.com/watch?v=mwTnWKAvFyo'),(19,'https://cdnimg.melon.co.kr/cm2/album/images/109/23/444/10923444_20220502140600_500.jpg','보금자리','임영웅','https://www.youtube.com/watch?v=Znpnf1HUmQ4'),(20,'https://cdnimg.melon.co.kr/cm2/album/images/109/95/477/10995477_20220701165440_500.jpg','그라데이션','10CM','https://www.youtube.com/watch?v=kQuxJbP6s8Y'),(21,'https://cdnimg.melon.co.kr/cm2/album/images/111/66/539/11166539_20230207143921_500.jpg','LUNCH','부석순 (SEVENTEEN)','https://www.youtube.com/watch?v=HBQXZjkh1_8'),(22,'https://cdnimg.melon.co.kr/cm2/album/images/106/10/525/10610525_20210518143433_500.jpg','다정히 내 이름을 부르면','경서예지','https://www.youtube.com/watch?v=b_6EfFZyBxY'),(23,'https://cdnimg.melon.co.kr/cm2/album/images/109/25/762/10925762_20220419152007_500.jpg','정이라고 하자 (Feat. 10CM)','BIG Naughty (서동현)','https://www.youtube.com/watch?v=DYrY1E4-9NI'),(24,'https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200918102847_500.jpg','Dynamite','방탄소년단','https://www.youtube.com/watch?v=gdZLi9oWNZg'),(25,'https://cdnimg.melon.co.kr/cm2/album/images/107/98/794/10798794_20211201113915_500.jpg','ELEVEN','IVE (아이브)','https://www.youtube.com/watch?v=--FmExEAsM8'),(26,'https://cdnimg.melon.co.kr/cm/album/images/101/49/492/10149492_500.jpg','모든 날, 모든 순간 (Every day, Every Moment)','폴킴','https://www.youtube.com/watch?v=1q_t6RNuH8c'),(27,'https://cdnimg.melon.co.kr/cm2/album/images/106/46/395/10646395_20210707141710_500.jpg','STAY','The Kid LAROI','https://www.youtube.com/watch?v=kTJczUoc26U'),(28,'https://cdnimg.melon.co.kr/cm2/album/images/107/78/556/10778556_20211116105621_500.jpg','오르트구름','윤하 (YOUNHA)','https://www.youtube.com/watch?v=cFgk2PMgPJ4'),(29,'https://cdnimg.melon.co.kr/cm2/album/images/109/22/231/10922231_20220527120653_500.jpg','HOT','세븐틴','https://www.youtube.com/watch?v=UIAncbsU1lY'),(30,'https://cdnimg.melon.co.kr/cm2/album/images/109/46/688/10946688_20220509134858_500.jpg','Good Boy Gone Bad','투모로우바이투게더','https://www.youtube.com/watch?v=Os_6c5j6YiQ'),(31,'https://cdnimg.melon.co.kr/cm2/album/images/109/08/834/10908834_20220404174407_500.jpg','봄여름가을겨울 (Still Life)','BIGBANG (빅뱅)','https://www.youtube.com/watch?v=eN5mG_yMDiM'),(32,'https://cdnimg.melon.co.kr/cm2/album/images/109/99/428/10999428_20220718113528_500.jpg','_WORLD','세븐틴','https://www.youtube.com/watch?v=jGjaL95ALVA'),(33,'https://cdnimg.melon.co.kr/cm2/album/images/106/82/284/10682284_20210817142421_500.jpg','LO$ER=LO♡ER','투모로우바이투게더','https://www.youtube.com/watch?v=JzODRUBBXpc'),(34,'https://cdnimg.melon.co.kr/cm2/album/images/106/82/284/10682284_20210817142421_500.jpg','교환일기 (두밧두 와리와리)','투모로우바이투게더','https://www.youtube.com/watch?v=sC9r-q62HZc'),(35,'https://cdnimg.melon.co.kr/cm2/album/images/111/72/485/11172485_20230210171815_500.jpg','Yesterday','박재범','https://www.youtube.com/watch?v=ATuP6CE0vxM'),(36,'https://cdnimg.melon.co.kr/cm2/album/images/111/59/047/11159047_20230127151002_500.jpg','친구로 지내다 보면 (Feat. 김민석 of 멜로망스)','BIG Naughty (서동현)','https://www.youtube.com/watch?v=j7PZv7Ni7pk'),(37,'https://cdnimg.melon.co.kr/cm2/album/images/106/17/217/10617217_20210531132328_500.jpg','0X1=LOVESONG (I Know I Love You) feat. Seori','투모로우바이투게더','https://www.youtube.com/watch?v=d5bbqKYu51w'),(38,'https://cdnimg.melon.co.kr/cm2/album/images/107/43/373/10743373_20211018161315_500.jpg','내 기쁨은 너가 벤틀리를 끄는 거야','김승민','https://www.youtube.com/watch?v=nhpteF75kg8'),(39,'https://cdnimg.melon.co.kr/cm2/album/images/110/62/828/11062828_20220923105240_500.jpg','그중에 그대를 만나','김호중','https://www.youtube.com/watch?v=Re-na85d8l0'),(40,'https://cdnimg.melon.co.kr/cm2/album/images/105/80/103/10580103_20211008114642_500.jpg','Off My Face','Justin Bieber','https://www.youtube.com/watch?v=ENjrJ_zyeUc'),(41,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/641/11158641_20230130141206_500.jpg','DJ','NCT 127','https://www.youtube.com/watch?v=OJeuyJfxw10'),(42,'https://cdnimg.melon.co.kr/cm2/album/images/109/99/428/10999428_20220718113528_500.jpg','돌고 돌아','세븐틴','https://www.youtube.com/watch?v=DgAAaV6xfrk'),(43,'https://cdnimg.melon.co.kr/cm2/album/images/106/48/182/10648182_20210709104950_500.jpg','Permission to Dance','방탄소년단','https://www.youtube.com/watch?v=CuklIb9d3fI'),(44,'https://cdnimg.melon.co.kr/cm/album/images/102/60/858/10260858_500.jpg','주저하는 연인들을 위해','잔나비','https://www.youtube.com/watch?v=5g4KsIizYhQ'),(45,'https://cdnimg.melon.co.kr/cm2/album/images/111/66/539/11166539_20230207143921_500.jpg','파이팅 해야지 (Feat. 이영지)','부석순 (SEVENTEEN)','https://www.youtube.com/watch?v=mBXBOLG06Wc'),(46,'https://cdnimg.melon.co.kr/cm2/album/images/109/03/868/10903868_20220330103544_500.jpg','사건의 지평선','윤하 (YOUNHA)','https://www.youtube.com/watch?v=BBdC1rl5sKY'),(47,'https://cdnimg.melon.co.kr/cm2/album/images/111/46/937/11146937_20230112154123_500.jpg','VIBE (feat. Jimin of BTS)','태양','https://www.youtube.com/watch?v=cXCBiF67jLM'),(48,'https://cdnimg.melon.co.kr/cm2/album/images/110/78/496/11078496_20221014153848_500.jpg','ANTIFRAGILE','LE SSERAFIM (르세라핌)','https://www.youtube.com/watch?v=pyf8cbqyfPs'),(49,'https://cdnimg.melon.co.kr/cm2/album/images/110/11/565/11011565_20220801102637_500.jpg','Attention','NewJeans','https://www.youtube.com/watch?v=js1CtxSY38I'),(50,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/153/11158153_20230126154403_500.jpg','Sugar Rush Ride','투모로우바이투게더','https://www.youtube.com/watch?v=cJ0WobKRPT8'),(51,'https://cdnimg.melon.co.kr/cm2/album/images/110/34/298/11034298_20220822101843_500.jpg','After LIKE','IVE (아이브)','https://www.youtube.com/watch?v=F0B7HDiY-10'),(52,'https://cdnimg.melon.co.kr/cm2/album/images/107/35/654/10735654_20211008114339_500.jpg','사랑은 늘 도망가','임영웅','https://www.youtube.com/watch?v=LKQ-18LoFQk'),(53,'https://cdnimg.melon.co.kr/cm2/album/images/111/24/139/11124139_20221215162633_500.jpg','Candy','NCT DREAM','https://www.youtube.com/watch?v=zuoSn3ObMz4'),(54,'https://cdnimg.melon.co.kr/cm2/album/images/111/15/007/11115007_20221202105416_500.jpg','마이웨이 (MY WAY) (Prod. R.Tee)','저스디스 (JUSTHIS)','https://www.youtube.com/watch?v=y4Ok11V6fz8'),(55,'https://cdnimg.melon.co.kr/cm2/album/images/111/15/359/11115359_20221202124614_500.jpg','잘가요','주호','https://www.youtube.com/watch?v=yfeaSjN1kSo'),(56,'https://cdnimg.melon.co.kr/cm2/album/images/110/00/171/11000171_20220708163659_500.jpg','그때 그 순간 그대로 (그그그)','WSG워너비 (가야G)','https://www.youtube.com/watch?v=kZvzjX35KxY'),(57,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/153/11158153_20230126154403_500.jpg','Happy Fools (feat. Coi Leray)','투모로우바이투게더','https://www.youtube.com/watch?v=OwRuCfYl_n4'),(58,'https://cdnimg.melon.co.kr/cm2/album/images/111/30/072/11130072_20221226144743_500.jpg','그댄 행복에 살텐데 (2022)','최유리','https://www.youtube.com/watch?v=mwTnWKAvFyo'),(59,'https://cdnimg.melon.co.kr/cm2/album/images/109/23/444/10923444_20220502140600_500.jpg','보금자리','임영웅','https://www.youtube.com/watch?v=Znpnf1HUmQ4'),(60,'https://cdnimg.melon.co.kr/cm2/album/images/109/95/477/10995477_20220701165440_500.jpg','그라데이션','10CM','https://www.youtube.com/watch?v=kQuxJbP6s8Y'),(61,'https://cdnimg.melon.co.kr/cm2/album/images/111/66/539/11166539_20230207143921_500.jpg','LUNCH','부석순 (SEVENTEEN)','https://www.youtube.com/watch?v=HBQXZjkh1_8'),(62,'https://cdnimg.melon.co.kr/cm2/album/images/106/10/525/10610525_20210518143433_500.jpg','다정히 내 이름을 부르면','경서예지','https://www.youtube.com/watch?v=b_6EfFZyBxY'),(63,'https://cdnimg.melon.co.kr/cm2/album/images/109/25/762/10925762_20220419152007_500.jpg','정이라고 하자 (Feat. 10CM)','BIG Naughty (서동현)','https://www.youtube.com/watch?v=DYrY1E4-9NI'),(64,'https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200918102847_500.jpg','Dynamite','방탄소년단','https://www.youtube.com/watch?v=gdZLi9oWNZg'),(65,'https://cdnimg.melon.co.kr/cm2/album/images/107/98/794/10798794_20211201113915_500.jpg','ELEVEN','IVE (아이브)','https://www.youtube.com/watch?v=--FmExEAsM8'),(66,'https://cdnimg.melon.co.kr/cm/album/images/101/49/492/10149492_500.jpg','모든 날, 모든 순간 (Every day, Every Moment)','폴킴','https://www.youtube.com/watch?v=1q_t6RNuH8c'),(67,'https://cdnimg.melon.co.kr/cm2/album/images/106/46/395/10646395_20210707141710_500.jpg','STAY','The Kid LAROI','https://www.youtube.com/watch?v=kTJczUoc26U'),(68,'https://cdnimg.melon.co.kr/cm2/album/images/107/78/556/10778556_20211116105621_500.jpg','오르트구름','윤하 (YOUNHA)','https://www.youtube.com/watch?v=cFgk2PMgPJ4'),(69,'https://cdnimg.melon.co.kr/cm2/album/images/109/22/231/10922231_20220527120653_500.jpg','HOT','세븐틴','https://www.youtube.com/watch?v=UIAncbsU1lY'),(70,'https://cdnimg.melon.co.kr/cm2/album/images/109/46/688/10946688_20220509134858_500.jpg','Good Boy Gone Bad','투모로우바이투게더','https://www.youtube.com/watch?v=Os_6c5j6YiQ'),(71,'https://cdnimg.melon.co.kr/cm2/album/images/109/08/834/10908834_20220404174407_500.jpg','봄여름가을겨울 (Still Life)','BIGBANG (빅뱅)','https://www.youtube.com/watch?v=eN5mG_yMDiM'),(72,'https://cdnimg.melon.co.kr/cm2/album/images/109/99/428/10999428_20220718113528_500.jpg','_WORLD','세븐틴','https://www.youtube.com/watch?v=jGjaL95ALVA'),(73,'https://cdnimg.melon.co.kr/cm2/album/images/106/82/284/10682284_20210817142421_500.jpg','LO$ER=LO♡ER','투모로우바이투게더','https://www.youtube.com/watch?v=JzODRUBBXpc'),(74,'https://cdnimg.melon.co.kr/cm2/album/images/106/82/284/10682284_20210817142421_500.jpg','교환일기 (두밧두 와리와리)','투모로우바이투게더','https://www.youtube.com/watch?v=sC9r-q62HZc'),(75,'https://cdnimg.melon.co.kr/cm2/album/images/111/72/485/11172485_20230210171815_500.jpg','Yesterday','박재범','https://www.youtube.com/watch?v=ATuP6CE0vxM'),(76,'https://cdnimg.melon.co.kr/cm2/album/images/111/59/047/11159047_20230127151002_500.jpg','친구로 지내다 보면 (Feat. 김민석 of 멜로망스)','BIG Naughty (서동현)','https://www.youtube.com/watch?v=j7PZv7Ni7pk'),(77,'https://cdnimg.melon.co.kr/cm2/album/images/106/17/217/10617217_20210531132328_500.jpg','0X1=LOVESONG (I Know I Love You) feat. Seori','투모로우바이투게더','https://www.youtube.com/watch?v=d5bbqKYu51w'),(78,'https://cdnimg.melon.co.kr/cm2/album/images/107/43/373/10743373_20211018161315_500.jpg','내 기쁨은 너가 벤틀리를 끄는 거야','김승민','https://www.youtube.com/watch?v=nhpteF75kg8'),(79,'https://cdnimg.melon.co.kr/cm2/album/images/110/62/828/11062828_20220923105240_500.jpg','그중에 그대를 만나','김호중','https://www.youtube.com/watch?v=Re-na85d8l0'),(80,'https://cdnimg.melon.co.kr/cm2/album/images/105/80/103/10580103_20211008114642_500.jpg','Off My Face','Justin Bieber','https://www.youtube.com/watch?v=ENjrJ_zyeUc'),(81,'https://cdnimg.melon.co.kr/cm2/album/images/111/58/641/11158641_20230130141206_500.jpg','DJ','NCT 127','https://www.youtube.com/watch?v=OJeuyJfxw10'),(82,'https://cdnimg.melon.co.kr/cm2/album/images/109/99/428/10999428_20220718113528_500.jpg','돌고 돌아','세븐틴','https://www.youtube.com/watch?v=DgAAaV6xfrk'),(83,'https://cdnimg.melon.co.kr/cm2/album/images/106/48/182/10648182_20210709104950_500.jpg','Permission to Dance','방탄소년단','https://www.youtube.com/watch?v=CuklIb9d3fI'),(84,'https://cdnimg.melon.co.kr/cm/album/images/102/60/858/10260858_500.jpg','주저하는 연인들을 위해','잔나비','https://www.youtube.com/watch?v=5g4KsIizYhQ');
/*!40000 ALTER TABLE `Song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SongMeta`
--

DROP TABLE IF EXISTS `SongMeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SongMeta` (
  `SONG_META_ID` bigint NOT NULL AUTO_INCREMENT,
  `SONG_ID` bigint NOT NULL,
  `SPOT_ID` bigint NOT NULL,
  `SONG_LIKED` int NOT NULL DEFAULT '0',
  `GIFT_CNT` int NOT NULL DEFAULT '0',
  `UPDATE_TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`SONG_META_ID`),
  KEY `FKvxkk5cf0u2nfhdmaesob2sr5` (`SONG_ID`),
  KEY `FKa4exbnfkcaxbl67lr72vkkl6i` (`SPOT_ID`),
  CONSTRAINT `FKa4exbnfkcaxbl67lr72vkkl6i` FOREIGN KEY (`SPOT_ID`) REFERENCES `Spot` (`SPOT_ID`),
  CONSTRAINT `FKvxkk5cf0u2nfhdmaesob2sr5` FOREIGN KEY (`SONG_ID`) REFERENCES `Song` (`SONG_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SongMeta`
--

LOCK TABLES `SongMeta` WRITE;
/*!40000 ALTER TABLE `SongMeta` DISABLE KEYS */;
INSERT INTO `SongMeta` VALUES (1,1,1,0,0,'2023-02-16 02:40:34'),(2,2,1,0,5,'2023-02-16 21:30:45'),(3,4,1,0,4,'2023-02-17 11:40:25');
/*!40000 ALTER TABLE `SongMeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Spot`
--

DROP TABLE IF EXISTS `Spot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Spot` (
  `SPOT_ID` bigint NOT NULL AUTO_INCREMENT,
  `SPOT_NAME` varchar(200) NOT NULL,
  `SPOT_ADDR` varchar(200) NOT NULL,
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SPOT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Spot`
--

LOCK TABLES `Spot` WRITE;
/*!40000 ALTER TABLE `Spot` DISABLE KEYS */;
INSERT INTO `Spot` VALUES (1,'멀캠점 (멀티캠퍼스 1201호)','멀티캠퍼스 1201호','');
/*!40000 ALTER TABLE `Spot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `USER_VIEW`
--

DROP TABLE IF EXISTS `USER_VIEW`;
/*!50001 DROP VIEW IF EXISTS `USER_VIEW`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `USER_VIEW` AS SELECT 
 1 AS `USER_ID`,
 1 AS `NICKNAME`,
 1 AS `PROFILE_IMG`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `USER_ID` bigint NOT NULL AUTO_INCREMENT,
  `NAME` varchar(20) NOT NULL,
  `TOKEN` varchar(200) DEFAULT NULL,
  `NICKNAME` varchar(100) NOT NULL,
  `PROFILE_MESSAGE` varchar(100) DEFAULT NULL,
  `PROFILE_IMG` varchar(200) NOT NULL DEFAULT 'https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',
  `EMAIL` varchar(50) DEFAULT NULL,
  `ROLE` varchar(20) DEFAULT NULL,
  `refresh_token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `NICKNAME` (`NICKNAME`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'sohee','abv12efw-- sedfwerg','sohee','안녕??','https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',NULL,NULL,NULL),(2,'gaok','abv12eqwqdfwerg','gaok',NULL,'https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',NULL,NULL,NULL),(3,'sungwhan','webv12ef1231','sungwhan',NULL,'https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',NULL,NULL,NULL),(4,'hosung','12wrtsedddfwerg','hosung',NULL,'https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',NULL,NULL,NULL),(5,'이가옥','Kakaodlrkdhr321@daum.net','닉네임 바꾸자!',NULL,'http://k.kakaocdn.net/dn/bb3Ng6/btrTz0Tq8Mh/ZRUC7JWSb2EdGtPvCoKOPK/img_640x640.jpg','dlrkdhr321@daum.net','ROLE_USER',NULL),(7,'김성환','Google110268871111520667205','나는성환',NULL,'https://lh3.googleusercontent.com/a/AEdFTp6qSlELPt4_lZ2i7C1MbhE5UAOCU2_5QJSpUTCL=s96-c','fanngineer@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjcsInJvbGUiOiJST0xFX1VTRVIiLCJuaWNrTmFtZSI6IuuCmOuKlOyEse2ZmCIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NjAxNjY5LCJleHAiOjE2ODQzNzc2Njl9.GzY9OY4mqAuoGb8dT_Zr-Zey47sVnrXK_S-ZyUcaBnc'),(8,'김성환','Kakaocjstk3795@nate.com','사용자8',NULL,'http://k.kakaocdn.net/dn/cOhsGy/btrLLiPDx6Y/XMO7d4D97RoKRKkXtwVkR1/img_640x640.jpg','cjstk3795@nate.com','ROLE_USER',NULL),(12,'이가옥','Google116700024119022074503','가옥',NULL,'https://lh3.googleusercontent.com/a/AEdFTp5p5LatU5dp1-_V-BhKg82hq7Ou4w5vZkYK7seJ=s96-c','dlrkdhr321@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEyLCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLqsIDsmKUiLCJ0eXBlIjoicmVmcmVzaCIsImlhdCI6MTY3NjUzMDU3MiwiZXhwIjoxNjg0MzA2NTcyfQ.5nxx_XWfYoa3CVdUwnqiJ9K72PaX-FLyJm-NZWQ39Ss'),(13,'sohee2','1029312347890132','sohee2 nickname',NULL,'https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927',NULL,NULL,NULL),(14,'밍밍','Google115065302997799389318','오기',NULL,'https://lh3.googleusercontent.com/a/AEdFTp6Sr5_wjMMcjtzZ1otLFQ2cdiq5Zru78hWwHvQM=s96-c','okkiiiie@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjE0LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsmKTquLAiLCJ0eXBlIjoicmVmcmVzaCIsImlhdCI6MTY3NjU5ODUyNCwiZXhwIjoxNjg0Mzc0NTI0fQ.SlhAP4cRf8TQl2NG08EzUxkqSZ0qarjyg_yoXD9ykbM'),(16,'김동현','Google105520423339007703815','사용자16',NULL,'https://lh3.googleusercontent.com/a/AEdFTp4W78YRf0ItYwyN5ul_UaUc0HmjKDt1APUNcSRg=s96-c','rlaehdgus1053@gmail.com','ROLE_USER',NULL),(17,'이수림','Kakaonull','우와!!!!!',NULL,'http://k.kakaocdn.net/dn/oNKyB/btqwIL0bEdY/SN4KVrOCr0LXukrJJVJjY0/img_640x640.jpg',NULL,'ROLE_USER',NULL),(18,'sohee yoon','Google117390672553383794650','역삼역 불주먹',NULL,'https://lh3.googleusercontent.com/a/AEdFTp7v4Wea3kTNDDqBkGts86LRC3zS3T-5fKemlhMa=s96-c','mandariny716@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjE4LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsl63sgrzsl60g67aI7KO866i5IiwidHlwZSI6InJlZnJlc2giLCJpYXQiOjE2NzY1OTYwNDYsImV4cCI6MTY4NDM3MjA0Nn0.HhohQvUE91KauLz0icnFrXMKiUrTUcglTKPqI8KPnfI'),(19,'신승호','Google105681488649028443446','사용자19',NULL,'https://lh3.googleusercontent.com/a/AEdFTp67qm45Jy-7lPeY16PcRscfjuV34mNPEK3BfNEkaA=s96-c','snghshn@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjE5LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAxOSIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NjAxNTY1LCJleHAiOjE2ODQzNzc1NjV9.mwb8eTUzwsjHMG0CYpomlv2PGFc5GxBR_WGM--Mvi38'),(20,'스윗펌킨','Google102312869021784191422','사용자20',NULL,'https://lh3.googleusercontent.com/a/AEdFTp46ZDHzDiZXb7gql-Uk1YFVCvvs_wGVT0dYY7-H4A=s96-c','moxnox63@gmail.com','ROLE_USER',NULL),(21,'김혜림','Kakaobljh1008@naver.com','사용자21',NULL,'http://k.kakaocdn.net/dn/Oto6J/btrXBayc1S5/XN71GPodjruqYyBn6Umn90/img_640x640.jpg','bljh1008@naver.com','ROLE_USER',NULL),(22,'이가옥','Kakao2653339856','키키',NULL,'http://k.kakaocdn.net/dn/bb3Ng6/btrTz0Tq8Mh/ZRUC7JWSb2EdGtPvCoKOPK/img_640x640.jpg','dlrkdhr321@daum.net','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjIyLCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLtgqTtgqQiLCJ0eXBlIjoicmVmcmVzaCIsImlhdCI6MTY3NjQ4ODUzNSwiZXhwIjoxNjg0MjY0NTM1fQ.tfeIvGKV5vYv55m3s5F5SOegiOe9uHKQT5ZOc1KBqX8'),(24,'윤소희','Kakao2669300458','사용자24',NULL,'http://k.kakaocdn.net/dn/KEUeB/btrQvYK0PVJ/xkgo3S89tF1okKx6FXIEA0/img_640x640.jpg',NULL,'ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI0LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyNCIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NTYwMDQ1LCJleHAiOjE2ODQzMzYwNDV9.yVEAT3cuPu4x2cYmIgff74O75TnBo2SI_MERO3NLnsw'),(25,'김호성','Kakao2654998510','사용자25',NULL,'http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg','dsrla123@naver.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI1LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyNSIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NjAxMjc4LCJleHAiOjE2ODQzNzcyNzh9.NjEtKatbT4Qt2liTB_woC32m_7jkJ-pH4n5ladHKutc'),(26,'곽준영','Google109973779296379053824','사용자26',NULL,'https://lh3.googleusercontent.com/a/AEdFTp57QGmjbh78R-yUZlQD8WL_wsX-2kkRJ9q1U7qp=s96-c','wnsdudrkwhr1@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI2LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyNiIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NjAwMTI1LCJleHAiOjE2ODQzNzYxMjV9.rDXuJhcI7ijCOG1KM4rLP8A6lZp0xyaFZmU9DaYRdSs'),(27,'이상현','Google110323146446838766833','사용자27',NULL,'https://lh3.googleusercontent.com/a/AEdFTp73E3tQ3f_BGQz6qdsTrHycQCgi54tkTIjkN5rPmQ=s96-c','megahawk88@gmail.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI3LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyNyIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NTk5ODY2LCJleHAiOjE2ODQzNzU4NjZ9.AQULNLb03Kj8gJB9kGcZdiyBlH2uo1wjuGqRMNzFJdY'),(28,'이상현(Ryan)','Kakao2669686778','사용자28',NULL,'http://k.kakaocdn.net/dn/ch6jSF/btrUJkjU3Id/s1d0acAEwuUW2Ce43CNBjk/img_640x640.jpg','megahawk@daum.net','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI4LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyOCIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NTk5ODg4LCJleHAiOjE2ODQzNzU4ODh9.jOAlA4jhOPvgVqbl_v3WO7b95fmnPP3Gj55n667Oc74'),(29,'김성환','Kakao2648903347','사용자29',NULL,'http://k.kakaocdn.net/dn/cOhsGy/btrLLiPDx6Y/XMO7d4D97RoKRKkXtwVkR1/img_640x640.jpg','cjstk3795@nate.com','ROLE_USER','eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjI5LCJyb2xlIjoiUk9MRV9VU0VSIiwibmlja05hbWUiOiLsgqzsmqnsnpAyOSIsInR5cGUiOiJyZWZyZXNoIiwiaWF0IjoxNjc2NjAxNDI5LCJleHAiOjE2ODQzNzc0Mjl9.KBkmyBmamn1EG1qdPB0eAndwakqWZF5l5aWgSvKogf8');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hibernate_sequence`
--

DROP TABLE IF EXISTS `hibernate_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hibernate_sequence` (
  `next_val` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hibernate_sequence`
--

LOCK TABLES `hibernate_sequence` WRITE;
/*!40000 ALTER TABLE `hibernate_sequence` DISABLE KEYS */;
INSERT INTO `hibernate_sequence` VALUES (29);
/*!40000 ALTER TABLE `hibernate_sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `user_nickname`
--

DROP TABLE IF EXISTS `user_nickname`;
/*!50001 DROP VIEW IF EXISTS `user_nickname`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_nickname` AS SELECT 
 1 AS `USER_ID`,
 1 AS `NICKNAME`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `user_view`
--

DROP TABLE IF EXISTS `user_view`;
/*!50001 DROP VIEW IF EXISTS `user_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_view` AS SELECT 
 1 AS `USER_ID`,
 1 AS `NICKNAME`,
 1 AS `PROFILE_IMG`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `USER_VIEW`
--

/*!50001 DROP VIEW IF EXISTS `USER_VIEW`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `USER_VIEW` AS select `User`.`USER_ID` AS `USER_ID`,`User`.`NICKNAME` AS `NICKNAME`,`User`.`PROFILE_IMG` AS `PROFILE_IMG` from `User` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_nickname`
--

/*!50001 DROP VIEW IF EXISTS `user_nickname`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_nickname` AS select `User`.`USER_ID` AS `USER_ID`,`User`.`NICKNAME` AS `NICKNAME` from `User` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_view`
--

/*!50001 DROP VIEW IF EXISTS `user_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_view` AS select `User`.`USER_ID` AS `USER_ID`,`User`.`NICKNAME` AS `NICKNAME`,`User`.`PROFILE_IMG` AS `PROFILE_IMG` from `User` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-17 11:45:53
