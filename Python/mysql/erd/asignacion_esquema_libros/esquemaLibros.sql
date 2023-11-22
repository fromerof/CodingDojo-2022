-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_libros` ;

-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_libros` DEFAULT CHARACTER SET utf8 ;
USE `esquema_libros` ;

-- -----------------------------------------------------
-- Table `esquema_libros`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `num_pages` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`favorites` (
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`author_id`, `book_id`),
  INDEX `fk_autores_has_libros_libros1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_autores_has_libros_autores_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `fk_autores_has_libros_autores`
    FOREIGN KEY (`author_id`)
    REFERENCES `esquema_libros`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_autores_has_libros_libros1`
    FOREIGN KEY (`book_id`)
    REFERENCES `esquema_libros`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
