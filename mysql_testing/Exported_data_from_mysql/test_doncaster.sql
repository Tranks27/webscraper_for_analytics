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
-- Table structure for table `doncaster`
--

DROP TABLE IF EXISTS `doncaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doncaster` (
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
-- Dumping data for table `doncaster`
--

LOCK TABLES `doncaster` WRITE;
/*!40000 ALTER TABLE `doncaster` DISABLE KEYS */;
INSERT INTO `doncaster` VALUES ('4.50','5.00','5.00','2.30','6.00','6.50','7.00','13.00','7.00','34.00','3.50','8.00'),('2.80','3.60','4.50','9.00','11.00','3.50','21.00','1.90','8.00','26.00','2.80','4.40'),('6.00','4.20','6.00','11.00','4.40','4.00','4.00','14.00','7.00','9.00','11.00','5.00'),('13.00','7.50','3.00','3.30','3.00','2.70','5.50','7.00','2.80','2.80','5.50','7.00'),('4.00','7.00','6.50','5.00','5.50','8.50','2.80','7.00','13.00','3.00','7.00','5.50'),('5.00','3.70','5.00','5.50','3.40','13.00','4.00','3.50','2.60','3.10','4.50','2.50'),('2','1','6','3','3','3','5','2','6','1','2','6'),('3','6','3','4','1','4','3','4','4','2','1','1'),('1','4','2','1','5','2','4','3','1','5','4','5'),('2.90','3.30','7.00','9.00','10.00','4.20','3.80','6.50','7.00','15.00','6.50','4.50'),('6.50','10.00','2.80','4.20','4.40','4.00','4.50','12.00','9.00','8.50','4.20','7.50'),('5.50','3.00','7.00','6.50','3.30','8.50','9.00','4.50','2.50','3.60','8.00','3.30'),('4.20','4.00','4.50','3.30','9.00','2.45','2.60','7.00','5.50','2.10','6.00','6.00'),('10.00','6.00','3.50','5.00','3.30','9.00','11.00','2.25','4.50','9.50','2.60','3.50'),('3.70','8.00','8.00','3.80','4.40','6.50','5.00','4.20','4.40','4.20','4.50','6.00'),('1','3','2','6','5','2','6','5','3','6','5','1'),('2','6','4','2','2','1','1','6','6','4','4','2'),('4','1','5','5','6','6','5','1','1','5','6','5'),('7.00','2.80','2.90','2.70','10.00','4.20','8.50','3.80','5.00','8.00','2.50','2.80'),('3.40','7.50','3.40','15.00','6.00','9.00','3.40','7.50','13.00','11.00','5.50','9.50'),('5.50','6.00','5.50','3.40','4.40','1.55','5.50','9.50','1.85','4.60','5.00','6.50'),('2.90','2.70','18.00','5.50','5.00','9.00','4.80','6.50','7.50','4.00','5.00','2.60'),('8.50','6.50','6.50','5.50','6.00','7.50','6.00','5.00','4.50','2.60','4.40','8.50'),('4.80','12.00','4.00','6.00','2.35','20.00','2.90','2.30','6.00','4.00','11.00','5.50'),('3','2','2','6','1','3','5','2','5','4','5','1'),('2','1','5','5','6','1','4','6','3','6','1','4'),('4','5','3','3','3','4','2','5','4','5','6','3');
/*!40000 ALTER TABLE `doncaster` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-08  0:16:39
