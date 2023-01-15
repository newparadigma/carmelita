CREATE DATABASE IF NOT EXISTS homestead COLLATE 'utf8mb4_general_ci';
USE homestead;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `telegram_id` int unsigned NOT NULL,
  `last_prediction_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `telegram_id` (`telegram_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
