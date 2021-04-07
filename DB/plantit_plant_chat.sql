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
-- Table structure for table `plant_chat`
--

DROP TABLE IF EXISTS `plant_chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant_chat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `level` int DEFAULT NULL,
  `message` text COLLATE utf8mb4_unicode_ci,
  `type` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant_chat`
--

LOCK TABLES `plant_chat` WRITE;
/*!40000 ALTER TABLE `plant_chat` DISABLE KEYS */;
INSERT INTO `plant_chat` VALUES (1,1,'물',1),(2,1,'맘마',1),(3,1,'까까',1),(4,1,'흙',2),(5,1,'안녕',0),(6,1,'응애',0),(7,1,'엄마',0),(8,1,'아빠',0),(9,1,'아임 구르트',0),(10,2,'물 주세요',1),(11,2,'목 말라요',1),(12,2,'아이 엠 항그리',1),(13,2,'흙 갈아줘요',2),(14,2,'놀아줘요!',0),(15,2,'안녕하세요!',0),(16,2,'몰라요',0),(17,2,'아임 구르트',0),(18,2,'예쁘면 다냐?',0),(19,3,'오늘은 에비앙이 좀 땡기네',1),(20,3,'이사 가고 싶다',2),(21,3,'아임 구르트',0),(22,3,'내가 들어올 때 노크 하랬지!',0),(23,3,'요즘 나에 대한 관심이 식은거 같아..',0),(24,3,'요즘 날씨가 너무 좋은거같아!',0),(25,3,'나만 친구 없어. 친구 좀 만들어줘',0),(26,3,'나를 더 귀하게 여기라고! 난 나사에서도 인정받은 몸이란말야!',0),(27,3,'너의 칙칙한 방에 내가 있으니 좀 낫지 않아?',0),(28,3,'너 내가 식물이라고 무시해?',0),(29,3,'오졌고 지렸고 개쩌는 거 인정하는 부분이구요 좌로 인정 우로 인정 앞구르기 인정 인정 올리지 말고 인정 내려 인정 안 해서 후회한다면 후회할 시간을 후회하는 각이구요 아리랑 고개를 넘어서 새가 지저귀는 부분이구요 인정하지 않는 사람 에바 참치 삼치 꽁치 가문의 수치 뭉치면 살고 흩어지면 삼각 사각 오각 생각 생각 죽는 각입니다요 대박 중박 소박 명박이도 인정하는 각 지리구요 오지고요 고요고요 고요한 밤이고요 실화냐? 다큐냐? 맨큐냐? 오져따리 오져따',0),(30,4,'오늘 적시자',1),(31,4,'넘넘넘 잘 했는데!혹시 물 조금만 더 줄 수 있어 ?!?',1),(32,4,'나 이제 자취하고싶어.',2),(33,4,'인장이 알아? 선인장이? 인장이 보고싶다. 걔는 까칠한 매력이 있어.',0),(34,4,'오늘은 산책하고 싶다. ',0),(35,4,'장미랑 한 잔 하고 싶다',0),(36,4,'이제 말 좀 그만 걸어줘...귀찮아...',3),(37,4,'그거 알아? 나를 1평에 3시간동안 두면 공기질이 훨씬 좋아진대!',0),(38,4,'어디서 배운 버르장머리냐 어른이 말씀하시는데 따박 따박 대들고 내가 하라는대로해 다.  세상 참 좋아졌어 윗사람이 뭘 하고 있으면, 도와드릴거라도 없냐고 물어봐야할거 아니냐! 내가 누군지 알아? 내가 진짜 성질 많이 죽었다! 요즘은 군대도 아니야! 요즘애들은 버릇이 없어요. 어른이 주면 그저 감사합니다하고 받는거야 이게 다 너잘되라고 하는 소리야 너보다 힘든 사람이 얼마나 많은데 감사할줄알아야지 ',0),(39,4,'아임 구르트',0),(40,4,'이거 이야기하려고 어그로 끌었다. 세계 최강의 에비앙 아니냐?',0),(41,5,'소자 물 한 잔 마시고 싶습니다.',1),(42,5,'소인의 흙에 이제 영양분이 없는듯 하옵니다.',2),(43,5,'진지 드셨나요? 시장하실텐데 어서 드시지요.',0),(44,5,'간밤에 깊은 잠 드셨는지요? 문안 인사 드립니다.',0),(45,5,'나를 키워주셔서 감사합니다. 은혜에 공기질로 보답하겠습니다.',0),(46,5,'아임 구르트',0),(47,5,'암모니아는 염기성을 띠기 때문에 생체 조직에 대해서 자극성인데 제가 그걸 없앨 수 있어요',3),(48,5,'포름알데하이드는 세계보건기구 산하 국제암연구기관에서 분류한 1군 발암물질로 대기질에 있는데 제가 없앨 수 있어요!',3),(49,5,'벤젠은 암이나 다른 질병을 일으킬 가능성이 많은데 제가 없애고 있어요!',3),(50,5,'자일렌에 노출될 경우 기억, 기분, 수면의 장애와 두통, 소화불량을 자주 경험할 수 있는데 제가 없애고 있어요',3),(51,5,'트리클로로에틸렌에 의한 주된 건강영향은 중추신경계 독성, 시력장애, 피로, 오심 등의 일반적 증상이 있을 수 있는데 제가 없애는데 이바지 하고 있어요',3);
/*!40000 ALTER TABLE `plant_chat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-07 22:28:51
