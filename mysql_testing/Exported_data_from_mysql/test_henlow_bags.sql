-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `henlow_bags`
--

DROP TABLE IF EXISTS `henlow_bags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `henlow_bags` (
  `R1` char(5) DEFAULT NULL,
  `R2` char(5) DEFAULT NULL,
  `R3` char(5) DEFAULT NULL,
  `R4` char(5) DEFAULT NULL,
  `R5` char(5) DEFAULT NULL,
  `R6` char(5) DEFAULT NULL,
  `R7` char(5) DEFAULT NULL,
  `R8` char(5) DEFAULT NULL,
  `R9` char(5) DEFAULT NULL,
  `R10` char(5) DEFAULT NULL,
  `R11` char(5) DEFAULT NULL,
  `R12` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `henlow_bags`
--

LOCK TABLES `henlow_bags` WRITE;
/*!40000 ALTER TABLE `henlow_bags` DISABLE KEYS */;
INSERT INTO `henlow_bags` VALUES ('-','3.40','4.40','5.50','3.50','4.40','10.00','4.00','5.00','3.10','8.00','5.00'),('2.80','3.60','4.00','8.00','5.00','3.00','3.80','6.00','8.00','8.50','4.20','3.20'),('4.00','9.00','3.40','3.30','6.00','4.60','3.20','3.20','3.10','4.50','5.50','11.00'),('-','3.90','2.40','5.00','8.50','6.00','6.00','2.50','8.00','8.00','3.30','8.00'),('2.25','16.00','16.00','2.60','9.00','6.00','3.10','7.50','3.70','3.00','9.50','2.90'),('6.00','3.30','14.00','8.50','2.60','6.00','9.50','-','4.40','6.50','2.90','5.00'),('2','1','4','3','2','2','4','1','3','3','6','5'),('6','4','2','5','3','3','3','2','1','1','4','2'),('5','2','3','4','1','5','1','5','6','2','1','4'),('2.90','4.00','2.60','5.00','4.80','7.00','4.40','8.00','1.80','4.80','-','-'),('4.00','3.40','5.50','3.60','3.40','3.70','7.50','2.60','6.00','7.50','-','-'),('8.00','-','3.50','4.80','16.00','5.00','3.60','3.90','7.00','2.70','-','-'),('12.00','2.50','4.40','3.60','2.90','3.40','2.70','6.50','6.50','5.50','-','-'),('6.00','5.00','16.00','16.00','-','4.60','6.00','5.00','8.00','3.50','-','-'),('3.20','11.00','6.50','4.00','3.10','6.00','9.00','6.00','7.00','10.00','-','-'),('1','4','1','3','1','2','4','2','4','3','-','-'),('2','5','2','2','2','1','1','1','1','5','-','-'),('4','1','5','4','4','5','2','6','3','2','-','-'),('3.80','4.50','2.50','2.90','5.50','3.30','1.70','4.50','4.60','5.00','-','-'),('5.00','4.80','9.50','8.50','5.00','2.60','6.00','4.00','4.20','6.00','-','-'),('7.00','7.00','2.80','3.10','6.00','5.50','7.00','6.00','4.20','3.50','-','-'),('3.90','3.50','8.00','8.00','11.00','5.50','9.00','4.50','6.50','7.00','-','-'),('4.80','4.40','7.00','7.00','2.90','12.00','8.00','3.60','2.50','3.10','-','-'),('4.60','5.00','6.00','4.50','3.50','7.00','7.00','7.00','-','7.00','-','-'),('3','4','4','3','3','2','1','3','5','2','-','-'),('4','1','1','2','1','3','3','4','1','3','-','-'),('1','3','3','1','6','4','2','1','2','5','-','-');
/*!40000 ALTER TABLE `henlow_bags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-08  0:16:40
