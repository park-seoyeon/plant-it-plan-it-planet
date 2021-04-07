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
-- Table structure for table `user_reward`
--

DROP TABLE IF EXISTS `user_reward`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_reward` (
  `user_number` int NOT NULL,
  `reward_cnt` int NOT NULL DEFAULT '0',
  `reward1` tinyint(1) NOT NULL DEFAULT '0',
  `reward2` tinyint(1) NOT NULL DEFAULT '0',
  `reward3` tinyint(1) NOT NULL DEFAULT '0',
  `reward4` tinyint(1) NOT NULL DEFAULT '0',
  `reward5` tinyint(1) NOT NULL DEFAULT '0',
  `reward6` tinyint(1) NOT NULL DEFAULT '0',
  `reward7` tinyint(1) NOT NULL DEFAULT '0',
  `reward8` tinyint(1) NOT NULL DEFAULT '0',
  `reward9` tinyint(1) NOT NULL DEFAULT '0',
  `reward10` tinyint(1) NOT NULL DEFAULT '0',
  `reward11` tinyint(1) NOT NULL DEFAULT '0',
  `reward11_1` tinyint(1) NOT NULL DEFAULT '0',
  `reward11_2` tinyint(1) NOT NULL DEFAULT '0',
  `reward11_3` tinyint(1) NOT NULL DEFAULT '0',
  `reward11_4` tinyint(1) NOT NULL DEFAULT '0',
  `reward11_5` tinyint(1) NOT NULL DEFAULT '0',
  `reward12` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_reward`
--

LOCK TABLES `user_reward` WRITE;
/*!40000 ALTER TABLE `user_reward` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_reward` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-07 22:28:53
