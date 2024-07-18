-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 05, 2023 at 09:08 AM
-- Server version: 5.1.37
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `applicant`
--

CREATE TABLE IF NOT EXISTS `applicant` (
  `apno` int(11) NOT NULL,
  `apname` varchar(50) NOT NULL,
  `apadd` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `contact` varchar(11) NOT NULL,
  `bdate` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `nomini` varchar(30) NOT NULL,
  `opbal` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `applicant`
--

INSERT INTO `applicant` (`apno`, `apname`, `apadd`, `city`, `contact`, `bdate`, `age`, `gender`, `nomini`, `opbal`) VALUES
(1, '', '', '', '', '', 0, '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `closeac`
--

CREATE TABLE IF NOT EXISTS `closeac` (
  `clno` int(11) NOT NULL,
  `cldate` date NOT NULL,
  `apno` int(11) NOT NULL,
  `reson` varchar(20) NOT NULL,
  `ramount` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `closeac`
--

INSERT INTO `closeac` (`clno`, `cldate`, `apno`, `reson`, `ramount`) VALUES
(1, '0000-00-00', 0, '', 0),
(4, '0000-00-00', 2, 'death', 15000),
(3, '0000-00-00', 1, 'Nati', 5000),
(5, '0005-05-23', 2, 'death', 13000);

-- --------------------------------------------------------

--
-- Table structure for table `deposit`
--

CREATE TABLE IF NOT EXISTS `deposit` (
  `slno` int(11) NOT NULL,
  `sldate` varchar(50) NOT NULL,
  `apno` int(11) NOT NULL,
  `perticular` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `deposit`
--

INSERT INTO `deposit` (`slno`, `sldate`, `apno`, `perticular`, `amount`) VALUES
(1, '', 0, '', 0),
(5, '5/5/23', 2, 'CASH', 5000),
(3, '11/29/22', 1, 'CASH', 5000);

-- --------------------------------------------------------

--
-- Table structure for table `interest`
--

CREATE TABLE IF NOT EXISTS `interest` (
  `trno` int(11) NOT NULL,
  `trdate` date NOT NULL,
  `apno` int(11) NOT NULL,
  `ifrom` date NOT NULL,
  `ito` date NOT NULL,
  `irate` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `interest`
--

INSERT INTO `interest` (`trno`, `trdate`, `apno`, `ifrom`, `ito`, `irate`, `amount`) VALUES
(1, '0000-00-00', 0, '0000-00-00', '0000-00-00', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `withdraw`
--

CREATE TABLE IF NOT EXISTS `withdraw` (
  `slno` int(11) NOT NULL,
  `sldate` varchar(50) NOT NULL,
  `apno` int(11) NOT NULL,
  `perticular` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `withdraw`
--

INSERT INTO `withdraw` (`slno`, `sldate`, `apno`, `perticular`, `amount`) VALUES
(1, '', 0, '', 0),
(4, '5/5/23', 2, 'DEBIT CARD', 2000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
