-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-07-2024 a las 21:58:20
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `click`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `categoria` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `titulo`, `precio`, `descripcion`, `imagen`, `cantidad`, `categoria`) VALUES
(8, 'Smart TV', '950000.00', 'LG 55 POLED', '2024112750Smart.jfif', 2, 'Video'),
(9, 'Equipo Sonido', '650599.00', 'Sony 1500 W', '2024112810sonido.jpg', 1, 'Audio'),
(10, 'Consola Video Juegos', '1500000.00', 'Play Station 5', '2024005054play.jfif', 2, 'Gaming'),
(11, 'smartphone', '550000.00', 'Motorola Moto g84 5G', '2024005338celular.jfif', 10, 'Telefonia'),
(13, 'Notebook', '1650000.00', 'Dell Core I7 2.3Ghz 8GB', '2024174005Noteboook.jfif', 2, 'Informatica'),
(16, 'Disco SSD', '520000.00', 'Sandisk 1TB', '2024165413disco.jpg', 4, 'Informatica'),
(18, 'Parlante Bluetooth Bose Homespeaker 500 Silver', '961900.00', 'El Parlante Bluetooth Bose Home Speaker 500 Silver ofrece un sonido estéreo de pared a pared desde un solo altavoz. Con dos transductores que apuntan en direcciones opuestas, este dispositivo crea un entorno acústico amplio y potente, capaz de llenar cualquier habitación con un rendimiento estéreo impresionante.', '2024161159bose.jpg', 23, 'Audio'),
(19, 'Smart Tv LG Smart Tv 43ur8750 Led Webos Uhd 4k 43 ', '598000.00', 'LG es innovación y eso se ve en cada uno de sus productos tecnológicos, pensados especialmente para que tu familia y vos disfruten mucho más de la vida. Tener un televisor LG es aprovechar la más alta calidad del mercado.  Con el Smart TV 43ur8750 vas a acceder a las aplicaciones en las que se encuentran tus contenidos favoritos. Además, podés navegar por Internet, interactuar en redes sociales y divertirte con videojuegos.', '2024162454lg.jpg', 25, 'Video'),
(20, 'Xiaomi Pocophone Poco X6 Pro Dual SIM 512 G', '755000.00', 'Con su potente procesador y memoria RAM de 12 GB tu equipo alcanzará un alto rendimiento con gran velocidad de transmisión de contenidos y ejecutará múltiples aplicaciones a la vez sin demoras.', '2024163113xiaomi.jpg', 32, 'Telefonia');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
