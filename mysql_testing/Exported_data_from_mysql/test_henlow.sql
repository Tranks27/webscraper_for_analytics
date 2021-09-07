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
-- Table structure for table `henlow`
--

DROP TABLE IF EXISTS `henlow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `henlow` (
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
-- Dumping data for table `henlow`
--

LOCK TABLES `henlow` WRITE;
/*!40000 ALTER TABLE `henlow` DISABLE KEYS */;
INSERT INTO `henlow` VALUES ('9.00','6.00','6.00','7.00','8.00','8.50','7.00','2.40','10.00','7.00','16.00','-'),('5.00','9.00','6.50','9.00','9.00','4.00','3.30','8.00','19.00','4.50','2.90','-'),('9.00','3.50','2.90','1.90','16.00','3.40','2.80','4.50','1.75','7.00','7.00','-'),('3.00','4.40','3.40','13.00','3.10','8.50','10.00','9.00','6.50','11.00','13.00','-'),('3.50','2.90','6.50','9.00','2.20','3.10','4.20','8.00','8.00','8.00','2.70','-'),('4.20','7.00','5.50','2.90','5.00','5.50','6.50','3.70','3.80','1.80','3.50','-'),('4','5','4','3','1','6','2','6','6','6','4','-'),('5','1','3','5','6','3','5','2','5','5','6','-'),('6','4','1','6','4','2','6','3','4','4','5','-'),('7.00','2.50','1.55','14.00','2.90','7.00','4.20','17.00','4.40','6.00','16.00','12.00'),('5.50','9.00','7.50','9.00','4.00','4.00','8.00','3.00','2.50','5.00','15.00','4.60'),('4.60','3.50','19.00','2.80','3.60','2.60','1.95','8.00','4.60','1.80','2.90','7.00'),('2.25','4.00','7.00','2.80','9.00','5.50','13.00','3.10','26.00','21.00','7.50','5.50'),('9.00','6.50','5.50','3.70','11.00','8.00','7.00','3.10','6.00','4.20','3.70','7.50'),('5.00','13.00','9.00','11.00','5.00','5.00','5.00','8.00','3.30','7.00','2.30','1.90'),('3','4','2','4','1','6','6','2','2','2','5','1'),('4','6','4','3','2','4','1','5','3','3','3','6'),('2','1','5','6','3','5','2','3','5','5','6','4');
/*!40000 ALTER TABLE `henlow` ENABLE KEYS */;
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
