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
-- Table structure for table `mbti_compatibility`
--

DROP TABLE IF EXISTS `mbti_compatibility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mbti_compatibility` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mbti_name` text COLLATE utf8mb4_unicode_ci,
  `best_partner` text COLLATE utf8mb4_unicode_ci,
  `best_expression` text COLLATE utf8mb4_unicode_ci,
  `worst_partner` text COLLATE utf8mb4_unicode_ci,
  `worst_expression` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mbti_compatibility`
--

LOCK TABLES `mbti_compatibility` WRITE;
/*!40000 ALTER TABLE `mbti_compatibility` DISABLE KEYS */;
INSERT INTO `mbti_compatibility` VALUES (1,'ISTJ','ESTP','자기애 뿜뿜 \"수선화\"','ENFP','천진난만한 \"프리지아\"'),(2,'ISTP','ESTJ','완벽주의자 \"노란 장미\"','ENTJ','주관 뚜렷 냉정한 \"퐁퐁국화\"'),(3,'ISFJ','ESFP','파티피플 신나는 \"델피늄\"','INTP','자신감 업업 \"해바라기\"'),(4,'ISFP','ESFJ','따뜻하고 상냥한 \"캄파눌라\"','INFP','소심한 관종 \"작약\"'),(5,'INTJ','ENFP','천진난만한 \"프리지아\"','ESTJ','완벽주의자 \"노란 장미\"'),(6,'INTP','ENTJ','주관 뚜렷 냉정한 \"퐁퐁국화\"','ISFJ','언제나 친절한 \"라그라스\"'),(7,'INFJ','ENTP','마이웨이 죽지 않는 \"마트리카리아\"','ESFP','파티피플 신나는 \"델피늄\"'),(8,'INFP','ENFJ','지혜롭고 부드러운 \"다알리아\"','ISFP','신비로운\"거베라\"'),(9,'ESTJ','ISTP','무심한 듯 쿨한\"라넌큘러스\"','ISTJ','애정표현에 약한 무뚝뚝한 \"망고튤립\"'),(10,'ESTP','ISTJ','애정표현에 약한 무뚝뚝한 \"망고튤립\"','ENFJ','지혜롭고 부드러운 \"다알리아\"'),(11,'ESFJ','ISFP','신비로운\"거베라\"','ENTP','마이웨이 죽지 않는 \"마트리카리아\"'),(12,'ESFP','ISFJ','언제나 친절한 \"라그라스\"','INFJ','겉차속따 \"핑크튤립\"'),(13,'ENTJ','INTP','자신감 업업 \"해바라기\"','ISTP','무심한 듯 쿨한\"라넌큘러스\"'),(14,'ENTP','INFJ','겉차속따 \"핑크튤립\"','ESFJ','따뜻하고 상냥한 \"캄파눌라\"'),(15,'ENFJ','INFP','소심한 관종 \"작약\"','ESTP','자기애 뿜뿜 \"수선화\"'),(16,'ENFP','INTJ','생각이 깊은 \"수국\"','ISTJ','애정표현에 약한 무뚝뚝한 \"망고튤립\"');
/*!40000 ALTER TABLE `mbti_compatibility` ENABLE KEYS */;
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
