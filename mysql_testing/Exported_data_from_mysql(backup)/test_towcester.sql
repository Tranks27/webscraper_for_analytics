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
-- Table structure for table `towcester`
--

DROP TABLE IF EXISTS `towcester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `towcester` (
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
-- Dumping data for table `towcester`
--

LOCK TABLES `towcester` WRITE;
/*!40000 ALTER TABLE `towcester` DISABLE KEYS */;
INSERT INTO `towcester` VALUES ('3.10','9.00','4.40','4.80','8.00','10.00','5.50','4.40','7.00','2.10','5.50','3.30'),('9.00','3.60','6.00','3.30','7.50','6.50','3.50','1.80','3.50','-','4.80','6.00'),('-','5.50','3.00','10.00','4.00','1.85','5.50','8.50','14.00','9.50','3.00','2.00'),('3.40','5.00','3.20','3.50','9.00','4.80','7.00','6.00','5.50','3.00','7.50','9.00'),('3.70','8.00','5.50','4.50','2.45','6.00','4.40','7.00','2.90','7.50','12.00','14.00'),('4.20','2.60','10.00','6.50','3.40','9.00','3.80','12.00','3.90','5.50','2.90','8.00'),('1','6','4','4','1','3','2','2','3','6','3','1'),('6','3','1','2','2','6','5','1','2','3','2','2'),('5','2','5','1','5','1','3','3','5','1','6','5');
/*!40000 ALTER TABLE `towcester` ENABLE KEYS */;
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
