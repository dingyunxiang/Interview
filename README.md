# Interview
用于爬去实习僧上的实习信息

##主要参数
kind参数用来指定徐亚抓取的职业名称
page -- 表明当前抓取的页数


##数据库表
id采用自增id,结构图如下

```
/*
 Navicat Premium Data Transfer

 Source Server         : Local_MySQL
 Source Server Type    : MySQL
 Source Server Version : 50711
 Source Host           : localhost
 Source Database       : interview

 Target Server Type    : MySQL
 Target Server Version : 50711
 File Encoding         : utf-8

 Date: 06/05/2016 16:55:05 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `interview`
-- ----------------------------
DROP TABLE IF EXISTS `interview`;
CREATE TABLE `interview` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `money` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `work_time` varchar(255) DEFAULT NULL,
  `publish_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

```
