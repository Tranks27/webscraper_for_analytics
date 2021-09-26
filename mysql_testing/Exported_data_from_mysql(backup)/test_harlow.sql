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
-- Table structure for table `harlow`
--

DROP TABLE IF EXISTS `harlow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `harlow` (
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
-- Dumping data for table `harlow`
--

LOCK TABLES `harlow` WRITE;
/*!40000 ALTER TABLE `harlow` DISABLE KEYS */;
INSERT INTO `harlow` VALUES ('3.40','2.10','12.00','2.15','3.30','2.35','2.35','4.20','4.20','15.00','6.00','-'),('4.00','8.00','4.40','5.50','15.00','2.90','6.00','6.50','5.50','3.60','5.00','-'),('5.00','5.50','3.00','26.00','8.00','4.40','6.00','7.00','3.50','3.30','4.60','-'),('3.80','3.20','3.60','8.00','5.50','11.00','4.40','3.40','8.00','11.00','13.00','-'),('16.00','21.00','6.00','9.00','3.40','7.50','21.00','4.40','3.50','2.60','2.25','-'),('4.80','9.00','5.00','3.00','3.80','41.00','5.00','4.50','7.00','8.00','5.50','-'),('6','4','6','2','5','5','4','5','3','3','5','-'),('1','1','4','5','4','4','6','1','1','2','2','-'),('5','6','3','1','1','2','2','2','5','1','4','-'),('2.90','16.00','5.50','11.00','8.00','9.50','9.00','13.00','13.00','3.40','3.70','-'),('18.00','3.20','1.95','26.00','3.80','3.80','1.75','3.70','4.50','-','3.50','-'),('8.00','20.00','7.00','5.00','2.35','2.10','4.20','21.00','1.65','3.70','4.00','-'),('5.50','8.50','8.00','21.00','8.00','4.50','4.50','21.00','7.50','4.80','11.00','-'),('3.30','4.50','4.80','4.00','9.00','6.50','21.00','-','6.50','4.80','10.00','-'),('3.90','2.10','10.00','1.60','5.00','26.00','13.00','1.30','21.00','4.40','4.20','-'),('1','6','2','1','6','2','6','6','1','5','2','-'),('5','1','1','6','5','1','4','1','5','6','1','-'),('2','2','4','5','3','4','2','2','3','1','5','-');
/*!40000 ALTER TABLE `harlow` ENABLE KEYS */;
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
