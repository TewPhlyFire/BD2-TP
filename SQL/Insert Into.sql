--Cliente
INSERT INTO Cliente 
(
    NIF_Cliente, 
    PNome_Cliente, 
    UNome_Cliente, 
    Contacto_Tel, 
    Morada, 
    Mail, 
    Password_Client
)
VALUES 
(
    123456789, 
    'João', 
    'Silva', 
    '912345678', 
    'Rua das Flores, 123', 
    'joao.silva@email.com', 
    'senhaSegura123'
);

--Funcionario
INSERT INTO Funcionario 
(
    PNome_Funcionario, 
    UNome_Funcionario
)
VALUES 
(
    'Maria', 
    'Santos'
);

--Categoria e Subcategoria
INSERT INTO Categoria 
(
    Id_Subcategoria, 
    Nome_Categoria
)
VALUES 
(
    NULL, 
    'Eletrônicos'
);

INSERT INTO Categoria 
(
    Id_Subcategoria, 
    Nome_Categoria
)
VALUES 
(
    1, 
    'Telemoveis'
);

INSERT INTO Categoria 
(
    Id_Subcategoria, 
    Nome_Categoria
)
VALUES 
(
    1, 
    'Computadores'
);

--Caixa
INSERT INTO Caixa
(
    Saldo
)
VALUES
(
    123
);

--Produto
INSERT INTO Produto 
(
    Nome_Produto, 
    Preco_Produto, 
    Id_Subcategoria, 
    Quantidade
)
VALUES 
(
    'Sony Xperia 5', 
    489.99, 
    1, 
    8
);

INSERT INTO Produto 
(
    Nome_Produto, 
    Preco_Produto, 
    Id_Subcategoria, 
    Quantidade
)
VALUES 
(
    'Microsoft Surface Pro 7', 
    850.00, 
    2, 
    2
);


--Pedido
INSERT INTO Pedido 
(
    Id_Produto, 
    Data_Hora, 
    Quantidade, 
    Total, 
    NIF_Cliente, 
    Id_Funcionario, 
    Id_Caixa
)
VALUES 
(
    1, 
    GETDATE(), 
    2, 
    399.99, 
    123456789, 
    1, 
    1
);
