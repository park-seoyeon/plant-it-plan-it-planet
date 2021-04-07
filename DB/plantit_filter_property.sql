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
-- Table structure for table `filter_property`
--

DROP TABLE IF EXISTS `filter_property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filter_property` (
  `id` int NOT NULL,
  `property` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `property_name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filter_property`
--

LOCK TABLES `filter_property` WRITE;
/*!40000 ALTER TABLE `filter_property` DISABLE KEYS */;
INSERT INTO `filter_property` VALUES (1,'leafy','잎이 있는 식물'),(2,'hanging','공중식물'),(3,'vine','덩굴식물'),(4,'cactus_succulent','선인장/다육식물'),(5,'leaf_shape','잎 모양'),(6,'air_purification','공기정화'),(7,'fragrant','향기나는'),(8,'pet_safe','반려동물 안전한'),(9,'low_light','빛이 적어도 되는'),(10,'has_fruit','열매 맺는'),(11,'wooden','목대 있는'),(12,'chubby','밑이 통통한'),(13,'has_flower','꽃이 피는'),(14,'holed','구멍'),(15,'broad','넓은'),(16,'round','둥근'),(17,'sharp','뾰족한'),(18,'oblong','길쭉한'),(19,'split','갈라진'),(20,'heart_shaped','하트모양'),(21,'star_shaped','별모양'),(22,'small','작은'),(23,'thick','두꺼운'),(24,'patterned','무늬'),(25,'flower_shaped','꽃 모양'),(26,'fat','통통한'),(27,'flat','납작한'),(28,'without_leaves','잎이 없음'),(29,'no_soil','흙이 필요 없는'),(30,'no_spike_cactus','가시가 없는');
/*!40000 ALTER TABLE `filter_property` ENABLE KEYS */;
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
