--
-- Table structure for table `sz_cities`
--

CREATE TABLE `sz_cities` (
  `name` varchar(49) DEFAULT NULL,
  `country` varchar(44) DEFAULT NULL,
  `subcountry` varchar(56) DEFAULT NULL,
  `geonameid` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `sz_fop`
--

CREATE TABLE `sz_fop` (
  `FIO` varchar(42) DEFAULT NULL,
  `ADDRESS` varchar(149) DEFAULT NULL,
  `KVED` varchar(136) DEFAULT NULL,
  `STAN` varchar(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `sz_jobs`
--

CREATE TABLE `sz_jobs` (
  `SOC` varchar(7) DEFAULT NULL,
  `Major Group` varchar(7) DEFAULT NULL,
  `Major Group Name` varchar(58) DEFAULT NULL,
  `Minor Group` varchar(7) DEFAULT NULL,
  `Minor Group Name` varchar(82) DEFAULT NULL,
  `Broad Occupation` varchar(11) DEFAULT NULL,
  `Broad Occupation Name` varchar(94) DEFAULT NULL,
  `Detailed Occupation Name` varchar(105) DEFAULT NULL,
  `Definition` varchar(828) DEFAULT NULL,
  `Reference Year` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;