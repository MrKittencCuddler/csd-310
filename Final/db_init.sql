
-- creates database
CREATE DATABASE whatabook;

-- user drop test
Drop USER IF EXISTS 'whatabook_user'@'localhost';

-- create user and add privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- database privileges to created user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- key drop test
ALTER TABLE whatabook DROP FOREIGN KEY fk_user;
ALTER TABLE whatabook DROP FOREIGN KEY fk_book;

-- table drop test
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;

-- creating tables yay
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);    

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);



-- store record insert
INSERT INTO store(locale)
    VALUES('347 Atlantic Street, Cooltown, NJ 85001');

-- book records insert
INSERT INTO book(book_name, author)
    VALUES('The Warded Man', 'Peter V. Brett');

INSERT INTO book(book_name, author)
    VALUES('One Punch Man', 'ONE');

INSERT INTO book(book_name, author)
    VALUES('Brotherhood of the Mamluks', 'Brad Graft');

INSERT INTO book(book_name, author)
    VALUES('MistBorn', 'Brandon Sanderson');

INSERT INTO book(book_name, author)
    VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');

INSERT INTO book(book_name, author)
    VALUES('Rangers Apprentice - The Ruins of Gorlan', 'John Flanagan');

INSERT INTO book(book_name, author)
    VALUES('Solo Leveling VOL 1', 'Chugong');

INSERT INTO book(book_name, author)
    VALUES('The Hero with a Thousand Faces', 'Joseph Campbell');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');


-- user inserts
INSERT INTO user(first_name, last_name)
    VALUES('Igor', 'Ajith');

INSERT INTO user(first_name, last_name)
    VALUES('Stace', 'Hyacinthus');

INSERT INTO user(first_name, last_name)
    VALUES('Lorrie', 'Lorinda');


-- wishlist inserts
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Igor'),
        (SELECT book_id FROM book WHERE book_name='One Punch Man')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Stace'),
        (SELECT book_id FROM book WHERE book_name='The Hero with a Thousand Faces')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Lorrie'),
        (SELECT book_id FROM book WHERE book_name='MistBorn')
    );