-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 28, 2022 at 04:22 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lioli_website`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('bc73d02abb43');

-- --------------------------------------------------------

--
-- Table structure for table `career`
--

CREATE TABLE `career` (
  `id` int(11) NOT NULL,
  `post` text NOT NULL,
  `location` text NOT NULL,
  `experience` text NOT NULL,
  `salary` text NOT NULL,
  `description` text NOT NULL,
  `requirements` text NOT NULL,
  `date_posted` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `career`
--

INSERT INTO `career` (`id`, `post`, `location`, `experience`, `salary`, `description`, `requirements`, `date_posted`) VALUES
(1, 'Area Sales Manager', 'Ahmedabad,Mumbai,Kerela,Chandigarh,Hyderabad,Jammu,Chennai,Delhi,Lucknow', '4 to 5 years', '35000 - 45000 PM', 'Current industry must be ceramics / Tile / Building material. Must have an experience in building & flooring materials like tiles, marbles, etc. He / she must be active in the designated location market.', 'Reaching the targets and goals set for your area.Maintaining and increasing sales of your company\'s products.Establishing, maintaining and expanding your customer base.Servicing the needs of your existing customers.Increasing business opportunities through various routes to market.Setting sales targets for individual reps and your team as a whole.  Recruiting and training sales staff.  Allocating areas to sales representatives.  Developing sales strategies and setting targets.  Monitoring your team\'s performance and motivating them to reach targets.  Compiling and analysing sales figures.  Possibly dealing with some major customer accounts yourself.  Collecting customer feedback and market research.  Reporting to senior managers.  Keeping up to date with products and competitors.  In some jobs, you may also be involved with marketing', '2022-01-25 13:22:40'),
(3, 'Front Desk Executive', 'Morbi', '2 Years', '18000+', 'We are looking for a pleasant Front Desk Executive to undertake all receptionist and clerical duties at the desk of our main entrance. You will be the “face” of the company for all visitors and will be responsible for the first impression we make. The ideal candidate will have a friendly and easy going personality while also being very perceptive and disciplined. The goal is to make guests and visitors feel comfortable and valued while on our premises.', 'Keep front desk tidy and presentable with all necessary material (pens, forms, paper etc).Greet and welcome guests, Clients & Customers. Answer questions and address complaints. Answer all incoming calls and redirect them or keep messages. Receive letters, packages etc and distribute them. Keep updated visitor records and files. Familiarity with office machines (eg fax, printer etc). Knowledge of office management and basic bookkeeping. Proficient in English, Hindi & Gujarati Excellent knowledge of MS Office', '2022-02-21 14:39:12');

-- --------------------------------------------------------

--
-- Table structure for table `catalogue`
--

CREATE TABLE `catalogue` (
  `id` int(11) NOT NULL,
  `pdf` text DEFAULT NULL,
  `preview` text NOT NULL,
  `catalogue_name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `catalogue`
--

INSERT INTO `catalogue` (`id`, `pdf`, `preview`, `catalogue_name`) VALUES
(9, 'Lioli Stone Arch 800x2400x15mm.pdf', '361e74e7d35c84b6.jpg', '800x2400mm'),
(14, 'Lioli_cleaning_and_mainenance_guide.pdf', 'a75a5a897ec00445.jpg', 'Cleaning And Maintainance Guide'),
(15, 'Lioli_General_Guidline_for_handling_cutting___Installation.pdf', '94f10706502e6887.jpg', 'General Guideline'),
(16, 'Manufacturer_recommendations_for_installation_of_large_format_tiles.pdf', 'bbe265a15544919a.jpg', 'Manufacturer Recommendations'),
(18, 'Lioli_Catalogue_2022.pdf', '5f85082fc556378f.jpg', 'Lioli Catalogue 2022');

-- --------------------------------------------------------

--
-- Table structure for table `collection`
--

