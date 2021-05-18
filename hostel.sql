-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2020 at 07:31 AM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hostel`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_user_name` varchar(200) NOT NULL,
  `admin_user_password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_user_name`, `admin_user_password`) VALUES
(1, 'admin', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `adminreportfeedback`
--

CREATE TABLE `adminreportfeedback` (
  `id` int(11) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminreportfeedback`
--

INSERT INTO `adminreportfeedback` (`id`, `fromdate`, `todate`) VALUES
(1, '2020-03-04', '2020-03-05'),
(2, '2020-03-06', '2020-03-06'),
(3, '2020-03-06', '2020-03-06'),
(4, '2020-03-06', '2020-03-06'),
(5, '2020-03-04', '2020-03-06'),
(6, '2020-03-06', '2020-03-11'),
(7, '2020-03-06', '2020-03-11');

-- --------------------------------------------------------

--
-- Table structure for table `cheif_warden`
--

CREATE TABLE `cheif_warden` (
  `cheifwarden_id` int(11) NOT NULL,
  `cheifwarden_user_name` varchar(200) NOT NULL,
  `cheifwarden_user_password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cheif_warden`
--

INSERT INTO `cheif_warden` (`cheifwarden_id`, `cheifwarden_user_name`, `cheifwarden_user_password`) VALUES
(1, 'admin', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `dayscholars`
--

CREATE TABLE `dayscholars` (
  `dayscholar_id` int(11) NOT NULL,
  `dayscholars_username` varchar(200) NOT NULL,
  `dayscholars_phone` varchar(100) NOT NULL,
  `dayscholars_mess` varchar(200) NOT NULL,
  `dayscholars_gender` varchar(100) NOT NULL,
  `dayscholars_rollno` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dayscholars`
--

INSERT INTO `dayscholars` (`dayscholar_id`, `dayscholars_username`, `dayscholars_phone`, `dayscholars_mess`, `dayscholars_gender`, `dayscholars_rollno`) VALUES
(4, 'admin', '9014912633', 'South', 'Male', '16a9105a2'),
(5, 'admin', '9014912633', 'South', 'Male', '16a9105a2'),
(6, 'admin', '9014912633', 'South', 'Male', '16a9105a2'),
(7, 'admin', '9014912633', 'South', 'Male', '16a9105a2'),
(8, 'sushma', '7995787737', 'South', 'Female', '16a91a0514'),
(9, 'dinesh', '9581800687', 'South', 'Male', '16a91a0544');

-- --------------------------------------------------------

--
-- Table structure for table `facultyattendance`
--

CREATE TABLE `facultyattendance` (
  `s.no` int(11) NOT NULL,
  `roll` varchar(100) DEFAULT NULL,
  `breakfast` varchar(200) NOT NULL,
  `lunch` varchar(200) NOT NULL,
  `dinner` varchar(200) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultyattendance`
--

INSERT INTO `facultyattendance` (`s.no`, `roll`, `breakfast`, `lunch`, `dinner`, `date`) VALUES
(3, '4455', 'morning', 'afternoon', '', '2020-03-04'),
(4, '4455', '', 'afternoon', '', '2020-03-20'),
(5, '', '', 'afternoon', '', '2020-03-20');

-- --------------------------------------------------------

--
-- Table structure for table `facultysuggestions`
--

CREATE TABLE `facultysuggestions` (
  `id` int(11) NOT NULL,
  `suggestions` varchar(1000) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultysuggestions`
--

INSERT INTO `facultysuggestions` (`id`, `suggestions`, `date`) VALUES
(1, 'hahgzhg', '0000-00-00'),
(2, '123456', '2020-02-27'),
(3, '1324567897894561230000000', '2020-02-27'),
(4, '123456789', '2020-03-04');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL,
  `feedback_item1` varchar(200) NOT NULL,
  `feedback_item2` varchar(200) NOT NULL,
  `feedback_item3` varchar(200) NOT NULL,
  `feedback_item4` varchar(200) NOT NULL,
  `feedback_item5` varchar(200) DEFAULT NULL,
  `feedback_item6` varchar(200) DEFAULT NULL,
  `feedback_item7` varchar(200) DEFAULT NULL,
  `feedback_item8` varchar(200) DEFAULT NULL,
  `feedback_item9` varchar(200) DEFAULT NULL,
  `feedback_item10` varchar(200) DEFAULT NULL,
  `feedback_item11` varchar(200) DEFAULT NULL,
  `feedback_item12` varchar(200) DEFAULT NULL,
  `feedback_item13` varchar(200) DEFAULT NULL,
  `feedback_item14` varchar(200) DEFAULT NULL,
  `feedback_item15` varchar(200) DEFAULT NULL,
  `feedback_item16` varchar(200) DEFAULT NULL,
  `feedback_item17` varchar(200) DEFAULT NULL,
  `feedback_item18` varchar(200) DEFAULT NULL,
  `feedback_item19` varchar(200) DEFAULT NULL,
  `feedback_item20` varchar(200) DEFAULT NULL,
  `feedback_breakfast` varchar(200) DEFAULT NULL,
  `feedback_lunch` varchar(200) DEFAULT NULL,
  `feedback_dinner` varchar(200) DEFAULT NULL,
  `feedback_sid` varchar(200) DEFAULT NULL,
  `feedback_fid` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `feedback_item1`, `feedback_item2`, `feedback_item3`, `feedback_item4`, `feedback_item5`, `feedback_item6`, `feedback_item7`, `feedback_item8`, `feedback_item9`, `feedback_item10`, `feedback_item11`, `feedback_item12`, `feedback_item13`, `feedback_item14`, `feedback_item15`, `feedback_item16`, `feedback_item17`, `feedback_item18`, `feedback_item19`, `feedback_item20`, `feedback_breakfast`, `feedback_lunch`, `feedback_dinner`, `feedback_sid`, `feedback_fid`) VALUES
(1, 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', NULL, NULL, NULL, NULL, NULL, 'breakfast', NULL, NULL, '3', NULL),
(2, 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', NULL, NULL, NULL, NULL, NULL, 'breakfast', NULL, NULL, '3', NULL),
(3, 'bad', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', 'good', NULL, NULL, NULL, NULL, NULL, 'breakfast', NULL, NULL, '3', NULL),
(4, 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', NULL, NULL, NULL, NULL, NULL, 'breakfast', NULL, NULL, '3', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `feedbackbreakfast`
--

CREATE TABLE `feedbackbreakfast` (
  `id` int(11) NOT NULL,
  `roll` varchar(100) DEFAULT NULL,
  `feedbackitem1` varchar(200) DEFAULT NULL,
  `feedbackitem2` varchar(200) DEFAULT NULL,
  `feedbackitem3` varchar(200) DEFAULT NULL,
  `feedbackitem4` varchar(200) DEFAULT NULL,
  `feedbackitem5` varchar(200) DEFAULT NULL,
  `feedbackitem6` varchar(200) DEFAULT NULL,
  `feedbackitem7` varchar(200) DEFAULT NULL,
  `feedbackitem8` varchar(200) DEFAULT NULL,
  `feedbackitem9` varchar(200) DEFAULT NULL,
  `feedbackitem10` varchar(200) DEFAULT NULL,
  `feedbackitem11` varchar(200) DEFAULT NULL,
  `feedbackitem12` varchar(200) DEFAULT NULL,
  `feedbackitem13` varchar(200) DEFAULT NULL,
  `feedbackitem14` varchar(200) DEFAULT NULL,
  `feedbackitem15` varchar(200) DEFAULT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedbackbreakfast`
--

INSERT INTO `feedbackbreakfast` (`id`, `roll`, `feedbackitem1`, `feedbackitem2`, `feedbackitem3`, `feedbackitem4`, `feedbackitem5`, `feedbackitem6`, `feedbackitem7`, `feedbackitem8`, `feedbackitem9`, `feedbackitem10`, `feedbackitem11`, `feedbackitem12`, `feedbackitem13`, `feedbackitem14`, `feedbackitem15`, `date`) VALUES
(18, '4455', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', '2020-03-03'),
(19, '', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', '2020-03-02'),
(20, '16A91A0514', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', '2020-03-04'),
(21, '16A91A0514', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'average', 'average', 'average', 'good', 'good', 'good', '2020-03-06'),
(22, '16A91A0522', 'average', 'average', 'good', 'good', 'good', 'average', 'good', 'good', 'good', 'good', 'bad', 'good', 'average', 'good', 'good', '2020-03-06'),
(23, '', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'average', '2020-03-08'),
(24, '', 'good', 'average', 'bad', 'good', 'average', 'good', 'average', 'bad', 'good', 'average', 'bad', 'bad', 'bad', 'average', 'average', '2020-03-09'),
(25, '16A91A0514', 'average', 'bad', 'good', 'average', 'good', 'bad', 'average', 'bad', 'good', 'average', 'good', 'bad', 'average', 'bad', 'average', '2020-03-10'),
(26, '', 'average', 'average', 'average', 'average', 'average', 'average', 'average', 'good', 'bad', 'average', 'good', 'average', 'bad', 'bad', 'average', '2020-03-13');

-- --------------------------------------------------------

--
-- Table structure for table `feedbackdinner`
--

CREATE TABLE `feedbackdinner` (
  `id` int(11) NOT NULL,
  `roll` varchar(100) DEFAULT NULL,
  `feedbackitem1` varchar(200) NOT NULL,
  `feedbackitem2` varchar(200) NOT NULL,
  `feedbackitem3` varchar(200) NOT NULL,
  `feedbackitem4` varchar(200) NOT NULL,
  `feedbackitem5` varchar(200) NOT NULL,
  `feedbackitem6` varchar(200) NOT NULL,
  `feedbackitem7` varchar(200) NOT NULL,
  `feedbackitem8` varchar(200) NOT NULL,
  `feedbackitem9` varchar(200) NOT NULL,
  `feedbackitem10` varchar(200) NOT NULL,
  `feedbackitem11` varchar(200) NOT NULL,
  `feedbackitem12` varchar(200) NOT NULL,
  `feedbackitem13` varchar(200) NOT NULL,
  `feedbackitem14` varchar(200) NOT NULL,
  `feedbackitem15` varchar(200) NOT NULL,
  `feedbackitem16` varchar(200) NOT NULL,
  `feedbackitem17` varchar(200) NOT NULL,
  `feedbackitem18` varchar(200) NOT NULL,
  `feedbackitem19` varchar(200) NOT NULL,
  `feedbackitem20` varchar(200) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedbackdinner`
--

INSERT INTO `feedbackdinner` (`id`, `roll`, `feedbackitem1`, `feedbackitem2`, `feedbackitem3`, `feedbackitem4`, `feedbackitem5`, `feedbackitem6`, `feedbackitem7`, `feedbackitem8`, `feedbackitem9`, `feedbackitem10`, `feedbackitem11`, `feedbackitem12`, `feedbackitem13`, `feedbackitem14`, `feedbackitem15`, `feedbackitem16`, `feedbackitem17`, `feedbackitem18`, `feedbackitem19`, `feedbackitem20`, `date`) VALUES
(1, '16A91A0514', 'bad', 'average', 'average', 'bad', 'good', 'average', 'average', 'good', 'average', 'average', 'average', 'good', 'average', 'good', 'average', 'average', 'good', 'average', 'average', 'good', '2020-03-10');

-- --------------------------------------------------------

--
-- Table structure for table `feedbacklunch`
--

CREATE TABLE `feedbacklunch` (
  `id` int(11) NOT NULL,
  `roll` varchar(100) DEFAULT NULL,
  `feedbackitem1` varchar(200) DEFAULT NULL,
  `feedbackitem2` varchar(200) DEFAULT NULL,
  `feedbackitem3` varchar(200) DEFAULT NULL,
  `feedbackitem4` varchar(200) DEFAULT NULL,
  `feedbackitem5` varchar(200) DEFAULT NULL,
  `feedbackitem6` varchar(200) DEFAULT NULL,
  `feedbackitem7` varchar(200) DEFAULT NULL,
  `feedbackitem8` varchar(200) DEFAULT NULL,
  `feedbackitem9` varchar(200) DEFAULT NULL,
  `feedbackitem10` varchar(200) DEFAULT NULL,
  `feedbackitem11` varchar(200) DEFAULT NULL,
  `feedbackitem12` varchar(200) DEFAULT NULL,
  `feedbackitem13` varchar(200) DEFAULT NULL,
  `feedbackitem14` varchar(200) DEFAULT NULL,
  `feedbackitem15` varchar(200) DEFAULT NULL,
  `feedbackitem16` varchar(200) DEFAULT NULL,
  `feedbackitem17` varchar(200) DEFAULT NULL,
  `feedbackitem18` varchar(200) DEFAULT NULL,
  `feedbackitem19` varchar(200) DEFAULT NULL,
  `feedbackitem20` varchar(200) DEFAULT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedbacklunch`
--

INSERT INTO `feedbacklunch` (`id`, `roll`, `feedbackitem1`, `feedbackitem2`, `feedbackitem3`, `feedbackitem4`, `feedbackitem5`, `feedbackitem6`, `feedbackitem7`, `feedbackitem8`, `feedbackitem9`, `feedbackitem10`, `feedbackitem11`, `feedbackitem12`, `feedbackitem13`, `feedbackitem14`, `feedbackitem15`, `feedbackitem16`, `feedbackitem17`, `feedbackitem18`, `feedbackitem19`, `feedbackitem20`, `date`) VALUES
(5, '4455', 'average', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', '2020-03-05'),
(6, '16A91A0514', 'good', 'average', 'good', 'bad', 'average', 'bad', 'good', 'average', 'good', 'average', 'average', 'bad', 'good', 'average', 'average', 'good', 'average', 'good', 'average', 'average', '2020-03-10');

-- --------------------------------------------------------

--
-- Table structure for table `itemlist`
--

CREATE TABLE `itemlist` (
  `id` int(11) NOT NULL,
  `item1` text,
  `item2` text,
  `item3` text,
  `item4` text,
  `item5` text,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `itemlist`
--

INSERT INTO `itemlist` (`id`, `item1`, `item2`, `item3`, `item4`, `item5`, `date`) VALUES
(7, 'drsda', 'hsgzvn', 'hznqw ', 'ywhzwqn ', 'jzmwsq', '2020-02-15'),
(8, 'tsgzvnw', 'mjdxns ', 'hsxzbs', 'xjzbsa ', 'hxzbs x', '2020-02-15'),
(9, 'bbbb', 'Any 1 Indian Breakfast', 'Chuteney 1', 'Chuteney 2', 'MILK', '2020-02-18'),
(10, 'idly', 'bajji', 'palli', 'Chuteney 2', 'tea', '0000-00-00'),
(11, 'bbbb', 'sss', 's', 'w33', 'rrr', '2020-02-27'),
(12, 'bbbb', 'sss', 'Chuteney 1', 'Chuteney 2', 'MILK', '0000-00-00'),
(13, 'Idly with Sambar & Egg', 'Any 1 Indian Breakfast', 'Chuteney 1', 'Chuteney 2', 'mn', '2020-02-27'),
(14, 'idly', 'dosa', 'yellow', 'white', 'milk', '2020-03-04'),
(15, 'idle', 'dosa', 'white', 'yellow', 'tea', '2020-03-05'),
(16, 'idly', 'dosa', 'white', 'yellow', 'Milk', '2020-03-08'),
(17, 'idly', 'dosa', 'white', 'yellow', 'tea', '2020-03-09'),
(18, 'idly', 'dosa', 'white', 'yellow', 'tea', '2020-03-10'),
(19, 'xccgf', 'q', 'rr', 'pv', 'vfv', '2020-03-12');

-- --------------------------------------------------------

--
-- Table structure for table `itemlistdinner`
--

CREATE TABLE `itemlistdinner` (
  `id` int(11) NOT NULL,
  `item1` text,
  `item2` text,
  `item3` text,
  `item4` text,
  `item5` text,
  `item6` text,
  `item7` text,
  `item8` text,
  `item9` text,
  `item10` text,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `itemlistdinner`
--

INSERT INTO `itemlistdinner` (`id`, `item1`, `item2`, `item3`, `item4`, `item5`, `item6`, `item7`, `item8`, `item9`, `item10`, `date`) VALUES
(1, 'bbbb', 'bxb ', 'nxvas ', 'vxva s', 'anhzswn', 'gvasbv', 'gsbavsq', 'hqnvzn', 'gszvawqab ', 'gwbsvab', '0000-00-00'),
(2, 'bbbb', 'bxb ', 'nxvas ', 'vxva s', 'anhzswn', 'gvasbv', 'gsbavsq', 'hqnvzn', 'gszvawqab ', 'gwbsvab', '0000-00-00'),
(3, 'we', 'wrtwqeyyj', 'dffg', 'mj', 'df', 'hh', 'ffh', 'jkj', 'y', 'sd', '2020-02-27');

-- --------------------------------------------------------

--
-- Table structure for table `itemlistlunch`
--

CREATE TABLE `itemlistlunch` (
  `id` int(11) NOT NULL,
  `item1` text,
  `item2` text,
  `item3` text,
  `item4` text,
  `item5` text,
  `item6` text,
  `item7` text,
  `item8` text,
  `item9` text,
  `item10` text,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `itemlistlunch`
--

INSERT INTO `itemlistlunch` (`id`, `item1`, `item2`, `item3`, `item4`, `item5`, `item6`, `item7`, `item8`, `item9`, `item10`, `date`) VALUES
(1, 'us', 'jxsn x', 'hws', 'hwznS', 'rgbgv', 'esffbfgbv', 'gfgbv', 'rdfvv', 'rtgb', 'hgvn ', '0000-00-00'),
(2, 'us', 'jxsn x', 'hws', 'hwznS', 'rgbgv', 'esffbfgbv', 'gfgbv', 'rdfvv', 'rtgb', 'hgvn ', '0000-00-00'),
(3, 'us', 'jxsn x', 'hws', 'hwznS', 'rgbgv', 'esffbfgbv', 'gfgbv', 'rdfvv', 'rtgb', 'hgvn ', '0000-00-00'),
(4, 'bhxjhaw', 'azhb', 'zaqN', 'ZAJZNa', 'thbjh', 'jhdcfd', 'uhdehw', 'jehbdxh', 'dbejhw', 'hgdwbjh', '0000-00-00'),
(5, 'rice', 'ns nm', 'dmn csnmd', 'jnax  ', 'rasam', 'curd', 'bjHBZ', 'M XMNA', 'sx ', '', '0000-00-00'),
(6, 'bbbb', 'Any 1 Indian Breakfast', 's', 'w33', 'mn', 'esffbfgbv', ' nb', 'vbbn', 'fgcb', 'fgv m', '2020-02-28'),
(7, 'Idly with Sambar & Egg', 'sss', 's', 'Chuteney 2', 'rrr', 'esffbfgbv', ' nb', 'vbbn', 'fgcb', 'fgv m', '2020-02-27'),
(8, 'rice', 'potato', 'tomato', 'brinjal', 'sambar', 'curd', 'coconut', 'papad', 'rasugulla', 'roti', '2020-03-10'),
(9, 'xccgf', 'q', 'rr', 'pv', 'vfv', 'cxsadsa', 'G', 'ASA', 'BGN', 'ASK', '2020-03-12'),
(10, 'xccgf', 'q', 'rr', 'pv', 'vfv', 'cxsadsa', 'G', 'ASA', 'BGN', 'ASK', '2020-03-12');

-- --------------------------------------------------------

--
-- Table structure for table `management`
--

CREATE TABLE `management` (
  `management_id` int(11) NOT NULL,
  `management_user_name` varchar(200) NOT NULL,
  `management_user_password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `management`
--

INSERT INTO `management` (`management_id`, `management_user_name`, `management_user_password`) VALUES
(1, 'admin', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `registrationformfaculty`
--

CREATE TABLE `registrationformfaculty` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `rollno` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `mailid` varchar(200) NOT NULL,
  `phoneno` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL,
  `specialization` varchar(200) NOT NULL,
  `messtype` varchar(200) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registrationformfaculty`
--

INSERT INTO `registrationformfaculty` (`id`, `name`, `rollno`, `gender`, `mailid`, `phoneno`, `course`, `specialization`, `messtype`, `password`) VALUES
(1, 'devipriya', '4455', 'female', 'sushmagarikipati123@gmail.com', '9581800687', 'btech', 'cse', 'south', '12345679');

-- --------------------------------------------------------

--
-- Table structure for table `registrationformstudent`
--

CREATE TABLE `registrationformstudent` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `rollno` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `mailid` varchar(200) NOT NULL,
  `phoneno` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL,
  `specialization` varchar(200) NOT NULL,
  `messtype` varchar(200) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registrationformstudent`
--

INSERT INTO `registrationformstudent` (`id`, `name`, `rollno`, `gender`, `mailid`, `phoneno`, `course`, `specialization`, `messtype`, `password`) VALUES
(8, 'sushma', '16A91A0514', 'female', 'sushmagarikipati123@gmail.com', '9581800687', 'btech', 'cse', 'north', '12345679'),
(9, 'varalakshmi', '16A91A0522', 'female', 'varalakshmi@gmail.com', '8096050149', 'btech', 'cse', 'south', '12345678'),
(10, 'pooja', '16A91A0528', 'female', 'poojachinni@gmail.com', '9866766164', 'btech', 'cse', 'south', '12345678'),
(11, 'radha', '16a91A0553', 'male', 'radha@gmail.com', '326478945', 'btech', 'cse', 'north', '12345'),
(12, 'gani', '16A91A0529', 'male', 'gani123@gmail.com', '8579461235', 'btech', 'cse', 'north', '12345678'),
(13, 'parnika', '16A91A0524', 'female', 'parnika@gmail.com', '8919534363', 'btech', 'cse', 'north', '12345678'),
(14, 'varun', '16A91A0517', 'male', 'varun@gmail.com', '7994545135', 'btech', 'cse', 'south', '12345678'),
(16, 'Dinesh', '16A91A0544', 'female', 'dinesh@gmail.com', '7995787', 'btech', 'cse', 'south', '12345678'),
(17, 'venkat', '16A91A0536', 'male', 'venkat@gmail.com', '8639062669', 'btech', 'cse', 'south', 'venkat12'),
(18, 'akhil', '16A91A0546', 'male', 'akhil@gmail.com', '7660081041', 'btech', 'cse', 'north', 'akhil123'),
(19, 'kavya', '16A91A0581', 'female', 'kavya@gmail.com', '9133041514', 'btech', 'cse', 'south', 'kavya123');

-- --------------------------------------------------------

--
-- Table structure for table `requirementissues`
--

CREATE TABLE `requirementissues` (
  `id` int(11) NOT NULL,
  `issues` varchar(1000) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `requirementissues`
--

INSERT INTO `requirementissues` (`id`, `issues`, `date`) VALUES
(25, 'cd', '2020-03-06'),
(26, 'zaaxs', '2020-03-12');

-- --------------------------------------------------------

--
-- Table structure for table `studentattendance`
--

CREATE TABLE `studentattendance` (
  `s.no` int(200) NOT NULL,
  `roll` varchar(100) DEFAULT NULL,
  `breakfast` varchar(200) DEFAULT NULL,
  `lunch` varchar(200) DEFAULT NULL,
  `dinner` varchar(200) DEFAULT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentattendance`
--

INSERT INTO `studentattendance` (`s.no`, `roll`, `breakfast`, `lunch`, `dinner`, `date`) VALUES
(3, '16A91A0514', 'morning', '', 'night', '2020-03-04'),
(4, '16A91A0514', 'morning', '', '', '2020-03-05'),
(5, '16A91A0514', 'morning', 'afternoon', '', '2020-03-10'),
(6, '16A91A0536', 'morning', 'afternoon', '', '2020-03-18');

-- --------------------------------------------------------

--
-- Table structure for table `studentsuggestions`
--

CREATE TABLE `studentsuggestions` (
  `id` int(11) NOT NULL,
  `suggestions` varchar(1000) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentsuggestions`
--

INSERT INTO `studentsuggestions` (`id`, `suggestions`, `date`) VALUES
(1, 'htdghgsaydgwysuhasuhushhaxHa', '0000-00-00'),
(4, 'hxhansbxhnzawshngqhs', '0000-00-00'),
(5, 'hgwdhvHJXQhabh', '0000-00-00'),
(6, 'htfwxhaVhxVAZSagz123', '0000-00-00'),
(7, 'htfwxhaVhxVAZSagz123', '0000-00-00'),
(8, '1234567890', '2020-02-27'),
(9, '123456789789456123', '2020-03-06'),
(12, '123456\r\n', '2020-03-06'),
(13, '1234567891234567891233\r\n', '2020-03-06'),
(14, '123456789\r\n', '2020-03-09'),
(15, 'abs', '2020-03-12'),
(16, 'abc', '2020-03-12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `adminreportfeedback`
--
ALTER TABLE `adminreportfeedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cheif_warden`
--
ALTER TABLE `cheif_warden`
  ADD PRIMARY KEY (`cheifwarden_id`);

--
-- Indexes for table `dayscholars`
--
ALTER TABLE `dayscholars`
  ADD PRIMARY KEY (`dayscholar_id`);

--
-- Indexes for table `facultyattendance`
--
ALTER TABLE `facultyattendance`
  ADD PRIMARY KEY (`s.no`);

--
-- Indexes for table `facultysuggestions`
--
ALTER TABLE `facultysuggestions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `feedbackbreakfast`
--
ALTER TABLE `feedbackbreakfast`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedbackdinner`
--
ALTER TABLE `feedbackdinner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedbacklunch`
--
ALTER TABLE `feedbacklunch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `itemlist`
--
ALTER TABLE `itemlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `itemlistdinner`
--
ALTER TABLE `itemlistdinner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `itemlistlunch`
--
ALTER TABLE `itemlistlunch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `management`
--
ALTER TABLE `management`
  ADD PRIMARY KEY (`management_id`);

--
-- Indexes for table `registrationformfaculty`
--
ALTER TABLE `registrationformfaculty`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registrationformstudent`
--
ALTER TABLE `registrationformstudent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `requirementissues`
--
ALTER TABLE `requirementissues`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentattendance`
--
ALTER TABLE `studentattendance`
  ADD PRIMARY KEY (`s.no`);

--
-- Indexes for table `studentsuggestions`
--
ALTER TABLE `studentsuggestions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `adminreportfeedback`
--
ALTER TABLE `adminreportfeedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `cheif_warden`
--
ALTER TABLE `cheif_warden`
  MODIFY `cheifwarden_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `dayscholars`
--
ALTER TABLE `dayscholars`
  MODIFY `dayscholar_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `facultyattendance`
--
ALTER TABLE `facultyattendance`
  MODIFY `s.no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `facultysuggestions`
--
ALTER TABLE `facultysuggestions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `feedbackbreakfast`
--
ALTER TABLE `feedbackbreakfast`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `feedbackdinner`
--
ALTER TABLE `feedbackdinner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `feedbacklunch`
--
ALTER TABLE `feedbacklunch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `itemlist`
--
ALTER TABLE `itemlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `itemlistdinner`
--
ALTER TABLE `itemlistdinner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `itemlistlunch`
--
ALTER TABLE `itemlistlunch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `management`
--
ALTER TABLE `management`
  MODIFY `management_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `registrationformfaculty`
--
ALTER TABLE `registrationformfaculty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `registrationformstudent`
--
ALTER TABLE `registrationformstudent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `requirementissues`
--
ALTER TABLE `requirementissues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `studentattendance`
--
ALTER TABLE `studentattendance`
  MODIFY `s.no` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `studentsuggestions`
--
ALTER TABLE `studentsuggestions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
