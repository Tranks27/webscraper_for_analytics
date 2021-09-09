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
-- Table structure for table `central_park`
--

DROP TABLE IF EXISTS `central_park`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `central_park` (
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
-- Dumping data for table `central_park`
--

LOCK TABLES `central_park` WRITE;
/*!40000 ALTER TABLE `central_park` DISABLE KEYS */;
INSERT INTO `central_park` VALUES ('1.85','13.00','2.50','2.90','4.40','6.00','3.50','3.80','16.00','5.50','8.50','11.00'),('7.00','7.00','2.60','-','2.30','2.20','2.05','8.00','11.00','4.50','5.00','6.50'),('5.50','9.00','15.00','8.00','9.00','7.00','11.00','7.00','7.00','2.45','3.20','5.00'),('5.50','5.50','6.00','2.50','8.00','3.80','8.00','2.60','3.80','7.00','-','34.00'),('41.00','2.15','12.00','4.20','7.00','8.00','12.00','8.00','1.65','8.50','3.60','1.60'),('6.00','3.30','7.00','6.50','4.80','7.50','6.00','4.40','13.00','5.00','3.50','7.00'),('6','6','4','1','4','4','2','4','4','6','3','6'),('2','1','5','5','2','1','6','1','6','1','2','1'),('4','4','2','4','1','2','5','6','5','3','6','2'),('4.40','-','8.00','4.00','2.90','8.00','3.00','6.50','3.00','4.80','3.70','-'),('12.00','-','3.50','1.95','3.30','9.00','3.50','7.00','8.00','8.50','7.00','-'),('2.30','-','2.90','7.00','16.00','5.50','7.50','12.00','3.00','2.90','3.20','-'),('8.00','-','6.50','14.00','9.50','5.50','7.00','7.50','3.80','7.50','6.00','-'),('3.20','-','3.90','12.00','2.90','5.50','6.00','4.80','8.00','5.00','9.00','-'),('9.00','-','9.00','4.40','9.00','1.95','4.50','1.75','10.00','3.50','3.50','-'),('3','-','1','4','5','5','2','6','5','1','4','-'),('4','-','3','6','2','6','1','5','2','3','6','-'),('1','-','2','2','1','4','4','4','3','2','2','-'),('2.80','4.40','5.00','5.00','4.40','6.00','6.50','21.00','8.50','4.40','6.50','5.50'),('9.50','3.10','8.00','2.50','8.00','17.00','9.50','-','4.20','9.50','2.70','3.50'),('7.00','8.00','2.50','8.50','3.50','3.30','3.80','3.00','6.00','5.50','2.90','10.00'),('4.40','9.00','6.50','7.00','5.00','8.00','6.00','3.50','3.80','3.30','11.00','7.00'),('4.50','2.90','5.50','10.00','8.50','13.00','7.00','9.00','4.20','3.50','14.00','4.20'),('4.40','7.00','4.50','3.00','3.10','1.90','2.25','2.50','3.80','6.00','3.90','2.90'),('1','2','1','6','3','3','6','3','6','6','6','3'),('2','5','3','4','4','6','1','5','2','5','3','6'),('4','3','2','5','1','1','4','4','5','2','1','1'),('8.00','9.50','7.00','4.40','4.20','8.00','3.90','3.50','2.10','8.00','12.00','-'),('6.50','3.00','8.00','3.40','6.50','3.60','6.50','2.40','-','3.90','-','-'),('12.00','2.60','3.50','6.00','11.00','3.30','4.80','8.00','2.10','8.00','1.45','-'),('2.25','4.00','8.00','2.80','2.80','8.50','8.00','4.50','11.00','2.80','-','-'),('4.20','16.00','11.00','7.50','3.00','9.00','4.80','10.00','13.00','7.50','5.50','-'),('4.40','7.50','1.90','11.00','8.00','3.00','3.00','8.00','9.00','3.60','4.80','-'),('4','3','4','2','1','4','6','3','3','5','3','-'),('6','1','1','1','4','6','5','4','1','1','5','-'),('5','2','6','4','5','1','3','2','4','2','1','-'),('8.00','8.00','3.20','2.20','7.00','7.00','4.20','8.00','3.90','-','2.90','1.55'),('1.75','19.00','8.00','6.50','2.70','5.50','4.20','3.30','6.50','-','10.00','7.00'),('6.00','8.00','4.40','8.00','-','5.50','4.40','9.00','2.90','-','8.00','13.00'),('11.00','2.50','2.90','4.00','3.00','5.50','3.60','12.00','7.00','-','15.00','4.50'),('4.40','6.00','7.00','6.00','8.00','3.50','3.50','11.00','6.00','-','2.00','12.00'),('11.00','2.50','8.00','8.00','3.90','3.60','-','1.90','4.20','-','7.00','9.00'),('2','6','5','4','2','5','1','6','3','-','1','2'),('3','5','1','1','4','4','5','2','6','-','5','1'),('1','1','2','5','6','6','4','5','1','-','3','5');
/*!40000 ALTER TABLE `central_park` ENABLE KEYS */;
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
