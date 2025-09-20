-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: python-project1
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `Order` int NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Amount` varchar(45) NOT NULL,
  PRIMARY KEY (`Order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partslist`
--

DROP TABLE IF EXISTS `partslist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partslist` (
  `Item No` int NOT NULL,
  `Item Name` varchar(45) NOT NULL,
  `Item amount` int NOT NULL,
  `Category` varchar(45) NOT NULL,
  `Item Cost` int NOT NULL,
  PRIMARY KEY (`Item No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partslist`
--

LOCK TABLES `partslist` WRITE;
/*!40000 ALTER TABLE `partslist` DISABLE KEYS */;
INSERT INTO `partslist` VALUES (111,'AMD Ryzen 5 3600',3,'Processor',12000),(112,'AMD Ryzen 5 5600',3,'Processor',15000),(113,'AMD Ryzen 5 5600G',3,'Processor',13500),(211,'MSI MAG b450m',3,'Motherboard',8500),(212,'Aurus Elite b450m argb',3,'Motherboard',11500),(213,'Aurus Elite b550m argb',3,'Motherboard',14500),(311,'Deepcool white argb',3,'Cooler',2800),(312,'Fantech Black rgb',3,'Cooler',1900),(313,'NZXT White 2600 rpm ARGB',3,'Cooler',4500),(411,'Montech Air100 white ARGB ',3,'Casing',6200),(412,'NZXT Revenger Mini',3,'Casing',4000),(413,'Deepcool white bk67',3,'Casing',4500),(511,'Teamsgate NVME M.2 PCIE 4.0 1TB',3,'SSD',9500),(512,'Seagate green 256GB',3,'SSD',2200),(513,'WD Green 500GB',3,'SSD',3500),(611,'Corsair Vengence 8Gb 3200hz DDR4',3,'RAM',2200),(612,'PNY XLR8 8GB ARGB 3200hz DDR4',3,'RAM',2600),(613,'OCPC 8GB ARGB 3200hz DDR4',3,'RAM',2600),(711,'GigaByte 450 watt',3,'PSU',4000),(712,'Deepcool 450watt 80+ Bronze',3,'PSU',5000),(713,'Thermaltake 550watt 80+Bronze',3,'PSU',6500),(811,'Sapphire Pulse RX6600 8GB',3,'GPU',26500),(812,'Nvidia RTX 3060 TI 12GB',3,'GPU',45000),(813,'AMD Radeon RX 6700 XT 12GB',3,'GPU',32000),(911,'Monitor 24 Inch',3,'Monitor',16500),(912,'HD Monitor 24 INCH 1080p',3,'Monitor',18500),(913,'LG UltraGear 27-inch 144Hz 1440p Monitor',3,'Monitor',18000),(1011,'A4 Tech regular Mouse',3,'Mouse',800),(1012,'Logitech g102 ARGB White',3,'Mouse',2800),(1013,'Razer DeathAdder Elite Gaming Mouse',3,'Mouse',4000);
/*!40000 ALTER TABLE `partslist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 19:54:04
