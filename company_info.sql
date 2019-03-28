/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.7.23 : Database - company_info
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`company_info` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `company_info`;

/*Table structure for table `info` */

DROP TABLE IF EXISTS `info`;

CREATE TABLE `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `legal_person` char(20) DEFAULT NULL COMMENT '法人',
  `official_website` varchar(30) DEFAULT NULL COMMENT '公司官网',
  `registration_code` varchar(30) DEFAULT NULL COMMENT '注册号',
  `credit_code` varchar(30) DEFAULT NULL COMMENT '社会信用码',
  `establishment_date` varchar(20) DEFAULT NULL COMMENT '成立日期',
  `type` varchar(30) DEFAULT NULL COMMENT '公司类型：有限或上市',
  `address` varchar(100) DEFAULT NULL COMMENT '地址',
  `term` varchar(30) DEFAULT NULL COMMENT '营业期限',
  `name` varchar(30) NOT NULL COMMENT '公司名',
  `employee_number` varchar(30) DEFAULT NULL COMMENT '员工数量',
  `status` varchar(30) DEFAULT NULL COMMENT '是否开业',
  `business_scope` text COMMENT '业务范围',
  `shareholders` varchar(1000) DEFAULT NULL COMMENT '股东',
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
