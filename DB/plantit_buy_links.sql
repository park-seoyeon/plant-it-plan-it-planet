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
-- Table structure for table `buy_links`
--

DROP TABLE IF EXISTS `buy_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buy_links` (
  `id` int NOT NULL,
  `plant_name` text COLLATE utf8mb4_unicode_ci,
  `buy_link` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buy_links`
--

LOCK TABLES `buy_links` WRITE;
/*!40000 ALTER TABLE `buy_links` DISABLE KEYS */;
INSERT INTO `buy_links` VALUES (1,'몬스테라 델리시오사','https://search.shopping.naver.com/search/all?query=몬스테라+델리시오사'),(2,'올리브 나무','https://search.shopping.naver.com/search/all?query=올리브+나무'),(3,'몬스테라 알보 바리에가타','https://search.shopping.naver.com/search/all?query=몬스테라+알보+바리에가타'),(4,'몬스테라 아단소니','https://search.shopping.naver.com/search/all?query=몬스테라+아단소니'),(5,'스투키','https://search.shopping.naver.com/search/all?query=스투키'),(6,'은엽 아카시아','https://search.shopping.naver.com/search/all?query=은엽+아카시아'),(7,'사계귤 (유주나무)','https://search.shopping.naver.com/search/all?query=사계귤+(유주나무)'),(8,'헤데라 (아이비)','https://search.shopping.naver.com/search/all?query=헤데라+(아이비)'),(9,'아레카야자','https://search.shopping.naver.com/search/all?query=아레카야자'),(10,'금전수 (돈나무)','https://search.shopping.naver.com/search/all?query=금전수+(돈나무)'),(11,'테이블 야자','https://search.shopping.naver.com/search/all?query=테이블+야자'),(12,'벵갈 고무나무','https://search.shopping.naver.com/search/all?query=벵갈+고무나무'),(13,'스파티필름','https://search.shopping.naver.com/search/all?query=스파티필름'),(14,'보스턴 고사리','https://search.shopping.naver.com/search/all?query=보스턴+고사리'),(15,'바질','https://search.shopping.naver.com/search/all?query=바질'),(16,'생선뼈 선인장 (피쉬본 선인장)','https://search.shopping.naver.com/search/all?query=생선뼈+선인장+(피쉬본+선인장)'),(17,'산세베리아 문샤인','https://search.shopping.naver.com/search/all?query=산세베리아+문샤인'),(18,'필로덴드론 콩고','https://search.shopping.naver.com/search/all?query=필로덴드론+콩고'),(19,'홍콩 야자 (쉐프렐라 홍콩)','https://search.shopping.naver.com/search/all?query=홍콩+야자+(쉐프렐라+홍콩)'),(20,'호야 카르노사 (무늬 호야)','https://search.shopping.naver.com/search/all?query=호야+카르노사+(무늬+호야)'),(21,'호주매화 (마누카)','https://search.shopping.naver.com/search/all?query=호주매화+(마누카)'),(22,'멜라니 고무나무','https://search.shopping.naver.com/search/all?query=멜라니+고무나무'),(23,'로즈마리','https://search.shopping.naver.com/search/all?query=로즈마리'),(24,'유카','https://search.shopping.naver.com/search/all?query=유카'),(25,'알로카시아 오도라','https://search.shopping.naver.com/search/all?query=알로카시아+오도라'),(26,'아스파라거스 나누스','https://search.shopping.naver.com/search/all?query=아스파라거스+나누스'),(27,'극락조화','https://search.shopping.naver.com/search/all?query=극락조화'),(28,'블루스타 고사리','https://search.shopping.naver.com/search/all?query=블루스타+고사리'),(29,'율마 (윌마)','https://search.shopping.naver.com/search/all?query=율마+(윌마)'),(30,'필로덴드론 셀로움','https://search.shopping.naver.com/search/all?query=필로덴드론+셀로움'),(31,'유칼립투스 구니','https://search.shopping.naver.com/search/all?query=유칼립투스+구니'),(32,'떡갈잎 고무나무','https://search.shopping.naver.com/search/all?query=떡갈잎+고무나무'),(33,'싱고니움','https://search.shopping.naver.com/search/all?query=싱고니움'),(34,'파키라','https://search.shopping.naver.com/search/all?query=파키라'),(35,'스킨답서스','https://search.shopping.naver.com/search/all?query=스킨답서스'),(36,'칼라디움','https://search.shopping.naver.com/search/all?query=칼라디움'),(37,'여인초','https://search.shopping.naver.com/search/all?query=여인초'),(38,'칼라데아 오르비폴리아','https://search.shopping.naver.com/search/all?query=칼라데아+오르비폴리아'),(39,'세네시오 칸디칸스 (엔젤윙)','https://search.shopping.naver.com/search/all?query=세네시오+칸디칸스+(엔젤윙)'),(40,'개운죽','https://search.shopping.naver.com/search/all?query=개운죽'),(41,'알로에 베라','https://search.shopping.naver.com/search/all?query=알로에+베라'),(42,'휘카스 움베르타','https://search.shopping.naver.com/search/all?query=휘카스+움베르타'),(43,'마오리 소포라','https://search.shopping.naver.com/search/all?query=마오리+소포라'),(44,'켄차 야자','https://search.shopping.naver.com/search/all?query=켄차+야자'),(45,'관음죽','https://search.shopping.naver.com/search/all?query=관음죽'),(46,'원숭이꼬리 선인장','https://search.shopping.naver.com/search/all?query=원숭이꼬리+선인장'),(47,'브레이니아 니보사 (소코라코)','https://search.shopping.naver.com/search/all?query=브레이니아+니보사+(소코라코)'),(48,'해피트리','https://search.shopping.naver.com/search/all?query=해피트리'),(49,'다바나 고사리','https://search.shopping.naver.com/search/all?query=다바나+고사리'),(50,'인도 고무나무','https://search.shopping.naver.com/search/all?query=인도+고무나무'),(51,'코로키아','https://search.shopping.naver.com/search/all?query=코로키아'),(52,'수박 페페로미아','https://search.shopping.naver.com/search/all?query=수박+페페로미아'),(53,'드라세나 드라코 (용혈수)','https://search.shopping.naver.com/search/all?query=드라세나+드라코+(용혈수)'),(54,'아가베 아테누아타','https://search.shopping.naver.com/search/all?query=아가베+아테누아타'),(55,'립살리스 트리고나','https://search.shopping.naver.com/search/all?query=립살리스+트리고나'),(56,'박쥐란','https://search.shopping.naver.com/search/all?query=박쥐란'),(57,'틸란드시아 시아네아','https://search.shopping.naver.com/search/all?query=틸란드시아+시아네아'),(58,'동백나무','https://search.shopping.naver.com/search/all?query=동백나무'),(59,'오렌지 자스민','https://search.shopping.naver.com/search/all?query=오렌지+자스민'),(60,'마란타 레우코네우라','https://search.shopping.naver.com/search/all?query=마란타+레우코네우라'),(61,'녹태고','https://search.shopping.naver.com/search/all?query=녹태고'),(62,'엽란','https://search.shopping.naver.com/search/all?query=엽란'),(63,'필로덴드론 옥시카르디움 \'브라질\'','https://search.shopping.naver.com/search/all?query=필로덴드론+옥시카르디움+\'브라질\''),(64,'미모사','https://search.shopping.naver.com/search/all?query=미모사'),(65,'백묘국','https://search.shopping.naver.com/search/all?query=백묘국'),(66,'아라우카리아','https://search.shopping.naver.com/search/all?query=아라우카리아'),(67,'칼라데아 세토사','https://search.shopping.naver.com/search/all?query=칼라데아+세토사'),(68,'유칼립투스 폴리안','https://search.shopping.naver.com/search/all?query=유칼립투스+폴리안'),(69,'페퍼민트','https://search.shopping.naver.com/search/all?query=페퍼민트'),(70,'애니시다','https://search.shopping.naver.com/search/all?query=애니시다'),(71,'칼랑코에','https://search.shopping.naver.com/search/all?query=칼랑코에'),(72,'수염 틸란드시아','https://search.shopping.naver.com/search/all?query=수염+틸란드시아'),(73,'산세베리아','https://search.shopping.naver.com/search/all?query=산세베리아'),(74,'무늬 푸미라','https://search.shopping.naver.com/search/all?query=무늬+푸미라'),(75,'알로카시아 아마조니카','https://search.shopping.naver.com/search/all?query=알로카시아+아마조니카'),(76,'덕구리난','https://search.shopping.naver.com/search/all?query=덕구리난'),(77,'히아신스','https://search.shopping.naver.com/search/all?query=히아신스'),(78,'소철','https://search.shopping.naver.com/search/all?query=소철'),(79,'펫츠 헤데라','https://search.shopping.naver.com/search/all?query=펫츠+헤데라'),(80,'안스리움 안드레아눔','https://search.shopping.naver.com/search/all?query=안스리움+안드레아눔'),(81,'필레아 페페로미오데스','https://search.shopping.naver.com/search/all?query=필레아+페페로미오데스'),(82,'틸란시아 세로그라피카','https://search.shopping.naver.com/search/all?query=틸란시아+세로그라피카'),(83,'알로카시아 프라이덱','https://search.shopping.naver.com/search/all?query=알로카시아+프라이덱'),(84,'페페로미아 페퍼스팟','https://search.shopping.naver.com/search/all?query=페페로미아+페퍼스팟'),(85,'보라 사랑초','https://search.shopping.naver.com/search/all?query=보라+사랑초'),(86,'접란 (클로로피텀)','https://search.shopping.naver.com/search/all?query=접란+(클로로피텀)'),(87,'알리 고무나무','https://search.shopping.naver.com/search/all?query=알리+고무나무'),(88,'화이트 고스트','https://search.shopping.naver.com/search/all?query=화이트+고스트'),(89,'라벤더','https://search.shopping.naver.com/search/all?query=라벤더'),(90,'코코스 야자 (코코넛 야자)','https://search.shopping.naver.com/search/all?query=코코스+야자+(코코넛+야자)'),(91,'드라세나 마지나타','https://search.shopping.naver.com/search/all?query=드라세나+마지나타'),(92,'크루시아','https://search.shopping.naver.com/search/all?query=크루시아'),(93,'후마타 고사리','https://search.shopping.naver.com/search/all?query=후마타+고사리'),(94,'디펜바키아 마리안느','https://search.shopping.naver.com/search/all?query=디펜바키아+마리안느'),(95,'염좌','https://search.shopping.naver.com/search/all?query=염좌'),(96,'무늬벤자민 고무나무','https://search.shopping.naver.com/search/all?query=무늬벤자민+고무나무'),(97,'피닉스 야자','https://search.shopping.naver.com/search/all?query=피닉스+야자'),(98,'줄리아 페페','https://search.shopping.naver.com/search/all?query=줄리아+페페'),(99,'알로카시아 블랙벨벳','https://search.shopping.naver.com/search/all?query=알로카시아+블랙벨벳'),(100,'드라세나 맛상게아나 (행운목)','https://search.shopping.naver.com/search/all?query=드라세나+맛상게아나+(행운목)'),(101,'아비스','https://search.shopping.naver.com/search/all?query=아비스'),(102,'장미허브','https://search.shopping.naver.com/search/all?query=장미허브'),(103,'산토소마 린드니','https://search.shopping.naver.com/search/all?query=산토소마+린드니'),(104,'왜성 바나나','https://search.shopping.naver.com/search/all?query=왜성+바나나'),(105,'티트리','https://search.shopping.naver.com/search/all?query=티트리'),(106,'축전','https://search.shopping.naver.com/search/all?query=축전'),(107,'긴잎 아카시아','https://search.shopping.naver.com/search/all?query=긴잎+아카시아'),(108,'용신목','https://search.shopping.naver.com/search/all?query=용신목'),(109,'제라늄','https://search.shopping.naver.com/search/all?query=제라늄'),(110,'드라세나 콤팩타','https://search.shopping.naver.com/search/all?query=드라세나+콤팩타'),(111,'러브체인','https://search.shopping.naver.com/search/all?query=러브체인'),(112,'백도선','https://search.shopping.naver.com/search/all?query=백도선'),(113,'디지고테카 아랄리아','https://search.shopping.naver.com/search/all?query=디지고테카+아랄리아'),(114,'에크메아 파시아타','https://search.shopping.naver.com/search/all?query=에크메아+파시아타'),(115,'청하각','https://search.shopping.naver.com/search/all?query=청하각'),(116,'멕시코 소철','https://search.shopping.naver.com/search/all?query=멕시코+소철'),(117,'팔손이 나무','https://search.shopping.naver.com/search/all?query=팔손이+나무'),(118,'필로덴드론 플로리다뷰티','https://search.shopping.naver.com/search/all?query=필로덴드론+플로리다뷰티'),(119,'십이지권','https://search.shopping.naver.com/search/all?query=십이지권'),(120,'호야 콤팩타 (리본호야)','https://search.shopping.naver.com/search/all?query=호야+콤팩타+(리본호야)'),(121,'드라세나 와네키','https://search.shopping.naver.com/search/all?query=드라세나+와네키'),(122,'무스카리','https://search.shopping.naver.com/search/all?query=무스카리'),(123,'베고니아','https://search.shopping.naver.com/search/all?query=베고니아'),(124,'녹영','https://search.shopping.naver.com/search/all?query=녹영'),(125,'유칼립투스 슈가검','https://search.shopping.naver.com/search/all?query=유칼립투스+슈가검'),(126,'청페페','https://search.shopping.naver.com/search/all?query=청페페'),(127,'은사초','https://search.shopping.naver.com/search/all?query=은사초'),(128,'틸란드시아 이오난사','https://search.shopping.naver.com/search/all?query=틸란드시아+이오난사'),(129,'더피 고사리','https://search.shopping.naver.com/search/all?query=더피+고사리'),(130,'하월시아 옵투사','https://search.shopping.naver.com/search/all?query=하월시아+옵투사'),(131,'시기지움 (피어리스)','https://search.shopping.naver.com/search/all?query=시기지움+(피어리스)'),(132,'남천','https://search.shopping.naver.com/search/all?query=남천'),(133,'튤립','https://search.shopping.naver.com/search/all?query=튤립'),(134,'알로카시아 사리안','https://search.shopping.naver.com/search/all?query=알로카시아+사리안'),(135,'크로톤','https://search.shopping.naver.com/search/all?query=크로톤'),(136,'블루 아이스','https://search.shopping.naver.com/search/all?query=블루+아이스'),(137,'루카덴드론','https://search.shopping.naver.com/search/all?query=루카덴드론'),(138,'필로덴드론 버킨 (무늬콩고)','https://search.shopping.naver.com/search/all?query=필로덴드론+버킨+(무늬콩고)'),(139,'디시디아 밀리언하트','https://search.shopping.naver.com/search/all?query=디시디아+밀리언하트'),(140,'틸란드시아 푼키아나','https://search.shopping.naver.com/search/all?query=틸란드시아+푼키아나'),(141,'휘카스 페티올라리스','https://search.shopping.naver.com/search/all?query=휘카스+페티올라리스'),(142,'디펜바키아 트로픽스노우','https://search.shopping.naver.com/search/all?query=디펜바키아+트로픽스노우'),(143,'레몬밤','https://search.shopping.naver.com/search/all?query=레몬밤'),(144,'오로라 페페','https://search.shopping.naver.com/search/all?query=오로라+페페'),(145,'아글라오네마','https://search.shopping.naver.com/search/all?query=아글라오네마'),(146,'페페로미아 프로스트라타','https://search.shopping.naver.com/search/all?query=페페로미아+프로스트라타'),(147,'안스리움 클라리너비움','https://search.shopping.naver.com/search/all?query=안스리움+클라리너비움'),(148,'석송','https://search.shopping.naver.com/search/all?query=석송'),(149,'프리지아','https://search.shopping.naver.com/search/all?query=프리지아'),(150,'천냥금','https://search.shopping.naver.com/search/all?query=천냥금'),(151,'왁스 플라워','https://search.shopping.naver.com/search/all?query=왁스+플라워'),(152,'비화옥','https://search.shopping.naver.com/search/all?query=비화옥'),(153,'필로덴드론 핑크프린세스','https://search.shopping.naver.com/search/all?query=필로덴드론+핑크프린세스'),(154,'마리모','https://search.shopping.naver.com/search/all?query=마리모'),(155,'둥근 잎 아카시아','https://search.shopping.naver.com/search/all?query=둥근+잎+아카시아'),(156,'흑법사','https://search.shopping.naver.com/search/all?query=흑법사'),(157,'비스마르크 야자','https://search.shopping.naver.com/search/all?query=비스마르크+야자'),(158,'학 자스민','https://search.shopping.naver.com/search/all?query=학+자스민'),(159,'안스리움 크리스탈리넘','https://search.shopping.naver.com/search/all?query=안스리움+크리스탈리넘'),(160,'오색 마삭줄 (초설 마삭줄)','https://search.shopping.naver.com/search/all?query=오색+마삭줄+(초설+마삭줄)'),(161,'필로덴드론 베루코섬','https://search.shopping.naver.com/search/all?query=필로덴드론+베루코섬'),(162,'지바시스 펠루치다 (실달개비, 엘레강스)','https://search.shopping.naver.com/search/all?query=지바시스+펠루치다+(실달개비,+엘레강스)'),(163,'목마가렛','https://search.shopping.naver.com/search/all?query=목마가렛'),(164,'무늬 산호수','https://search.shopping.naver.com/search/all?query=무늬+산호수'),(165,'트리안','https://search.shopping.naver.com/search/all?query=트리안'),(166,'초코리프','https://search.shopping.naver.com/search/all?query=초코리프'),(167,'아프리칸 바이올렛','https://search.shopping.naver.com/search/all?query=아프리칸+바이올렛'),(168,'필로덴드론 레몬라임','https://search.shopping.naver.com/search/all?query=필로덴드론+레몬라임'),(169,'연화죽','https://search.shopping.naver.com/search/all?query=연화죽'),(170,'장미','https://search.shopping.naver.com/search/all?query=장미'),(171,'콜레우스','https://search.shopping.naver.com/search/all?query=콜레우스'),(172,'워터 코인','https://search.shopping.naver.com/search/all?query=워터+코인'),(173,'시클라멘','https://search.shopping.naver.com/search/all?query=시클라멘'),(174,'마블 선인장','https://search.shopping.naver.com/search/all?query=마블+선인장'),(175,'개나리 자스민','https://search.shopping.naver.com/search/all?query=개나리+자스민'),(176,'디시디아 메론','https://search.shopping.naver.com/search/all?query=디시디아+메론'),(177,'타라','https://search.shopping.naver.com/search/all?query=타라'),(178,'프테리스','https://search.shopping.naver.com/search/all?query=프테리스'),(179,'필로덴드론 글로리오섬','https://search.shopping.naver.com/search/all?query=필로덴드론+글로리오섬'),(180,'산세베리아 하니','https://search.shopping.naver.com/search/all?query=산세베리아+하니'),(181,'슈퍼바 산세베리아','https://search.shopping.naver.com/search/all?query=슈퍼바+산세베리아'),(182,'휘토니아','https://search.shopping.naver.com/search/all?query=휘토니아'),(183,'괴마옥','https://search.shopping.naver.com/search/all?query=괴마옥'),(184,'필로덴드론 멜라노크리섬','https://search.shopping.naver.com/search/all?query=필로덴드론+멜라노크리섬'),(185,'쿠션부쉬','https://search.shopping.naver.com/search/all?query=쿠션부쉬'),(186,'디시디아 화이트','https://search.shopping.naver.com/search/all?query=디시디아+화이트'),(187,'사랑초 옵투사','https://search.shopping.naver.com/search/all?query=사랑초+옵투사'),(188,'디운에둘레 소철','https://search.shopping.naver.com/search/all?query=디운에둘레+소철'),(189,'수선화','https://search.shopping.naver.com/search/all?query=수선화'),(190,'안스리움 리갈레','https://search.shopping.naver.com/search/all?query=안스리움+리갈레'),(191,'무레이 소철','https://search.shopping.naver.com/search/all?query=무레이+소철'),(192,'디바오 소철','https://search.shopping.naver.com/search/all?query=디바오+소철'),(193,'산호수','https://search.shopping.naver.com/search/all?query=산호수'),(194,'금청각','https://search.shopping.naver.com/search/all?query=금청각'),(195,'율리치아나 스프랄리스','https://search.shopping.naver.com/search/all?query=율리치아나+스프랄리스'),(196,'틸란드시아 준세아','https://search.shopping.naver.com/search/all?query=틸란드시아+준세아'),(197,'안스리움 포게티','https://search.shopping.naver.com/search/all?query=안스리움+포게티'),(198,'썰프레아','https://search.shopping.naver.com/search/all?query=썰프레아'),(199,'바로크 벤자민','https://search.shopping.naver.com/search/all?query=바로크+벤자민'),(200,'필로덴드론 플로우마니','https://search.shopping.naver.com/search/all?query=필로덴드론+플로우마니'),(201,'귀면각','https://search.shopping.naver.com/search/all?query=귀면각'),(202,'디시디아 애플','https://search.shopping.naver.com/search/all?query=디시디아+애플'),(203,'필로덴드론 베루코섬 X 멜라노크리섬','https://search.shopping.naver.com/search/all?query=필로덴드론+베루코섬+X+멜라노크리섬'),(204,'금사철','https://search.shopping.naver.com/search/all?query=금사철'),(205,'틸란드시아 바일레이','https://search.shopping.naver.com/search/all?query=틸란드시아+바일레이'),(206,'아스플레니움 코브라','https://search.shopping.naver.com/search/all?query=아스플레니움+코브라'),(207,'백운각','https://search.shopping.naver.com/search/all?query=백운각'),(208,'필로덴드론 마메이','https://search.shopping.naver.com/search/all?query=필로덴드론+마메이'),(209,'아라비안 자스민','https://search.shopping.naver.com/search/all?query=아라비안+자스민'),(210,'디시디아 넘초크','https://search.shopping.naver.com/search/all?query=디시디아+넘초크'),(211,'틸란드시아 휴스톤','https://search.shopping.naver.com/search/all?query=틸란드시아+휴스톤'),(212,'틸란드시아 스트릭타','https://search.shopping.naver.com/search/all?query=틸란드시아+스트릭타'),(213,'눈꽃 선인장','https://search.shopping.naver.com/search/all?query=눈꽃+선인장'),(214,'틸란드시아 드루이드','https://search.shopping.naver.com/search/all?query=틸란드시아+드루이드'),(215,'틸란드시아 카풋 메두사','https://search.shopping.naver.com/search/all?query=틸란드시아+카풋+메두사'),(216,'아프리칸 미니바이올렛','https://search.shopping.naver.com/search/all?query=아프리칸+미니바이올렛'),(217,'틸란드시아 아르젠티아','https://search.shopping.naver.com/search/all?query=틸란드시아+아르젠티아'),(218,'틸란드시아 셀레리아나','https://search.shopping.naver.com/search/all?query=틸란드시아+셀레리아나'),(219,'틸란드시아 애란토스','https://search.shopping.naver.com/search/all?query=틸란드시아+애란토스'),(220,'필로덴드론 파스타짜넘','https://search.shopping.naver.com/search/all?query=필로덴드론+파스타짜넘'),(221,'틸란드시아 이오난사 푸에고','https://search.shopping.naver.com/search/all?query=틸란드시아+이오난사+푸에고'),(222,'호리더스 소철','https://search.shopping.naver.com/search/all?query=호리더스+소철'),(223,'자주 만년초 (부자란)','https://search.shopping.naver.com/search/all?query=자주+만년초+(부자란)'),(224,'틸란드시아 필리폴리아','https://search.shopping.naver.com/search/all?query=틸란드시아+필리폴리아'),(225,'틸란드시아 쉬데이아나','https://search.shopping.naver.com/search/all?query=틸란드시아+쉬데이아나'),(226,'미니 알로에','https://search.shopping.naver.com/search/all?query=미니+알로에'),(227,'수채화 고무나무','https://search.shopping.naver.com/search/all?query=수채화+고무나무'),(228,'머틀허브','https://search.shopping.naver.com/search/all?query=머틀허브'),(229,'무늬아이비','https://search.shopping.naver.com/search/all?query=무늬아이비');
/*!40000 ALTER TABLE `buy_links` ENABLE KEYS */;
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