DROP TABLE IF EXISTS Pedido;
DROP TABLE IF EXISTS Promo;
DROP TABLE IF EXISTS Produto;
DROP TABLE IF EXISTS Categoria;
DROP TABLE IF EXISTS Funcionario;
DROP TABLE IF EXISTS Cliente;

CREATE TABLE Cliente
(
    NIF_Cliente        INT           PRIMARY KEY     NOT NULL,
    PNome_Cliente      VARCHAR(10)                   NOT NULL,
    UNome_Cliente      VARCHAR(10)                   NOT NULL,
    Contacto_Tel       VARCHAR(20)                   NOT NULL,
    Morada             VARCHAR(50)                   NOT NULL,
    Mail               VARCHAR(50)                   NOT NULL,
    Password_Client    VARCHAR(20)                   NOT NULL        
);

CREATE TABLE Funcionario
(
    Id_Funcionario          SERIAL              PRIMARY KEY     NOT NULL,
    PNome_Funcionario       VARCHAR(10)                         NOT NULL,
    UNome_Funcionario       VARCHAR(10)                         NOT NULL,
    Senha_Funcionario       VARCHAR(255)                        NOT NULL
);

CREATE TABLE Categoria 
( 
    Id_Categoria            SERIAL      PRIMARY KEY         NOT NULL, 
    Id_subcategoria         INT, 
    Nome_Categoria          VARCHAR(15)                     NOT NULL, 
    
    CONSTRAINT FK_SubCat FOREIGN KEY (Id_subcategoria) REFERENCES Categoria (Id_Categoria)
);

CREATE TABLE Produto 
( 
    Id_Produto              SERIAL              PRIMARY KEY      NOT NULL, 
    Nome_Produto            VARCHAR(100)                         NOT NULL, 
    Descricao               VARCHAR(100),
    Preco_original          DECIMAL(5,2)     DEFAULT 0.00        NOT NULL,
    Preco                   DECIMAL(5,2)     DEFAULT 0.00        NOT NULL, 
    Id_subcategoria         INT, 
    Quantidade              INT              DEFAULT 0, 
    
    CONSTRAINT FK_Produto_Categoria FOREIGN KEY (Id_subcategoria) REFERENCES Categoria (Id_Categoria)
);

CREATE TABLE Promo
(
    Id_Promo        SERIAL              PRIMARY KEY     NOT NULL,
    Id_Produto      INT                 NOT NULL,
    Data_Inicio     DATE                NOT NULL,
    Data_Fim        DATE                NOT NULL,
    Desconto        DECIMAL(5,2)        DEFAULT 0.00    NOT NULL,

    CONSTRAINT FK_Promo_Produto FOREIGN KEY (Id_Produto) REFERENCES Produto (Id_Produto)
);

/*
CREATE TABLE Pedido
(
    Id_Pedido       SERIAL              PRIMARY KEY     NOT NULL,
    Id_Produto      INT                 NOT NULL,
    Data_Hora       TIMESTAMP           DEFAULT CURRENT_TIMESTAMP   NOT NULL,
    Quantidade      INT                 DEFAULT 1       NOT NULL,
    Total           DECIMAL(5,2)        DEFAULT 0.00    NOT NULL,
    NIF_Cliente     INT,
    Id_Funcionario  INT,

    CONSTRAINT FK_Pedido_Produto     FOREIGN KEY (Id_Produto)     REFERENCES Produto (Id_Produto),
    CONSTRAINT FK_Pedido_Cliente     FOREIGN KEY (NIF_Cliente)    REFERENCES Cliente (NIF_Cliente),
    CONSTRAINT FK_Pedido_Funcionario FOREIGN KEY (Id_Funcionario) REFERENCES Funcionario (Id_Funcionario)
);*/