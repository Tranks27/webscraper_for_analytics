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
-- Table structure for table `nottingham_bags`
--

DROP TABLE IF EXISTS `nottingham_bags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nottingham_bags` (
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
-- Dumping data for table `nottingham_bags`
--

LOCK TABLES `nottingham_bags` WRITE;
/*!40000 ALTER TABLE `nottingham_bags` DISABLE KEYS */;
INSERT INTO `nottingham_bags` VALUES ('5.00','13.00','9.50','7.50','4.20','7.00','8.00','20.00','15.00','8.00','3.20','3.40'),('3.80','3.40','2.40','4.00','5.50','5.00','10.00','-','6.50','4.20','21.00','3.40'),('9.00','4.20','9.00','8.00','4.00','21.00','8.50','1.40','21.00','3.70','13.00','-'),('6.50','8.50','4.00','-','4.20','2.25','1.70','14.00','2.00','2.25','2.60','5.50'),('2.40','3.50','6.00','1.85','9.00','4.40','14.00','5.50','3.20','11.00','10.00','6.00'),('8.00','6.00','4.50','6.00','3.80','8.50','5.50','7.50','9.50','-','4.00','4.40'),('2','5','2','5','6','5','6','3','5','2','4','1'),('4','3','3','6','4','1','4','5','4','4','3','6'),('6','2','4','3','3','3','5','6','6','5','6','2'),('9.00','5.00','3.40','8.00','3.00','3.50','6.00','2.80','4.00','13.00','-','-'),('3.20','10.00','3.70','5.00','4.20','4.40','7.50','4.20','-','3.30','-','-'),('11.00','4.60','3.80','6.00','5.00','7.50','8.50','8.50','8.00','11.00','-','-'),('1.90','16.00','13.00','2.90','4.40','8.50','10.00','5.50','2.30','2.25','-','-'),('16.00','15.00','7.50','3.10','-','5.50','2.30','7.00','10.00','4.60','-','-'),('5.00','1.60','4.20','8.00','4.40','3.10','3.00','4.00','3.00','7.50','-','-'),('4','6','2','2','2','6','3','1','4','5','-','-'),('6','2','1','6','3','3','6','2','3','4','-','-'),('5','1','6','5','4','1','1','4','1','2','-','-'),('2.60','17.00','8.50','3.20','5.50','5.50','3.60','5.50','3.30','3.90','-','-'),('12.00','5.50','8.50','4.50','10.00','3.80','7.00','2.80','6.00','3.20','-','-'),('8.00','7.50','3.30','3.80','5.50','8.50','5.50','10.00','4.60','4.60','-','-'),('4.50','3.00','6.00','14.00','4.50','4.40','7.00','7.50','5.00','5.50','-','-'),('6.50','9.50','2.50','6.00','10.00','4.20','3.60','3.50','3.60','8.00','-','-'),('3.20','2.15','6.00','3.90','2.05','3.40','3.80','4.50','9.50','6.00','-','-'),('1','4','5','6','6','6','1','2','3','2','-','-'),('3','6','3','1','3','2','6','3','1','6','-','-'),('6','3','2','2','1','5','5','4','5','1','-','-'),('13.00','5.00','13.00','6.00','7.00','11.00','6.00','10.00','4.60','4.40','9.00','4.50'),('2.80','8.50','3.80','6.50','7.00','9.00','5.50','7.50','3.30','6.50','8.00','3.00'),('4.40','4.40','2.70','-','7.00','10.00','4.20','9.00','12.00','9.00','8.00','6.00'),('4.20','3.30','12.00','4.50','3.70','6.00','6.50','1.65','2.70','2.90','4.80','5.00'),('9.50','4.50','7.50','4.50','2.80','1.75','7.00','5.00','9.00','8.00','1.65','11.00'),('3.50','4.60','2.70','2.05','4.40','4.20','2.45','6.00','5.50','3.10','9.50','3.40'),('2','6','2','4','2','6','2','2','2','3','2','6'),('6','4','6','6','1','5','3','5','1','6','4','2'),('1','5','5','5','4','3','5','6','6','5','5','3'),('3.60','3.00','-','9.00','11.00','9.00','1.75','3.60','9.00','9.50','3.60','4.60'),('3.80','7.50','3.00','7.00','2.60','6.50','21.00','2.60','2.90','1.65','3.40','7.50'),('6.50','7.00','5.00','1.90','2.00','1.80','2.80','3.00','4.80','7.00','3.70','-'),('8.00','3.50','4.80','6.00','8.00','7.50','8.00','11.00','3.70','15.00','5.00','4.00'),('6.50','4.00','9.00','9.00','-','11.00','17.00','3.30','17.00','26.00','8.50','-'),('3.30','8.00','2.70','9.00','17.00','8.50','26.00','10.00','15.00','6.00','7.00','3.50'),('6','1','4','3','2','2','1','5','3','1','2','1'),('5','5','2','2','6','3','2','2','2','6','3','2'),('1','2','3','1','1','6','6','1','4','2','6','3'),('6.50','4.80','3.40','8.00','2.70','4.00','2.25','7.00','2.40','2.90','-','-'),('2.50','2.80','8.50','4.00','7.50','4.60','7.50','3.40','6.50','7.00','-','-'),('8.00','4.40','8.50','3.70','10.00','6.50','5.00','9.00','5.00','8.00','-','-'),('3.50','8.00','8.50','4.00','3.40','4.00','7.50','8.00','3.50','8.50','-','-'),('6.00','5.00','2.70','4.00','8.00','8.00','7.50','3.40','8.50','3.20','-','-'),('7.00','6.50','3.90','6.50','4.20','3.60','4.40','3.30','10.00','4.40','-','-'),('2','4','6','5','4','5','1','2','3','1','-','-'),('1','6','1','4','6','2','2','6','4','5','-','-'),('6','2','4','3','5','1','3','1','2','6','-','-'),('4.50','6.00','3.30','6.00','5.00','3.90','13.00','8.00','2.70','6.50','-','-'),('5.00','8.50','7.50','4.60','3.90','3.40','5.50','9.00','11.00','4.40','-','-'),('4.00','3.30','1.90','5.50','6.50','6.00','7.00','5.00','3.00','3.60','-','-'),('8.50','5.00','10.00','19.00','8.00','11.00','9.00','5.50','6.00','3.80','-','-'),('4.20','8.50','6.50','8.00','3.40','4.60','1.50','2.60','14.00','12.00','-','-'),('4.20','2.60','17.00','1.85','4.00','4.20','11.00','3.70','4.20','3.80','-','-'),('1','1','5','1','2','5','5','3','1','5','-','-'),('5','2','3','5','5','6','2','4','6','3','-','-'),('4','6','2','6','3','1','3','1','3','1','-','-'),('9.50','2.70','5.50','3.50','6.50','6.50','12.00','3.80','7.00','8.00','2.70','5.50'),('7.00','6.50','5.00','5.50','3.00','6.00','7.00','4.80','6.00','7.00','9.00','5.50'),('4.40','4.40','2.80','3.20','4.80','13.00','2.70','9.00','6.50','5.00','7.00','2.70'),('3.10','8.00','6.00','5.50','8.50','2.15','3.60','2.30','4.00','2.60','5.00','12.00'),('4.50','8.50','5.00','13.00','3.00','4.50','7.00','8.00','4.40','8.50','3.70','2.35'),('4.00','3.50','5.50','3.90','8.00','5.00','3.70','8.00','2.90','3.20','6.00','-'),('4','5','5','1','1','5','5','4','6','3','3','3'),('5','6','3','2','3','2','4','1','1','4','5','5'),('3','3','4','6','6','1','6','2','2','6','4','2'),('1.80','4.00','4.20','4.50','7.50','7.00','4.80','1.40','9.50','3.70','8.50','4.00'),('5.00','9.50','5.50','4.50','21.00','4.50','5.00','21.00','34.00','10.00','3.40','10.00'),('7.00','3.50','4.80','7.00','1.95','3.70','4.00','17.00','2.80','2.35','4.40','1.70'),('8.00','5.50','5.50','3.70','12.00','5.00','4.00','8.00','19.00','9.00','2.70','16.00'),('10.00','7.00','4.40','3.90','19.00','4.20','4.20','10.00','9.50','7.00','21.00','8.00'),('6.50','3.30','3.90','12.00','2.80','5.00','16.00','7.00','1.85','7.00','8.50','17.00'),('1','6','6','1','6','5','4','1','5','3','6','2'),('4','3','1','3','4','6','3','4','6','1','2','5'),('6','2','2','6','3','4','1','6','3','5','5','6');
/*!40000 ALTER TABLE `nottingham_bags` ENABLE KEYS */;
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
