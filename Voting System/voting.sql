/*
MySQL Data Transfer
Source Host: localhost
Source Database: voting
Target Host: localhost
Target Database: voting
Date: 2022/3/5 0:09:22
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for administrator_info
-- ----------------------------
DROP TABLE IF EXISTS `administrator_info`;
CREATE TABLE `administrator_info` (
  `aid` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `passcode` int(10) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for candidate_info
-- ----------------------------
DROP TABLE IF EXISTS `candidate_info`;
CREATE TABLE `candidate_info` (
  `cid` int(10) NOT NULL AUTO_INCREMENT,
  `can_name` varchar(20) NOT NULL,
  `gender` char(10) NOT NULL,
  `position` varchar(10) NOT NULL,
  `party_symbol` char(10) NOT NULL,
  `nomination` char(5) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for cast_vote
-- ----------------------------
DROP TABLE IF EXISTS `cast_vote`;
CREATE TABLE `cast_vote` (
  `cid` int(10) NOT NULL,
  `vid` int(10) NOT NULL,
  `vote_no` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result` (
  `cid` int(10) NOT NULL,
  `position` varchar(10) NOT NULL,
  `party_symbol` char(10) NOT NULL,
  `vote_no` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for voter_info
-- ----------------------------
DROP TABLE IF EXISTS `voter_info`;
CREATE TABLE `voter_info` (
  `vid` int(10) NOT NULL AUTO_INCREMENT,
  `votername` varchar(20) NOT NULL,
  `gender` char(10) NOT NULL,
  `age` int(10) NOT NULL,
  `position` varchar(10) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `passcode` int(10) NOT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `administrator_info` VALUES ('1', 'admin123', '123456');
INSERT INTO `administrator_info` VALUES ('2', 'admin123', '123456');
INSERT INTO `administrator_info` VALUES ('3', 'admin123', '123456');
INSERT INTO `administrator_info` VALUES ('4', 'admin456', '123456');
