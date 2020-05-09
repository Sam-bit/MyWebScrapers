-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2020 at 08:04 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facts`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `article_url` text NOT NULL,
  `article_title` text NOT NULL,
  `article_thumbnail` text DEFAULT NULL,
  `article_date` double DEFAULT NULL,
  `article_subtitle` double DEFAULT NULL,
  `article_content` text NOT NULL,
  `article_checked_by` text DEFAULT NULL,
  `article_verdict` text DEFAULT NULL,
  `article_alt_verdict` text DEFAULT NULL,
  `article_site_id` int(11) DEFAULT NULL,
  `article_sync_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sources`
--

CREATE TABLE `sources` (
  `src_id` int(11) NOT NULL,
  `src_name` text NOT NULL,
  `src_alt_name` text DEFAULT NULL,
  `src_logo` text DEFAULT NULL,
  `src_is_ifcn_approved` int(11) DEFAULT NULL,
  `src_address` text DEFAULT NULL,
  `src_is_active` int(11) DEFAULT 1,
  `src_country` text DEFAULT NULL,
  `src_supported_by` text DEFAULT NULL,
  `src_language` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sources`
--
ALTER TABLE `sources`
  ADD PRIMARY KEY (`src_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sources`
--
ALTER TABLE `sources`
  MODIFY `src_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
