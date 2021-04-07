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
-- Table structure for table `mbti`
--

DROP TABLE IF EXISTS `mbti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mbti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mbti_name` text COLLATE utf8mb4_unicode_ci,
  `mbti_expression` text COLLATE utf8mb4_unicode_ci,
  `flower_language` text COLLATE utf8mb4_unicode_ci,
  `flower_description` varchar(400) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mbti`
--

LOCK TABLES `mbti` WRITE;
/*!40000 ALTER TABLE `mbti` DISABLE KEYS */;
INSERT INTO `mbti` VALUES (1,'ISTJ','애정표현에 약한 무뚝뚝한 \"망고튤립\"','수줍은 사랑의 표시','•차분하고 말이 느린 편이고 신중해요\r•규칙이 엄격한 약간은 꼰대같은...보수적인...\r•사람 많은 곳에 가면 금방 지쳐요'),(2,'ISTP','무심한 듯 쿨한\"라넌큘러스\"','매력','•남에게 별로 관심이 없고 선 긋기 잘해요\r•꽂히는 건 무조건 해야 하는 즉흥적인 성격\r•남의 일에 간섭 안 하고 간섭받는 거 싫어해요'),(3,'ISFJ','언제나 친절한 \"라그라스\"','당신의 친절에 감사합니다','•나서는 건 실지만 관심은 좋아요\r•다른 사람의 감정을 잘 캐치하고 공감도 잘해요\r•쓸데없는 감정 소모를 싫어해요'),(4,'ISFP','신비로운\"거베라\"','신비로움','•안 착하다고 생각하는데 남들이 착하다고 해요\r•모든 일에 의욕이 부족하지만 한 번 삘 타면 제대로\r•개인 시간은 필수, 개인 공간 침범 극혐'),(5,'INTJ','생각이 깊은 \"수국\"','진심','•사람들이랑 친해지는 데 오래 걸리지만, 관계 정리는 칼 같이\r•혼자 있는 것을 좋아하는 완전한 개인주의자\r•효율성이 떨어지는 시스템을 싫어해요'),(6,'INTP','자신감 업업 \"해바라기\"','프라이드','•조용하고 말이 없지만 내가 관심 있는 건 말이 많아요\r•혼자 있는 게 제일 편하고 행복한 자발적 아싸\r•친한 친구여도 별일 없으면 연락 잘 안 해요'),(7,'INFJ','겉차속따 \"핑크튤립\"','애정,배려','•조용한데 다 같이 놀러 가면 춤추고 노래하고 싶어요\r•관종이지만 내성적이라 평소에는 티가 나지 않아요\r•신중한 완벽주의자라 행동 전에 시뮬레이션 500번'),(8,'INFP','소심한 관종 \"작약\"','수줍음','•완벽하지 못할 거라면 아예 시작도 안해요\r•남한테 의지하기 싫어서 혼자 해결하려 해요\r•개인적인 이야기를 남들한테 하는 거 싫어해요'),(9,'ESTJ','완벽주의자 \"노란 장미\"','완벽한 성취','•현실적이고 호불호가 확실해요\r•과정보다는 결과가 중요한 워커홀릭\r•남이 일을 못 하면 답답해서 잔소리가 심해져요'),(10,'ESTP','자기애 뿜뿜 \"수선화\"','자기사랑,자존심,신비','•흥미 위주의 놀이가 좋고 즉흥적이에요\r•순발력과 임기응변 능력이 뛰어나요\r•통제하려 하거나 독립성을 인정해 주지 않으면 화나요'),(11,'ESFJ','따뜻하고 상냥한 \"캄파눌라\"','따뜻한사랑,상냥한사랑','•쓸데없이 걱정이 많은 스타일이에요\r•공감능력이 좋아서 상대방의 기분을 잘 맞춰줘요\r•사람을 좋아해서 내 사람들이 힘들면 힘들어요'),(12,'ESFP','파티피플 신나는 \"델피늄\"','단신을 행복하게 해줄게요','•사교적 긍정적 낙천적이에요\r•일은 최대한 미루다 한 번에 끝내버려요\r•유리 멘탈이라 혼자 있는 걸 힘들어해요'),(13,'ENTJ','주관 뚜렷 냉정한 \"퐁퐁국화\"','내 마음은 진심입니다','•답답한 사람이랑 같이 일하면 혼자 총대 메고 다해요\r•피해 주는 거, 피해받는 거 싫어하고 남 일에 관심 없어요\r•반복되는 실수 용납하지 않아요'),(14,'ENTP','마이웨이 죽지 않는 \"마트리카리아\"','역경에 굴하지 않는 강인함','•혼자서 돌아다니는 게 제일 편하고 독립심이 강한 마이웨이\r•자기합리화랑 포기를 잘해요\r•정해진 틀이나 반복적인 일을 가장 싫어해요'),(15,'ENFJ','지혜롭고 부드러운 \"다알리아\"','감사,화려,우아','•말로 사람을 움직이게 하는 능력이 탁월해요\r•핵인싸고 쾌활하지만, 스트레스받으면 세상 다운\r•사람을 잘 믿고 나보다 남이 먼저라 갈등을 싫어해요'),(16,'ENFP','천진난만한 \"프리지아\"','천진난만','•싫고 좋은 게 표정에서 드러나요\r•표현력이 매우 풍부하고 대화하는 걸 좋아해요\r•소외되는 걸 싫어해요');
/*!40000 ALTER TABLE `mbti` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-07 22:28:56
