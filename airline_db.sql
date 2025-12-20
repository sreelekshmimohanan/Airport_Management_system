-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2024 at 05:49 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `airline_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline_customer_reg`
--

CREATE TABLE IF NOT EXISTS `airline_customer_reg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(150) NOT NULL,
  `hname` varchar(150) NOT NULL,
  `district` varchar(150) NOT NULL,
  `street` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `pin` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `airline_customer_reg`
--

INSERT INTO `airline_customer_reg` (`id`, `fname`, `hname`, `district`, `street`, `phone`, `gender`, `dob`, `pin`, `email`, `password`) VALUES
(1, 'Jerin James', 'abcd', 'Pathanamthitta', 'Konni', '9809898987', 'male', '1998-01-09', '686738', 'j@gmail.com', '123'),
(2, 'Ann', 'abcd', 'Pathanamthitta', 'Konni', '9809898987', 'female', '2002-08-09', '686738', 'a@gamil.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_reg`
--

CREATE TABLE IF NOT EXISTS `airline_staff_reg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `district` varchar(150) NOT NULL,
  `hname` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `pin` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `airline_staff_reg`
--

INSERT INTO `airline_staff_reg` (`id`, `name`, `district`, `hname`, `phone`, `gender`, `pin`, `email`, `password`) VALUES
(1, 'Davood', 'Thrissur', 'abcd', '9876543210', 'Male', '686738', 'd@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_bookingchild`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_bookingchild` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(150) NOT NULL,
  `lname` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `idproof_no` varchar(150) NOT NULL,
  `bookingmaster_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `airline_tbl_bookingc_bookingmaster_id_bd516c45_fk_airline_t` (`bookingmaster_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `airline_tbl_bookingchild`
--

INSERT INTO `airline_tbl_bookingchild` (`id`, `fname`, `lname`, `gender`, `idproof_no`, `bookingmaster_id`) VALUES
(1, 'Davood', 'd', 'Male', '32767834HJK', 1),
(2, 'sam', 's', 'Male', '6712JGJG', 1),
(3, 'Ann', 'K', 'Female', '32767834HJK', 1),
(4, 'sam', 'K', 'Male', '32767834HJK', 2),
(5, 'Appu', 's', 'Female', '32767834HJK', 2),
(6, 'loki', 'lok', 'Male', '32767834HJK', 3),
(7, 'Ann', 'K', 'Female', '6712JGJG', 3),
(8, 'sam', 's', 'Female', '32767834HJK', 3),
(9, 'Pass1', 'p', 'Male', '7826768766', 4),
(10, 'pass2', 'p', 'Female', '2343543535', 4),
(11, 'pass3', 'p', 'Female', '34565466546', 4),
(12, 'Davood', 's', 'Male', '32767834HJK', 5);

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_bookingmaster`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_bookingmaster` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total_traveller_no` varchar(150) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` varchar(150) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `routeassign_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `airline_tbl_bookingm_customer_id_4e2bc428_fk_airline_c` (`customer_id`),
  KEY `airline_tbl_bookingm_routeassign_id_e8676dfc_fk_airline_t` (`routeassign_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `airline_tbl_bookingmaster`
--

INSERT INTO `airline_tbl_bookingmaster` (`id`, `total_traveller_no`, `total_amount`, `status`, `customer_id`, `routeassign_id`) VALUES
(1, '3', '65000.00', 'Booked', 1, 3),
(2, '2', '100000.00', 'Cancelled', 1, 2),
(3, '3', '60000.00', 'Booked', 2, 3),
(4, '3', '45000.00', 'Cancelled', 1, 5),
(5, '1', '30000.00', 'Booked', 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_flight`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_flight` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `flight_name` varchar(150) NOT NULL,
  `flight_model` varchar(150) NOT NULL,
  `flight_maxcap` varchar(150) NOT NULL,
  `business_cap` varchar(150) NOT NULL,
  `first_cap` varchar(150) NOT NULL,
  `economy_cap` varchar(150) NOT NULL,
  `year` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `airline_tbl_flight`
--

INSERT INTO `airline_tbl_flight` (`id`, `flight_name`, `flight_model`, `flight_maxcap`, `business_cap`, `first_cap`, `economy_cap`, `year`, `status`) VALUES
(1, 'Airbus 320', 'A330', '600', '100', '100', '350', '2018', 'Active'),
(2, ' Boeing 737', 'B737', '300', '50', '50', '170', '2023', 'Active'),
(4, 'A 320 neo', 'A320neo', '200', '20', '30', '130', '1998', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_login`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `user_type` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `airline_tbl_login`
--

INSERT INTO `airline_tbl_login` (`id`, `email`, `password`, `user_type`, `status`) VALUES
(1, 'j@gmail.com', '123', 'customer', 'Active'),
(2, 'd@gmail.com', '123', 'staff', 'Active'),
(3, 'a@gamil.com', '123', 'customer', 'Active'),
(4, 'Js@gmail.com', 'Jeeeyddbb344@', 'staff', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_payment`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `payment_amt` varchar(150) NOT NULL,
  `card_no` varchar(150) NOT NULL,
  `card_name` varchar(150) NOT NULL,
  `card_type` varchar(150) NOT NULL,
  `cvv` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `bookingmaster_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `airline_tbl_payment_bookingmaster_id_9da14b32_fk_airline_t` (`bookingmaster_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `airline_tbl_payment`
--

INSERT INTO `airline_tbl_payment` (`id`, `payment_amt`, `card_no`, `card_name`, `card_type`, `cvv`, `status`, `bookingmaster_id`) VALUES
(2, '65000.00', '4355325364464321', 'jerin', 'Male', '123', 'Paid', 1),
(3, '100000.00', '5676767516756333', 'jerin', 'Male', '123', 'Paid', 2),
(4, '45000.00', '4363464565464644', 'jerin', 'Male', '566', 'Paid', 4),
(5, '30000.00', '5654647547645645', 'jerin', 'Male', '345', 'Paid', 5);

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_route`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_route` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `starting_point` varchar(150) NOT NULL,
  `destination` varchar(150) NOT NULL,
  `distance` varchar(150) NOT NULL,
  `stop` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `airline_tbl_route`
--

INSERT INTO `airline_tbl_route` (`id`, `starting_point`, `destination`, `distance`, `stop`) VALUES
(1, 'Cochin International Airport, India (COK)', 'Dubai International Airport(DXB)', '4H 20M', 'Direct'),
(2, 'Kochi (COK)', 'Sharjah (SHJ)', '5h 27m', 'Direct'),
(3, 'Thiruvananthapuram(TRV)', 'New Delhi (DEL)', '3h 20m', 'Direct'),
(4, 'Kochi (COK)', 'New Delhi (DEL)', '3h 15m', 'Direct'),
(5, 'Thiruvananthapuram (TRV)', 'Dubai - United Arab Emirates(DXB)', '4h 20m', 'Direct'),
(6, 'Bengaluru (BLR) ', ' Kochi (COK)', '1h 10m', 'Direct'),
(7, 'Cochin International Airport, India (COK)', 'Dubai International Airport, (DXB)', '6 Hrs', 'Bangalore');

-- --------------------------------------------------------

--
-- Table structure for table `airline_tbl_routeassign`
--

CREATE TABLE IF NOT EXISTS `airline_tbl_routeassign` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `arrival_date` date NOT NULL,
  `departure_date` date NOT NULL,
  `arrival_time` time(6) NOT NULL,
  `departure_time` time(6) NOT NULL,
  `first_class_rate` decimal(10,2) NOT NULL,
  `business_class_rate` decimal(10,2) NOT NULL,
  `normal_class_rate` decimal(10,2) NOT NULL,
  `infant_rate` decimal(10,2) NOT NULL,
  `status` varchar(150) NOT NULL,
  `flight_id` bigint(20) NOT NULL,
  `route_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `airline_tbl_routeass_flight_id_10bceb2a_fk_airline_t` (`flight_id`),
  KEY `airline_tbl_routeass_route_id_a58d6dda_fk_airline_t` (`route_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `airline_tbl_routeassign`
--

INSERT INTO `airline_tbl_routeassign` (`id`, `arrival_date`, `departure_date`, `arrival_time`, `departure_time`, `first_class_rate`, `business_class_rate`, `normal_class_rate`, `infant_rate`, `status`, `flight_id`, `route_id`) VALUES
(1, '2024-02-13', '2024-02-13', '14:30:00.000000', '10:00:00.000000', '45000.00', '30000.00', '20000.00', '10000.00', 'Cancelled', 1, 1),
(2, '2024-02-14', '2024-02-14', '15:00:00.000000', '10:00:00.000000', '50000.00', '40000.00', '20000.00', '10000.00', 'Cancelled', 2, 2),
(3, '2024-03-07', '2024-03-07', '09:00:00.000000', '05:00:00.000000', '30000.00', '20000.00', '10000.00', '5000.00', 'Active', 4, 5),
(4, '2024-02-20', '2024-02-20', '11:00:00.000000', '10:00:00.000000', '20000.00', '15000.00', '5000.00', '2000.00', 'Active', 2, 6),
(5, '2024-03-05', '2024-03-05', '17:00:00.000000', '15:00:00.000000', '30000.00', '20000.00', '10000.00', '5000.00', 'Active', 1, 3),
(6, '2024-03-20', '2024-03-20', '17:00:00.000000', '14:00:00.000000', '50000.00', '40000.00', '20000.00', '10000.00', 'Active', 4, 2),
(7, '2024-03-27', '2024-03-27', '18:00:00.000000', '10:00:00.000000', '40000.00', '30000.00', '20000.00', '12000.00', 'Active', 4, 7);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=61 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer_reg', 7, 'add_customer_reg'),
(26, 'Can change customer_reg', 7, 'change_customer_reg'),
(27, 'Can delete customer_reg', 7, 'delete_customer_reg'),
(28, 'Can view customer_reg', 7, 'view_customer_reg'),
(29, 'Can add staff_reg', 8, 'add_staff_reg'),
(30, 'Can change staff_reg', 8, 'change_staff_reg'),
(31, 'Can delete staff_reg', 8, 'delete_staff_reg'),
(32, 'Can view staff_reg', 8, 'view_staff_reg'),
(33, 'Can add tbl_login', 9, 'add_tbl_login'),
(34, 'Can change tbl_login', 9, 'change_tbl_login'),
(35, 'Can delete tbl_login', 9, 'delete_tbl_login'),
(36, 'Can view tbl_login', 9, 'view_tbl_login'),
(37, 'Can add tbl_flight', 10, 'add_tbl_flight'),
(38, 'Can change tbl_flight', 10, 'change_tbl_flight'),
(39, 'Can delete tbl_flight', 10, 'delete_tbl_flight'),
(40, 'Can view tbl_flight', 10, 'view_tbl_flight'),
(41, 'Can add tbl_route', 11, 'add_tbl_route'),
(42, 'Can change tbl_route', 11, 'change_tbl_route'),
(43, 'Can delete tbl_route', 11, 'delete_tbl_route'),
(44, 'Can view tbl_route', 11, 'view_tbl_route'),
(45, 'Can add tbl_routeassign', 12, 'add_tbl_routeassign'),
(46, 'Can change tbl_routeassign', 12, 'change_tbl_routeassign'),
(47, 'Can delete tbl_routeassign', 12, 'delete_tbl_routeassign'),
(48, 'Can view tbl_routeassign', 12, 'view_tbl_routeassign'),
(49, 'Can add tbl_bookingmaster', 13, 'add_tbl_bookingmaster'),
(50, 'Can change tbl_bookingmaster', 13, 'change_tbl_bookingmaster'),
(51, 'Can delete tbl_bookingmaster', 13, 'delete_tbl_bookingmaster'),
(52, 'Can view tbl_bookingmaster', 13, 'view_tbl_bookingmaster'),
(53, 'Can add tbl_bookingchild', 14, 'add_tbl_bookingchild'),
(54, 'Can change tbl_bookingchild', 14, 'change_tbl_bookingchild'),
(55, 'Can delete tbl_bookingchild', 14, 'delete_tbl_bookingchild'),
(56, 'Can view tbl_bookingchild', 14, 'view_tbl_bookingchild'),
(57, 'Can add tbl_payment', 15, 'add_tbl_payment'),
(58, 'Can change tbl_payment', 15, 'change_tbl_payment'),
(59, 'Can delete tbl_payment', 15, 'delete_tbl_payment'),
(60, 'Can view tbl_payment', 15, 'view_tbl_payment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'airline', 'customer_reg'),
(8, 'airline', 'staff_reg'),
(14, 'airline', 'tbl_bookingchild'),
(13, 'airline', 'tbl_bookingmaster'),
(10, 'airline', 'tbl_flight'),
(9, 'airline', 'tbl_login'),
(15, 'airline', 'tbl_payment'),
(11, 'airline', 'tbl_route'),
(12, 'airline', 'tbl_routeassign'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-01-09 04:57:51.094172'),
(2, 'auth', '0001_initial', '2024-01-09 04:57:52.024437'),
(3, 'admin', '0001_initial', '2024-01-09 04:57:52.224667'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-01-09 04:57:52.240289'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-01-09 04:57:52.249991'),
(6, 'airline', '0001_initial', '2024-01-09 04:57:52.360162'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-01-09 04:57:52.429458'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-01-09 04:57:52.464828'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-01-09 04:57:52.482668'),
(10, 'auth', '0004_alter_user_username_opts', '2024-01-09 04:57:52.500333'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-01-09 04:57:52.527480'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-01-09 04:57:52.531577'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-01-09 04:57:52.531577'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-01-09 04:57:52.580322'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-01-09 04:57:52.614528'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-01-09 04:57:52.678899'),
(17, 'auth', '0011_update_proxy_permissions', '2024-01-09 04:57:52.678899'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-01-09 04:57:52.732538'),
(19, 'sessions', '0001_initial', '2024-01-09 04:57:52.849176'),
(20, 'airline', '0002_staff_reg', '2024-01-09 10:05:25.085409'),
(21, 'airline', '0003_tbl_login', '2024-02-13 04:07:46.560983'),
(22, 'airline', '0004_tbl_flight', '2024-02-13 04:53:49.517321'),
(23, 'airline', '0005_tbl_route', '2024-02-13 07:00:30.383783'),
(24, 'airline', '0006_tbl_routeassign', '2024-02-13 11:28:21.631625'),
(25, 'airline', '0007_tbl_bookingmaster', '2024-02-15 13:41:15.943750'),
(26, 'airline', '0008_tbl_bookingchild', '2024-02-15 14:23:13.925475'),
(27, 'airline', '0009_tbl_payment', '2024-02-16 03:56:05.564865'),
(28, 'airline', '0010_tbl_route_stop', '2024-03-17 15:39:44.886585');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1ech6vt4k5wokn4rn0276e6ve9uhc14f', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rh6bL:dElp8pHCuWsFwqDCAd_imfhaTt5pY2NLbkXUFKxeUxI', '2024-03-18 11:35:23.740172'),
('4ea81ekb289jxl88ei9cm7bi91jkkq83', 'e30:1rh5Sr:xFMvRNHfYx89IfXQlRJhnwdILOz-ECPyWrE42ALQbCM', '2024-03-18 10:22:33.946410'),
('9gjdpp1ujpjbkz3ngkvljkczyelwiuq7', 'e30:1rltgs:tD_8r9h0j5w9TTLETVy42aoUXn34yLeCyGkhebh_uWw', '2024-03-31 16:48:54.037556'),
('c9hnvkf5agea35yhjdv6xhm3h151kqvf', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rh5Fj:u5ijgreOhyTJpqCWKFEId5tH21Yi7xSgRv8lnL3zjwQ', '2024-03-18 10:08:59.722109'),
('fo9234gfp6rl9r5e18p7y1p45ze3mkqx', 'e30:1rNAAf:F3-QzW1v9NlpR57763gH4n8T1blLzwEV-zBnEBNQbCk', '2024-01-23 11:21:25.596984'),
('j390k3v8audmpizlbo8kb4xpreblal04', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rl2Ch:a-IMiQrhejCQX56mIspzsEkehGCaWbRJnYK-Giyg_RI', '2024-03-29 07:42:11.578213'),
('jj196no1kdam25h4saya5rp7qei5d1fu', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiBKYW1lcyIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rZteI:iMNt6gqt6-T_yMePJApzmZwTyFfUqn5Y8kQwfi5nsZU', '2024-02-27 14:20:38.160151'),
('nmcu161gcp1yunzjhimo36qavu51kv57', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiBKYW1lcyIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rabE9:knSqZ-tFKfB7XotYfLp-b_5JxLIvd9pPKu7mff-Ckzc', '2024-02-29 12:52:33.646047'),
('oivv2u6598kic9r3p6t4d5welva8jj7b', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rl0C9:Vm-7Zk7FBl6NzKj3AyQexaZD33uf7D9h8PenQxmi8Nw', '2024-03-29 05:33:29.645759'),
('op8tc7olwpq2fgi6rjezvwf6brzh277w', '.eJyrVirOTFGyMtRRKs5LzE1VslJySSzLz09RAgqk5iZm5gBFUhzSQSy95PxcoHByKVRDcilUh1dqUWaegheQUwyWh-nLQtJXCwDYFyGp:1rc4ZC:BiAkNM_8gApNBgTtvWCX80pGLaR8yWo5fJLDnR2IGbU', '2024-03-04 14:24:22.765337'),
('qb6q9oxz3cljqqj5npy1czsjw0qe78tk', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiBKYW1lcyIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rasmj:-zy-hzY-PhiMd7Y00M5gRii2cRL-N1KZeRJJi5A9fYA', '2024-03-01 07:37:25.065477'),
('qt1rwfmdt7aqpj6ri7uev717nza4v4fm', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiBKYW1lcyIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rbGmr:DQD1CbzzqIN63jVUs5KTmhNUEJRxGbgxDuLOrVb62vQ', '2024-03-02 09:15:09.508793'),
('u4u68q3h45twoxhg4ecvdmm9y4l7izhf', 'eyJjdWlkIjoxLCJjdW5hbWUiOiJKZXJpbiBKYW1lcyIsImN1ZW1haWwiOiJqQGdtYWlsLmNvbSJ9:1rbIG2:2rBNrrw_zMBvJcBuIqmKG8XkNpBZArIm8Bkrpec3ZLM', '2024-03-02 10:49:22.619782'),
('v513njd6y1auan36al8o8xxolcwpuxiq', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1rN9c4:4YAvKsG8KRi4KE4YQNwmHF18t2IdXljTP-Bi5gaFz_M', '2024-01-23 10:45:40.720270');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_tbl_bookingchild`
--
ALTER TABLE `airline_tbl_bookingchild`
  ADD CONSTRAINT `airline_tbl_bookingc_bookingmaster_id_bd516c45_fk_airline_t` FOREIGN KEY (`bookingmaster_id`) REFERENCES `airline_tbl_bookingmaster` (`id`);

--
-- Constraints for table `airline_tbl_bookingmaster`
--
ALTER TABLE `airline_tbl_bookingmaster`
  ADD CONSTRAINT `airline_tbl_bookingm_customer_id_4e2bc428_fk_airline_c` FOREIGN KEY (`customer_id`) REFERENCES `airline_customer_reg` (`id`),
  ADD CONSTRAINT `airline_tbl_bookingm_routeassign_id_e8676dfc_fk_airline_t` FOREIGN KEY (`routeassign_id`) REFERENCES `airline_tbl_routeassign` (`id`);

--
-- Constraints for table `airline_tbl_payment`
--
ALTER TABLE `airline_tbl_payment`
  ADD CONSTRAINT `airline_tbl_payment_bookingmaster_id_9da14b32_fk_airline_t` FOREIGN KEY (`bookingmaster_id`) REFERENCES `airline_tbl_bookingmaster` (`id`);

--
-- Constraints for table `airline_tbl_routeassign`
--
ALTER TABLE `airline_tbl_routeassign`
  ADD CONSTRAINT `airline_tbl_routeass_flight_id_10bceb2a_fk_airline_t` FOREIGN KEY (`flight_id`) REFERENCES `airline_tbl_flight` (`id`),
  ADD CONSTRAINT `airline_tbl_routeass_route_id_a58d6dda_fk_airline_t` FOREIGN KEY (`route_id`) REFERENCES `airline_tbl_route` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
