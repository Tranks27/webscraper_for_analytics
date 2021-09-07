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
-- Table structure for table `central_park_bags`
--

DROP TABLE IF EXISTS `central_park_bags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `central_park_bags` (
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
-- Dumping data for table `central_park_bags`
--

LOCK TABLES `central_park_bags` WRITE;
/*!40000 ALTER TABLE `central_park_bags` DISABLE KEYS */;
INSERT INTO `central_park_bags` VALUES ('2.50','3.30','8.00','8.00','5.50','3.00','5.00','3.60','8.50','3.50','4.00','2.50'),('9.00','3.50','7.00','4.20','7.50','3.00','18.00','4.80','6.50','11.00','7.50','16.00'),('3.50','9.00','4.60','5.50','1.95','6.50','4.40','14.00','3.60','3.00','3.00','6.00'),('4.60','3.50','4.20','3.10','3.00','5.00','7.50','8.50','9.00','9.00','4.50','6.50'),('8.00','9.00','9.50','7.50','19.00','9.50','3.20','3.50','2.70','6.50','12.00','3.00'),('6.00','4.80','2.10','3.60','11.00','5.00','2.70','3.30','3.90','3.20','3.90','6.00'),('3','2','1','6','6','4','6','5','5','3','3','4'),('4','4','2','2','1','1','1','4','3','6','1','6'),('1','1','6','4','4','2','4','2','6','5','6','5'),('5.00','4.00','6.00','8.50','3.40','2.60','8.00','5.00','11.00','6.50','2.60','9.00'),('4.00','8.00','11.00','8.00','2.10','8.00','2.80','6.00','7.00','4.00','-','6.00'),('4.40','3.30','3.30','11.00','7.50','2.60','3.80','2.60','4.80','4.40','11.00','5.00'),('4.50','8.50','4.40','4.00','8.00','8.00','7.00','4.50','8.50','11.00','2.90','2.40'),('4.00','6.50','9.00','2.00','12.00','13.00','2.80','10.00','3.40','2.50','4.50','4.00'),('8.00','3.10','2.70','4.80','6.00','5.00','9.00','4.50','2.35','7.00','4.60','8.00'),('2','6','6','5','4','2','4','1','4','3','1','4'),('1','3','5','4','2','3','5','6','6','4','6','5'),('4','2','4','2','3','1','3','5','3','6','5','6');
/*!40000 ALTER TABLE `central_park_bags` ENABLE KEYS */;
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
