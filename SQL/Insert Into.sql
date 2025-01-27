-- Delete
DELETE FROM Pedido
DELETE FROM Produto
DELETE FROM Categoria
DELETE FROM Caixa
DELETE FROM Funcionario
DELETE FROM Cliente


--Cliente
INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client)
VALUES (123456789, 'João', 'Silva', '912345678', 'Rua das Flores, 123', 'joao.silva@email.com', 'senhaSegura123');

INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client) 
VALUES (987654321, 'John', 'Doe', '123-456-7890', '123 Main St', 'johndoe@example.com', 'securepassword');

--Funcionario
INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario)
VALUES ('Maria', 'Santos');

--Categoria e Subcategoria
INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (NULL, 'Eletrônicos');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (1, 'Telemoveis');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (1, 'Computadores');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (NULL, 'Bebidas')

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (2, 'Energéticas');

--Caixa
INSERT INTO Caixa(Saldo)
VALUES(123);

--Produto
INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Sony Xperia 5', 489.99, 1, 8);

INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Microsoft Surface Pro 7 plus', 850.00, 2, 2);

INSERT INTO Produto(Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Red Bull 25cl', 1.50, 2, 10);

--Pedido
INSERT INTO Pedido (Id_Produto, Data_Hora, Quantidade, Total, NIF_Cliente, Id_Funcionario, Id_Caixa)
VALUES (1, GETDATE(), 2, 399.99, 123456789, 1, 1);