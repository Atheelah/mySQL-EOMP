-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: lifechoicesonline
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `No` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `ID` varchar(13) DEFAULT NULL,
  `date_time_in` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `date_time_out` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Apples','fruit@gmail.com','1234567890','1234567890012','2021-07-10 20:30:00','2021-07-10 20:30:00'),(2,'Green','color@gmail.com','1234567890','1234567890012','2021-07-10 20:31:11','2021-07-10 20:31:11'),(3,'Atheelah','atheelahvanderschyff17@gmail.com','0722786174','0007170122084','2021-07-10 20:32:10','2021-07-10 20:32:10'),(4,'Abdurazak','zakkie.arendse.aa@gmail.com','0660916857','9604047206251','2021-07-10 20:33:22','2021-07-10 20:33:22'),(5,'Wahleed','wahleedkamies@gmail.com','0780445283','7106245300080','2021-07-10 21:09:54','2021-07-10 21:09:21');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nextofkin`
--

DROP TABLE IF EXISTS `nextofkin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nextofkin` (
  `No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `UserNo` int NOT NULL,
  PRIMARY KEY (`No`),
  KEY `UserNo` (`UserNo`),
  CONSTRAINT `nextofkin_ibfk_1` FOREIGN KEY (`UserNo`) REFERENCES `User` (`No`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nextofkin`
--

LOCK TABLES `nextofkin` WRITE;
/*!40000 ALTER TABLE `nextofkin` DISABLE KEYS */;
INSERT INTO `nextofkin` VALUES (28,'Banana','1234567890',1),(29,'Red','1234567890',2),(30,'Kader','0835170213',3),(31,'Aziza','0753698215',4),(32,'Nazeem','0833531212',5);
/*!40000 ALTER TABLE `nextofkin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 10:09:26
