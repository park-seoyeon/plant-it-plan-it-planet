-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: j4a101.p.ssafy.io    Database: plantit
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `user_detail`
--

DROP TABLE IF EXISTS `user_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_detail` (
  `user_number` int NOT NULL,
  `mbti_name` text COLLATE utf8mb4_unicode_ci,
  `mbti_expression` text COLLATE utf8mb4_unicode_ci,
  `flower_language` text COLLATE utf8mb4_unicode_ci,
  `flower_description` varchar(400) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `best_partner` text COLLATE utf8mb4_unicode_ci,
  `best_expression` text COLLATE utf8mb4_unicode_ci,
  `worst_partner` text COLLATE utf8mb4_unicode_ci,
  `worst_expression` text COLLATE utf8mb4_unicode_ci,
  `recommanded_plant_1_id` int DEFAULT NULL,
  `recommanded_plant_1_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_1_intro` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_2_id` int DEFAULT NULL,
  `recommanded_plant_2_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_2_intro` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_3_id` int DEFAULT NULL,
  `recommanded_plant_3_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_3_intro` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_4_id` int DEFAULT NULL,
  `recommanded_plant_4_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_4_intro` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_5_id` int DEFAULT NULL,
  `recommanded_plant_5_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recommanded_plant_5_intro` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_detail`
--

LOCK TABLES `user_detail` WRITE;
/*!40000 ALTER TABLE `user_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-07 22:28:55
