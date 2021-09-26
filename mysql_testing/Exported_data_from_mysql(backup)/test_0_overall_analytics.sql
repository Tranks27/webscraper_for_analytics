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
-- Table structure for table `0_overall_analytics`
--

DROP TABLE IF EXISTS `0_overall_analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `0_overall_analytics` (
  `id` int NOT NULL,
  `num_races` int DEFAULT NULL,
  `Stra1_1` decimal(5,2) DEFAULT NULL,
  `Stra1_2` decimal(5,2) DEFAULT NULL,
  `Stra1_3` decimal(5,2) DEFAULT NULL,
  `Stra1_4` decimal(5,2) DEFAULT NULL,
  `Stra1_5` decimal(5,2) DEFAULT NULL,
  `Stra1_6` decimal(5,2) DEFAULT NULL,
  `Stra2_1` decimal(5,2) DEFAULT NULL,
  `Stra2_2` decimal(5,2) DEFAULT NULL,
  `Stra2_3` decimal(5,2) DEFAULT NULL,
  `Stra2_4` decimal(5,2) DEFAULT NULL,
  `Stra2_5` decimal(5,2) DEFAULT NULL,
  `Stra2_6` decimal(5,2) DEFAULT NULL,
  `Stra3_1` decimal(5,2) DEFAULT NULL,
  `Stra3_2` decimal(5,2) DEFAULT NULL,
  `Stra3_3` decimal(5,2) DEFAULT NULL,
  `Stra3_4` decimal(5,2) DEFAULT NULL,
  `Stra3_5` decimal(5,2) DEFAULT NULL,
  `Stra3_6` decimal(5,2) DEFAULT NULL,
  `Stra4_11` decimal(5,2) DEFAULT NULL,
  `Stra4_12` decimal(5,2) DEFAULT NULL,
  `Stra4_13` decimal(5,2) DEFAULT NULL,
  `Stra4_14` decimal(5,2) DEFAULT NULL,
  `Stra4_15` decimal(5,2) DEFAULT NULL,
  `Stra4_21` decimal(5,2) DEFAULT NULL,
  `Stra4_22` decimal(5,2) DEFAULT NULL,
  `Stra4_23` decimal(5,2) DEFAULT NULL,
  `Stra4_24` decimal(5,2) DEFAULT NULL,
  `Stra4_25` decimal(5,2) DEFAULT NULL,
  `Stra4_31` decimal(5,2) DEFAULT NULL,
  `Stra4_32` decimal(5,2) DEFAULT NULL,
  `Stra4_33` decimal(5,2) DEFAULT NULL,
  `Stra4_34` decimal(5,2) DEFAULT NULL,
  `Stra4_35` decimal(5,2) DEFAULT NULL,
  `Stra4_41` decimal(5,2) DEFAULT NULL,
  `Stra4_42` decimal(5,2) DEFAULT NULL,
  `Stra4_43` decimal(5,2) DEFAULT NULL,
  `Stra4_44` decimal(5,2) DEFAULT NULL,
  `Stra4_45` decimal(5,2) DEFAULT NULL,
  `Stra4_51` decimal(5,2) DEFAULT NULL,
  `Stra4_52` decimal(5,2) DEFAULT NULL,
  `Stra4_53` decimal(5,2) DEFAULT NULL,
  `Stra4_54` decimal(5,2) DEFAULT NULL,
  `Stra4_55` decimal(5,2) DEFAULT NULL,
  `Stra4_61` decimal(5,2) DEFAULT NULL,
  `Stra4_62` decimal(5,2) DEFAULT NULL,
  `Stra4_63` decimal(5,2) DEFAULT NULL,
  `Stra4_64` decimal(5,2) DEFAULT NULL,
  `Stra4_65` decimal(5,2) DEFAULT NULL,
  `Stra5_11` decimal(5,2) DEFAULT NULL,
  `Stra5_12` decimal(5,2) DEFAULT NULL,
  `Stra5_13` decimal(5,2) DEFAULT NULL,
  `Stra5_14` decimal(5,2) DEFAULT NULL,
  `Stra5_15` decimal(5,2) DEFAULT NULL,
  `Stra5_21` decimal(5,2) DEFAULT NULL,
  `Stra5_22` decimal(5,2) DEFAULT NULL,
  `Stra5_23` decimal(5,2) DEFAULT NULL,
  `Stra5_24` decimal(5,2) DEFAULT NULL,
  `Stra5_25` decimal(5,2) DEFAULT NULL,
  `Stra5_31` decimal(5,2) DEFAULT NULL,
  `Stra5_32` decimal(5,2) DEFAULT NULL,
  `Stra5_33` decimal(5,2) DEFAULT NULL,
  `Stra5_34` decimal(5,2) DEFAULT NULL,
  `Stra5_35` decimal(5,2) DEFAULT NULL,
  `Stra5_41` decimal(5,2) DEFAULT NULL,
  `Stra5_42` decimal(5,2) DEFAULT NULL,
  `Stra5_43` decimal(5,2) DEFAULT NULL,
  `Stra5_44` decimal(5,2) DEFAULT NULL,
  `Stra5_45` decimal(5,2) DEFAULT NULL,
  `Stra5_51` decimal(5,2) DEFAULT NULL,
  `Stra5_52` decimal(5,2) DEFAULT NULL,
  `Stra5_53` decimal(5,2) DEFAULT NULL,
  `Stra5_54` decimal(5,2) DEFAULT NULL,
  `Stra5_55` decimal(5,2) DEFAULT NULL,
  `Stra5_61` decimal(5,2) DEFAULT NULL,
  `Stra5_62` decimal(5,2) DEFAULT NULL,
  `Stra5_63` decimal(5,2) DEFAULT NULL,
  `Stra5_64` decimal(5,2) DEFAULT NULL,
  `Stra5_65` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `0_overall_analytics`
--

LOCK TABLES `0_overall_analytics` WRITE;
/*!40000 ALTER TABLE `0_overall_analytics` DISABLE KEYS */;
INSERT INTO `0_overall_analytics` VALUES (1,3647,34.18,26.21,17.90,14.90,10.82,5.89,22.07,22.70,22.89,19.19,15.72,9.29,16.40,20.05,21.39,21.88,19.34,14.38,10.92,9.30,6.67,4.68,2.61,8.15,6.45,4.19,2.55,1.98,4.81,3.86,3.33,2.47,1.12,4.22,2.89,2.19,1.92,1.00,2.78,2.01,1.62,1.26,0.64,1.40,1.34,0.82,0.54,0.62,5.35,4.52,3.41,3.29,3.13,4.96,4.29,3.53,2.89,2.76,3.26,4.16,3.23,3.04,3.03,3.21,2.84,2.34,3.12,3.38,3.08,1.94,2.35,2.41,2.38,4.20,3.19,3.37,2.88,2.80);
/*!40000 ALTER TABLE `0_overall_analytics` ENABLE KEYS */;
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
