-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 14-08-2026 a las 00:47:24
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Usuario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `ID` int(11) NOT NULL,
  `garrafones_20` int(11) NOT NULL,
  `filtros` int(11) NOT NULL,
  `tapas` int(11) NOT NULL,
  `garrafones_11` int(11) NOT NULL,
  `botella_600` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `litros`
--

CREATE TABLE `litros` (
  `ID` int(11) NOT NULL,
  `litros` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `litros`
--

INSERT INTO `litros` (`ID`, `litros`, `precio`, `fecha`, `hora`) VALUES
(4847155, 1, 5, '2026-01-02', '22:10:00'),
(46286713, 1, 5, '2020-00-00', '00:00:00'),
(50438542, 1, 5, '2026-01-02', '23:00:00'),
(55540185, 1, 5, '2000-00-00', '00:00:00'),
(79198979, 1, 5, '2020-00-00', '00:00:00'),
(81303578, 10, 12, '2026-08-13', '12:11:54'),
(94445089, 1, 5, '2026-08-13', '13:03:24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `litros`
--
ALTER TABLE `litros`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `litros`
--
ALTER TABLE `litros`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94445090;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