CREATE TABLE `collection` (
  `id` int(11) NOT NULL,
  `collection` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `collection`
--

INSERT INTO `collection` (`id`, `collection`) VALUES
(1, 'Marble Series'),
(4, 'Terrazzo Series'),
(5, 'Stone Series'),
(6, 'Concrete Series'),
(7, 'Onyx Series'),
(8, 'Orgatech Series'),
(9, 'Wooden Series'),
(10, 'Art Series'),
(11, 'Bookmatch'),
(12, 'Meek Series');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `assistence` varchar(200) DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `profession` varchar(200) DEFAULT NULL,
  `representing_company` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `country` text DEFAULT NULL,
  `message` text DEFAULT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `download`
--

CREATE TABLE `download` (
  `id` int(11) NOT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `catalogue` varchar(200) DEFAULT NULL,
  `city` text DEFAULT NULL,
  `message` text DEFAULT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `download`
--

INSERT INTO `download` (`id`, `full_name`, `email`, `phone`, `catalogue`, `city`, `message`, `date`) VALUES
(1, 'Admin Cretx', 'musimshad98@gmail.com', '1234567895', 'Manufacturer Recommendations', 'Ahmedabad', 'Nothing', '2022-02-28 13:19:42');

-- --------------------------------------------------------

--
-- Table structure for table `gallery`
--

CREATE TABLE `gallery` (
  `id` int(11) NOT NULL,
  `preview` text DEFAULT NULL,
  `link` text DEFAULT NULL,
  `video` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gallery`
--

INSERT INTO `gallery` (`id`, `preview`, `link`, `video`) VALUES
(3, NULL, 'https://www.youtube.com/embed/MxwMsCmQei0', NULL),
(4, '24432e92452e2ae4.png', NULL, 'premium.mp4'),
(6, NULL, 'https://www.youtube.com/embed/G5uX-t53038', NULL),
(7, '4044051593c38b8b.png', NULL, 'Lioli_Video_Square-1.m4v'),
(8, 'df05dd818b3f908f.png', NULL, 'Lioli_Video-1.m4v'),
(9, 'edd08251e51f71c1.png', NULL, 'Lioli_Vid_6_Converted.m4v'),
(10, 'a1a4ae2ba9ba554d.png', NULL, 'Liolistonarch-1.m4v'),
(11, '4118012ada5e3e69.png', NULL, 'Lioli_Final_Audio.mp4'),
(12, '20a2f88e34324f76.png', NULL, 'Lioli_5_Sound-1.m4v');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `product_name` varchar(200) DEFAULT NULL,
  `collection_id` int(11) NOT NULL,
  `surface_id` int(11) NOT NULL,
  `thickness_id` int(11) NOT NULL,
  `size_id` int(11) NOT NULL,
  `product_image` text NOT NULL,
  `preview` varchar(30) NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL
) ;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `product_name`, `collection_id`, `surface_id`, `thickness_id`, `size_id`, `product_image`, `preview`, `is_deleted`) VALUES
(1, 'Armani Brown', 1, 1, 1, 1, '1cbe535fARMANI_BROWN_F1.jpg,1cbe535fARMANI_BROWN_F2.jpg,1cbe535fARMANI_BROWN_F3.jpg,1cbe535fARMANI_BROWN_F4.jpg,1cbe535fARMANI_BROWN_F5.jpg,1cbe535fARMANI_BROWN_F6.jpg', '76fc7699d20c23ff.jpg', 0),
(2, 'Armani Gold', 1, 1, 1, 1, '80364e4fARMANI_GOLD_05_1050x1780_002_F1.jpg,80364e4fARMANI_GOLD_05_1050x1780_002_F2.jpg,80364e4fARMANI_GOLD_05_1050x1780_002_F3.jpg,80364e4fARMANI_GOLD_05_1050x1780_002_F4.jpg,80364e4fARMANI_GOLD_05_1050x1780_002_F5.jpg', 'afc44953ef26f6b0.jpg', 0),
(3, 'Armani Grey', 1, 1, 1, 1, 'feaa6d86ARMANI_GREY_F1.jpg,feaa6d86ARMANI_GREY_F2.jpg,feaa6d86ARMANI_GREY_F3.jpg,feaa6d86ARMANI_GREY_F4.jpg,feaa6d86ARMANI_GREY_F5.jpg', '62900247fccb0a5b.jpg', 0),
(4, 'Avola Mocha', 5, 3, 1, 1, '571616f3Avola-F1.jpg,571616f3Avola-F2.jpg,571616f3Avola-F3.jpg,571616f3Avola-F4.jpg', 'a790b1740a4b05df.jpg', 0),
(5, 'Beton Flakes', 4, 3, 1, 1, 'e2dd1b24BETON_FLAKE_GREY-F1.jpg,e2dd1b24BETON_FLAKE_GREY-F2.jpg,e2dd1b24BETON_FLAKE_GREY-F3.jpg,e2dd1b24BETON_FLAKE_GREY-F4.jpg', 'a896b197b933fa61.jpg', 0),
(6, 'Botticino Florito', 1, 1, 1, 1, '54791854BOTTICINO_FIORITO_A.jpg,54791854BOTTICINO_FIORITO_B.jpg,54791854BOTTICINO_FIORITO_C.jpg,54791854BOTTICINO_FIORITO_D.jpg', 'fc48df6f4ec32ec1.jpg', 0),
(7, 'Armani Gold', 1, 3, 1, 1, 'bd513b05ARMANI_GOLD_05_1050x1780_002_F1.jpg,bd513b05ARMANI_GOLD_05_1050x1780_002_F2.jpg,bd513b05ARMANI_GOLD_05_1050x1780_002_F3.jpg,bd513b05ARMANI_GOLD_05_1050x1780_002_F4.jpg,bd513b05ARMANI_GOLD_05_1050x1780_002_F5.jpg', '0156a23be97ebe89.jpg', 0),
(8, 'Armani Grey', 1, 3, 1, 1, '96d3ddb1ARMANI_GREY_F1.jpg,96d3ddb1ARMANI_GREY_F2.jpg,96d3ddb1ARMANI_GREY_F3.jpg,96d3ddb1ARMANI_GREY_F4.jpg,96d3ddb1ARMANI_GREY_F5.jpg', 'a5a0dc82118532fd.jpg', 0),
(9, 'Bruno Flakes', 4, 3, 1, 1, '44eda95bBRUNO_FLAKES-F1.jpg,44eda95bBRUNO_FLAKES-F2.jpg,44eda95bBRUNO_FLAKES-F3.jpg,44eda95bBRUNO_FLAKES-F4.jpg', '5809cbd8709d57b3.jpg', 0),
(10, 'Calacutta Bianco Oro', 1, 1, 1, 1, 'd673b8c9CALACUTTA_BINACO_ORO_F-1.jpg,d673b8c9CALACUTTA_BINACO_ORO_F-2.jpg,d673b8c9CALACUTTA_BINACO_ORO_F-3.jpg,d673b8c9CALACUTTA_BINACO_ORO_F-4.jpg,d673b8c9CALACUTTA_BINACO_ORO_F-5.jpg', 'f8e83f74c87ef0aa.jpg', 0),
(11, 'Emperador Classic', 1, 1, 1, 1, 'af5ddb8dEMPERADOR_CLASSIC-F1.jpg,af5ddb8dEMPERADOR_CLASSIC-F2.jpg,af5ddb8dEMPERADOR_CLASSIC-F3.jpg,af5ddb8dEMPERADOR_CLASSIC-F4.jpg', '3301411d42e9df45.jpg', 0),
(12, 'Emperador Light', 1, 1, 1, 1, '89e25de2EMPERADOR_LIGHT_F1.jpg,89e25de2EMPERADOR_LIGHT_F2.jpg,89e25de2EMPERADOR_LIGHT_F3.jpg,89e25de2EMPERADOR_LIGHT_F4.jpg', 'ddeb3527fe07039d.jpg', 0),
(13, 'Grigio Nuvolato', 1, 1, 1, 1, '27a47d92GRIGIO_NUOVOLATO_F1.jpg,27a47d92GRIGIO_NUOVOLATO_F2.jpg,27a47d92GRIGIO_NUOVOLATO_F3.jpg,27a47d92GRIGIO_NUOVOLATO_F4.jpg', '5ca1901e59060ba7.jpg', 0),
(14, 'Lithic Antracite', 6, 3, 1, 1, 'f8aa858bLITHIC_ANTRACITE-F2.jpg,f8aa858bLITHIC_ANTRACITE-F3.jpg,f8aa858bLITHIC_ANTRACITE-F4.jpg,f8aa858bLITHIC_ANTRACITE-F-1.jpg', 'c63ea1d140009eab.jpg', 0),
(15, 'Lithic Coin', 6, 3, 1, 1, 'd5081125LITHIC_COIN-F1.jpg,d5081125LITHIC_COIN-F2.jpg,d5081125LITHIC_COIN-F3.jpg,d5081125LITHIC_COIN-F4.jpg', 'f4a8709ba23befd1.jpg', 0),
(16, 'Lithic Latte', 6, 3, 1, 1, '12345516LITHIC_LATTE-F1.jpg,12345516LITHIC_LATTE-F2.jpg,12345516LITHIC_LATTE-F3.jpg,12345516LITHIC_LATTE-F4.jpg', '9927aaa59dafc2f0.jpg', 0),
(17, 'Nero Marquina', 1, 1, 1, 1, '352ce187NERO_MARQUINA_F1.jpg,352ce187NERO_MARQUINA_F2.jpg,352ce187NERO_MARQUINA_F3.jpg,352ce187NERO_MARQUINA_F4.jpg,352ce187NERO_MARQUINA_F5.jpg,352ce187NERO_MARQUINA_F6.jpg', '5e2ecb2d92e10e15.jpg', 0),
(18, 'Omani', 1, 1, 1, 1, '3e456ad1OMANI_F1.jpg,3e456ad1OMANI_F2.jpg,3e456ad1OMANI_F3.jpg,3e456ad1OMANI_F4.jpg,3e456ad1OMANI_F5.jpg,3e456ad1OMANI_F6.jpg', '6a574d8829446876.jpg', 0),
(19, 'Pietra Gey', 1, 1, 1, 1, 'bb7b5379PIETRA_GREY-F1.jpg,bb7b5379PIETRA_GREY-F2.jpg,bb7b5379PIETRA_GREY-F3.jpg,bb7b5379PIETRA_GREY-F4.jpg,bb7b5379PIETRA_GREY-F5.jpg,bb7b5379PIETRA_GREY-F6.jpg', '7c93a330538f4646.jpg', 0),
(20, 'Pietra Gey', 1, 3, 1, 1, '0d3f59adPIETRA_GREY-F1.jpg,0d3f59adPIETRA_GREY-F2.jpg,0d3f59adPIETRA_GREY-F3.jpg,0d3f59adPIETRA_GREY-F4.jpg,0d3f59adPIETRA_GREY-F5.jpg,0d3f59adPIETRA_GREY-F6.jpg', '4d3538de5ab23fc9.jpg', 0),
(21, 'Regal Beige', 1, 1, 1, 1, 'b0550327REGAL_BEIGE_04_1120x1910_F1.jpg,b0550327REGAL_BEIGE_04_1120x1910_F2.jpg,b0550327REGAL_BEIGE_04_1120x1910_F3.jpg,b0550327REGAL_BEIGE_04_1120x1910_F4.jpg', '927ce11ec74f7262.jpg', 0),
(22, 'Statuario Bianco', 1, 1, 1, 1, 'f7437ce7STATUARIO_BIANCO_F-1.jpg,f7437ce7STATUARIO_BIANCO_F-2.jpg,f7437ce7STATUARIO_BIANCO_F-3.jpg,f7437ce7STATUARIO_BIANCO_F-4.jpg,f7437ce7STATUARIO_BIANCO_F-5.jpg,f7437ce7STATUARIO_BIANCO_F-6.jpg', 'd5208e3cdd64bd36.jpg', 0),
(23, 'Statuario Venetian', 1, 1, 1, 1, '7aa9d8d5STATUARIO_VENETIAN_1.jpg,7aa9d8d5STATUARIO_VENETIAN_2.jpg,7aa9d8d5STATUARIO_VENETIAN_3.jpg,7aa9d8d5STATUARIO_VENETIAN_4.jpg,7aa9d8d5STATUARIO_VENETIAN_5.jpg,7aa9d8d5STATUARIO_VENETIAN_6.jpg', '8b4e890e05cba7a0.jpg', 0),
(24, 'Statuario Venetian', 1, 3, 1, 1, '8c1bfd0bSTATUARIO_VENETIAN_1.jpg,8c1bfd0bSTATUARIO_VENETIAN_2.jpg,8c1bfd0bSTATUARIO_VENETIAN_3.jpg,8c1bfd0bSTATUARIO_VENETIAN_4.jpg,8c1bfd0bSTATUARIO_VENETIAN_5.jpg,8c1bfd0bSTATUARIO_VENETIAN_6.jpg', '7d4409babe60b302.jpg', 0),
(25, 'Travertine Beige', 1, 1, 1, 1, '69edd842TRAVERTINE_BEIGE_F-1.jpg,69edd842TRAVERTINE_BEIGE_F-2.jpg,69edd842TRAVERTINE_BEIGE_F-3.jpg,69edd842TRAVERTINE_BEIGE_F-4.jpg', '7fdba354951b2f36.jpg', 0),
(26, 'Travertine Beige', 1, 3, 1, 1, '92b70fb9TRAVERTINE_BEIGE_F-1.jpg,92b70fb9TRAVERTINE_BEIGE_F-2.jpg,92b70fb9TRAVERTINE_BEIGE_F-3.jpg,92b70fb9TRAVERTINE_BEIGE_F-4.jpg', 'ba895b97aeb466f6.jpg', 0),
(27, 'Calacutta Bianco Oro', 1, 1, 2, 4, 'a331efe1CALACUTTA_BINACO_ORO-F1_copy.jpg,a331efe1CALACUTTA_BINACO_ORO-F2_copy.jpg,a331efe1CALACUTTA_BINACO_ORO-F3_copy.jpg,a331efe1CALACUTTA_BINACO_ORO-F4_copy.jpg,a331efe1CALACUTTA_BINACO_ORO-F5_copy.jpg,a331efe1CALACUTTA_BINACO_ORO-F6_copy.jpg', '2380c2dc60bed07d.jpg', 0),
(28, 'Statuario Venetian', 1, 1, 2, 4, '519c5562STATUARIO_VENETIAN-F1.jpg,519c5562STATUARIO_VENETIAN-F2.jpg,519c5562STATUARIO_VENETIAN-F3.jpg,519c5562STATUARIO_VENETIAN-F4.jpg,519c5562STATUARIO_VENETIAN-F5.jpg,519c5562STATUARIO_VENETIAN-F6.jpg', '988cbc813f6ca0de.jpg', 0),
(29, 'Statuario Venetian', 1, 3, 2, 4, 'b7ddd8c2STATUARIO_VENETIAN-F1.jpg,b7ddd8c2STATUARIO_VENETIAN-F2.jpg,b7ddd8c2STATUARIO_VENETIAN-F3.jpg,b7ddd8c2STATUARIO_VENETIAN-F4.jpg,b7ddd8c2STATUARIO_VENETIAN-F5.jpg,b7ddd8c2STATUARIO_VENETIAN-F6.jpg', '0ebc966dc4505ddc.jpg', 0),
(30, 'Antique Grey', 1, 1, 2, 4, '240d5ac5ANTIQUE_GREY_F1.jpg,240d5ac5ANTIQUE_GREY_F2.jpg,240d5ac5ANTIQUE_GREY_F3.jpg,240d5ac5ANTIQUE_GREY_F4.jpg,240d5ac5ANTIQUE_GREY_F5.jpg', '59ef331018c39595.jpg', 0),
(31, 'Armani Silver', 1, 1, 2, 4, '9974dcd4ARMANI_SILVER-1.jpg,9974dcd4ARMANI_SILVER-2.jpg,9974dcd4ARMANI_SILVER-3.jpg,9974dcd4ARMANI_SILVER-4.jpg,9974dcd4ARMANI_SILVER-5.jpg,9974dcd4ARMANI_SILVER-6.jpg', '506a5c3a4845d2a4.jpg', 0),
(32, 'Statuario', 1, 1, 2, 4, 'b40bbca7SATUARIO_F1_copy.jpg,b40bbca7SATUARIO_F2_copy.jpg,b40bbca7SATUARIO_F3_copy.jpg,b40bbca7SATUARIO_F4_copy.jpg,b40bbca7SATUARIO_F5_copy.jpg,b40bbca7SATUARIO_F6_copy.jpg', '92e45163696ce2ef.jpg', 0),
(33, 'Statuario', 1, 3, 2, 4, 'b22e1493SATUARIO_F1_copy.jpg,b22e1493SATUARIO_F2_copy.jpg,b22e1493SATUARIO_F3_copy.jpg,b22e1493SATUARIO_F4_copy.jpg,b22e1493SATUARIO_F5_copy.jpg,b22e1493SATUARIO_F6_copy.jpg', '2370c52d16bee710.jpg', 0),
(34, 'Celio', 1, 1, 2, 4, 'c99e2289CELIO_p1_copy.jpg,c99e2289CELIO_p2_copy.jpg,c99e2289CELIO_p3_copy.jpg,c99e2289CELIO_p4_copy.jpg,c99e2289CELIO_p5_copy.jpg,c99e2289CELIO_p6_copy.jpg', '81621d7068266405.jpg', 0),
(35, 'Burberry Beige', 1, 1, 2, 4, '935ff683BURBERRY_BEIGE-F1_copy.jpg,935ff683BURBERRY_BEIGE-F2_copy.jpg,935ff683BURBERRY_BEIGE-F3_copy.jpg,935ff683BURBERRY_BEIGE-F4_copy.jpg', '228ad4a4940d2ef1.jpg', 0),
(36, 'Beton Flakes', 4, 3, 2, 4, '483afd07BETON_FLAKE_BROWN_F1.jpg,483afd07BETON_FLAKE_BROWN_F2.jpg,483afd07BETON_FLAKE_BROWN_F3.jpg,483afd07BETON_FLAKE_BROWN_F4.jpg', '6711215c1aeb0013.jpg', 0),
(37, 'Cemento Anracite', 6, 3, 2, 4, '2334f2f2CEMENTO_ANTRACITE-F1.jpg,2334f2f2CEMENTO_ANTRACITE-F2.jpg,2334f2f2CEMENTO_ANTRACITE-F3.jpg,2334f2f2CEMENTO_ANTRACITE-F4.jpg', '0fda42aff8357b1c.jpg', 0),
(38, 'Cemento Beige', 6, 3, 2, 4, '7bf6a3cbCEMENTO_BEIGE-F1.jpg,7bf6a3cbCEMENTO_BEIGE-F2.jpg,7bf6a3cbCEMENTO_BEIGE-F3.jpg,7bf6a3cbCEMENTO_BEIGE-F4.jpg', '14e2d904185b4968.jpg', 0),
(39, 'Cemento Bianco', 6, 3, 2, 4, '47cd5443CEMENTO_BIANCO-F1.jpg,47cd5443CEMENTO_BIANCO-F2.jpg,47cd5443CEMENTO_BIANCO-F3.jpg,47cd5443CEMENTO_BIANCO-F4.jpg', 'f8e6f76f3826fefd.jpg', 0),
(40, 'Cemento Tortora', 6, 3, 2, 4, '0a37fa7cCEMENTO_TORTORA_F1.jpg,0a37fa7cCEMENTO_TORTORA_F2.jpg,0a37fa7cCEMENTO_TORTORA_F3.jpg,0a37fa7cCEMENTO_TORTORA_F4.jpg', '9e284fb3d8538c86.jpg', 0),
(41, 'Exposed Cemento Fabrico Latte', 6, 3, 2, 4, 'db0aa356EXPOSED_CEMENTO_FABRICO_LATTE-F1.jpg,db0aa356EXPOSED_CEMENTO_FABRICO_LATTE-F2.jpg,db0aa356EXPOSED_CEMENTO_FABRICO_LATTE-F3.jpg,db0aa356EXPOSED_CEMENTO_FABRICO_LATTE-F4.jpg', 'bb3e1ddc24f28acf.jpg', 0),
(42, 'Exposed Cemento Fabrico Antracite', 6, 3, 2, 4, '5109467fEXPOSED_CEMENTO_FABRICO_ANTRACITE_ORG-F1.jpg,5109467fEXPOSED_CEMENTO_FABRICO_ANTRACITE_ORG-F2.jpg,5109467fEXPOSED_CEMENTO_FABRICO_ANTRACITE_ORG-F3.jpg,5109467fEXPOSED_CEMENTO_FABRICO_ANTRACITE_ORG-F4.jpg', '50551d3e7d800d30.jpg', 0),
(43, 'Exposed Cemento Fabrico Beige', 6, 3, 2, 4, '7b9cc692EXPOSED_CEMENTO_FABRICO_BEIGE-F1.jpg,7b9cc692EXPOSED_CEMENTO_FABRICO_BEIGE-F2.jpg,7b9cc692EXPOSED_CEMENTO_FABRICO_BEIGE-F3.jpg,7b9cc692EXPOSED_CEMENTO_FABRICO_BEIGE-F4.jpg', '38cba52fba61869e.jpg', 0),
(44, 'Exposed Cemento Fabrico Bianco', 6, 3, 2, 4, 'aeb1317dEXPOSED_CEMENTO_FABRICO_BIANCO-F1.jpg,aeb1317dEXPOSED_CEMENTO_FABRICO_BIANCO-F2.jpg,aeb1317dEXPOSED_CEMENTO_FABRICO_BIANCO-F3.jpg,aeb1317dEXPOSED_CEMENTO_FABRICO_BIANCO-F4.jpg', 'eb87ebbaa2dc93d3.jpg', 0),
(45, 'Exposed Cemento Fabrico Coin', 6, 3, 2, 4, '2fbf4676EXPOSED_CEMENTO_FABRICO_COIN-F1.jpg,2fbf4676EXPOSED_CEMENTO_FABRICO_COIN-F2.jpg,2fbf4676EXPOSED_CEMENTO_FABRICO_COIN-F3.jpg,2fbf4676EXPOSED_CEMENTO_FABRICO_COIN-F4.jpg', '930050941b7502bd.jpg', 0),
(46, 'Afyon White', 1, 1, 1, 3, '92a7b2eeAFYON_WHITE_F1.jpg,92a7b2eeAFYON_WHITE_F2.jpg,92a7b2eeAFYON_WHITE_F3.jpg', '0dba0ea7f2def0b8.jpg', 0),
(47, 'Antique Grey', 1, 1, 1, 3, 'ebd15287ANTIQUE_GREY_A.jpg,ebd15287ANTIQUE_GREY_B.jpg,ebd15287ANTIQUE_GREY_C.jpg,ebd15287ANTIQUE_GREY_copy.jpg', '0fde42ef56758d7d.jpg', 0),
(48, 'Apuane Statuario', 1, 1, 1, 3, 'b27f97b1Apune_5faces_f1.jpg,b27f97b1Apune_5faces_f2.jpg,b27f97b1Apune_5faces_f3.jpg,b27f97b1Apune_5faces_f4.jpg,b27f97b1Apune_5faces_f5.jpg', '4f25daf391961075.jpg', 0),
(49, 'Arabescato Statuario', 1, 1, 1, 3, 'db72fdc8ARABESCATO_SATUARIO-1.jpg,db72fdc8ARABESCATO_SATUARIO-2.jpg,db72fdc8ARABESCATO_SATUARIO-3.jpg', '5b9f9da6656ee623.jpg', 0),
(50, 'Ardesia Grigio', 5, 5, 1, 3, 'df46f36dARDESIA_GRIGIO-F1.jpg,df46f36dARDESIA_GRIGIO-F2.jpg,df46f36dARDESIA_GRIGIO-F3.jpg,df46f36dARDESIA_GRIGIO-F4.jpg', '8fb0ea2b1ef6ad4b.jpg', 0),
(51, 'Ardesia Silver', 5, 5, 1, 3, '0f8db42dARDESIA_SILVER-F1.jpg,0f8db42dARDESIA_SILVER-F2.jpg,0f8db42dARDESIA_SILVER-F3.jpg,0f8db42dARDESIA_SILVER-F4.jpg', '27a5d0f82f9fe775.jpg', 0),
(52, 'Arenisca Crema', 5, 3, 1, 3, 'd08da795Arenisca_crema_1.jpg,d08da795Arenisca_crema_2.jpg,d08da795Arenisca_crema_3.jpg', 'b62a99a85acc8d27.jpg', 0),
(53, 'Arenisca Night', 5, 3, 1, 3, '7a8f555fArenisca_night_F1.jpg,7a8f555fArenisca_night_F2.jpg,7a8f555fArenisca_night_F3.jpg', '3e1d1525ace41772.jpg', 0),
(54, 'Armani Brown', 1, 1, 1, 3, 'f417a1f8ARMANI_BROWN_copy.jpg,f417a1f8ARMANI_BROWN_F1.jpg,f417a1f8ARMANI_BROWN_F2.jpg,f417a1f8ARMANI_BROWN_F3.jpg', 'f481de122322157d.jpg', 0),
(55, 'Armani Gold', 1, 1, 1, 3, 'ee6b6418ARMANI_GOLD_05_1050x1780_002-F-1.jpg,ee6b6418ARMANI_GOLD_05_1050x1780_002-F-2.jpg,ee6b6418ARMANI_GOLD_05_1050x1780_002-F-3.jpg', '7bda13ace05075a5.jpg', 0),
(56, 'Armani Grey', 1, 1, 1, 3, '56fc4debARMANI_GREY_F1.jpg,56fc4debARMANI_GREY_F2.jpg,56fc4debARMANI_GREY_F3.jpg', 'ee1c8ef1ecf11ef6.jpg', 0),
(57, 'Armani Grey', 1, 3, 1, 3, '224ec090ARMANI_GREY_F3.jpg,224ec090ARMANI_GREY_F2.jpg,224ec090ARMANI_GREY_F1.jpg', '06290588db95e847.jpg', 0),
(58, 'Armani Silver', 1, 1, 1, 3, '3452da0cSILVER_ARMANI-F3.jpg,3452da0cSILVER_ARMANI-F2.jpg,3452da0cSILVER_ARMANI-F1.jpg', 'c54625af4cd23a85.jpg', 0),
(59, 'Ashford Black', 1, 1, 1, 3, '71d1c4c3ASHFORD_BLACK_F1.jpg,71d1c4c3ASHFORD_BLACK_F2.jpg,71d1c4c3ASHFORD_BLACK_F3.jpg', 'ad841ee734872901.jpg', 0),
(60, 'Astonia Grey', 1, 1, 1, 3, 'b73cafd5ASTONIA_GREY_FST183A13_1_160x320_A2-P1.jpg,b73cafd5ASTONIA_GREY_FST183A13_1_160x320_A2-P2.jpg,b73cafd5ASTONIA_GREY_FST183A13_1_160x320_A2-P3.jpg', 'f3c64d3ce5614ec0.jpg', 0),
(61, 'Astonia Grey', 1, 3, 1, 3, '3e7926a3ASTONIA_GREY_FST183A13_1_160x320_A2-P1.jpg,3e7926a3ASTONIA_GREY_FST183A13_1_160x320_A2-P2.jpg,3e7926a3ASTONIA_GREY_FST183A13_1_160x320_A2-P3.jpg', 'be0bbaae5f47be40.jpg', 0),
(62, 'Beton Flakes Grey', 4, 3, 1, 3, '4c2eac2bBETON_FLAKE_GREY-F1.jpg,4c2eac2bBETON_FLAKE_GREY-F2.jpg', 'ae622d9e2923d73d.jpg', 0),
(63, 'Bianco Lasa', 1, 1, 1, 3, '9cbdd6b7BIANCO_LASA-F1.jpg,9cbdd6b7BIANCO_LASA-F2.jpg,9cbdd6b7BIANCO_LASA-F3.jpg', '103c0ca347b9de90.jpg', 0),
(64, 'Botticino Fiorito', 1, 1, 1, 3, '68ad99a9BOTTICINO_FIORITO_A.jpg,68ad99a9BOTTICINO_FIORITO_B.jpg', '238e6aeccb3aabaa.jpg', 0),
(65, 'Breccia Blue', 1, 1, 1, 3, '9745238dBRECCIA_BLUE-F1.jpg,9745238dBRECCIA_BLUE-F2.jpg', '92a7e0d5b6012955.jpg', 0),
(66, 'Bruno Flakes ', 4, 3, 1, 3, '3d60753cBRUNO_FLAKES-F1.jpg,3d60753cBRUNO_FLAKES-F2.jpg', 'e9505e3c98d4c775.jpg', 0),
(67, 'Calacatta Macchia Vecchia', 1, 1, 1, 3, '005046aeCalacatta_Macchia_Vecchia_F1.jpg,005046aeCalacatta_Macchia_Vecchia_F2.jpg,005046aeCalacatta_Macchia_Vecchia_F3.jpg', 'b89ab59aa48998c8.jpg', 0),
(68, 'Calacutta Bianco Oro', 1, 1, 1, 3, '550da37aCALACUTTA_BINACO_ORO-F1.jpg,550da37aCALACUTTA_BINACO_ORO-F2.jpg,550da37aCALACUTTA_BINACO_ORO-F3.jpg', '38a191fa070024f2.jpg', 0),
(69, 'Calacutta Borghini', 1, 1, 1, 3, 'e0d2b7caCALACUTTA_BORGHINI-F1.jpg,e0d2b7caCALACUTTA_BORGHINI-F2.jpg,e0d2b7caCALACUTTA_BORGHINI-F3.jpg', '4ab6f47907df2df5.jpg', 0),
(70, 'Calacutta Borghini', 1, 3, 1, 3, 'bee69bb7CALACUTTA_BORGHINI-F1.jpg,bee69bb7CALACUTTA_BORGHINI-F2.jpg,bee69bb7CALACUTTA_BORGHINI-F3.jpg', 'b9e82cc3aad34b33.jpg', 0),
(71, 'Calacatta Luxe', 1, 1, 1, 3, '38deedb6CALACATTA_LUXE_F1.jpg,38deedb6CALACATTA_LUXE_F2.jpg,38deedb6CALACATTA_LUXE_F3.jpg', 'afe8059c4930a46d.jpg', 0),
(72, 'Celio', 1, 1, 1, 3, 'b3faf4e2CELIO-F1.jpg,b3faf4e2CELIO-F2.jpg,b3faf4e2CELIO-F3.jpg', '7929b1ef92fb94f5.jpg', 0),
(73, 'Cemento Flakes', 4, 3, 1, 3, 'a8081c2cCEMENTO_FLAKES-F1.jpg,a8081c2cCEMENTO_FLAKES-F2.jpg', '217a2298d2478b64.jpg', 0),
(74, 'Cordoso Grey ', 5, 5, 1, 3, '4b5dc53fCORDOSO_GREY_F1.jpg,4b5dc53fCORDOSO_GREY_F2.jpg,4b5dc53fCORDOSO_GREY_F3.jpg', '66cafb6a60080198.jpg', 0),
(75, 'Cordoso Silver', 5, 5, 1, 3, '5b6c5edbCORDOSO_SILVER_F1.jpg,5b6c5edbCORDOSO_SILVER_F2.jpg,5b6c5edbCORDOSO_SILVER_F3.jpg', 'a14409fa3dbad40c.jpg', 0),
(76, 'Damasta Grey', 1, 1, 1, 3, 'ab7b95d31_F1.jpg,ab7b95d31_F2.jpg,ab7b95d31_F3.jpg', '6d1a79343c2175a7.jpg', 0),
(77, 'Dior Gold', 1, 1, 1, 3, 'b57b09ecDIOR_GOLD_F1.jpg,b57b09ecDIOR_GOLD_F2.jpg,b57b09ecDIOR_GOLD_F3.jpg,c4687f73b57b09ecDIOR_GOLD_F2.jpg', '80d65b620a3aef32.jpg', 0),
(78, 'Dolce Grey', 11, 1, 1, 3, '8e065321DOLCE_GREY_F1.jpg,8e065321DOLCE_GREY_F2.jpg', 'cbdbbfe3637aea69.jpg', 0),
(79, 'Emperador Light', 1, 1, 1, 3, '715e5225EMPERADOR_LIGHT_1.jpg,715e5225EMPERADOR_LIGHT_2.jpg,715e5225EMPERADOR_LIGHT_3.jpg,715e5225EMPERADOR_LIGHT_4.jpg', 'ff3119349bac430e.jpg', 0),
(80, 'Everest White', 1, 1, 1, 3, '53fd35d4everest_white.jpg', '80ce12a73a1a7e1c.jpg', 0),
(81, 'Everest White', 1, 3, 1, 3, '2cab01e4everest_white.jpg', '7543144dbbe5d702.jpg', 0),
(82, 'Fantasy Onyx', 7, 1, 1, 3, '3c2c55c7FANTASY_ONYX-F1.jpg,3c2c55c7FANTASY_ONYX-F2.jpg,3c2c55c7FANTASY_ONYX-F3.jpg', '428864c6e1a23a8c.jpg', 0),
(83, 'Flora Mosaic', 10, 1, 1, 3, '41d1cfecFLORA_MOSAIC-BM-B.jpg,41d1cfecFLORA_MOSAIC-BM-A.jpg', '3b777e75a3a0ec76.jpg', 0),
(84, 'Flora Mosaic', 11, 1, 1, 3, '69890058FLORA_MOSAIC-BM-A.jpg,69890058FLORA_MOSAIC-BM-B.jpg', '586fcab561f3dce7.jpg', 0),
(85, 'Graphite Onyx', 7, 1, 1, 3, 'dc796f01GRAPHITE_ONYX_F1.jpg,dc796f01GRAPHITE_ONYX_F2.jpg,dc796f01GRAPHITE_ONYX_F3.jpg', '56c38c4ad0128371.jpg', 0),
(86, 'Graphite Onyx', 11, 1, 1, 3, 'd3f2d506GRAPHITE_ONYX_F3.jpg,d3f2d506GRAPHITE_ONYX_F2.jpg,d3f2d506GRAPHITE_ONYX_F1.jpg', 'c197558400763ea6.jpg', 0),
(87, 'Grigio Nuvolato', 1, 1, 1, 3, '492efe19Grigio_nuovolato-P2.jpg,492efe19Grigio_nuovolato-P1.jpg', '1d8395e32293cb72.jpg', 0),
(88, 'Grunge Copper', 8, 4, 1, 3, '6cb81704GRUNGE_COPPER_F1.jpg,6cb81704GRUNGE_COPPER_F2.jpg', '82e95047d418a748.jpg', 0),
(89, 'Irish Brown', 1, 1, 1, 3, '9a621374IRISH_BROWN-F1.jpg,9a621374IRISH_BROWN-F2.jpg', '6d6b1d4562802f65.jpg', 0),
(90, 'Iron Grey', 8, 4, 1, 3, '15d4fe52IRON_GREY-F1.jpg,15d4fe52IRON_GREY-F2.jpg', '3dbd6125b1e62155.jpg', 0),
(91, 'Lithic Latte', 6, 3, 1, 3, 'c1cba8a1LITHIC_LATTE-F1.jpg,c1cba8a1LITHIC_LATTE-F2.jpg,c1cba8a1LITHIC_LATTE-F3.jpg,44fa739fc1cba8a1LITHIC_LATTE-F2.jpg', '50caba7e8e3eb9b7.jpg', 0),
(92, 'Mont Blanc Crystal', 1, 1, 1, 3, '29598f46MONT_BLANC_CRYSTAL_F1.jpg,29598f46MONT_BLANC_CRYSTAL_F2.jpg,29598f46MONT_BLANC_CRYSTAL_F3.jpg', '3b4f61bfa7af170c.jpg', 0),
(93, 'Mountain Coin', 5, 3, 1, 3, '3cab6160MOUNTAIN_COIN_F1.jpg,3cab6160MOUNTAIN_COIN_F2.jpg,3cab6160MOUNTAIN_COIN_F3.jpg', 'bbb3f10edf8df411.jpg', 0),
(94, 'Mountain Tortora', 5, 3, 1, 3, '4b9c7926MOUNTAIN_TORTORA_F1.jpg,4b9c7926MOUNTAIN_TORTORA_F2.jpg,4b9c7926MOUNTAIN_TORTORA_F3.jpg', 'd87488f8bffd80d7.jpg', 0),
(95, 'Negresco Grigio', 5, 3, 1, 3, 'c3b667fcNEGRESCO_GRIGIO_F1.jpg,c3b667fcNEGRESCO_GRIGIO_F2.jpg', '7318876a74351cec.jpg', 0),
(96, 'Negresco Latte', 5, 3, 1, 3, '7760dbfeNEGRESCO_LATTE_F1.jpg,7760dbfeNEGRESCO_LATTE_F2.jpg', 'dec532911a289445.jpg', 0),
(97, 'Nero Marquina', 1, 1, 1, 3, 'f12a1e94NERO_MARQUINA_F1.jpg,f12a1e94NERO_MARQUINA_F2.jpg,f12a1e94NERO_MARQUINA_F3.jpg', 'fad4d7aec9bdfc8e.jpg', 0),
(98, 'Nero Marquina', 1, 3, 1, 3, 'e9e2e4a1NERO_MARQUINA_F1.jpg,e9e2e4a1NERO_MARQUINA_F2.jpg,e9e2e4a1NERO_MARQUINA_F3.jpg', '211f6fc8065baf7f.jpg', 0),
(99, 'Apuane Statuario', 1, 6, 2, 6, 'd83e5d42APUANE_SATUARIO_F1.jpg,d83e5d42APUANE_SATUARIO_F2.jpg', '33293a121e84056c.jpg', 0),
(100, 'Apuane Statuario', 11, 3, 2, 6, 'a59dc5a6APUANE_SATUARIO_F1.jpg,a59dc5a6APUANE_SATUARIO_F2.jpg', '18c813d66d48173d.jpg', 0),
(101, 'Armani Silver', 1, 6, 2, 6, 'cd57bda7ARMANI_SILVER-F1.jpg,cd57bda7ARMANI_SILVER-F2.jpg,cd57bda7ARMANI_SILVER-F3.jpg', '1261c637c0b3ae54.jpg', 0),
(102, 'Astonia Grey', 1, 6, 2, 6, '9eee610bASTONIA_GREY_FST183A13_F1.jpg,9eee610bASTONIA_GREY_FST183A13_F2.jpg,9eee610bASTONIA_GREY_FST183A13_F3.jpg', '2f914390c9e7e284.jpg', 0),
(103, 'Astonia Grey', 1, 3, 2, 6, '5c80c64eASTONIA_GREY_FST183A13_F1.jpg,5c80c64eASTONIA_GREY_FST183A13_F2.jpg,5c80c64eASTONIA_GREY_FST183A13_F3.jpg', '43fa8bcde176ec49.jpg', 0),
(104, 'Belgium Stone', 8, 5, 2, 6, 'b8748ca0BELGIUM_STONE-F1.jpg,b8748ca0BELGIUM_STONE-F2.jpg', '2ecac73239fc9e87.jpg', 0),
(105, 'Bianco Lasa', 1, 6, 2, 6, '63a9ceedBIANCO_LASA-F1.jpg,63a9ceedBIANCO_LASA-F2.jpg,63a9ceedBIANCO_LASA-F3.jpg', '8ea885fc1fbfa0b9.jpg', 0),
(106, 'Bianco Lasa', 11, 6, 2, 6, 'aa310a2aBIANCO_LASA-F1.jpg,aa310a2aBIANCO_LASA-F2.jpg,aa310a2aBIANCO_LASA-F3.jpg', '7bb32e799c0a9812.jpg', 0),
(107, 'Bianco Lasa', 1, 3, 1, 6, '5c0a0556BIANCO_LASA-F1.jpg,5c0a0556BIANCO_LASA-F2.jpg,5c0a0556BIANCO_LASA-F3.jpg', 'dd68e94f81583ca0.jpg', 0),
(108, 'Bronze Armani', 1, 6, 2, 6, 'c05af86bBRONZE_ARMANI-F1.jpg,c05af86bBRONZE_ARMANI-F2.jpg,c05af86bBRONZE_ARMANI-F3.jpg', '991283bec0971fb1.jpg', 0),
(109, 'Bronze Armani', 1, 3, 2, 6, 'be127a5cBRONZE_ARMANI-F1.jpg,be127a5cBRONZE_ARMANI-F2.jpg,be127a5cBRONZE_ARMANI-F3.jpg', 'd78117c3b39c58f9.jpg', 0),
(110, 'Calacutta Bianco Oro', 1, 6, 2, 6, 'b70deb61CALACUTTA_BINACO_ORO-F1.jpg,b70deb61CALACUTTA_BINACO_ORO-F2.jpg,b70deb61CALACUTTA_BINACO_ORO-F3.jpg', '22f8a5d411813a7c.jpg', 0),
(111, 'Calacutta Bianco Oro', 1, 3, 2, 6, 'c822ea0eCALACUTTA_BINACO_ORO-F1.jpg,c822ea0eCALACUTTA_BINACO_ORO-F2.jpg,c822ea0eCALACUTTA_BINACO_ORO-F3.jpg', '985a46ad1f0b1c35.jpg', 0),
(112, 'Calacutta Borghini', 1, 6, 2, 6, '5537e54dCALACUTTA_BORGHINI-F1.jpg,5537e54dCALACUTTA_BORGHINI-F2.jpg,5537e54dCALACUTTA_BORGHINI-F3.jpg', 'fe3841d1dd0ef1b6.jpg', 0),
(113, 'Calacutta Borghini', 1, 3, 2, 6, '45d4c8d5CALACUTTA_BORGHINI-F1.jpg,45d4c8d5CALACUTTA_BORGHINI-F2.jpg,45d4c8d5CALACUTTA_BORGHINI-F3.jpg', '900d75d94fa2461b.jpg', 0),
(114, 'Calacutta Borghini', 11, 6, 2, 6, '8c244b09CALACUTTA_BORGHINI_BM.png,8c244b09CALACUTTA_BORGHINI_BM-P-A.jpg,8c244b09CALACUTTA_BORGHINI_BM-P-B.jpg', '3e447d663f6432a4.png', 0),
(115, 'Calacutta Borghini', 11, 3, 2, 6, 'c480b02bCALACUTTA_BORGHINI_BM.png,c480b02bCALACUTTA_BORGHINI_BM-P-A.jpg,c480b02bCALACUTTA_BORGHINI_BM-P-B.jpg', '2aa35a83294fac18.png', 0),
(116, 'Carrara', 1, 6, 2, 6, '4589ac18CARRARA-NEW-F1.jpg,4589ac18CARRARA-NEW-F2.jpg', 'ad4cdf1f35abaae6.jpg', 0),
(117, 'Carrara', 1, 3, 2, 6, '53653f6fCARRARA-NEW-F1.jpg,53653f6fCARRARA-NEW-F2.jpg', '8cc217b890f61240.jpg', 0),
(118, 'Carrara', 11, 6, 2, 6, '30fb1809CARRARA_BOOK_MATCH.png,30fb1809CARRARA_BOOK_MATCH-P-A.jpg,30fb1809CARRARA_BOOK_MATCH-P-B.jpg', 'a21b3ee63a4d3f41.jpg', 0),
(119, 'Carrara', 11, 3, 2, 6, '90fe0254CARRARA_BOOK_MATCH.png,90fe0254CARRARA_BOOK_MATCH-P-A.jpg,90fe0254CARRARA_BOOK_MATCH-P-B.jpg', '90ce94ff24cc3cd8.jpg', 0),
(120, 'Carrara Ultimo', 1, 6, 2, 6, '2d9fd7c8CARRARA_ULTIMO-F1.jpg,2d9fd7c8CARRARA_ULTIMO-F2.jpg,2d9fd7c8CARRARA_ULTIMO-F3.jpg', '815429190e213307.jpg', 0),
(121, 'Carrara Ultimo', 1, 3, 2, 6, '5fefb9b1CARRARA_ULTIMO-F1.jpg,5fefb9b1CARRARA_ULTIMO-F2.jpg,5fefb9b1CARRARA_ULTIMO-F3.jpg', 'f5a8585e24c03f47.jpg', 0),
(122, 'Cava Antracite', 8, 4, 2, 6, '0981c37fCAVA_ANTRACITE-F1.jpg,0981c37fCAVA_ANTRACITE-F2.jpg', '80bd7e6abd0aeda5.jpg', 0),
(123, 'Celio', 1, 6, 2, 6, '1194540dCELIO_F1.jpg,1194540dCELIO_F2.jpg,1194540dCELIO_F3.jpg', '9b43362b63e03ffa.jpg', 0),
(124, 'Honey Onyx', 7, 6, 2, 6, '1d416b71Honey_Onyx_F1.jpg,1d416b71Honey_Onyx_F2.jpg', '315021ad0d09ba78.jpg', 0),
(125, 'Iron Corten', 8, 4, 2, 6, '603c82feIRON_CORTEN-F1.jpg,603c82feIRON_CORTEN-F2.jpg', 'f8821b8b97bc957e.jpg', 0),
(126, 'Iron Copper', 8, 4, 2, 6, '7b65c3e4IRON_COPPER-F1.jpg,7b65c3e4IRON_COPPER-F2.jpg', '7d805adf2c056118.jpg', 0),
(127, 'Lithic Antracite', 6, 5, 2, 6, 'ddcc7f51LITHIC_ANTRACITE-F1.jpg,ddcc7f51LITHIC_ANTRACITE-F3.jpg,ddcc7f51LITHIC_ANTRACITE-F2.jpg', '48daf2f3d36d9a5b.jpg', 0),
(128, 'Lithic Coin', 6, 5, 2, 6, 'aa15ddd0LITHIC_COIN-F1.jpg,aa15ddd0LITHIC_COIN-F2.jpg,aa15ddd0LITHIC_COIN-F3.jpg', '5e3522f58ce0a945.jpg', 0),
(129, 'Lithic Nero', 6, 5, 2, 6, 'aee37b27LITHIC_NERO_F1.jpg,aee37b27LITHIC_NERO_F2.jpg,aee37b27LITHIC_NERO_F3.jpg', '7d5bce82f639e5a1.jpg', 0),
(130, 'Meek Artic', 12, 3, 2, 6, '2e56dc4eMEEK_ARTIC.jpg', 'af4333298b86659f.jpg', 0),
(131, 'Meek Ash ', 12, 3, 2, 6, 'a33014d6MEEK_ASH.jpg', 'c8e19223636871eb.jpg', 0),
(132, 'Meek Coal ', 12, 3, 2, 6, 'a66dbb48MEEK_COAL.jpg', '868e50c128102f65.jpg', 0),
(133, 'Meek Oyster', 12, 3, 2, 6, 'ce0f397fMEEK_OYSTER.jpg', '2eb15aeeb08d9750.jpg', 0),
(134, 'Meek Smoke', 12, 3, 2, 6, '489d154cMEEK_SMOKE.jpg', '38c0cc9e73ebf40a.jpg', 0),
(135, 'Meek Walnut ', 12, 3, 2, 6, '28b683ecMEEK_WALNUT.jpg', '0e50f06071a5a23a.jpg', 0),
(136, 'Meek', 12, 3, 2, 6, 'b36900b7MEEK_ARTIC.jpg,b36900b7MEEK_ASH.jpg,b36900b7MEEK_BARISTA.jpg,b36900b7MEEK_COAL.jpg,b36900b7MEEK_CORN.jpg,b36900b7MEEK_MOCHA.jpg,b36900b7MEEK_OYSTER.jpg,b36900b7MEEK_SMOKE.jpg,b36900b7MEEK_UMBER.jpg,b36900b7MEEK_WALNUT.jpg', '4d0b90da7727bce0.jpg', 0),
(137, 'Iron Grey', 8, 4, 2, 6, '011146baIRON_GREY-F1.jpg,011146baIRON_GREY-F2.jpg', '41e32ce60742079d.jpg', 0),
(138, 'Nero Marquina', 1, 6, 2, 6, 'c9386a2cNERO_MARQUINA_F1_copy.JPG,c9386a2cNERO_MARQUINA_F2_copy.jpg,c9386a2cNERO_MARQUINA_F3.jpg', '997c8d3e7d89dbcd.jpg', 0),
(139, 'Nero Marquina', 8, 4, 2, 6, '690510ccNERO_MARQUINA_F1_copy.JPG,690510ccNERO_MARQUINA_F2_copy.jpg,690510ccNERO_MARQUINA_F3.jpg', 'bba110858903788a.jpg', 0),
(140, 'Pietra Grey', 1, 6, 2, 6, '6913483ePIETRA_GREY_F1.jpg,6913483ePIETRA_GREY_F2.jpg,6913483ePIETRA_GREY_F3.jpg', 'c72865720c80438f.jpg', 0),
(141, 'Pietra Grey', 1, 3, 2, 6, '62bf0e1aPIETRA_GREY_F1.jpg,62bf0e1aPIETRA_GREY_F2.jpg,62bf0e1aPIETRA_GREY_F3.jpg', '17a63dbd495e757e.jpg', 0),
(142, 'Statuario', 11, 6, 2, 6, '27e0c7b2SATUARIO_BOOKMATCH.png,27e0c7b2SATUARIO_BOOKMATCH-P-A.jpg,27e0c7b2SATUARIO_BOOKMATCH-P-B.jpg', '06d2291bad5de534.png', 0),
(143, 'Statuario Nuvo', 1, 6, 2, 6, '93a4c921STATUARIO_NUVO-BOOK_MATCH.png,93a4c921STATUARIO_NUVO-BOOK_MATCH-P-A.jpg,93a4c921STATUARIO_NUVO-BOOK_MATCH-P-B.jpg', '214fc90445924bda.png', 0),
(144, 'Statuario Nuvo', 11, 3, 2, 6, '962c287cSTATUARIO_NUVO-BOOK_MATCH-P-A.jpg,962c287cSTATUARIO_NUVO-BOOK_MATCH-P-B.jpg', 'd6d0659015a65ece.png', 0),
(145, 'Statuario Platina', 11, 6, 2, 6, 'ecde94d5STATUARIO_PLATINA_F1.jpg,ecde94d5STATUARIO_PLATINA_F2.jpg,ecde94d5STATUARIO_PLATINA_F3.jpg', '656ccff20077d1ba.jpg', 0),
(146, 'Statuario Platina', 11, 3, 2, 6, 'a0be3c47STATUARIO_PLATINA_F1.jpg,a0be3c47STATUARIO_PLATINA_F2.jpg,a0be3c47STATUARIO_PLATINA_F3.jpg', 'd9bc33b8e97097f7.jpg', 0),
(147, 'Statuario Venetian', 1, 6, 2, 6, 'a59665caSTATUARIO_VENETIAN-F1.jpg,a59665caSTATUARIO_VENETIAN-F2.jpg,a59665caSTATUARIO_VENETIAN-F3.jpg', '852bad1f110bb352.jpg', 0),
(148, 'Statuario Venetian', 11, 6, 2, 6, '90de54beSTATUARIO_VENETIAN-F1.jpg,90de54beSTATUARIO_VENETIAN-F2.jpg,90de54beSTATUARIO_VENETIAN-F3.jpg', '7e265ce0a1c2321a.jpg', 0),
(149, 'Statuario Venetian', 11, 3, 2, 6, 'a2aa7ab7STATUARIO_VENETIAN-F1.jpg,a2aa7ab7STATUARIO_VENETIAN-F2.jpg,a2aa7ab7STATUARIO_VENETIAN-F3.jpg', '6256db9f1ee17f23.jpg', 0),
(150, 'Statuario Venato', 11, 6, 2, 6, '51756b67STATUARIO_VENATO_BOOKMATCH-P-A.jpg,51756b67STATUARIO_VENATO_BOOKMATCH-P-B.jpg', '5ea1c0458caad20d.png', 0),
(151, 'Statuario Venato', 11, 3, 2, 6, 'c17c1a7cSTATUARIO_VENATO_BOOKMATCH-P-A.jpg,c17c1a7cSTATUARIO_VENATO_BOOKMATCH-P-B.jpg', '02538360627dc13d.png', 0),
(152, 'Omani', 1, 1, 1, 3, '5122fd8bOMANI_1.jpg,5122fd8bOMANI_2.jpg,5122fd8bOMANI_3.jpg,5122fd8bOMANI_4.jpg', 'b4d2f95f339808db.jpg', 0),
(153, 'Onice Bianco', 7, 1, 1, 3, '2261738eONICE_BIANCO-F1.jpg,2261738eONICE_BIANCO-F2.jpg,2261738eONICE_BIANCO-F3.jpg', '0051d10235da8c1c.jpg', 0),
(154, 'Pietra Grey', 1, 1, 1, 3, 'f062312fPIETRA_GREY-F1.jpg,f062312fPIETRA_GREY-F2.jpg,f062312fPIETRA_GREY-F3.jpg,f062312fPIETRA_GREY-F4.jpg', '7768d39ba30b9985.jpg', 0),
(155, 'Pietra Grey', 1, 3, 1, 3, '989b8160PIETRA_GREY-F1.jpg,989b8160PIETRA_GREY-F2.jpg,989b8160PIETRA_GREY-F3.jpg,989b8160PIETRA_GREY-F4.jpg', 'd4191d0f7581f94e.jpg', 0),
(156, 'Silver River', 1, 1, 1, 3, '01dd5a75SILVER_RIVER_F1.jpg,01dd5a75SILVER_RIVER_F2.jpg,01dd5a75SILVER_RIVER_F3.jpg', '26dca263ecdc67b6.jpg', 0),
(157, 'Statuario', 1, 1, 1, 3, '88fa942eSATUARIO-F1.jpg,88fa942eSATUARIO-F2.jpg,88fa942eSATUARIO-F3.jpg,88fa942eSATUARIO-LINE_CONTINUE-3_FACE.jpg,88fa942eSATUARIO_RENDOM.jpg', '0258f0756951c5b8.jpg', 0),
(158, 'Statuario Norwell', 1, 1, 1, 3, '0f448ee1STATUARIO_NORWELL_F1.jpg,0f448ee1STATUARIO_NORWELL_F2.jpg,0f448ee1STATUARIO_NORWELL_F3.jpg', '507954a056ccd48b.jpg', 0),
(159, 'Statuario Norwell', 1, 3, 1, 3, '596e6e2bSTATUARIO_NORWELL_F1.jpg,596e6e2bSTATUARIO_NORWELL_F2.jpg,596e6e2bSTATUARIO_NORWELL_F3.jpg', '604e9c1bca4cbd9d.jpg', 0),
(160, 'Statuario Platina', 1, 1, 1, 3, '71d35221STATUARIO_PLATINA_1.jpg,71d35221STATUARIO_PLATINA_2.jpg,71d35221STATUARIO_PLATINA_3.jpg', '73707113318e67d9.jpg', 0),
(161, 'Statuario Platina', 1, 1, 1, 3, '725d9bc2STATUARIO_PLATINA_A.jpg,725d9bc2STATUARIO_PLATINA_B.jpg,725d9bc2STATUARIO_PLATINA_BOOK_MATCH.jpg', '70a2db3ac45825bf.jpg', 0),
(162, 'Stratum Portoro', 1, 1, 1, 3, '58d7bf0bSTRATUM_PORTORO_F1.jpg,58d7bf0bSTRATUM_PORTORO_F2.jpg,58d7bf0bSTRATUM_PORTORO_F3.jpg', 'efd15bcc0d0bd031.jpg', 0),
(163, 'Stratum Portoro', 1, 3, 1, 3, '33028200STRATUM_PORTORO_F1.jpg,33028200STRATUM_PORTORO_F2.jpg,33028200STRATUM_PORTORO_F3.jpg', '62ac6643b50e4ed3.jpg', 0),
(164, 'Stratum Portoro', 1, 1, 1, 3, '491202f4STRATUM_PORTORO_F1.jpg,491202f4STRATUM_PORTORO_F2.jpg,491202f4STRATUM_PORTORO_F3.jpg', 'e07cee10af883de7.jpg', 0),
(165, 'Travertine Beige', 1, 3, 1, 3, '8c8fb385TRAVERTINE_BEIGE_1.jpg,8c8fb385TRAVERTINE_BEIGE_2.jpg', '65823d291506dea5.jpg', 0),
(166, 'Travertine Beige', 1, 1, 1, 3, '682650eaTRAVERTINE_BEIGE_1.jpg,682650eaTRAVERTINE_BEIGE_2.jpg', 'cf4f5e95268b34d1.jpg', 0),
(167, 'Tera Flakes', 4, 3, 1, 3, '8d985cbaTERRA_FLAKES_F1.jpg,8d985cbaTERRA_FLAKES_F2.jpg,8d985cbaTERRA_FLAKES_F3.jpg,8d985cbaTERRA_FLAKES_F4.jpg', '00492438a78efeb4.jpg', 0),
(168, 'Cemento Antracite', 6, 3, 4, 3, 'bb62d695CEMENTO_ANTRACITE_IN_TX_18_945_A_TCID_GREYF1.jpg,bb62d695CEMENTO_ANTRACITE_IN_TX_18_945_A_TCID_GREYF2.jpg', '4c8b701685625c83.jpg', 0),
(169, 'Iron Grey', 8, 4, 4, 3, '8a4149a3IRON_GREY-F1.jpg,8a4149a3IRON_GREY-F2.jpg', '1b8477c09becb6ae.jpg', 0),
(170, 'Lithic Coin', 6, 3, 4, 3, 'a6d6dde6LITHIC_COIN-F1.jpg,a6d6dde6LITHIC_COIN-F2.jpg,a6d6dde6LITHIC_COIN-F3.jpg', 'fccbd951bd959690.jpg', 0),
(171, 'Mountain Tortora', 5, 3, 4, 3, 'f7b26424MOUNTAIN_TORTORA_F1.jpg,f7b26424MOUNTAIN_TORTORA_F2.jpg,f7b26424MOUNTAIN_TORTORA_F3.jpg', '21a4e9dc01a4d879.jpg', 0),
(172, 'Cordoso Grey', 5, 5, 4, 3, '74e779c2CORDOSO_GREY_F1.jpg,74e779c2CORDOSO_GREY_F2.jpg,74e779c2CORDOSO_GREY_F3.jpg', '2a170b5f733305d6.jpg', 0),
(173, 'Blue Pearl', 1, 1, 3, 5, 'ab046441BLUE_PEARL.jpg', 'da72d5fea0ccfd6d.jpg', 0),
(174, 'Grey Sonata', 1, 1, 3, 5, 'dbdcb39dGREY_SONATA.jpg', 'e0018d54622dc2f4.jpg', 0),
(175, 'Meek Artic', 12, 1, 3, 5, '42d8739cMEEK_ARTIC.jpg', '114c07ef6613e8a2.jpg', 0),
(176, 'Meek Ash ', 12, 1, 1, 5, 'c6b1899fMEEK_ASH.JPG', '2b863f52ba220735.JPG', 0),
(177, 'Meek Coal ', 12, 1, 3, 5, '758f4eb6MEEK_COAL.JPG', '8952ddfa706fd32e.JPG', 0),
(178, 'Meek Smoke', 12, 1, 3, 5, 'fa35e8d3MEEK_SMOKE.JPG', '4d25a1c83fa84084.JPG', 0),
(179, 'Meek Walnut', 12, 1, 3, 5, '7307deb1MEEK_WALNUT.JPG', '30f25f0969c21b21.JPG', 0),
(180, 'Midnight Marquina', 1, 1, 3, 5, 'a3ec2dd2MIDNIGHT_MARQUINA.jpg', '7bf05ed58f15c4e3.jpg', 0),
(181, 'Pietra Grey', 1, 1, 3, 5, 'f98b2acdPIETRA_GREY_NEW.jpg', 'd2ee2efe3e2e383c.jpg', 0),
(182, 'Saint Laurent', 1, 1, 3, 5, '48e650edSAINT_LAURENT.jpg', 'aa3f830f7c411608.jpg', 0),
(183, 'Statuario Vienna', 1, 1, 3, 5, '282f7cd5STATUARIO_VIENNA.jpg', 'a19e2eb8383e8560.jpg', 0),
(184, 'Statuario Vigili', 1, 1, 3, 5, 'd7379fe5STATUARIO_VIGILI.jpg', '204a767f56f0b111.jpg', 0),
(185, 'Claros Mocha', 1, 1, 1, 3, '4fd48c87CLAROS_MOCHA_F1.jpg,4fd48c87CLAROS_MOCHA_F2.jpg,4fd48c87CLAROS_MOCHA_F3.jpg', '6437e94995bea106.jpg', 0),
(186, 'Meridiana Marron', 1, 1, 1, 3, 'f7b8641dMERIDIANA_MARRON.jpg,f7b8641dMERIDIANA_MARRON_A.jpg,f7b8641dMERIDIANA_MARRON_B.jpg', '003c77fade2154c2.jpg', 0),
(187, 'Saint Laurent', 1, 3, 1, 1, '08e39c5bBLACK_SAINT_LAURENT_1.jpg', 'e31cc17b5f9fc1ea.jpg', 0),
(188, 'Saint Laurent', 1, 1, 1, 1, 'a9abe9a3BLACK_SAINT_LAURENT_1.jpg', '41e6a21d4d9fb057.jpg', 0),
(189, 'Saint Laurent', 1, 1, 1, 3, '75857842BLACK_SAINT_LAURENT_1.jpg', 'e2a180b02b780c6f.jpg', 0),
(190, 'Saint Laurent', 1, 3, 1, 3, 'f2a96b69BLACK_SAINT_LAURENT_1.jpg', '7345adae3fc8be6b.jpg', 0),
(191, 'Saint Laurent', 1, 6, 2, 6, 'f0936e92BLACK_SAINT_LAURENT_1.jpg', '643872a638da2c82.jpg', 0),
(192, 'Saint Laurent', 1, 5, 2, 1, 'dd143dc5BLACK_SAINT_LAURENT_1.jpg', '3698084078d2f6ba.jpg', 0),
(193, 'Saint Laurent', 8, 4, 2, 6, '72c61357BLACK_SAINT_LAURENT_1.jpg', '29a039658e556dd2.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `resume`
--

CREATE TABLE `resume` (
  `id` int(11) NOT NULL,
  `first_name` text NOT NULL,
  `last_name` text NOT NULL,
  `email` text NOT NULL,
  `mobile` text NOT NULL,
  `address` text NOT NULL,
  `city` text NOT NULL,
  `state` text NOT NULL,
  `postal_code` text NOT NULL,
  `resume` text NOT NULL,
  `date_posted` datetime NOT NULL,
  `location` text DEFAULT NULL,
  `post` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `resume`
--

INSERT INTO `resume` (`id`, `first_name`, `last_name`, `email`, `mobile`, `address`, `city`, `state`, `postal_code`, `resume`, `date_posted`, `location`, `post`) VALUES
(7, 'Ronit', 'Mali', 'ronitmali@yahoo.com', '7600595222', 'Navsari bazar surat', 'SURAT', 'Gujarat', '394210', 'Ronit_CV-3.pdf', '2022-02-18 17:08:28', '-', '-'),
(8, 'Ronit', 'Mali', 'ronitmali@yahoo.com', '7600595222', 'Navsari bazar surat', 'SURAT', 'Gujarat', '394210', 'Ronit_CV-3.pdf', '2022-02-18 17:08:33', '-', '-'),
(9, 'Rajpalsinh', 'Zala', 'abcd@myemailid.com', '9512300650', 'Lioli Morbi', 'Morbi', 'Gujarat', '363636', 'sorting_incharge.docx', '2022-02-24 12:13:16', 'Morbi', 'Front Desk Executive'),
(10, 'Rajpalsinh', 'Zala', 'brand@lioliceramica.com', '9512300650', 'Lioli Morbi', 'Morbi', 'Gujarat', '382715', 'sorting_incharge.docx', '2022-02-24 12:14:29', '-', '-'),
(11, 'Rajpalsinh', 'Zala', 'mayurbhainekamche!@gmail.com', '9512300650', 'Lioli Morbi', 'Morbi', 'Gujarat', '363636', 'sorting_incharge.docx', '2022-02-24 12:18:21', '-', '-'),
(12, 'Sarthak ', 'Sharma', 'sarthak001sharma@gmail.com', '6387672514', 'LIG 166 AMBEDKAR NAGAR GUJAINI ', 'Kanpur ', 'Uttar Pradesh ', '208022', 'sarthak_sharma_ACCOUNTANT.pdf', '2022-02-25 06:22:52', '-', '-'),
(13, 'Manish ', 'Behal', 'manib29@rediffmail.com', '9757462479', 'Matunga', 'Mumbai', 'Maharashtra', '400019', 'manibcv.docx', '2022-02-26 08:27:31', 'Mumbai', 'Area Sales Manager'),
(14, 'Vanita', 'Patil', 'contactvanita007@gmail.com', '8291114563', 'Room no.10, Anand Society, Jokim compound, PN road, Bhandup West', 'Mumbai', 'Maharashtra', '400078', '0_Resume_53.pdf', '2022-02-26 10:47:33', '-', '-'),
(15, 'Jay', 'Vamja', 'jayvamja21@gmail.com', '+919016356109', 'Ishwariya', 'AMRELI', 'Gujrat', '365601', 'VAMJA_JAY.pdf', '2022-02-27 08:40:56', 'Ahmedabad', 'Area Sales Manager'),
(16, 'Jay', 'Vamja', 'jayvamja21@gmail.com', '+919016356109', 'Ishwariya', 'AMRELI', 'Gujrat', '365601', 'VAMJA_JAY.pdf', '2022-02-27 08:41:11', 'Ahmedabad', 'Area Sales Manager'),
(17, 'Jay', 'Vamja', 'jayvamja21@gmail.com', '+919016356109', 'Ishwariya', 'AMRELI', 'Gujrat', '365601', 'VAMJA_JAY.pdf', '2022-02-27 08:42:36', 'Morbi', 'Front Desk Executive'),
(18, 'Shamshuddin ', 'Kazi ', 'shamskazi18@gmail.com', '9920094418', 'Dockyard Road - Mazgaon', 'Mumbai', 'Maharashtra', '400010', 'Shams.docx', '2022-02-27 21:35:22', '-', '-'),
(19, 'alpita', 'Modak', 'alpita_modak@rediffmail.com', '7900132837', 'Kandivli west', 'mumbai', 'maharastra', '400067', 'Resume_-_Alpita_Modak-1_1_.doc', '2022-02-28 04:55:53', '-', '-'),
(20, 'Jyotika ', 'Rana', 'jyotinrana@gmail.com', '9833729005', 'A/305, Samta Bldg, Chira Bazar, Dadi Santok Lane, Marine Lines,', 'Mumbai ', 'Maharashtra', '400002', 'RESUME_JNR.pdf', '2022-02-28 10:23:51', '-', '-'),
(21, 'Rushabh ', 'Mehta', 'rushabhmeheta91@gmail.com', '9867950343', 'Pantnagar, Ghatkopar East', 'Mumbai', 'Maharashtra', '400075', 'Mehta_Resume_pdf.pdf', '2022-02-28 11:52:25', 'Mumbai', 'Area Sales Manager');

-- --------------------------------------------------------

--
-- Table structure for table `size`
--

CREATE TABLE `size` (
  `id` int(11) NOT NULL,
  `size` varchar(200) DEFAULT NULL,
  `size_image` text NOT NULL,
  `order_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `size`
--

INSERT INTO `size` (`id`, `size`, `size_image`, `order_by`) VALUES
(1, '1200x1200mm', '5c80ad21f0827101.jpg', 4),
(3, '1200x2400mm', '1d92f8a40b11ee7b.jpg', 2),
(4, '1600x1600mm', '814ec13de1600948.jpg', 5),
(5, '800x2400mm', '6074cddf2e9874a6.jpg', 3),
(6, '1600x3200mm', '62575fb90291e72f.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `surface`
--

CREATE TABLE `surface` (
  `id` int(11) NOT NULL,
  `surface` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `surface`
--

INSERT INTO `surface` (`id`, `surface`) VALUES
(1, 'Lustrous'),
(3, 'Rustic Matt'),
(4, 'Orgatech'),
(5, 'Structure Matt'),
(6, 'Crystalline');

-- --------------------------------------------------------

--
-- Table structure for table `thickness`
--

CREATE TABLE `thickness` (
  `id` int(11) NOT NULL,
  `thickness` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `thickness`
--

INSERT INTO `thickness` (`id`, `thickness`) VALUES
(1, '6mm,9mm'),
(2, '6mm,9mm,12 mm'),
(3, '15mm'),
(4, '6mm');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `mobile_number` varchar(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(60) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `permission` int(11) DEFAULT NULL,
  `date_added` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `mobile_number`, `first_name`, `last_name`, `email`, `password`, `is_active`, `permission`, `date_added`) VALUES
(1, '9904073595', 'Master Admin', 'Cretx Infotech', 'admin@cretxinc.com', 'Nlrzq!NEVOic', 1, 0, '2022-01-21 18:07:26'),
(2, '9512300684', 'Ankit', 'Lioli', 'brand@lioliceramica.com', 'Brand#Lioli@684', 1, 1, '2022-02-18 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `career`
--
ALTER TABLE `career`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `catalogue`
--
ALTER TABLE `catalogue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `collection`
--
ALTER TABLE `collection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `download`
--
ALTER TABLE `download`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gallery`
--
ALTER TABLE `gallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `collection_id` (`collection_id`),
  ADD KEY `size_id` (`size_id`),
  ADD KEY `surface_id` (`surface_id`),
  ADD KEY `thickness_id` (`thickness_id`);

--
-- Indexes for table `resume`
--
ALTER TABLE `resume`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `size`
--
ALTER TABLE `size`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `surface`
--
ALTER TABLE `surface`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `thickness`
--
ALTER TABLE `thickness`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mobile_number` (`mobile_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `career`
--
ALTER TABLE `career`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `catalogue`
--
ALTER TABLE `catalogue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `collection`
--
ALTER TABLE `collection`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `download`
--
ALTER TABLE `download`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `gallery`
--
ALTER TABLE `gallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `resume`
--
ALTER TABLE `resume`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `size`
--
ALTER TABLE `size`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `surface`
--
ALTER TABLE `surface`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `thickness`
--
ALTER TABLE `thickness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`collection_id`) REFERENCES `collection` (`id`),
  ADD CONSTRAINT `product_ibfk_2` FOREIGN KEY (`size_id`) REFERENCES `size` (`id`),
  ADD CONSTRAINT `product_ibfk_3` FOREIGN KEY (`surface_id`) REFERENCES `surface` (`id`),
  ADD CONSTRAINT `product_ibfk_4` FOREIGN KEY (`thickness_id`) REFERENCES `thickness` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
