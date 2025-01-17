DROP TABLE IF EXISTS Pedido
DROP TABLE IF EXISTS Produto
DROP TABLE IF EXISTS Categoria
DROP TABLE IF EXISTS Caixa
DROP TABLE IF EXISTS Funcionario
DROP TABLE IF EXISTS Cliente


CREATE TABLE Cliente
(
    NIF_Cliente        INT           PRIMARY KEY     NOT NULL,
    PNome_Cliente      VARCHAR(10)                   NOT NULL,
    UNome_Cliente      VARCHAR(10)                   NOT NULL,
    Contacto_Tel       VARCHAR(20)                   NOT NULL,
    Morada             VARCHAR(50)                   NOT NULL,
    Mail               VARCHAR(50)                   NOT NULL,
    Password_Client    VARCHAR(20)                   NOT NULL        
)

CREATE TABLE Funcionario
(
    Id_Funcionario          INT IDENTITY(1,1)   PRIMARY KEY     NOT NULL,
    PNome_Funcionario       VARCHAR(10)                         NOT NULL,
    UNome_Funcionario       VARCHAR(10)                         NOT NULL,
)

CREATE TABLE Caixa
(
    Id_Caixa    INT IDENTITY(1,1)    PRIMARY KEY,
    Saldo       DECIMAL(100,2)       DEFAULT(0)
)

CREATE TABLE Categoria
(
    Id_Categoria        INT IDENTITY(1,1)   PRIMARY KEY     NOT NULL,
    Id_Categoria_Parent INT,
    Nome_Categoria      VARCHAR(15)                         NOT NULL,

    CONSTRAINT ID_SubCat FOREIGN KEY (Id_Categoria) REFERENCES Categoria (Id_Categoria)
)

CREATE TABLE Produto
(
    Id_Produto         INT IDENTITY(1,1)   PRIMARY KEY         NOT NULL,
    Nome_Produto       VARCHAR(25)                             NOT NULL,
    Preco_Produto      DECIMAL(5,2)        DEFAULT(0.00)       NOT NULL,
    Id_Subcategoria    INT,
    Quantidade         INT                 DEFAULT(0),

    CONSTRAINT FK_Produto_Categoria FOREIGN KEY (Id_Subcategoria) REFERENCES Categoria (Id_Subcategoria)
)

CREATE TABLE Pedido
(
    Id_Pedido       INT IDENTITY(1,1)   PRIMARY KEY                     NOT NULL,
    Id_Produto      INT                                                 NOT NULL,
    Data_Hora       DATETIME            DEFAULT(CURRENT_TIMESTAMP),
    Quantidade      INT                 DEFAULT(1)                      NOT NULL,
    Total           DECIMAL(5,2)        DEFAULT(0.00)                   NOT NULL,
    NIF_Cliente     INT,
    Id_Funcionario  INT,
    Id_Caixa        INT,

    CONSTRAINT FK_Pedido_Produto     FOREIGN KEY (Id_Produto)     REFERENCES Produto (Id_Produto),
    CONSTRAINT FK_Pedido_Cliente     FOREIGN KEY (NIF_Cliente)    REFERENCES Cliente (NIF_Cliente),
    CONSTRAINT FK_Pedido_Funcionario FOREIGN KEY (Id_Funcionario) REFERENCES Funcionario (Id_Funcionario),
    CONSTRAINT FK_Pedido_Caixa       FOREIGN KEY (Id_Caixa)       REFERENCES Caixa (Id_Caixa)
)
