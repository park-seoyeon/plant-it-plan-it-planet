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
-- Table structure for table `survey`
--

DROP TABLE IF EXISTS `survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey` (
  `question_number` int NOT NULL,
  `question` text COLLATE utf8mb4_unicode_ci,
  `answer_01` text COLLATE utf8mb4_unicode_ci,
  `answer_02` text COLLATE utf8mb4_unicode_ci,
  `answer_03` text COLLATE utf8mb4_unicode_ci,
  `answer_04` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`question_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey`
--

LOCK TABLES `survey` WRITE;
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
INSERT INTO `survey` VALUES (1,'처음 만나는 사람들에게 나는?','자리에서 누가 말을 걸러 올 때까지 기다린다','주변을 서성이며 말을 건넬 때 까지 기다린다','먼저 말을 건네지만 조금 어색하다','자연스럽게 친한척 말을 건넨다'),(2,'주말에 나는 주로?','친구들이 불러도 혼자만의 시간을 가진다','약속에 나가긴 하지만 혼자 있는게 더 좋다','친구들이 부르면 흔쾌히 나간다','먼저 나서서 친구들과 약속을 잡는다'),(3,'업무를 할 때 나는?','남들이 하는 방식으로 따라가는게 좋다','남들이 하는 방식으로 따라가다 나만의 방식을 적용해본다','나만의 방식으로 일하다 남들이 하는 방식을 적용해 본다.','나만의 방식으로 일하는게 좋다'),(4,'주변 사람들이 나를 보면?','꾸준하고 참을성 있다는 말을 자주 한다','일할 때는 꾸준하고 참을성 있다는 말을 자주한다','가끔 창의적이고 독창적인 면이 있다는 말을 자주한다','창의적이고 독창적이라는 말을 자주한다'),(5,'거절해야하는 상황이 오면 나는?','강력하게 할 수 없다고 거절한다','고민하다가 거절한다','고민하다가 대부분 들어주는 편이다','친구의 부탁이니 들어준다'),(6,'화가 났을 때 나는?','논리적으로 말하며 따진다','화가난 부분을 돌려 말한다','할 말이 많지만 어디서부터 말할지 모르겠다','할 말이 많지만 너무 분해서 눈물부터 난다'),(7,'끝나고 집에 가서 공부하려 했는데,\r친구들이 놀자고 붙잡는다. 나는?','이유를 말하며 거절한다','계획에 없던 일이라 당황스러워한다','조금 생각해 보지만 같이 간다','너무 좋아서 바로 함께 간다'),(8,'가고싶은 여행지 스타일은?','시간 장소 이동경로 모든걸 세세하게!','장소와 이동 경로는 짜지만 시간은 자유롭게!','큰 계획만 세우고 나머지는 자유롭게!','그때그때 생각나는대로!'),(9,'식물을 두려는 장소에 빛이 들어오는 시간은?','빛이 잘 들지 않는다 (예. 북향, 창과 거리가 있는 실내)','하루 2~3시간 정도 (예. 동향, 서향)','하루 6시간 (예, 남향 거실)','거의 온 종일 (예. 테라스, 베란다, 실외)'),(10,'평소, 창문을 얼마나 자주 여나요?','거의 환기하지 않는다','일주일에 2~3번 주기적으로 환기한다','하루 2~3시간 주기적으로 환기한다','항상 열어둔다'),(11,'식물을 두려는 장소는 얼마나 건조한가요?','목이 칼칼할 정도로 건조하다','습하지도, 건조하지도 않다','약간 습한데, 불쾌하지는 않다','공기의 무게가 느껴질 정도로 습하다'),(12,'식물을 두려는 장소에 아이나 반려동물이 있나요?','둘 다 없다','반려동물이 있다','아이가 있다','아이와 반려동물 모두 있다');
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;
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
