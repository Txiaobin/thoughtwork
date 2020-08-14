-- Database: `movielens`
CREATE DATABASE IF NOT EXISTS `movielens` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `movielens`;

-- 表的结构 `genome_tags`
DROP TABLE IF EXISTS `genome_tags`;
CREATE TABLE IF NOT EXISTS `genome_tags` (
  `tagid` varchar(10) NOT NULL,
  `tag` varchar(255) NOT NULL,
  PRIMARY KEY (`tagid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 表的结构 `movie`
DROP TABLE IF EXISTS `movie`;
CREATE TABLE IF NOT EXISTS `movie` (
  `movieid` varchar(10) NOT NULL,
  `title` varchar(100) NOT NULL,
  `genres` varchar(100) NOT NULL,
  `imdbld` varchar(100) NOT NULL,
  `tmbdld` varchar(100) NOT NULL,
  `tagld` varchar(10) NOT NULL,
  `relevance` varchar(255) NOT NULL,
  PRIMARY KEY (`movieid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 表的结构 `rating`
DROP TABLE IF EXISTS `rating`;
CREATE TABLE IF NOT EXISTS `rating` (
  `userId` varchar(10) NOT NULL,
  `movieId` varchar(10) NOT NULL,
  `tag` varchar(100) NOT NULL,
  `tagtime` varchar(100) NOT NULL,
  `rating` varchar(10) NOT NULL,
  `ratingtime` varchar(100) NOT NULL,
  PRIMARY KEY (`movieId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 
LOAD DATA infile '..\date\ml-latest-small\comment.csv'