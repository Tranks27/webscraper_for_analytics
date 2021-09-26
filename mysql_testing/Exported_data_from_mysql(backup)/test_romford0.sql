-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
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
-- Table structure for table `romford`
--

DROP TABLE IF EXISTS `romford`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `romford` (
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
-- Dumping data for table `romford`
--

LOCK TABLES `romford` WRITE;
/*!40000 ALTER TABLE `romford` DISABLE KEYS */;
INSERT INTO `romford` VALUES ('4.00','10.00','8.50','6.50','11.00','4.80','7.00','5.00','6.00','4.00','9.00','3.50'),('7.00','2.40','3.30','3.70','4.00','7.00','3.30','4.00','4.00','4.00','3.90','3.80'),('10.00','4.80','3.80','5.00','8.00','4.00','6.00','2.35','3.50','4.40','5.00','4.60'),('4.00','12.00','11.00','7.50','2.80','4.50','3.20','6.00','11.00','7.00','3.50','8.00'),('4.50','6.50','4.00','3.60','6.00','4.00','5.00','7.00','9.00','18.00','4.00','4.60'),('3.30','3.40','3.60','4.50','3.50','4.60','7.00','11.00','2.60','2.90','6.00','4.40'),('2','5','5','5','6','4','4','1','1','1','2','1'),('4','6','1','2','2','5','5','2','2','3','4','2'),('1','1','6','4','4','6','2','6','6','2','1','5'),('7.50','2.25','5.00','8.50','3.50','2.90','5.00','2.10','2.50','4.40','3.30','2.25'),('4.50','7.00','7.00','8.00','6.50','5.50','8.00','13.00','8.00','4.00','8.00','7.50'),('5.50','6.00','3.30','2.60','3.50','4.00','4.00','3.90','6.00','15.00','4.40','4.50'),('3.40','6.50','6.00','6.50','5.50','7.50','12.00','6.50','2.60','3.80','2.25','4.00'),('4.20','10.00','3.00','3.10','6.00','10.00','2.70','7.00','15.00','3.10','8.00','11.00'),('4.80','4.00','7.00','5.50','4.80','3.50','4.00','6.00','6.50','5.50','16.00','7.00'),('6','4','4','5','1','6','5','6','4','6','4','1'),('5','6','3','2','2','1','6','2','3','5','1','2'),('2','1','6','4','5','5','3','5','1','3','3','3'),('12.00','9.50','6.50','5.50','3.70','1.50','3.50','4.40','4.50','5.00','4.40','3.70'),('4.00','3.00','5.00','1.75','5.50','4.50','17.00','4.60','3.50','7.50','5.50','5.00'),('2.20','2.90','6.50','19.00','8.50','21.00','3.30','3.20','-','4.80','12.00','20.00'),('6.00','17.00','2.10','18.00','4.20','16.00','4.50','3.00','6.00','4.50','3.70','3.40'),('13.00','2.80','5.50','4.20','6.50','7.00','5.50','18.00','5.00','3.40','3.30','2.50'),('4.20','17.00','13.00','7.00','3.60','7.00','4.50','7.50','3.00','5.00','5.00','-'),('3','3','5','2','6','1','5','4','4','5','1','4'),('1','1','4','1','4','6','1','2','6','6','4','5'),('6','2','3','6','3','5','2','3','2','1','6','1'),('7.00','7.00','7.00','8.00','8.00','2.90','5.00','5.50','8.50','4.00','6.50','-'),('5.00','3.40','4.50','2.90','9.00','4.50','4.80','12.00','3.00','3.30','2.45','-'),('3.00','7.00','5.00','4.50','3.50','3.70','5.50','7.00','6.50','7.50','4.60','-'),('5.00','3.60','4.50','4.00','3.50','6.00','10.00','4.80','2.80','4.50','4.00','-'),('3.70','12.00','4.50','8.00','4.20','9.00','5.50','4.00','10.00','4.50','7.00','-'),('8.00','2.80','3.70','4.80','4.20','4.60','2.40','2.50','4.80','6.00','7.50','-'),('2','3','3','3','5','4','3','1','3','2','3','-'),('6','2','4','1','1','6','2','4','6','4','6','-'),('5','6','2','2','2','5','1','2','1','5','4','-'),('5.50','7.00','10.00','5.00','7.00','5.50','4.80','10.00','3.90','3.50','8.00','3.70'),('5.00','7.00','3.00','5.00','2.80','3.80','6.00','7.00','4.00','4.60','4.40','3.70'),('4.60','4.20','6.50','5.50','6.50','5.00','3.00','3.70','4.00','6.50','4.80','5.50'),('6.00','7.50','5.00','4.40','4.50','4.50','6.50','2.90','5.50','4.00','3.30','7.00'),('3.30','2.70','6.00','3.70','7.00','6.50','5.00','7.50','5.50','4.50','4.50','5.50'),('4.80','3.70','2.90','5.00','3.40','3.40','2.90','3.60','6.00','6.00','5.50','4.20'),('4','1','6','3','2','4','6','6','3','5','5','6'),('2','3','4','4','3','6','5','5','6','2','4','2'),('6','2','1','2','5','5','3','1','2','1','6','1'),('3.60','4.00','2.25','8.00','2.60','2.60','3.50','8.00','3.20','3.20','5.50','5.00'),('6.50','4.60','5.00','5.50','5.50','9.50','10.00','3.70','3.60','9.00','5.00','4.50'),('4.50','7.00','3.30','3.00','14.00','3.60','5.00','4.60','3.80','3.50','7.50','3.80'),('4.00','4.50','21.00','4.00','4.50','9.50','8.00','4.60','11.00','5.00','6.00','5.50'),('7.00','9.00','4.80','5.00','3.50','3.70','3.70','5.00','11.00','7.00','2.40','9.00'),('4.60','2.70','11.00','5.50','7.00','6.00','3.40','3.70','4.00','4.40','5.50','3.50'),('2','1','1','4','1','3','5','3','1','6','5','3'),('6','2','2','3','6','5','4','4','3','4','4','1'),('3','6','5','1','2','2','1','6','2','1','6','4'),('10.00','4.40','4.50','2.50','3.20','5.50','4.50','15.00','1.70','5.50','2.60','3.60'),('3.00','4.60','14.00','11.00','6.00','4.50','8.00','3.50','13.00','17.00','9.00','9.50'),('6.00','17.00','3.70','7.00','10.00','21.00','4.00','4.20','6.50','7.00','5.50','4.60'),('3.20','9.00','2.40','3.20','5.50','2.00','3.90','4.40','9.50','3.20','4.00','12.00'),('8.00','2.40','14.00','7.50','21.00','34.00','3.70','7.00','7.50','3.30','9.50','2.90'),('4.40','4.40','4.80','5.50','2.30','3.80','7.50','3.60','6.50','4.50','4.50','4.50'),('2','5','4','6','6','3','6','1','2','3','1','3'),('6','1','6','4','2','2','3','3','1','4','2','1'),('3','4','5','1','1','4','5','5','3','5','4','6'),('4.50','9.00','13.00','2.10','9.00','5.00','3.50','2.50','4.50','6.00','6.00','-'),('3.10','5.50','5.00','3.50','5.00','5.00','14.00','4.50','4.50','3.10','3.80','-'),('3.60','3.20','3.30','5.00','3.30','3.00','6.00','5.00','3.00','3.20','2.70','-'),('10.00','3.60','3.40','8.00','4.00','3.50','3.50','5.50','6.50','7.50','6.50','-'),('5.00','5.00','4.20','10.00','13.00','5.50','6.50','5.50','5.50','4.80','7.00','-'),('4.80','3.40','6.00','10.00','3.00','8.50','3.00','8.50','5.50','7.00','5.00','-'),('6','4','6','4','3','3','5','3','3','3','6','-'),('2','5','3','6','6','2','1','5','6','5','5','-'),('1','6','5','3','1','1','6','1','5','6','2','-'),('7.00','8.00','3.70','12.00','8.00','3.60','9.50','2.50','8.00','3.90','8.00','6.50'),('5.00','2.10','3.30','9.00','3.70','7.00','7.00','6.00','6.50','3.90','5.00','6.50'),('14.00','5.50','10.00','3.10','3.30','2.50','5.00','6.00','12.00','2.50','9.00','5.00'),('2.10','3.50','-','8.50','5.50','4.50','4.40','4.50','2.00','8.00','5.00','6.00'),('6.00','13.00','2.35','2.30','4.00','5.50','3.50','9.00','8.00','8.00','1.90','2.40'),('5.00','6.50','6.00','5.00','5.50','15.00','2.90','5.00','3.50','9.00','9.00','4.80'),('5','2','2','6','4','1','6','3','4','3','1','5'),('6','1','5','5','1','3','3','5','3','2','5','2'),('2','6','6','3','5','4','5','6','6','1','2','6'),('4.50','5.50','4.80','7.00','15.00','4.50','3.50','4.80','3.80','6.50','14.00','3.90'),('5.50','11.00','5.50','3.50','5.50','8.50','13.00','2.40','5.50','15.00','7.00','3.50'),('6.50','4.80','5.50','5.50','2.50','3.70','9.00','5.50','6.50','2.00','4.20','5.50'),('10.00','2.25','10.00','12.00','5.50','5.00','3.80','8.50','4.50','7.00','5.50','4.00'),('5.50','6.50','3.70','4.20','13.00','2.60','3.90','5.50','3.30','5.50','1.85','6.50'),('2.30','5.00','2.90','2.80','2.80','13.00','3.50','6.00','7.00','4.20','8.00','6.50'),('4','3','4','6','3','1','4','1','2','5','2','2'),('2','6','1','5','5','3','5','2','5','6','4','6'),('1','5','6','3','6','4','6','3','6','3','3','4'),('4.50','12.00','13.00','26.00','15.00','2.90','9.00','8.00','4.80','6.00','3.30','3.30'),('8.00','14.00','3.80','15.00','5.50','4.50','4.50','3.50','2.80','-','5.50','8.00'),('3.90','2.90','2.20','1.65','2.25','4.50','5.50','8.00','15.00','17.00','9.00','9.00'),('5.00','3.60','13.00','2.30','4.00','12.00','19.00','10.00','2.20','1.90','4.20','3.20'),('6.00','4.00','7.00','16.00','9.50','3.70','3.30','2.60','21.00','8.00','3.50','16.00'),('3.40','3.80','4.00','21.00','4.80','10.00','2.60','4.50','8.00','2.90','7.50','2.90'),('6','5','5','3','1','3','6','2','1','6','5','2'),('2','4','3','4','6','6','2','1','4','4','1','1'),('4','6','6','5','2','5','1','6','6','5','6','3'),('5.00','5.00','4.80','3.30','2.70','3.50','2.60','6.00','8.00','4.00','7.00','-'),('4.40','2.60','3.50','5.50','7.50','3.50','3.20','2.70','9.00','3.10','3.00','-'),('3.50','9.00','4.50','3.30','6.50','10.00','8.00','4.60','6.00','13.00','8.00','-'),('6.00','8.00','6.50','4.80','8.00','4.80','6.50','5.50','4.50','8.00','3.50','-'),('6.00','3.20','3.80','10.00','4.40','4.00','8.50','7.00','7.00','3.40','3.50','-'),('4.40','5.50','6.50','5.00','3.00','6.00','4.80','4.80','1.90','4.00','8.00','-'),('5','6','6','4','4','1','3','4','6','1','2','-'),('3','5','1','6','1','5','6','2','4','2','5','-'),('6','3','5','2','6','3','5','1','3','4','6','-'),('7.00','5.50','5.50','3.60','4.00','10.00','5.50','7.00','5.50','3.80','3.80','5.00'),('2.35','4.60','3.50','9.00','18.00','2.30','3.80','10.00','3.70','9.00','3.50','6.50'),('8.50','13.00','3.30','11.00','2.90','3.50','4.00','5.00','9.50','3.90','6.50','4.00'),('5.50','3.50','11.00','2.25','3.00','5.50','3.50','2.50','6.00','5.00','12.00','7.50'),('3.20','5.00','9.50','9.50','4.40','4.50','8.00','6.00','3.70','6.50','3.40','7.50'),('8.00','3.00','3.30','3.50','15.00','17.00','5.50','3.50','3.50','3.50','4.20','2.40'),('1','5','2','4','5','4','2','4','4','5','2','6'),('2','6','6','2','4','2','4','6','5','6','5','3'),('6','2','5','6','3','5','3','1','6','3','1','1'),('11.00','8.00','4.00','8.00','4.00','5.00','6.50','6.00','3.60','5.50','7.00','4.50'),('11.00','11.00','5.50','3.70','12.00','5.50','4.20','12.00','8.50','1.95','6.00','4.40'),('6.50','3.70','3.50','6.00','13.00','5.50','3.70','2.35','7.50','13.00','4.00','3.50'),('10.00','11.00','9.00','8.50','2.00','3.40','7.00','4.50','4.50','9.50','2.60','6.00'),('2.50','2.80','3.40','5.00','5.00','8.00','7.50','3.40','3.10','4.40','10.00','7.50'),('2.20','2.60','5.50','2.25','6.00','3.10','2.70','9.50','4.60','5.50','3.50','3.70'),('6','1','6','2','4','2','2','1','2','4','6','4'),('5','6','1','3','6','5','4','3','1','6','2','6'),('2','3','2','5','1','6','6','5','5','2','5','1'),('3.60','7.00','2.10','3.10','1.90','2.00','5.00','1.25','-','19.00','3.50','2.50'),('8.00','9.50','16.00','5.50','3.50','31.00','10.00','15.00','3.80','1.55','7.50','5.50'),('3.70','2.45','8.00','5.50','17.00','6.50','12.00','-','7.00','3.60','3.50','8.00'),('7.00','4.60','3.60','3.50','6.00','3.90','4.60','13.00','2.10','10.00','10.00','4.40'),('15.00','3.70','9.50','6.50','8.00','15.00','2.30','17.00','19.00','8.00','2.50','7.00'),('2.70','10.00','5.00','8.50','14.00','6.00','6.50','6.50','3.30','-','21.00','6.00'),('3','3','6','3','1','1','6','1','6','2','3','1'),('4','1','5','6','3','6','2','6','2','3','1','4'),('6','6','4','4','4','3','5','4','4','4','4','5'),('9.00','9.00','9.00','6.50','5.50','4.60','2.05','3.20','5.00','4.50','4.80','-'),('6.50','3.50','4.20','4.80','8.00','6.00','9.50','6.50','5.50','4.00','3.00','-'),('7.00','5.50','4.00','3.50','8.50','3.20','8.00','6.50','4.60','6.50','5.50','-'),('3.10','6.00','3.00','7.50','4.50','5.00','4.50','4.50','5.00','4.00','3.20','-'),('4.80','6.00','5.50','3.50','3.50','6.00','6.00','6.50','6.50','6.00','8.00','-'),('2.90','2.80','6.00','4.60','3.00','4.50','5.00','3.60','3.00','3.60','8.00','-'),('4','4','3','2','2','3','6','1','6','6','2','-'),('6','2','6','6','1','4','5','6','5','1','4','-'),('5','1','5','5','3','2','4','4','2','4','3','-');
/*!40000 ALTER TABLE `romford` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-27  0:56:28