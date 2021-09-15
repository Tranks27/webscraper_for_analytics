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
-- Table structure for table `towcester_bags`
--

DROP TABLE IF EXISTS `towcester_bags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `towcester_bags` (
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
-- Dumping data for table `towcester_bags`
--

LOCK TABLES `towcester_bags` WRITE;
/*!40000 ALTER TABLE `towcester_bags` DISABLE KEYS */;
INSERT INTO `towcester_bags` VALUES ('7.00','6.00','5.50','13.00','3.50','4.80','2.70','19.00','6.00','7.00','26.00','7.50'),('4.80','2.25','2.20','1.28','4.20','3.10','2.20','8.50','5.50','8.50','3.50','12.00'),('9.50','6.00','7.00','21.00','6.00','4.40','18.00','91.00','4.00','10.00','3.30','13.00'),('1.75','7.00','16.00','7.50','3.20','9.50','12.00','31.00','3.70','7.00','2.35','3.40'),('5.50','3.20','7.00','5.00','7.00','6.50','5.00','3.00','5.50','19.00','7.00','5.50'),('12.00','20.00','3.30','21.00','7.00','4.00','9.00','1.60','4.40','1.45','-','2.00'),('4','2','6','5','1','6','1','5','6','4','2','5'),('5','5','2','2','4','1','5','6','4','5','5','6'),('3','3','1','3','5','3','2','1','1','6','1','4'),('6.00','4.60','6.50','3.10','3.20','11.00','3.20','6.00','13.00','5.50','4.00','-'),('3.70','7.00','10.00','2.80','6.50','2.90','3.20','2.90','-','3.20','2.90','-'),('5.50','4.80','2.80','3.50','6.50','-','4.60','3.30','1.90','4.00','4.80','-'),('3.10','10.00','3.30','3.30','2.20','7.00','5.00','4.40','-','8.00','-','-'),('4.50','7.00','7.00','6.50','4.60','7.00','4.80','6.00','3.50','5.50','4.80','-'),('8.00','2.00','4.50','8.00','8.00','4.60','8.50','9.00','8.00','3.20','8.00','-'),('5','6','5','2','3','5','5','4','3','2','2','-'),('2','3','6','5','1','2','4','1','6','5','5','-'),('1','5','3','1','2','4','3','2','4','1','1','-'),('4.00','7.00','4.80','7.00','2.90','3.00','6.50','3.00','-','-','4.00','5.00'),('6.00','3.20','7.00','5.00','5.00','5.00','6.50','4.00','8.00','2.90','5.50','2.30'),('2.70','3.30','2.60','9.50','7.00','5.00','5.00','-','2.10','4.60','2.05','3.60'),('8.50','3.20','8.00','3.20','8.00','4.20','7.00','4.50','5.50','2.45','7.50','-'),('12.00','6.00','3.50','3.60','5.50','4.60','4.00','3.20','8.00','15.00','3.60','-'),('3.50','-','9.00','2.15','5.50','9.00','2.30','6.00','8.00','8.00','7.50','3.20'),('3','5','3','6','1','1','6','2','3','4','3','5'),('5','3','6','3','6','5','4','5','4','3','1','2'),('4','1','5','1','3','2','5','1','5','5','4','1'),('8.50','5.00','15.00','5.00','3.60','3.00','5.00','3.70','3.70','5.00','5.00','5.00'),('4.80','9.00','5.50','7.00','5.50','4.80','4.40','5.00','4.40','3.50','2.70','5.00'),('7.00','4.50','3.10','9.00','5.00','5.50','4.80','3.20','5.00','4.40','7.00','2.25'),('1.85','3.70','15.00','2.15','4.50','3.60','2.30','4.00','4.20','7.00','7.00','8.00'),('9.00','5.00','3.00','13.00','9.00','7.00','21.00','14.00','5.50','3.90','9.00','8.50'),('6.50','3.70','3.40','3.70','3.50','8.00','7.00','5.50','6.00','6.00','3.40','5.00'),('4','6','3','6','3','1','3','6','1','2','6','6'),('3','3','5','4','4','4','2','1','4','6','5','4'),('2','2','6','3','2','2','4','5','2','5','4','5'),('7.50','6.50','1.40','5.50','26.00','3.80','21.00','3.20','3.30','15.00','9.00','11.00'),('2.60','12.00','7.50','18.00','2.00','3.50','3.70','21.00','5.50','2.35','6.50','8.50'),('14.00','9.50','4.50','11.00','3.30','15.00','3.40','3.40','5.00','2.50','3.30','8.00'),('17.00','1.60','-','7.00','4.20','26.00','2.60','9.50','2.35','8.50','16.00','4.50'),('3.30','5.00','34.00','1.35','9.50','3.90','8.50','16.00','13.00','6.00','2.50','2.80'),('3.70','10.00','8.00','26.00','2.90','7.00','2.50','13.00','11.00','4.40','2.70','-'),('5','4','1','5','3','1','4','3','1','6','3','6'),('6','5','6','3','4','4','5','5','2','3','6','1'),('2','1','2','4','2','6','1','2','3','5','2','4'),('5.50','9.00','4.60','4.60','3.40','11.00','3.90','12.00','9.00','5.00','3.80','3.80'),('9.50','3.70','3.90','3.20','7.00','5.00','3.30','5.50','6.00','7.50','2.10','4.80'),('6.50','3.80','3.50','5.00','4.00','3.30','6.50','6.00','3.50','3.10','9.00','8.00'),('1.80','3.30','3.70','6.00','8.00','5.50','2.90','3.20','8.50','6.50','6.00','1.90'),('9.00','10.00','11.00','6.00','2.70','3.60','12.00','15.00','4.50','4.80','13.00','14.00'),('6.50','3.70','6.00','4.60','9.00','4.80','7.00','2.15','2.60','3.70','5.00','8.00'),('4','6','2','3','2','6','4','4','6','3','6','1'),('5','4','4','1','5','4','1','6','3','6','1','4'),('6','2','3','4','6','3','6','1','1','4','4','2'),('3.50','6.00','3.10','3.50','3.70','5.50','12.00','4.60','4.20','11.00','-','-'),('3.50','2.80','3.30','6.00','5.00','10.00','4.20','4.00','4.50','5.50','-','-'),('12.00','4.00','6.00','3.90','4.00','3.50','7.00','2.20','5.00','3.80','-','-'),('4.40','7.00','11.00','7.50','6.00','2.80','5.50','8.00','5.50','3.50','-','-'),('6.00','4.40','3.70','3.70','8.00','7.00','4.00','9.50','4.00','3.80','-','-'),('4.60','8.00','9.00','6.00','3.70','4.80','2.70','8.00','5.50','5.50','-','-'),('2','2','1','5','1','4','5','3','5','4','-','-'),('5','3','5','1','4','5','6','2','1','6','-','-'),('4','1','4','3','6','3','4','1','2','2','-','-'),('2.90','7.50','4.00','9.00','4.40','4.00','7.00','2.50','3.20','7.50','3.70','2.70'),('14.00','4.50','11.00','11.00','17.00','6.50','9.00','5.00','9.00','3.50','3.20','5.00'),('2.70','6.00','2.05','1.70','3.30','5.00','5.00','8.00','4.00','4.80','4.40','8.00'),('3.30','2.80','4.50','5.50','3.20','4.20','2.80','7.00','3.00','4.40','5.00','2.90'),('14.00','3.50','13.00','7.50','16.00','4.50','9.00','9.00','7.00','5.50','14.00','11.00'),('7.50','8.50','8.00','5.50','3.30','4.40','2.60','3.30','7.00','3.80','4.50','8.00'),('3','1','2','3','6','6','2','1','4','2','2','1'),('4','5','6','6','3','5','5','6','1','6','5','4'),('6','4','4','5','1','4','6','4','3','1','3','6'),('1.90','5.50','6.00','3.50','2.50','2.90','20.00','3.60','2.45','2.00','7.50','9.00'),('15.00','8.50','9.50','-','7.00','8.00','1.35','7.50','12.00','6.50','4.00','4.40'),('7.50','21.00','10.00','4.80','7.00','7.50','2.70','9.50','6.00','20.00','8.00','-'),('19.00','2.45','6.50','3.30','3.40','3.70','31.00','6.00','9.00','8.50','4.00','4.00'),('13.00','4.60','6.00','6.00','9.00','3.80','5.50','4.50','1.95','4.60','2.50','4.80'),('2.60','3.70','1.80','4.00','3.70','8.00','8.50','10.00','26.00','8.50','5.00','2.90'),('6','4','6','1','1','1','2','5','5','2','4','5'),('1','5','5','6','4','2','3','3','2','6','2','6'),('3','6','4','5','6','5','1','4','3','1','5','3'),('5.00','5.00','6.00','7.00','5.00','2.70','7.00','5.50','5.00','4.40','3.00','-'),('7.00','1.80','7.00','6.50','2.60','4.00','4.50','3.00','-','8.00','3.50','-'),('5.50','16.00','12.00','9.00','6.00','8.00','3.00','3.00','5.50','9.00','9.00','-'),('3.30','7.00','5.00','5.00','5.00','4.40','12.00','8.00','2.30','6.00','5.50','-'),('8.00','7.50','1.90','2.50','5.50','9.00','4.60','4.50','TBD','4.80','11.00','-'),('3.10','5.50','6.00','3.70','7.00','5.50','3.70','12.00','8.50','2.35','4.00','-'),('6','4','5','5','2','1','6','2','1','3','1','-'),('5','5','4','4','5','3','2','3','6','1','2','-'),('1','6','1','6','4','4','5','4','4','2','5','-');
/*!40000 ALTER TABLE `towcester_bags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-09 11:42:22